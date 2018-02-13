"""create sessions table

Revision ID: b00e3d457ada
Revises: ec2ddccf60aa
Create Date: 2018-02-13 13:32:37.423559

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b00e3d457ada'
down_revision = 'ec2ddccf60aa'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'session',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('user_id', sa.Integer, sa.ForeignKey('user.id'))
    )
    op.create_index('ix_session_user_id', 'session', ['user_id'])


def downgrade():
    op.drop_index('ix_session_user_id', 'session')
    op.drop_table('session')
