"""se le agrega clausula unique a email

Revision ID: 8e36ccfed795
Revises: 309c9535a0bf
Create Date: 2022-10-08 09:51:38.980024

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8e36ccfed795'
down_revision = '309c9535a0bf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'users', ['email'], schema='test_schema')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', schema='test_schema', type_='unique')
    # ### end Alembic commands ###