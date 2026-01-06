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
        print(Fore.GREEN+"1. Login")
        print(Fore.GREEN+"2. Register")
        print(Fore.GREEN+"3. Exit")

    @staticmethod
    def admin_menu():
        """Displays admin options and handles actions."""
        print(Fore.BLUE+"<>"*14)
        print(Fore.LIGHTYELLOW_EX+">>>>>>Admin Dashboard<<<<<<<")
        print(Fore.BLUE+"<>"*14)
        print(Fore.GREEN+"1. View Menu")
        print(Fore.GREEN+"2. Manage Menu")
        print(Fore.GREEN+"3. Manage Orders") 
        print(Fore.GREEN+"4. Manage Staff")
        print(Fore.GREEN+"5. Manage Tables")
        print(Fore.GREEN+"6. View Reports")
        print(Fore.GREEN+"7. Back")
        choice=Validation.menu_choice()
        return choice
    @staticmethod
    def staff_menu():
        """Displays staff options and performs tasks."""
        print(Fore.BLUE+"<>"*14)
        print(Fore.LIGHTYELLOW_EX+">>>>>>Staff Dashboard<<<<<<<")
        print(Fore.BLUE+"<>"*14)
        print(Fore.GREEN+"1. View Menu")
        print(Fore.GREEN+"2. Take Orders")
        print(Fore.GREEN+"3. View Orders") 
        print(Fore.GREEN+"4. Update Order Status")
        print(Fore.GREEN+"5. Generate Bill")
        print(Fore.GREEN+"6. Table Booking")
        print(Fore.GREEN+"7. Back")
        choice=Validation.menu_choice()
        return choice
