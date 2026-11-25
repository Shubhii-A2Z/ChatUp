"""index chatup_threads user_id

Revision ID: dddfff6b8e40
Revises: 1d8316dc2137
Create Date: 2026-11-25 18:43:13.081634

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dddfff6b8e40'
down_revision: Union[str, Sequence[str], None] = '1d8316dc2137'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_index(
        index_name="ix_chatup_threads_user_id",
        table_name="chatup_threads",
        columns=["user_id"],
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_index(
        index_name="ix_chatup_threads_user_id",
        table_name="chatup_threads",
    )
