"""initial migration

Revision ID: 1671375a9017
Revises: 
Create Date: 2018-02-13 12:30:26.005619

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1671375a9017'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'user',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(200), nullable=False),
        sa.Column('password', sa.String(10), nullable=False)
    )
    op.create_index('ix_user_name', 'user', ['name'])


def downgrade():
    op.drop_index('ix_user_name', 'user')
    op.drop_table('user')
