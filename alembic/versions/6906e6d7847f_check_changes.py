"""check changes

Revision ID: 6906e6d7847f
Revises: 6efb885142c4
Create Date: 2025-02-05 19:29:22.746832

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6906e6d7847f'
down_revision: Union[str, None] = '6efb885142c4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('class_time', sa.Column('available', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('class_time', 'available')
    # ### end Alembic commands ###
