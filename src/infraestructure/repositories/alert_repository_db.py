from ...domain.entities.alert import Alert
from ...domain.interfaces.alert_repository import IAlertrepository

class AlertrepositoryDB(IAlertrepository):
    def __init__(self, session):
        self.session = session

    async def add(self, alert: Alert) -> Alert:
        self.session.add(alert)
        await self.session.commit()
        await self.session.refresh(alert)
        return alert
    
    # Implement other methods as needed, such as get, update, delete, etc.