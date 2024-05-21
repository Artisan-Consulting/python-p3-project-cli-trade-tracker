"""initialisation

Revision ID: aacd13f5447b
Revises: 38ac71bdf1e0
Create Date: 2024-05-20 12:18:49.416802

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'aacd13f5447b'
down_revision: Union[str, None] = '38ac71bdf1e0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
