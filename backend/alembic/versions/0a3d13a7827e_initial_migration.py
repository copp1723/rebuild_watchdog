"""initial_migration

Revision ID: 0a3d13a7827e
Revises: 
Create Date: 2025-05-05 08:14:15.421692

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '0a3d13a7827e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Create users table
    op.create_table('users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('username', sa.String(length=50), nullable=False),
        sa.Column('email', sa.String(length=255), nullable=True),
        sa.Column('password_hash', sa.String(length=255), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
        sa.Column('last_login', sa.DateTime(timezone=True), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('username'),
        sa.UniqueConstraint('email')
    )


def downgrade() -> None:
    op.drop_table('users')