"""empty message

Revision ID: 5ff51c832dcf
Revises: ab32fff8ad7d
Create Date: 2022-11-21 18:35:17.489896

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5ff51c832dcf'
down_revision = 'ab32fff8ad7d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('city', 'id',
               existing_type=sa.INTEGER(),
               nullable=False,
               autoincrement=True)
    op.drop_column('city', 'city_id')
    op.add_column('ride_or_walk', sa.Column('ride_or_walk_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'ride_or_walk', 'userprofile', ['ride_or_walk_id'], ['ride_or_walk_id'])
    op.alter_column('state', 'id',
               existing_type=sa.INTEGER(),
               nullable=False,
               autoincrement=True)
    op.drop_column('state', 'state_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('state', sa.Column('state_id', sa.VARCHAR(length=64), nullable=False))
    op.alter_column('state', 'id',
               existing_type=sa.INTEGER(),
               nullable=True,
               autoincrement=True)
    op.drop_constraint(None, 'ride_or_walk', type_='foreignkey')
    op.drop_column('ride_or_walk', 'ride_or_walk_id')
    op.add_column('city', sa.Column('city_id', sa.VARCHAR(length=64), nullable=False))
    op.alter_column('city', 'id',
               existing_type=sa.INTEGER(),
               nullable=True,
               autoincrement=True)
    # ### end Alembic commands ###
