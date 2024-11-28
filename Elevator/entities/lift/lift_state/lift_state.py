from abc import ABC, abstractmethod

class LiftState(ABC):
    def __init__(self, lock):
        self.lock = lock 
        
    @abstractmethod
    def add_request(self, floors):
        pass

    @abstractmethod
    def recalculate_priorities(self, requests_to_process, base_floor):
        pass
