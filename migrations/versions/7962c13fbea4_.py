"""empty message

Revision ID: 7962c13fbea4
Revises: 
Create Date: 2021-01-25 21:38:55.038092

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7962c13fbea4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('todo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=256), nullable=True),
    sa.Column('status', sa.Integer(), nullable=True),
    sa.Column('due', sa.String(length=64), nullable=True),
    sa.Column('tstamp', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('todo')
    # ### end Alembic commands ###
