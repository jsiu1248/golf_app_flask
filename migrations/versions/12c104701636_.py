"""empty message

Revision ID: 12c104701636
Revises: 8d0b8ac94a82
Create Date: 2022-11-19 22:54:12.676659

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '12c104701636'
down_revision = '8d0b8ac94a82'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('posts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=64), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('description_html', sa.Text(), nullable=True),
    sa.Column('slug', sa.String(length=128), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('slug')
    )
    op.create_index(op.f('ix_posts_timestamp'), 'posts', ['timestamp'], unique=False)
    op.add_column('comments', sa.Column('description', sa.Text(), nullable=True))
    op.add_column('comments', sa.Column('post_id', sa.Integer(), nullable=False))
    op.add_column('comments', sa.Column('description_html', sa.Text(), nullable=True))
    op.create_foreign_key(None, 'comments', 'users', ['user_id'], ['id'])
    op.drop_column('comments', 'reply')
    op.drop_column('comments', 'reply_id')
    op.drop_column('comments', 'title')
    op.drop_column('comments', 'comment')
    op.drop_column('comments', 'comment_html')
    op.add_column('location', sa.Column('location_id', sa.String(length=64), nullable=False))
    op.drop_column('location', 'id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('location', sa.Column('id', sa.INTEGER(), nullable=False))
    op.drop_column('location', 'location_id')
    op.add_column('comments', sa.Column('comment_html', sa.TEXT(), nullable=True))
    op.add_column('comments', sa.Column('comment', sa.TEXT(), nullable=True))
    op.add_column('comments', sa.Column('title', sa.VARCHAR(length=64), nullable=True))
    op.add_column('comments', sa.Column('reply_id', sa.INTEGER(), nullable=True))
    op.add_column('comments', sa.Column('reply', sa.TEXT(), nullable=True))
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.drop_column('comments', 'description_html')
    op.drop_column('comments', 'post_id')
    op.drop_column('comments', 'description')
    op.drop_index(op.f('ix_posts_timestamp'), table_name='posts')
    op.drop_table('posts')
    # ### end Alembic commands ###
