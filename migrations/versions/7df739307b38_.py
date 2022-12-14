"""empty message

Revision ID: 7df739307b38
Revises: d4655d61e960
Create Date: 2022-11-21 15:40:43.330319

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7df739307b38'
down_revision = 'd4655d61e960'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_profile', sa.Column('age', sa.Integer(), nullable=True))
    op.drop_column('users', 'age')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('age', sa.INTEGER(), nullable=True))
    op.drop_column('user_profile', 'age')
    # ### end Alembic commands ###
