
import warnings
from typing import List

from ...entities.user.truecaller_user import TrueCallerUser
from .trie_node                       import TrieNode

class UserNameTrie:
    def __init__(self, users):
        self.build(users)
        self.root = TrieNode()

    ############################ Private utility methods ##############################
    def _get_user_contacts(self, node: TrieNode, user_contact_numbers, search_limit):
        
        if node.completion_status:
            user_contact_numbers.extend(node.node_values)
            return

        for child in node.characters:
            if child and len(user_contact_numbers) < search_limit:
                self._get_user_contacts(child, user_contact_numbers, search_limit)

    ####################################################################################

    def build(self, users: List[TrueCallerUser]):
        """
        Method to be used for initial build.
        """
        for user in users:
            self.insert(user.preferred_name, user.phone_number)

    def insert(self, name, contact_number):
        node: TrieNode = self.root

        for ch in name:
            if node.characters[ord(ch)]:
                node = node.characters[ord(ch)]
                continue

            node.characters[ord(ch)] = TrieNode()
            node = node.characters[ord(ch)]
        
        node.completion_status = True
        node.node_values.append(contact_number)
    
    def remove(self, name, contact_number):
        node:TrieNode = self.root

        for ch in name:
            if node.characters[ord(ch)]:
                node = node.characters[ord(ch)]
                continue
        
            warnings.warn(f"Name {name} does not exist. Nothing"
                          "removed from trie store.")
            return
        
        if contact_number in node.node_values:
            node.node_values.remove(contact_number)
        
        if not node.node_values:
            node.completion_status = False

    def search_name_by_prefix(self, name_prefix, search_limit=5):
         # Reach to the node covering contact_prefix.
        node = self.root

        for ch in name_prefix:
            if node.characters[ord(ch)]:
                node = node.characters[ord(ch)]
                continue
            
            warnings.warn(f"No name found for prefix {name_prefix}")
            return []
        
        if node.completion_status:
            return node.node_values
        
         # Search for all users with name_prefix as prefix only upto search_limit
        # i.e. 5 contacts are enough for now.
        user_contact_numbers = []
        self._get_user_contacts(node, user_contact_numbers, search_limit)

        return user_contact_numbers
