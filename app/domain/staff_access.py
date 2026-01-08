from app.menu.food_menu import Food_menu
from app.menu.all_menu import Menu
from app.domain.take_order import Order_Take
class Staff_handle:
    @staticmethod
    def menu_show_staff(email):
        while True:
            choice=Menu.staff_menu()
            if choice==1:
                Food_menu.food_items()
            elif choice ==2:
                Order_Take.take_order()
            elif choice==7:
                print("Logout Successfull...")
                break   
            else:
                print("Invalid Choice.") 