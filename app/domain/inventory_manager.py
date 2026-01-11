from app.domain.read_write import ReadWrite
from app.model.json_file import Path
from app.validation.all_validation import Validation
from app.model.colors import Color

class InventoryManager:
    @staticmethod
    def manage_inventory():
        print(Color.YELLOW+"\n")
        print(Color.BRIGHT_BLUE+"=" * 50)
        print(Color.YELLOW+"MANAGE INVENTORY")
        print(Color.BRIGHT_BLUE+"=" * 50)
        
        while True:
            print(Color.WHITE+"\n1. View Low Stock (<100)")
            print(Color.WHITE+"2. View All Inventory")
            print(Color.WHITE+"3. Add Stock")
            print(Color.WHITE+"0. Back")
            print(Color.BRIGHT_BLUE+"-" * 50)
            
            choice = Validation.menu_choice()
            
            if choice == 0:
                break
            elif choice == 1:
                InventoryManager.view_low_stock()
            elif choice == 2:
                InventoryManager.view_all()
            elif choice == 3:
                InventoryManager.add_stock()
            else:
                print(Color.RED+"Invalid option!")
            
            input(Color.YELLOW+"\nPress Enter...")

    @staticmethod
    def get_inventory():
        inventory_data = ReadWrite.read(Path.inventory_data_path)
        return inventory_data.get("inventory", [])

    @staticmethod
    def save_inventory(inventory):
        inventory_data = {"inventory": inventory}
        ReadWrite.write_json(inventory_data, Path.inventory_data_path)

    @staticmethod
    def view_low_stock():
        inventory = InventoryManager.get_inventory()
        low_stock = [item for item in inventory if item.get("available_half_qty", 0) < 100]
        
        print(Color.RED+"\nLOW STOCK ITEMS (<100):")
        print(Color.BRIGHT_BLUE+"=" * 50)
        
        if low_stock:
            print(Color.WHITE+f"{'No':<4} {'Item':<30} {'Stock'}")
            print(Color.BRIGHT_BLUE+"-" * 50)
            for i, item in enumerate(low_stock):
                qty = item.get("available_half_qty", 0)
                print(Color.WHITE+f"{i+1:<4} {item.get('name', 'N/A')[:29]:<30} "+Color.RED+f"{qty}")
        else:
            print(Color.GREEN+"No low stock items!")
        
        print(Color.BRIGHT_BLUE+"=" * 50)

    @staticmethod
    def view_all():
        inventory = InventoryManager.get_inventory()
        
        print(Color.YELLOW+"\nALL INVENTORY:")
        print(Color.BRIGHT_BLUE+"=" * 50)
        print(Color.WHITE+f"{'No':<4} {'Item':<30} {'Category':<15} {'Stock'}")
        print(Color.BRIGHT_BLUE+"-" * 50)
        
        for i, item in enumerate(inventory):
            qty = item.get("available_half_qty", 0)
            stock_color = Color.RED if qty < 100 else Color.GREEN
            print(Color.WHITE+f"{i+1:<4} {item.get('name', 'N/A')[:29]:<30} {item.get('category', 'N/A'):<15} "+stock_color+f"{qty}")
        
        print(Color.BRIGHT_BLUE+"-" * 50)

    @staticmethod
    def add_stock():
        inventory = InventoryManager.get_inventory()
        
        if not inventory:
            print(Color.RED+"No inventory items!")
            return
        
        print(Color.YELLOW+"\nSELECT ITEM TO ADD STOCK:")
        print(Color.BRIGHT_BLUE+"-" * 50)
        print(Color.WHITE+f"{'No':<4} {'Item':<30} {'Stock'}")
        print(Color.BRIGHT_BLUE+"-" * 50)
        
        for i, item in enumerate(inventory):
            qty = item.get("available_half_qty", 0)
            stock_color = Color.RED if qty < 100 else Color.GREEN
            print(Color.WHITE+f"{i+1:<4} {item.get('name', 'N/A')[:29]:<30} "+stock_color+f"{qty}")
        
        print(Color.BRIGHT_BLUE+"-" * 50)
        
        try:
            choice = int(input(Color.BRIGHT_BLUE+"Enter item number: "))
            if 1 <= choice <= len(inventory):
                item = inventory[choice-1]
                item_name = item.get('name', 'Unknown')
                current_stock = item.get('available_half_qty', 0)
                
                print(Color.YELLOW+f"\n{item_name}")
                print(Color.CYAN+f"Current Stock: {current_stock}")
                
                add_qty = int(input(Color.BRIGHT_BLUE+"Add quantity: "))
                
                if add_qty > 0:
                    new_stock = current_stock + add_qty
                    item['available_half_qty'] = new_stock
                    InventoryManager.save_inventory(inventory)
                    
                    status = Color.GREEN+"OK" if new_stock >= 100 else Color.RED+"LOW STOCK"
                    print(Color.GREEN+f"\nUpdated: {current_stock} → {new_stock} ({status})")
                else:
                    print(Color.RED+"Quantity must be > 0!")
            else:
                print(Color.RED+"Invalid selection!")
        except ValueError:
            print(Color.RED+"Enter valid number!")
        except Exception as e:
            print(Color.RED+f"Error: {e}")
