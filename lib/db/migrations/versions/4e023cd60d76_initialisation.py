"""initialisation

Revision ID: 4e023cd60d76
Revises: aacd13f5447b
Create Date: 2024-05-20 12:23:39.141541

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4e023cd60d76'
down_revision: Union[str, None] = 'aacd13f5447b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
