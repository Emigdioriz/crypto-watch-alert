from ...domain.entities.alert import Alert
from ...domain.interfaces.alert_repository import IAlertrepository
from ...application.dtos.alert_dtos import AlertCreateDTO

class CreateAlertUseCase:
    def __init__(self, repository: IAlertrepository):
        self.repository = repository

    async def execute(self, dto: AlertCreateDTO) -> Alert:

        if dto.target_price <= 0:
            raise ValueError("Target price must be a positive decimal.")

        alert = Alert(symbol=dto.symbol, target_price=dto.target_price)
        return await self.repository.add(alert)