from pydantic import BaseModel, Field
from decimal import Decimal
from uuid import UUID

class AlertCreateDTO(BaseModel):
    symbol: str = Field(example="BTCUSDT")
    target_price: Decimal = Field(example="50000.00", alias="targetPrice")