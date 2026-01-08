from app.domain.read_write import ReadWrite
from colorama import Fore , init
init(autoreset=True)

class Order_Take:
    def take_order():
        inventory_data = ReadWrite.read_inventory()
        inventory_list = inventory_data["inventory"]

        print(Fore.LIGHTYELLOW_EX+"\nAvailable Items:")
        for item in inventory_list:
            print(Fore.LIGHTBLUE_EX+"-",Fore.BLUE+ item["name"])

        while True:
            item_name = input(Fore.WHITE+"\nEnter item name: ").strip()

            if not item_name:
                print(Fore.RED+"Item name cannot be empty.")
                continue

            if not item_name.replace(" ", "").isalpha():
                print(Fore.RED+"Item name must contain only letters.")
                continue

            item_name = item_name.title()

            found_item = None
            for item in inventory_list:
                if item["name"] == item_name:
                    found_item = item
                    break

            if not found_item:
                print(Fore.RED+"Item not found in inventory. Please enter a valid item name.")
            else:
                break

        while True:
            size = input(Fore.WHITE+"Half or Full: ").strip().lower()
            if size not in ["half", "full"]:
                print(Fore.RED+"Please enter 'half' or 'full' only.")
            else:
                break

        while True:
            try:
                qty = int(input(Fore.WHITE+"Enter quantity: "))
                if qty <= 0:
                    print(Fore.RED+"Quantity must be greater than 0.")
                else:
                    break
            except ValueError:
                print(Fore.RED+"Quantity must be a number.")

        required_half_qty = qty if size == "half" else qty * 2

        if found_item["available_half_qty"] >= required_half_qty:
            found_item["available_half_qty"] -= required_half_qty
            ReadWrite.write_inventory(inventory_data)

            print(Fore.GREEN+"\nOrder placed successfully")
            print(Fore.WHITE+f"Remaining stock (half): {found_item['available_half_qty']}")
        else:
            print(Fore.RED+"\nNot enough stock available")
            print(Fore.WHITE+f"Available (half): {found_item['available_half_qty']}")
