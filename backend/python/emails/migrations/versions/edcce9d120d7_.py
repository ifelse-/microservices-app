"""empty message

Revision ID: edcce9d120d7
Revises: 
Create Date: 2023-10-29 18:42:44.966707

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'edcce9d120d7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('send_email',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ticketId', sa.Integer(), nullable=True),
    sa.Column('userId', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('ticketId'),
    sa.UniqueConstraint('userId')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('send_email')
    # ### end Alembic commands ###
