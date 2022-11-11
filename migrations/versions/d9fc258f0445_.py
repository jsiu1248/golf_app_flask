"""empty message

Revision ID: d9fc258f0445
Revises: 5fa2e251275f
Create Date: 2022-11-10 16:07:54.058845

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd9fc258f0445'
down_revision = '5fa2e251275f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('follows',
    sa.Column('follower_id', sa.Integer(), nullable=False),
    sa.Column('following_id', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['follower_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['following_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('follower_id', 'following_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('follows')
    # ### end Alembic commands ###
