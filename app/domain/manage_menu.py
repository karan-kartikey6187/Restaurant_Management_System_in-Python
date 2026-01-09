from app.domain.manage_menu_item import Manage_item
from app.menu.all_menu import Menu
from colorama import Fore , init
init(autoreset=True)
class Manage_menu:
    def menu_manage(email):
        while True:
            choice=Menu.manage_food_menu()
            if choice==1:
                Manage_item.add_item()
            elif choice==2:
                Manage_item.delete_item()
            elif choice==3:
                Manage_item.update_item(email)
            elif choice==4:
                break              
            else: 
                print(Fore.RED+"Invalid Choice Enter Choice(1-4)")   

