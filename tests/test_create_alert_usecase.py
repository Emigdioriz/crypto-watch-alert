import pytest
from src.domain.entities.alert import Alert, AlertStatus
from src.domain.interfaces.alert_repository import IAlertrepository
from src.application.dtos.alert_dtos import AlertCreateDTO
from src.application.use_cases.create_alert import CreateAlertUseCase

class MockAlertRepository(IAlertrepository):
    def __init__(self):
        self.alerts = []

    async def add(self, alert: Alert) -> Alert:
        self.alerts.append(alert)
        return alert

@pytest.mark.asyncio
async def test_create_alert_use_case():
    # Arrange
    mock_repo = MockAlertRepository()
    use_case = CreateAlertUseCase(repository=mock_repo)
    dto = AlertCreateDTO(symbol="BTCUSDT", targetPrice=50000.00)

    # Act
    created_alert = await use_case.execute(dto)

    # Assert
    assert created_alert.symbol == dto.symbol
    assert created_alert.target_price == dto.target_price
    assert created_alert.status == AlertStatus.PENDING