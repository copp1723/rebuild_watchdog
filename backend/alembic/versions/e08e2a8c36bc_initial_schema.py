"""initial_schema

Revision ID: e08e2a8c36bc
Revises: 0a3d13a7827e
Create Date: 2025-05-05 08:15:15.421692

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'e08e2a8c36bc'
down_revision = '0a3d13a7827e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('uploads',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('filename', sa.String(length=255), nullable=False),
    sa.Column('original_filename', sa.String(length=255), nullable=False),
    sa.Column('file_size', sa.Integer(), nullable=False),
    sa.Column('file_type', sa.String(length=50), nullable=False),
    sa.Column('upload_date', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('status', sa.String(length=20), nullable=True),
    sa.Column('row_count', sa.Integer(), nullable=True),
    sa.Column('column_count', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    
    op.create_table('charts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('upload_id', sa.Integer(), nullable=True),
    sa.Column('chart_type', sa.String(length=50), nullable=False),
    sa.Column('chart_data', sa.JSON(), nullable=False),
    sa.Column('chart_options', sa.JSON(), nullable=True),
    sa.Column('file_path', sa.String(length=255), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.ForeignKeyConstraint(['upload_id'], ['uploads.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    
    op.create_table('data_columns',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('upload_id', sa.Integer(), nullable=True),
    sa.Column('column_name', sa.String(length=255), nullable=False),
    sa.Column('column_type', sa.String(length=50), nullable=False),
    sa.Column('has_missing_values', sa.Boolean(), nullable=True),
    sa.Column('statistics', sa.JSON(), nullable=True),
    sa.ForeignKeyConstraint(['upload_id'], ['uploads.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('upload_id', 'column_name', name='uix_upload_column')
    )
    
    op.create_table('insights',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('upload_id', sa.Integer(), nullable=True),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('insight_type', sa.String(length=50), nullable=False),
    sa.Column('metrics', sa.JSON(), nullable=False),
    sa.Column('chart_url', sa.String(length=255), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.ForeignKeyConstraint(['upload_id'], ['uploads.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    
    op.create_table('questions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('upload_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('question_text', sa.Text(), nullable=False),
    sa.Column('answer_text', sa.Text(), nullable=True),
    sa.Column('insight_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.ForeignKeyConstraint(['insight_id'], ['insights.id'], ),
    sa.ForeignKeyConstraint(['upload_id'], ['uploads.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('questions')
    op.drop_table('insights')
    op.drop_table('data_columns')
    op.drop_table('charts')
    op.drop_table('uploads')
    # ### end Alembic commands ###
