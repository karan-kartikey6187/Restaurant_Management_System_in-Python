from app.validation.all_validation import Validation
from colorama import Fore , init
init(autoreset=True)
class Menu:
    @staticmethod
    def main_menu():
        """Shows main menu options: Login, Register, Exit."""
        print(Fore.BLUE+"<>"*13)
        print(Fore.LIGHTYELLOW_EX+"======= Main Menu =======")
        print(Fore.BLUE+"<>"*13)
        print(Fore.LIGHTYELLOW_EX+"1. Login.")
        print(Fore.LIGHTYELLOW_EX+"2. Register.")
        print(Fore.LIGHTYELLOW_EX+"3. Exit.")

    @staticmethod
    def admin_menu():
        """Displays admin options and handles actions."""
        print(Fore.BLUE+"<>"*14)
        print(Fore.LIGHTYELLOW_EX+">>>>>>Admin Dashboard<<<<<<<")
        print(Fore.BLUE+"<>"*14)
        print(Fore.LIGHTYELLOW_EX+"1. View Menu")
        print(Fore.LIGHTYELLOW_EX+"2. Manage Menu")
        print(Fore.LIGHTYELLOW_EX+"3. Manage Orders") 
        print(Fore.LIGHTYELLOW_EX+"4. Manage Staff")
        print(Fore.LIGHTYELLOW_EX+"5. Manage Tables")
        print(Fore.LIGHTYELLOW_EX+"6. View Reports")
        print(Fore.LIGHTYELLOW_EX+"7. Logout.")
        choice=Validation.menu_choice()
        return choice
    @staticmethod
    def staff_menu():
        """Displays staff options and performs tasks."""
        print(Fore.BLUE+"<>"*14)
        print(Fore.LIGHTYELLOW_EX+">>>>>>Staff Dashboard<<<<<<<")
        print(Fore.BLUE+"<>"*14)
        print(Fore.LIGHTYELLOW_EX+"1. View Menu")
        print(Fore.LIGHTYELLOW_EX+"2. Take Orders")
        print(Fore.LIGHTYELLOW_EX+"3. View Orders") 
        print(Fore.LIGHTYELLOW_EX+"4. Update Order Status")
        print(Fore.LIGHTYELLOW_EX+"5. Generate Bill")
        print(Fore.LIGHTYELLOW_EX+"6. Table Booking")
        print(Fore.LIGHTYELLOW_EX+"7. Logout.")
        choice=Validation.menu_choice()
        return choice
    
    @staticmethod
    def manage_food_menu ():
        while True:
            print(Fore.BLUE+"<>"*14)
            print(Fore.LIGHTYELLOW_EX+">>>>>>>>Manage Menu<<<<<<<<<")
            print(Fore.BLUE+"<>"*14)
            print(Fore.LIGHTYELLOW_EX+"1. Add Menu Item")
            print(Fore.LIGHTYELLOW_EX+"2. Delete Menu Item") 
            print(Fore.LIGHTYELLOW_EX+"3. Update Menu Item")
            print(Fore.LIGHTYELLOW_EX+"4. Back")
            choice=Validation.menu_choice()
            return choice    
    
        
