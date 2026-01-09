from app.menu.all_menu import Menu
from app.auth.staff_registation import Staff
from app.domain.read_write import ReadWrite
from app.model.json_file import Path
from app.auth.login import Login
from app.validation.all_validation import Validation
from colorama import Fore , init
init(autoreset=True)

class Main():
    """
    Displays the main menu options to the user and
    handles user selection for navigation.
    """
    @staticmethod
    def dashboard_menu():
        all_data=[]
        while True:
            Menu.main_menu()
            choice=Validation.menu_choice()
            if choice==1:
                Login.login_user() 
            elif choice==2:
                data=Staff.register()
                all_data=ReadWrite.read(Path.staff_data_path)
                all_data.append(data)
                ReadWrite.write_json(all_data,Path.staff_data_path)
            elif choice==3:
                print(Fore.GREEN+"Exit Successfull....")
                break   
            else:
                print(Fore.RED+"Please Enter The Number Between(1-3)")







        
