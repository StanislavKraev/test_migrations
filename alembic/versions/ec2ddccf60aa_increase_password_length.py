"""increase password length

Revision ID: ec2ddccf60aa
Revises: 1671375a9017
Create Date: 2018-02-13 12:35:32.157293

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ec2ddccf60aa'
down_revision = '1671375a9017'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column(
        'user',
        'password',
        existing_type=sa.String(length=10),
        type_=sa.String(length=20)
    )


def downgrade():
    op.alter_column(
        'user',
        'password',
        existing_type=sa.String(length=20),
        type_=sa.String(length=10)
    )
