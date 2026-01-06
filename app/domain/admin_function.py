from app.menu.food_menu import Food_menu
class Admin_handle:
    @staticmethod
    def menu_show(choice):
        if choice==1:
             Food_menu.food_items()
             return
        else:
            print("Invalid Input.")     


