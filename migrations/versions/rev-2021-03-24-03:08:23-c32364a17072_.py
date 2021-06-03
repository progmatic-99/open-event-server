"""empty message

Revision ID: c32364a17072
Revises: 681bb276443e
Create Date: 2021-03-24 03:08:23.725124

"""

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = 'c32364a17072'
down_revision = '681bb276443e'


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('events', sa.Column('is_chat_enabled', sa.Boolean(), nullable=False, server_default='False'))
    op.add_column('events_version', sa.Column('is_chat_enabled', sa.Boolean(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('events_version', 'is_chat_enabled')
    op.drop_column('events', 'is_chat_enabled')
    # ### end Alembic commands ###
