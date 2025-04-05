"""add_BudgetItem

Revision ID: 94486c9d93de
Revises: f9ad20e44ace
Create Date: 2025-04-05 15:53:47.942815

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '94486c9d93de'
down_revision: Union[str, None] = 'f9ad20e44ace'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('budgetItem',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('allocatedAmount', sa.Numeric(), nullable=False),
    sa.Column('saving', sa.Boolean(), nullable=False),
    sa.Column('budgetGroupId', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['budgetGroupId'], ['budgetGroup.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('budgetItem')
    # ### end Alembic commands ###
