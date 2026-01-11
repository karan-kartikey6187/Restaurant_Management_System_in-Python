from app.validation.all_validation import Validation
from app.model.colors import Color

class Menu:
    @staticmethod
    def main_menu():
        """Shows main menu options: Login, Register, Exit."""
        print(Color.BRIGHT_BLUE+"--"*13)
        print(Color.YELLOW+"------- Main Menu --------")
        print(Color.BRIGHT_BLUE+"--"*13)
        print(Color.WHITE+"1. Login")
        print(Color.WHITE+"2. Register")
        print(Color.WHITE+"3. Exit")

    @staticmethod
    def admin_menu():
        """Displays admin options and handles actions."""
        print(Color.BRIGHT_BLUE+"--"*14)
        print(Color.YELLOW+">>>>>>Admin Dashboard<<<<<<<")
        print(Color.BRIGHT_BLUE+"--"*14)
        print(Color.WHITE+"1. View Menu")
        print(Color.WHITE+"2. Manage Menu") 
        print(Color.WHITE+"3. Remove Staff")
        print(Color.WHITE+"4. Manage Tables")
        print(Color.WHITE+"5. View Reports")
        print(Color.WHITE+"6. Manage Inventory")
        print(Color.WHITE+"7. Logout.")
        choice=Validation.menu_choice()
        return choice

    @staticmethod
    def staff_menu():
        """Displays staff options and performs tasks."""
        print(Color.BRIGHT_BLUE+"--"*14)
        print(Color.YELLOW+">>>>>>Staff Dashboard<<<<<<<")
        print(Color.BRIGHT_BLUE+"--"*14)
        print(Color.WHITE+"1. View Menu")
        print(Color.WHITE+"2. Take Orders")
        print(Color.WHITE+"3. View Orders")
        print(Color.WHITE+"4. Do Payment") 
        print(Color.WHITE+"5. Generate Bill")
        print(Color.WHITE+"6. Table Booking")
        print(Color.WHITE+"7. Logout.")
        choice=Validation.menu_choice()
        return choice
    
    @staticmethod
    def manage_food_menu ():
        while True:
            print(Color.BRIGHT_BLUE+"--"*14)
            print(Color.YELLOW+">>>>>>>Manage Menu<<<<<<<<")
            print(Color.BRIGHT_BLUE+"--"*14)
            print(Color.WHITE+"1. Add Menu Item")
            print(Color.WHITE+"2. Delete Menu Item") 
            print(Color.WHITE+"3. Update Menu Item")
            print(Color.WHITE+"4. Back")
            choice=Validation.menu_choice()
            return choice
