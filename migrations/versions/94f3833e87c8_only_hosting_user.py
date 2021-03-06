""" only hosting_user

Revision ID: 94f3833e87c8
Revises: 30198a96098a
Create Date: 2021-01-30 23:47:48.304565

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '94f3833e87c8'
down_revision = '30198a96098a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('appointments_hosting_user_id_fkey', 'appointments', type_='foreignkey')
    op.drop_constraint('appointments_invited_user_id_fkey', 'appointments', type_='foreignkey')
    op.drop_column('appointments', 'hosting_user_id')
    op.drop_column('appointments', 'invited_user_id')
    op.add_column('both_users', sa.Column('appointment_id', sa.Integer(), nullable=False))
    op.drop_constraint('both_users_invited_user_id_fkey', 'both_users', type_='foreignkey')
    op.drop_constraint('both_users_hosting_user_id_fkey', 'both_users', type_='foreignkey')
    op.create_foreign_key(None, 'both_users', 'appointments', ['appointment_id'], ['id'])
    op.create_foreign_key(None, 'both_users', 'users', ['hosting_user_id'], ['id'])
    op.drop_column('both_users', 'invited_user_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('both_users', sa.Column('invited_user_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'both_users', type_='foreignkey')
    op.drop_constraint(None, 'both_users', type_='foreignkey')
    op.create_foreign_key('both_users_hosting_user_id_fkey', 'both_users', 'appointments', ['hosting_user_id'], ['id'])
    op.create_foreign_key('both_users_invited_user_id_fkey', 'both_users', 'users', ['invited_user_id'], ['id'])
    op.drop_column('both_users', 'appointment_id')
    op.add_column('appointments', sa.Column('invited_user_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('appointments', sa.Column('hosting_user_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.create_foreign_key('appointments_invited_user_id_fkey', 'appointments', 'users', ['invited_user_id'], ['id'])
    op.create_foreign_key('appointments_hosting_user_id_fkey', 'appointments', 'users', ['hosting_user_id'], ['id'])
    # ### end Alembic commands ###
