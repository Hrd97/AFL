"""empty message

Revision ID: 634a03c88b31
Revises: 752cf80ab7a8
Create Date: 2020-04-26 18:38:50.420237

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '634a03c88b31'
down_revision = '752cf80ab7a8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('like', sa.Column('projectid', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'like', 'project', ['projectid'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'like', type_='foreignkey')
    op.drop_column('like', 'projectid')
    # ### end Alembic commands ###
