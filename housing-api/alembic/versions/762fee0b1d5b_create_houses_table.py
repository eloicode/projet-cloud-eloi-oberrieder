"""create houses table

Revision ID: 762fee0b1d5b
Revises: 
Create Date: 2025-01-20 09:17:19.522663

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '762fee0b1d5b'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('houses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('longitude', sa.Float(), nullable=True),
    sa.Column('latitude', sa.Float(), nullable=True),
    sa.Column('housing_median_age', sa.Integer(), nullable=True),
    sa.Column('total_rooms', sa.Integer(), nullable=True),
    sa.Column('total_bedrooms', sa.Integer(), nullable=True),
    sa.Column('population', sa.Integer(), nullable=True),
    sa.Column('households', sa.Integer(), nullable=True),
    sa.Column('median_income', sa.Float(), nullable=True),
    sa.Column('median_house_value', sa.Float(), nullable=True),
    sa.Column('ocean_proximity', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_houses_id'), 'houses', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_houses_id'), table_name='houses')
    op.drop_table('houses')
    # ### end Alembic commands ###
