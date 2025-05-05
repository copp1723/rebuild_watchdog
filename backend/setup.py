from setuptools import setup, find_packages

setup(
    name="watchdog_backend",
    version="0.1",
    packages=find_packages(where="."),
    package_dir={"": "."},  # Important for correct package discovery
    install_requires=[
        "fastapi>=0.95.2",
        "sqlalchemy>=2.0",
        "psycopg2-binary>=2.9.5",
        "python-jose[cryptography]>=3.3.0",
        "passlib[bcrypt]>=1.7.4",
        "python-multipart>=0.0.6",
        "alembic>=1.10.2"
    ],
    python_requires=">=3.11",
) 