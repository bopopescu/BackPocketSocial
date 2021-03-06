"""empty message

Revision ID: f287055677c4
Revises: 679c9d8f6fe2
Create Date: 2018-06-12 13:02:53.809810

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f287055677c4'
down_revision = '679c9d8f6fe2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('body', sa.String(length=500), nullable=True))
    op.drop_column('post', 'post_content')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('post_content', sa.VARCHAR(length=200), autoincrement=False, nullable=True))
    op.drop_column('post', 'body')
    # ### end Alembic commands ###
