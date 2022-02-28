"""add last few columns to posts table

Revision ID: 3352433b951b
Revises: 1986b44af261
Create Date: 2022-02-28 17:22:37.093575

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3352433b951b'
down_revision = '1986b44af261'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column(
        'published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('posts', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
