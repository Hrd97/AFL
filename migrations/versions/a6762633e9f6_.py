"""empty message

Revision ID: a6762633e9f6
Revises: 8510f01e41d4
Create Date: 2020-04-26 14:12:36.229910

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a6762633e9f6'
down_revision = '8510f01e41d4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comment', sa.Column('time', sa.CHAR(length=50), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('comment', 'time')
    # ### end Alembic commands ###
