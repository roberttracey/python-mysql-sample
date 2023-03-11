"""Initial migration.

Revision ID: d0c7b8e4b57c
Revises: 
Create Date: 2022-11-08 17:00:02.151921

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd0c7b8e4b57c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('name',
    sa.Column('name', sa.String(length=50), nullable=True)
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('name')
    # ### end Alembic commands ###