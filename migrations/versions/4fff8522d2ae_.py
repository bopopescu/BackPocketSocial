"""empty message

Revision ID: 4fff8522d2ae
Revises: afd1281aad7b
Create Date: 2018-06-15 19:01:24.872937

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4fff8522d2ae'
down_revision = 'afd1281aad7b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_task_name', table_name='task')
    op.drop_table('task')
    op.add_column('fy_one_goals', sa.Column('client_id', sa.Integer(), nullable=True))
    op.add_column('fy_one_goals', sa.Column('isCompleted', sa.Boolean(), nullable=True))
    op.add_column('fy_one_goals', sa.Column('isPartialCompleted', sa.Boolean(), nullable=True))
    op.add_column('fy_one_goals', sa.Column('post_id', sa.Integer(), nullable=True))
    op.add_column('fy_one_goals', sa.Column('survey_result', sa.String(length=20000), nullable=True))
    op.drop_constraint('fy_one_goals_user_id_fkey', 'fy_one_goals', type_='foreignkey')
    op.create_foreign_key(None, 'fy_one_goals', 'user', ['client_id'], ['id'])
    op.drop_column('fy_one_goals', 'relevant_fy01')
    op.drop_column('fy_one_goals', 'FirstDraftGoal')
    op.drop_column('fy_one_goals', 'endDate')
    op.drop_column('fy_one_goals', 'timely_fy01')
    op.drop_column('fy_one_goals', 'specific_fy01')
    op.drop_column('fy_one_goals', 'user_id')
    op.drop_column('fy_one_goals', 'achievable_fy01')
    op.drop_column('fy_one_goals', 'measurable_fy01')
    op.drop_column('fy_one_goals', 'startDate')
    op.drop_column('fy_one_goals', 'finalGoal_fy01')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('fy_one_goals', sa.Column('finalGoal_fy01', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.add_column('fy_one_goals', sa.Column('startDate', sa.VARCHAR(length=10), autoincrement=False, nullable=True))
    op.add_column('fy_one_goals', sa.Column('measurable_fy01', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.add_column('fy_one_goals', sa.Column('achievable_fy01', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.add_column('fy_one_goals', sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('fy_one_goals', sa.Column('specific_fy01', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.add_column('fy_one_goals', sa.Column('timely_fy01', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.add_column('fy_one_goals', sa.Column('endDate', sa.VARCHAR(length=10), autoincrement=False, nullable=True))
    op.add_column('fy_one_goals', sa.Column('FirstDraftGoal', sa.VARCHAR(length=500), autoincrement=False, nullable=True))
    op.add_column('fy_one_goals', sa.Column('relevant_fy01', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'fy_one_goals', type_='foreignkey')
    op.create_foreign_key('fy_one_goals_user_id_fkey', 'fy_one_goals', 'user', ['user_id'], ['id'])
    op.drop_column('fy_one_goals', 'survey_result')
    op.drop_column('fy_one_goals', 'post_id')
    op.drop_column('fy_one_goals', 'isPartialCompleted')
    op.drop_column('fy_one_goals', 'isCompleted')
    op.drop_column('fy_one_goals', 'client_id')
    op.create_table('task',
    sa.Column('id', sa.VARCHAR(length=36), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=128), autoincrement=False, nullable=True),
    sa.Column('description', sa.VARCHAR(length=128), autoincrement=False, nullable=True),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('complete', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='task_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='task_pkey')
    )
    op.create_index('ix_task_name', 'task', ['name'], unique=False)
    # ### end Alembic commands ###