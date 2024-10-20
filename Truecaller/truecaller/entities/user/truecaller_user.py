from .abstract_truecaller_user import AbstractTrueCallerUser

class TrueCallerUser(AbstractTrueCallerUser):
    _THRESHOLD = 10

    def __init__(self, 
                 phone_number=None, 
                 registered_name=None,
                 preferred_name=None,
                 spam_count=0,
                 verified_status=False,
                 category=None,
                 blocked_users=[]):
        self.phone_number = phone_number
        self.registered_name = registered_name
        self.preferred_name = preferred_name
        self.spam_count = spam_count
        self.verified_status = verified_status
        self.category = category
        self.blocked_users = blocked_users

    # Define getters and setters (Defined a few below)
    def get_phone_number(self):
        return self.phone_number

    def get_name(self):
        return self.get_name

    def is_spam(self):
        return self.spam_count > self._THRESHOLD

    def is_verified(self):
        return self.verified_status

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number
    
    def set_preferred_name(self, preferred_name):
        self.preferred_name = preferred_name
    
    def set_spam_count(self, spam_count):
        self.spam_count = spam_count
    

