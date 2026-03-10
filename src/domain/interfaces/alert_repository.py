from abc import ABC, abstractmethod
from uuid import UUID
from ..entities.alert import Alert

class IAlertrepository(ABC):
    @abstractmethod
    def add(self, alert: Alert) -> Alert:
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_by_id(self, alert_id: UUID):
        pass