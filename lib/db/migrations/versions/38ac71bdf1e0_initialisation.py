"""initialisation

Revision ID: 38ac71bdf1e0
Revises: 95b51a245903
Create Date: 2024-05-20 12:16:51.579529

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '38ac71bdf1e0'
down_revision: Union[str, None] = '95b51a245903'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
