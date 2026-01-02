from app.validation.all_validation import Validation
class Menu:
    def main_menu(self):
        print("\n===== Main Menu =====")
        print("1. Login")
        print("2. Register")
        print("3. Exit")
        choice=Validation.main_menu_choice(self)
        return choice
    
    def admin_menu(self):
        while True:
            print(">>>>>>>>Admin Dashboard<<<<<<<<<")
            print("1. Manage Menu")
            print("2. Manage Orders") 
            print("3. Manage Staff")
            print("4. Manage Tables")
            print("5. View Reports")
            print("6. Back")
            choice=Validation.main_menu_choice(self)
            return choice

    def staff_menu(self):
        while True:
            print(">>>>>>>>Staff Dashboard<<<<<<<<<")
            print("1. Take Orders")
            print("2. View Orders") 
            print("3. Update Order Status")
            print("4. Generate Bill")
            print("5. Table Booking")
            print("6. Back")
            choice=Validation.main_menu_choice(self)
            return choice

            