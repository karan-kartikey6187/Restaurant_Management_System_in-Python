from app.menu.food_menu import Food_menu
from app.domain.manage_menu import Manage_menu
from app.menu.all_menu import Menu
class Admin_handle:
    @staticmethod
    def menu_show(choice):
        if choice==1:
             Food_menu.food_items()
             return
        elif choice ==2:
             choice=Menu.manage_food_menu()
             Manage_menu.menu_manage(choice)

        else:
            print("Invalid Input.")     


