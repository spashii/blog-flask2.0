"""user:bio and last_seen

Revision ID: 2a4899fb5c29
Revises: a9064a9009de
Create Date: 2020-04-19 02:07:22.812048

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2a4899fb5c29'
down_revision = 'a9064a9009de'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('bio', sa.String(length=128), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'bio')
    # ### end Alembic commands ###