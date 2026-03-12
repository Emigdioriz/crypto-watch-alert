from pydantic import BaseModel, Field
from decimal import Decimal
from datetime import datetime
from uuid import UUID
from .common.response_dto import BaseResponse


class AlertCreateDTO(BaseModel):
    symbol: str = Field(example="BTCUSDT")
    target_price: Decimal = Field(example="50000.00", alias="targetPrice")


class AlertReadDTO(BaseResponse):
    id: UUID
    symbol: str
    target_price: Decimal = Field(alias="targetPrice")
    status: str
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")