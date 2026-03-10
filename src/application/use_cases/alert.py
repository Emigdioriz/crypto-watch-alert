from uuid import UUID
from ...domain.entities.alert import Alert
from ...domain.interfaces.alert_repository import IAlertrepository
from ..dtos.alert_dtos import AlertCreateDTO

class BaseAlertUseCase:
    def __init__(self, repository: IAlertrepository):
        self.repository = repository


class CreateAlertUseCase(BaseAlertUseCase):
    async def execute(self, dto: AlertCreateDTO) -> Alert:

        if dto.target_price <= 0:
            raise ValueError("Target price must be a positive decimal.")

        alert = Alert(symbol=dto.symbol, target_price=dto.target_price)
        return await self.repository.add(alert)


class GetAlertsUseCase(BaseAlertUseCase):
    async def execute(self):
        alerts = await self.repository.get_all()
        return alerts


class GetAlertByIdUseCase(BaseAlertUseCase):
    async def execute(self, alert_id: UUID):
        alert = await self.repository.get_by_id(alert_id)
        return alert