"""se hace que el codigo del rol sea unico

Revision ID: a67f5a1ebc6a
Revises: 25e3c865df61
Create Date: 2022-11-01 15:31:40.956104

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a67f5a1ebc6a'
down_revision = '25e3c865df61'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'groups', ['code'], schema='authentication')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'groups', schema='authentication', type_='unique')
    # ### end Alembic commands ###