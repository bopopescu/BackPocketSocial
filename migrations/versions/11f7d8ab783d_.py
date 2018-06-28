"""empty message

Revision ID: 11f7d8ab783d
Revises: a3b0ab80eed9
Create Date: 2018-06-26 20:17:02.273516

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '11f7d8ab783d'
down_revision = 'a3b0ab80eed9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_todotask_due_date', table_name='todotask')
    op.drop_index('ix_todotask_timestamp', table_name='todotask')
    op.drop_table('todotask')
    op.add_column('task', sa.Column('due_date', sa.DateTime(), nullable=True))
    op.add_column('task', sa.Column('priority', sa.String(length=10), nullable=True))
    op.add_column('task', sa.Column('timestamp', sa.DateTime(), nullable=True))
    op.create_index(op.f('ix_task_due_date'), 'task', ['due_date'], unique=False)
    op.create_index(op.f('ix_task_timestamp'), 'task', ['timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_task_timestamp'), table_name='task')
    op.drop_index(op.f('ix_task_due_date'), table_name='task')
    op.drop_column('task', 'timestamp')
    op.drop_column('task', 'priority')
    op.drop_column('task', 'due_date')
    op.create_table('todotask',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('todo_name', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('todo_priority', mysql.VARCHAR(length=10), nullable=True),
    sa.Column('due_date', mysql.DATETIME(), nullable=True),
    sa.Column('user_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('timestamp', mysql.DATETIME(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='todotask_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='big5',
    mysql_engine='InnoDB'
    )
    op.create_index('ix_todotask_timestamp', 'todotask', ['timestamp'], unique=False)
    op.create_index('ix_todotask_due_date', 'todotask', ['due_date'], unique=False)
    # ### end Alembic commands ###
