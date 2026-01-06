from app.menu.all_menu import Menu
from app.auth.staff_registation import Staff
from app.domain.read_write import ReadWrite
from app.model.json_file import Path
from app.auth.login import Login
from app.validation.all_validation import Validation
json_file=Path.staff_data_path

class Main():
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
                all_data=ReadWrite.read()
                all_data.append(data)
                ReadWrite.write_json(all_data)
            elif choice==3:
                break   








        
