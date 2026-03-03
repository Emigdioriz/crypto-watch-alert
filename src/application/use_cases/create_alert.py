from ...domain.entities.alert import Alert
from ...domain.interfaces.alert_repository import IAlertrepository
from ...application.dtos.alert_dtos import AlertCreateDTO

class CreateAlertUseCase:
    def __init__(self, repository: IAlertrepository):
        self.repository = repository

    def execute(self, dto: AlertCreateDTO) -> Alert:
        alert = Alert(symbol=dto.symbol, target_price=dto.target_price)
        return self.repository.add(alert)