"""empty message

Revision ID: ee38126c3610
Revises: 3f9d26da2206
Create Date: 2018-06-25 15:25:28.073939

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ee38126c3610'
down_revision = '3f9d26da2206'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('assignments', sa.Column('student_id', sa.Integer(), nullable=True))
    op.add_column('assignments', sa.Column('timestamp', sa.DateTime(), nullable=True))
    op.create_index(op.f('ix_assignments_timestamp'), 'assignments', ['timestamp'], unique=False)
    op.create_foreign_key(None, 'assignments', 'user', ['student_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'assignments', type_='foreignkey')
    op.drop_index(op.f('ix_assignments_timestamp'), table_name='assignments')
    op.drop_column('assignments', 'timestamp')
    op.drop_column('assignments', 'student_id')
    # ### end Alembic commands ###