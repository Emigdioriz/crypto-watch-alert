from abc import ABC, abstractmethod
from ..entities.alert import Alert

class IAlertrepository(ABC):
    @abstractmethod
    def add(self, alert: Alert) -> Alert:
        pass