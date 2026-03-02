from ...domain.entities.alert import Alert
from ...domain.interfaces.alert_repository import IAlertrepository

class AlertrepositoryDB(IAlertrepository):
    def __init__(self, session):
        self.session = session

    def add(self, alert: Alert) -> Alert:
        self.session.add(alert)
        self.session.commit()
        self.session.refresh(alert)
        return alert
    
    # Implement other methods as needed, such as get, update, delete, etc.