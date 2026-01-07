from app.domain.manage_menu_item import Manage_item

class Manage_menu:
    def menu_manage(choice):
        if choice==1:
            Manage_item.add_item()
        elif choice==2:
            Manage_item.delete_item()
        else: 
            print("Invalid Choice.")   

