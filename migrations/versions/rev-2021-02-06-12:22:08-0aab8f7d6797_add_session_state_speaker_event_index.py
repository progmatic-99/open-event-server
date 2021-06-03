"""Add session state speaker event index

Revision ID: 0aab8f7d6797
Revises: a00006a65bff
Create Date: 2021-02-06 12:22:08.290585

"""

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = '0aab8f7d6797'
down_revision = 'a00006a65bff'


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('session_event_idx', 'sessions', ['event_id'], unique=False)
    op.create_index('session_state_idx', 'sessions', ['state'], unique=False)
    op.create_index('speaker_event_idx', 'speaker', ['event_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('speaker_event_idx', table_name='speaker')
    op.drop_index('session_state_idx', table_name='sessions')
    op.drop_index('session_event_idx', table_name='sessions')
    # ### end Alembic commands ###
