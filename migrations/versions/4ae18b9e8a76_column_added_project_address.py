"""column added project -> address

Revision ID: 4ae18b9e8a76
Revises: dafd11916289
Create Date: 2022-02-25 12:01:53.812497

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4ae18b9e8a76'
down_revision = 'dafd11916289'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('projects', sa.Column('address', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('projects', 'address')
    # ### end Alembic commands ###
