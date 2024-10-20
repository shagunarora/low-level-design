
import warnings

from .trie_node import TrieNode

class ContactNumberTrie:
    def __init__(self, contact_numbers):
        self.build(contact_numbers)
        self.root = TrieNode()

    ##### Private utility methods #############
    def _get_user_contacts(self, node, user_contact_numbers, search_limit):
        
        if node.completion_status:
            user_contact_numbers.extend(node.node_values)
            return

        for child in node.characters:
            if child and len(user_contact_numbers) < search_limit:
                self._get_user_contacts(child, user_contact_numbers, search_limit)

    ###########################################

    def build(self, contact_numbers):
        """
        Method to be used for initial build.
        """
        for contact_number in contact_numbers:
            self.insert(contact_number)

    def insert(self, contact_number: str):
        node = self.root

        for ch in contact_number:
            if node.characters[ord(ch)]:
                node = node.characters[ord(ch)]
                continue

            node.characters[ord(ch)] = TrieNode()
            node = node.characters[ord(ch)]
        
        node.completion_status = True
        node.node_values.append(contact_number)
    
    def remove(self, contact_number: str):
        """
        Set word completion status for the contact number to False.
        """
        node = self.root

        for ch in contact_number:
            if node.characters[ord(ch)]:
                node = node.characters[ord(ch)]
                continue
        
            warnings.warn(f"Phone number {contact_number} does not exist. Nothing"
                          "removed from trie store.")
            return
        
        node.completion_status = False
        node.node_values = []
    
    def search_contact_number_prefix(self, contact_prefix, search_limit = 5):
        """
        Reach to the point containing the prefix, then return all contact numbers
        that are possible for that prefix. Search will restrict to search_limit
        i.e. will only return 5 contacts. This way system will not perform 
        unnecessary processing beacuse client/frontent mostly shows 5-10 results
        in dropdown.

        :return : This method will return all user_ids i.e. contact numbers of
                  all the users with given contact_prefix. These user ids can 
                  be used to retrieve actual user instance from 
                  TrueCallerUserService.
        """
        # Reach to the node covering contact_prefix.
        node = self.root

        for ch in contact_prefix:
            if node.characters[ord(ch)]:
                node = node.characters[ord(ch)]
                continue
            
            warnings.warn(f"No word found for prefix {contact_prefix}")
            return []
        
        if node.completion_status:
            return [contact_prefix]
    
        # Search for all users with contact_prefix as prefix only upto search_limit
        # i.e. 5 contacts are enough for now.
        user_contact_numbers = []
        self._get_user_contacts(node, user_contact_numbers, search_limit)

        return user_contact_numbers
    