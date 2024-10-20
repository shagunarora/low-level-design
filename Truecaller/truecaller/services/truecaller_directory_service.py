
import warnings

from ..commons.trie_store.user_name_trie        import UserNameTrie
from ..commons.singleton_meta                   import SingletonMeta
from ..commons.trie_store.contact_number_trie   import ContactNumberTrie
from ..entities.user.truecaller_user            import TrueCallerUser
from ..commons.profile_observer                 import ProfileObserver

from .truecaller_user_service                   import TrueCallerUserService

class TrueCallerDirectoryService(ProfileObserver, metaclass=SingletonMeta):
    truecaller_user_service = TrueCallerUserService()

    def __init__(self):
        # We can use some third-party data structures as well to ease search.
        # TODO: Check BloomFilter and Elastic search. (For now going with Trie.)
        self.users_by_phone_number_trie = ContactNumberTrie(list(self.truecaller_user_service.phone_number_to_users_map.keys()))
        self.users_by_name_trie = UserNameTrie(list(self.truecaller_user_service.phone_number_to_users_map.values()))
    
    ############################ Private utility methods ##############################
    def _get_user_by_contact_numbers(self, contact_numbers):
        users = []
        for contact_number in contact_numbers:
            user = self.truecaller_user_service.phone_number_to_users_map.get(contact_number, None)

            if not user:
                warnings.warn(f"No user with contact number {contact_number} found in database.")
            
            users.append(user)
        
        return users
    
    ####################################################################################
    
    def user_added(self, user:TrueCallerUser):
        # Add user in both the trie/stores i.e. by phone number and preferred name.
        self.users_by_phone_number_trie.insert(user.phone_number)
        self.users_by_name_trie.insert(user.preferred_name, user.phone_number)

    def user_removed(self, user:TrueCallerUser):
        # Remove user from both the trie i.e. by phone number and preferred name.
        self.users_by_phone_number_trie.remove(user.phone_number)
        self.users_by_name_trie.remove(user.preferred_name, user.phone_number)

    def user_updated(self, user:TrueCallerUser):
        """
        We are assuming user cannot update its phone number as phone number 
        in our system is considered as primary key/unique id to identify 
        individuals.
        
        Users can only update meta data e.g. preferred name etc. Only update 
        that will require trie to update is preferred name update which is 
        used to build NameTrie.

        """
        # Check if preferred name is updated, if yes then update name trie.
        # Since we are considering contact number as our user_id, we are assuming
        # user cannot update contact number. User will have to create a new user
        # for using a new contact number.
        old_user = self.truecaller_user_service.phone_number_to_users_map[user.phone_number]
        if old_user.preferred_name != user.preferred_name:
            # Update name trie.
            self.users_by_name_trie.remove(old_user.preferred_name, old_user.phone_number)
            self.users_by_name_trie.insert(user.preferred_name, user.phone_number)
            print("Preferred name successfully updated in Trie.")


    def search_by_phone_number(self, phone_number):
        users = self.users_by_phone_number_trie.search_contact_number_prefix(phone_number)
        return users
    
    def search_by_number_prefix(self, phone_number_prefix):
        contact_numbers = self.users_by_phone_number_trie.search_contact_number_prefix(phone_number_prefix)
        return self._get_user_by_contact_numbers(contact_numbers)

    def search_by_name(self, name):
        contact_numbers = self.users_by_name_trie.search_name_by_prefix(name)
        return self._get_user_by_contact_numbers(contact_numbers)

    def search_by_name_prefix(self, name_prefix):
        contact_numbers = self.users_by_name_trie.search_name_by_prefix(name_prefix)
        return self._get_user_by_contact_numbers(contact_numbers)
