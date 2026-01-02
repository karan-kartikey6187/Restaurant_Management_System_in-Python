from app.validation.all_validation import Validation
from app.menu.all_menu import Menu
import getpass

class Login:
    def login_user(self, all_data):
        print(">>>>>Login-Menu<<<<<<")
        email = Validation.email(self)
        for item in all_data:
            if item["email"] == email:
                password = getpass.getpass("Enter Your Password: ")
                if item["password"] == password:
                    print("Login Successfull.")
                    if item["role"] == "Staff":
                        choice=Menu.staff_menu(self)
                    elif item["role"] == "Admin":
                        choice=Menu.admin_menu(self)
                else:
                    print("Incorrect password!")
                    break
