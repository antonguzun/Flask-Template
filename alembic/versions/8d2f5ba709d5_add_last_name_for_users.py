"""add last_name for users

Revision ID: 8d2f5ba709d5
Revises: 0b44ef6fa08d
Create Date: 2020-03-15 16:47:12.164291

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8d2f5ba709d5'
down_revision = '0b44ef6fa08d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('last_name', sa.String(length=80), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'last_name')
    # ### end Alembic commands ###