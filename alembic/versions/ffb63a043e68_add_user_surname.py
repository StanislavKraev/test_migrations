"""add user surname

Revision ID: ffb63a043e68
Revises: ec2ddccf60aa
Create Date: 2018-02-13 12:43:00.181493

"""
from alembic import op
from sqlalchemy import Column, String

# revision identifiers, used by Alembic.

revision = 'ffb63a043e68'
down_revision = 'ec2ddccf60aa'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        'user',
        Column('surname', String(200), nullable=True, default="")
    )

    connection = op.get_bind()
    connection.execute("""
        UPDATE public.user
        SET surname = 'testovich'
        RETURNING id, password
    """)


def downgrade():
    op.drop_column('user', 'surname')
