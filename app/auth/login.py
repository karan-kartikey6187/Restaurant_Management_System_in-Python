from app.validation.all_validation import Validation
from app.domain.read_write import ReadWrite
from app.model.error_module import Module
from app.domain.admin_function import Admin_handle
from app.domain.staff_access import Staff_handle
from app.model.json_file import Path
from app.model.role_model import Role
from colorama import Fore , init
init(autoreset=True)
import getpass

class Login:
    @staticmethod
    def login_user():
        all_data = ReadWrite.read(Path.staff_data_path)
        print(Fore.BLUE+"="*22)
        print(Fore.YELLOW+">>>>>Login-Menu<<<<<<")
        print(Fore.BLUE+"="*22)
        email=Validation.email(Module.login)
        found = False 
        for item in all_data:
            if item["email"] == email:
                found = True
                password = getpass.getpass(Fore.WHITE+"Enter Your Password: ")

                if item["password"] == password:
                    print(Fore.GREEN+"Login Successful.")

                    if item["role"] == Role.staff:
                            Staff_handle.menu_show_staff(email)

                    elif item["role"] == Role.admin:
                            Admin_handle.menu_show(email)

                else:
                    print(Fore.RED+"Incorrect password!")
                break 
        if not found:
             print(Fore.RED+"Email not found")
