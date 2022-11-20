"""empty message

Revision ID: a94a56f26eeb
Revises: 23d4339c8c1e
Create Date: 2022-11-19 22:25:14.906707

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a94a56f26eeb'
down_revision = '23d4339c8c1e'
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