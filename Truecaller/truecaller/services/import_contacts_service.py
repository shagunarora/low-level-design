
class ImportContactService:

    @classmethod
    def import_contacts(cls, user):
        """
        Returning dummy values for now. System can use external
        APIs to fetch contact details stored in phone/simcard 
        based on user phone number, id etc.
        """
        imported_contacts = [{"phone_number": "+91 8900909XX", "name": "Alaya"}, 
                             {"phone_number": "+1 57789XX", "name": "Ben"}, 
                             {"phone_number": "+91 5779990XX", "name": "Jelly"}]
        
        return imported_contacts
    