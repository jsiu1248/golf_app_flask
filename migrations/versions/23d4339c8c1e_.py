"""empty message

Revision ID: 23d4339c8c1e
Revises: 3e70a737605e
Create Date: 2022-11-19 20:30:49.804718

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '23d4339c8c1e'
down_revision = '3e70a737605e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'comments', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'comments', type_='foreignkey')
    # ### end Alembic commands ###
