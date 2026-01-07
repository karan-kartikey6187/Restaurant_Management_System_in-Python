from app.menu.food_menu import Food_menu
from app.domain.manage_menu import Manage_menu
from app.menu.all_menu import Menu
class Admin_handle:
    @staticmethod
    def menu_show(choice,email):
        if choice==1:
             Food_menu.food_items()
             return
        elif choice ==2:
             while True:
               choice=Menu.manage_food_menu()
               if choice==4:
                   break
               Manage_menu.menu_manage(choice,email)     
