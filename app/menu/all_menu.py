from app.validation.all_validation import Validation
from colorama import Fore , init
init(autoreset=True)
class Menu:
    @staticmethod
    def main_menu():
        print(Fore.BLUE+"<>"*13)
        print(Fore.LIGHTYELLOW_EX+"======= Main Menu =======")
        print(Fore.BLUE+"<>"*13)
        print(Fore.GREEN+"1. Login")
        print(Fore.GREEN+"2. Register")
        print(Fore.GREEN+"3. Exit")

    @staticmethod
    def admin_menu():
        print(Fore.BLUE+"<>"*14)
        print(Fore.LIGHTYELLOW_EX+">>>>>>Admin Dashboard<<<<<<<")
        print(Fore.BLUE+"<>"*14)
        print(Fore.GREEN+"1. Manage Menu")
        print(Fore.GREEN+"2. Manage Orders") 
        print(Fore.GREEN+"3. Manage Staff")
        print(Fore.GREEN+"4. Manage Tables")
        print(Fore.GREEN+"5. View Reports")
        print(Fore.GREEN+"6. Back")
        choice=Validation.menu_choice()
        return choice
    @staticmethod
    def staff_menu():
        print(Fore.BLUE+"<>"*14)
        print(Fore.LIGHTYELLOW_EX+">>>>>>Staff Dashboard<<<<<<<")
        print(Fore.BLUE+"<>"*14)
        print(Fore.GREEN+"1. Take Orders")
        print(Fore.GREEN+"2. View Orders") 
        print(Fore.GREEN+"3. Update Order Status")
        print(Fore.GREEN+"4. Generate Bill")
        print(Fore.GREEN+"5. Table Booking")
        print(Fore.GREEN+"6. Back")
        choice=Validation.menu_choice()
        return choice
