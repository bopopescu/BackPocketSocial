"""empty message

Revision ID: 9449157a15e2
Revises: ee38126c3610
Create Date: 2018-06-25 15:58:20.865565

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9449157a15e2'
down_revision = 'ee38126c3610'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('firstName', sa.String(length=64), nullable=True))
    op.add_column('user', sa.Column('lastName', sa.String(length=64), nullable=True))
    op.add_column('user', sa.Column('mobileNumber', sa.String(length=12), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'mobileNumber')
    op.drop_column('user', 'lastName')
    op.drop_column('user', 'firstName')
    # ### end Alembic commands ###