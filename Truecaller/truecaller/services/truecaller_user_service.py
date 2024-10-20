
from ..commons.singleton_meta           import SingletonMeta
from ..commons.profile_observer         import ProfileObserverEvents
from ..entities.user.truecaller_user    import TrueCallerUser

class TrueCallerUserService(metaclass=SingletonMeta):

    def __init__(self):
        self.phone_number_to_users_map = self.import_data()
        self.profile_observers = []

    def import_data(self):
        """
        Import data from database. Currently returns dummy data.
        """
        return {
            "567889999": TrueCallerUser("567889999", "Shagun Arora", "shagun"),
            "577889999": TrueCallerUser("577889999", "Jack", "jack"),
            "989898767": TrueCallerUser("989898767", "Armyman", "arman"),
        }

    def register_user(self, phone_number, registered_name=None, preferred_name=None):
        if phone_number is None:
            # TODO: Add other check to validate phone number for e.g.
            # number of digits expected in phone number etc.
            raise KeyError("Please enter a valid phone number")

        # Check if a user with phone_number already exist in database.
        if phone_number in self.phone_number_to_users_map:
            raise KeyError(f"User with phone number {phone_number} already exist in system.")

        user = TrueCallerUser(phone_number, registered_name, preferred_name)

        # Save user in database/Dictionary maintained in current service.
        self.phone_number_to_users_map[phone_number] = user

        # Update truecaller global directory. This new phone number should
        # be added in tries/store for search service.
        self.notify_observers(ProfileObserverEvents.USER_ADDED, user)

    def delete_user(self, phone_number):
        if phone_number not in self.phone_number_to_users_map:
            raise KeyError(f"User with phone number: {phone_number} do not exist.")
    
        user = self.phone_number_to_users_map[phone_number]
        del self.phone_number_to_users_map[phone_number]

        # Update observers to handle removal of this user.
        self.notify_observers(ProfileObserverEvents.USER_REMOVED, user)

        print(f"User with phone number {phone_number} deleted successfully.")
        
    
    def update_preferred_name(self, phone_number, updated_name):
        if phone_number not in self.phone_number_to_users_map:
            raise KeyError(f"User with phone number: {phone_number} do not exist.")

        user = self.phone_number_to_users_map[phone_number]
        user.set_preferred_name(updated_name)
        
        # After any change we should notify observers. TODO: How exactly this will work.
        self.notify_observers(ProfileObserverEvents.USER_UPDATED, user)

        self.phone_number_to_users_map[user.phone_number] = user

    def get_user(self, phone_number):
        if phone_number not in self.phone_number_to_users_map:
            raise KeyError("No user with input phone number present.")

        return self.phone_number_to_users_map[phone_number]

    def register_observer(self, observer):
        if observer in self.observers:
            # Raise warning/ Create observers list as set. Removal and addition
            # will be in O(logn) complexity.
            return 
        
        self.observers.append(observer)
    
    def remove_observer(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)     

    def notify_observers(self, event, user):
        if event == ProfileObserverEvents.USER_ADDED:
            for profile_observer in self.profile_observers:
                profile_observer.user_added(user)
        
        elif event == ProfileObserverEvents.USER_REMOVED:
            for profile_observer in self.profile_observers:
                profile_observer.user_removed(user)
        
        elif event == ProfileObserverEvents.USER_UPDATED:
            for profile_observer in self.profile_observers:
                profile_observer.user_updated(user)
        
        else:
            raise Warning(f"No observers were notified as {event} is not "
                          " a valid event.")
        