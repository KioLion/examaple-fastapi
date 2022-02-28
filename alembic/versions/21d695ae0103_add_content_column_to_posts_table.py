"""add content column to posts table

Revision ID: 21d695ae0103
Revises: f01809a06af9
Create Date: 2022-02-28 17:09:22.097492

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '21d695ae0103'
down_revision = 'f01809a06af9'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
