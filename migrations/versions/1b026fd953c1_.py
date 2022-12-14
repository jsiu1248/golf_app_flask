"""empty message

Revision ID: 1b026fd953c1
Revises: b59dc7f5ec25
Create Date: 2022-11-16 23:11:38.591904

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1b026fd953c1'
down_revision = 'b59dc7f5ec25'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('reply_id', sa.Integer(), nullable=True))
    op.add_column('comments', sa.Column('reply', sa.Text(), nullable=True))
    op.create_foreign_key(None, 'comments', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.drop_column('comments', 'reply')
    op.drop_column('comments', 'reply_id')
    # ### end Alembic commands ###
