from abc    import ABC, abstractmethod
from enum import Enum

class ProfileObserverEvents(Enum):
    USER_ADDED = "user_added"
    USER_UPDATED = "user_updated"
    USER_REMOVED = "user_removed"

class ProfileObserver(ABC):
    @abstractmethod
    def user_added(self):
        pass

    @abstractmethod
    def user_removed(self):
        pass

    @abstractmethod
    def user_updated(self):
        pass
