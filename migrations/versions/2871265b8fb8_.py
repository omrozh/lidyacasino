"""empty message

Revision ID: 2871265b8fb8
Revises: 
Create Date: 2024-05-23 14:38:15.096670

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2871265b8fb8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('payment_source',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('is_active_payment_source', sa.Boolean(), nullable=True),
    sa.Column('payment_type', sa.String(), nullable=True),
    sa.Column('payment_number', sa.String(), nullable=True),
    sa.Column('account_holder_name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_assigned_permission',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_fk', sa.String(), nullable=True),
    sa.Column('permission_fk', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_permissions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('permissions_list', sa.String(), nullable=True),
    sa.Column('permission_name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('withdrawal_request', schema=None) as batch_op:
        batch_op.add_column(sa.Column('withdraw_type', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('bank_id', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('withdrawal_request', schema=None) as batch_op:
        batch_op.drop_column('bank_id')
        batch_op.drop_column('withdraw_type')

    op.drop_table('user_permissions')
    op.drop_table('user_assigned_permission')
    op.drop_table('payment_source')
    # ### end Alembic commands ###