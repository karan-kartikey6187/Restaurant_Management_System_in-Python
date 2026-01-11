from app.menu.food_menu import Food_menu
from app.domain.manage_menu import Manage_menu
from app.menu.all_menu import Menu
from app.report.reports import Reports
from app.domain.remove_staff import StaffManager
from app.domain.manage_tables import TableManager
from app.domain.inventory_manager import InventoryManager
from app.model.colors import Color

class Admin_handle:
    @staticmethod
    def menu_show(email):
        while True:
            choice=Menu.admin_menu()
            if choice==1:
                Food_menu.food_items()
            elif choice ==2:
                Manage_menu.menu_manage(email)
            elif choice ==3:
                StaffManager.remove_staff()
            elif choice==4:
                TableManager.manage_tables()    
            elif choice==5:
                Reports.view_reports()
            elif choice==6:
                InventoryManager.manage_inventory()    
            elif choice==7:
                print(Color.RED+"Logout Successfull..."+Color.RESET)
                break   
            else:
                print(Color.RED+"Invalid Choice."+Color.RESET)    
                    
