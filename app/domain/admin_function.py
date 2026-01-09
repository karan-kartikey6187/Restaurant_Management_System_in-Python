from app.menu.food_menu import Food_menu
from app.domain.manage_menu import Manage_menu
from app.menu.all_menu import Menu
from colorama import Fore , init
init(autoreset=True)

class Admin_handle:
    @staticmethod
    def menu_show(email):
        while True:
            choice=Menu.admin_menu()
            if choice==1:
                Food_menu.food_items()
            
            elif choice ==2:
                Manage_menu.menu_manage(email)

            elif choice==7:
                print(Fore.GREEN+"Logout Successfull...")
                break   
            else:
                print(Fore.RED+"Invalid Choice.")    
                    
