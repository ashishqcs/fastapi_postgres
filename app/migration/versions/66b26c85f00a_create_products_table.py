"""create products table

Revision ID: 66b26c85f00a
Revises: 
Create Date: 2023-01-30 13:34:46.812911

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '66b26c85f00a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'products',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('price', sa.Float),
    )


def downgrade() -> None:
    pass
