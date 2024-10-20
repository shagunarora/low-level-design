from abc            import ABC, abstractmethod

class AbstractTrueCallerUser(ABC):
    @abstractmethod
    def get_phone_number(self):
        pass
    
    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def is_spam(self):
        pass

    @abstractmethod
    def is_verified(self):
        pass
    