"""add users table

Revision ID: 096483c4102c
Revises: 21d695ae0103
Create Date: 2022-02-28 17:13:03.752787

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '096483c4102c'
down_revision = '21d695ae0103'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade():
    op.drop_table('users')
    pass
