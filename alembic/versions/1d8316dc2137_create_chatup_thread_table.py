"""create chatup_thread table

Revision ID: 1d8316dc2137
Revises: a5d2c6605b6a
Create Date: 2026-11-25 18:31:37.435348

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1d8316dc2137'
down_revision: Union[str, Sequence[str], None] = 'a5d2c6605b6a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "chatup_threads",
        sa.Column(
            "thread_id",
            sa.Text(),
            primary_key=True,
        ),
        sa.Column(
            "user_id",
            sa.Text(),
            sa.ForeignKey(column="chatup_users.user_id", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.Column(
            "title",
            sa.Text(),
            server_default=sa.text("'New Chat'"),
            nullable=False,
        ),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("chatup_threads")
