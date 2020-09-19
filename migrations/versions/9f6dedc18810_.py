"""empty message

Revision ID: 9f6dedc18810
Revises: 6d189470a620
Create Date: 2020-09-19 09:51:35.479831

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9f6dedc18810'
down_revision = '6d189470a620'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_food_date_consumed', table_name='food')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('ix_food_date_consumed', 'food', ['date_consumed'], unique=False)
    # ### end Alembic commands ###
