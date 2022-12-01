"""empty message

Revision ID: 27740827874c
Revises: 1dd2458ac764
Create Date: 2022-11-28 18:47:35.622733

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '27740827874c'
down_revision = '1dd2458ac764'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('userprofile', sa.Column('profile_picture', sa.BLOB(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('userprofile', 'profile_picture')
    # ### end Alembic commands ###