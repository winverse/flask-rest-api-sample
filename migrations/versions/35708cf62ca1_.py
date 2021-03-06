"""empty message

Revision ID: 35708cf62ca1
Revises: f6e054fcb63f
Create Date: 2021-01-26 21:00:05.220210

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '35708cf62ca1'
down_revision = 'f6e054fcb63f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('username', sa.String(length=256), nullable=True))
    op.drop_column('user', 'uesrname')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('uesrname', sa.VARCHAR(length=256), autoincrement=False, nullable=True))
    op.drop_column('user', 'username')
    # ### end Alembic commands ###
