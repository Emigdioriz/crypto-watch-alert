from tests.fixtures.db_fixtures import db_session
from src.infraestructure.repositories.alert_repository_db import AlertrepositoryDB
from src.domain.entities.alert import Alert, AlertStatus


def test_add_alert_to_db(db_session):
    repo = AlertrepositoryDB(db_session)
    alert = Alert(symbol="BTCUSD", target_price=50000.00)
    saved_alert = repo.add(alert)
    assert saved_alert.id is not None
    assert saved_alert.symbol == "BTCUSD"
    assert saved_alert.target_price == 50000.00
    assert saved_alert.status == AlertStatus.PENDING
    assert saved_alert.id == alert.id  # Ensure the same alert instance is returned with an ID assigned
