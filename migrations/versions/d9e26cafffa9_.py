"""empty message

Revision ID: d9e26cafffa9
Revises: 9449157a15e2
Create Date: 2018-06-26 19:51:20.644260

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd9e26cafffa9'
down_revision = '9449157a15e2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todotask', sa.Column('date', sa.DateTime(), nullable=True))
    op.create_index(op.f('ix_todotask_date'), 'todotask', ['date'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_todotask_date'), table_name='todotask')
    op.drop_column('todotask', 'date')
    # ### end Alembic commands ###