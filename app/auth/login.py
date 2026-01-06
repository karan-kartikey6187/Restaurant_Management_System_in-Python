from app.validation.all_validation import Validation
from app.domain.read_write import ReadWrite
from app.menu.all_menu import Menu
from app.model.error_module import Module
from app.domain.admin_function import Admin_handle
from colorama import Fore , init
init(autoreset=True)
import getpass

class Login:
    @staticmethod
    def login_user():
        module=Module.login
        all_data = ReadWrite.read()
        print(Fore.BLUE+"="*22)
        print(Fore.YELLOW+">>>>>Login-Menu<<<<<<")
        print(Fore.BLUE+"="*22)
        email=Validation.email(module)
        found = False 
        for item in all_data:
            if item["email"] == email:
                found = True
                password = getpass.getpass(Fore.WHITE+"Enter Your Password: ")

                if item["password"] == password:
                    print(Fore.GREEN+"Login Successful.")

                    if item["role"] == "Staff":
                        while True:
                            choice=Menu.staff_menu()
                            Admin_handle.menu_show(choice)

                    elif item["role"] == "Admin":
                        while True:
                            choice=Menu.admin_menu()
                            Admin_handle.menu_show(choice)
                else:
                    print(Fore.RED+"Incorrect password!")
                break 
        if not found:
             print(Fore.RED+"Email not found")
