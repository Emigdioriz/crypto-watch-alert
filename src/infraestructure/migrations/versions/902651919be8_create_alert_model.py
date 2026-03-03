"""create_alert_model

Revision ID: 902651919be8
Revises: 
Create Date: 2026-03-03 14:14:47.698989

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '902651919be8'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "alerts",
        sa.Column("id", sa.UUID(as_uuid=True), primary_key=True),
        sa.Column("symbol", sa.String, nullable=False),
        sa.Column("target_price", sa.Numeric, nullable=False),
        sa.Column("status", sa.Enum("PENDING", "TRIGGERED", name="alertstatus"), nullable=False, server_default="PENDING"),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), onupdate=sa.text("now()"), nullable=False),
    )


def downgrade() -> None:
    op.drop_table("alerts")
