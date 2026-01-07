from app.domain.manage_menu_item import Manage_item

class Manage_menu:
    def menu_manage(choice,email):
        if choice==1:
            Manage_item.add_item()
        elif choice==2:
            Manage_item.delete_item()
        elif choice==3:
            Manage_item.update_item(email)          
        else: 
            print("Invalid Choice.")   

