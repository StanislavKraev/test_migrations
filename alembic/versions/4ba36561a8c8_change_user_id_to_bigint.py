"""change user id to bigint

Revision ID: 4ba36561a8c8
Revises: ec2ddccf60aa
Create Date: 2018-02-13 13:44:38.707491

"""
from alembic import op
from sqlalchemy import Integer, BigInteger


# revision identifiers, used by Alembic.

revision = '4ba36561a8c8'
down_revision = 'ec2ddccf60aa'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column(
        'user',
        'id',
        existing_type=Integer,
        type_=BigInteger
    )


def downgrade():
    op.alter_column(
        'user',
        'id',
        existing_type=BigInteger,
        type_=Integer
    )
