"""add foreign key to onboarding

Revision ID: 469fd4001eb2
Revises: 9859ac58a532
Create Date: 2025-06-15 17:55:42.174927

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '469fd4001eb2'
down_revision = '9859ac58a532'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('onboardings', schema=None) as batch_op:
        batch_op.add_column(sa.Column('employee_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(batch_op.f('fk_onboardings_employee_id_employees'), 'employees', ['employee_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('onboardings', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_onboardings_employee_id_employees'), type_='foreignkey')
        batch_op.drop_column('employee_id')

    # ### end Alembic commands ###
