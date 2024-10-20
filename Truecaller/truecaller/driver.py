"""
Main application class which will include all the driver
code to test the design.

1. Register User [x]
2. Search by contact number prefix [x]  
3. Search by name prefix. [x]
4. Report spam. 
6. Block users.
7. Unblock user.
8. Direct Search by contact number. (Whenever user recieves call on device, truecaller should
   return user associated with contact number to client) [x]

"""
from Truecaller.truecaller.services.truecaller_directory_service import TrueCallerDirectoryService
from Truecaller.truecaller.services.truecaller_user_service      import TrueCallerUserService


true_caller_service = TrueCallerUserService()
true_caller_directory_service = TrueCallerDirectoryService()


# Prerequisites
# 1. Register truecaller global directory service to user service as an
#    observer, this is to ensure if there is any crud operation on user, 
#    directory service will update data stored in directory.
true_caller_service.register_observer(true_caller_directory_service)

# Register three users
true_caller_service.register_user("568993893", "Aryan", "Aryan")
true_caller_service.register_user("577223337", "Raghav", "Raghav")
true_caller_service.register_user("577980278", "Emily", "Emily")

# Search users by contact number prefix.
print(true_caller_directory_service.search_by_number_prefix("577"))
print(true_caller_directory_service.search_by_number_prefix("56"))

# Search users by name prefix.
print(true_caller_directory_service.search_by_name_prefix("Ar"))
print(true_caller_directory_service.search_by_name_prefix("Sh"))
