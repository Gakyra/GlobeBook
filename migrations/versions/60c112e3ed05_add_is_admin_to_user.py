"""Add is_admin to User

Revision ID: 60c112e3ed05
Revises: a2583e3f953e
Create Date: 2024-10-17 21:33:12.336626

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '60c112e3ed05'
down_revision = 'a2583e3f953e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_admin', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('is_admin')

    # ### end Alembic commands ###
