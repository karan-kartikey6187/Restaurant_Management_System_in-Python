from app.domain.read_write import ReadWrite
from app.model.json_file import Path
from colorama import Fore, init
import re
init(autoreset=True)

class Order_Take:

    @staticmethod
    def take_order():
        
        inventory_data = ReadWrite.read(Path.inventory_data_path)
        inventory_list = inventory_data["inventory"]

        print(Fore.LIGHTYELLOW_EX + "\nAvailable Items:")
        for item in inventory_list:
            print(Fore.LIGHTBLUE_EX + "- " + Fore.BLUE + item["name"])

        while True:
            item_name = input(Fore.WHITE + "\nEnter item name: ").strip()

            if not item_name:
                print(Fore.RED + "Item name cannot be empty.")
                continue

            if not re.match(r"^[A-Za-z ]+$", item_name):
                print(Fore.RED + "Item name must contain only letters and spaces.")
                continue

            item_name = item_name.title()

            found_item = next(
                (item for item in inventory_list if item["name"] == item_name),
                None
            )

            if not found_item:
                print(Fore.RED + "Item not found in inventory.")
            else:
                break

        size = None
        if found_item.get("category") != "breads" and "available_half_qty" in found_item:
            while True:
                size = input(Fore.WHITE + "Half or Full: ").strip().lower()
                if size not in ("half", "full"):
                    print(Fore.RED + "Please enter 'half' or 'full' only.")
                else:
                    break
        while True:
            try:
                qty = int(input(Fore.WHITE + "Enter quantity: "))
                if qty <= 0:
                    print(Fore.RED + "Quantity must be greater than 0.")
                else:
                    break
            except ValueError:
                print(Fore.RED + "Quantity must be a number.")

        category = found_item.get("category")

        if category == "breads":
            if found_item["available_half_qty"] < qty:
                print(Fore.RED + "\nNot enough stock available")
                print(Fore.WHITE + f"Available: {found_item['available_half_qty']}")
                return

            found_item["available_half_qty"] -= qty
            print(Fore.WHITE + f"Remaining stock: {found_item['available_half_qty']}")

        elif "available_half_qty" in found_item:
            required_qty = qty if size == "half" else qty * 2

            if found_item["available_half_qty"] < required_qty:
                print(Fore.RED + "\nNot enough stock available")
                print(Fore.WHITE + f"Available (half units): {found_item['available_half_qty']}")
                return

            found_item["available_half_qty"] -= required_qty
            print(Fore.WHITE + f"Remaining stock (half units): {found_item['available_half_qty']}")

        else:
            if found_item.get("available_qty", 0) < qty:
                print(Fore.RED + "\nNot enough stock available")
                print(Fore.WHITE + f"Available: {found_item.get('available_qty', 0)}")
                return

            found_item["available_qty"] -= qty
            print(Fore.WHITE + f"Remaining stock: {found_item['available_qty']}")

        ReadWrite.write_json(inventory_data, Path.inventory_data_path)
        print(Fore.GREEN + "\nOrder placed successfully")
