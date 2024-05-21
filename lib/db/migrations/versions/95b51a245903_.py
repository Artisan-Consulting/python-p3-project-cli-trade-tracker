"""empty message

Revision ID: 95b51a245903
Revises: 095fb3bc48f8
Create Date: 2024-05-20 12:16:06.969829

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '95b51a245903'
down_revision: Union[str, None] = '095fb3bc48f8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
