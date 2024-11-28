from abc import ABC, abstractmethod

class LiftSelectionStrategy(ABC):
    @abstractmethod
    def get_lift(self, current_floor, destination_floor):
        pass
