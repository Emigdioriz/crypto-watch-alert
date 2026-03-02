import enum
from decimal import Decimal
from uuid import UUID, uuid4
from sqlalchemy import String, DateTime, func, Enum
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from sqlalchemy.orm import Mapped, mapped_column, mapped_as_dataclass, relationship
from ....config.db import mapper_registry
from datetime import datetime
from typing import TYPE_CHECKING

class AlertStatus(enum.Enum):
    PENDING = "PENDING"
    TRIGGERED = "TRIGGERED"


@mapped_as_dataclass(mapper_registry)
class Alert:
    __tablename__ = "alerts"

    def __init__(self, target_price: Decimal):
        if target_price <=0:
            raise ValueError("Target price must be a positive decimal.")


    id: Mapped[UUID] = mapped_column(PGUUID(as_uuid=True), primary_key=True, init=False, default_factory=uuid4)
    symbol: Mapped[str] = mapped_column(String, nullable=False)
    target_price: Mapped[Decimal] = mapped_column(nullable=False)
    status: Mapped[AlertStatus] = mapped_column(Enum(AlertStatus), nullable=False, default=AlertStatus.PENDING)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        init=False,
        nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        onupdate=func.now(),
        server_default=func.now(),
        init=False,
        nullable=False
    )