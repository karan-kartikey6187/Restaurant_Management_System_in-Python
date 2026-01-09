from app.domain.read_write import ReadWrite
from app.model.error_module import Module
from app.model.logs_path import Logs
from app.validation.all_validation import Validation
from app.model.json_file import Path
from colorama import Fore , init
init(autoreset=True)

class Manage_item:

    @staticmethod
    def add_item():
        data=ReadWrite.read(Path.food_item_path)

        inventory_data=ReadWrite.read(Path.inventory_data_path)

        category = input(Fore.GREEN + "Category (starters/main_course/breads/drinks/desserts): ").strip().lower()

        if category not in data["menu"]:
            print(Fore.RED + "Invalid category")
            return

        name = input("Item name: ").strip().title()

        if not name.replace(" ", "").isalpha():
            print(Fore.RED + "Invalid Name. Use letters only.")
            return

        if not name:
            print(Fore.RED + "Item name cannot be empty")
            return

        for item in data["menu"][category]:
            if item["name"] == name:
                print(Fore.RED + "Item already exists")
                return

        try:
            if category in ["starters", "main_course"]:
                food_type = input("Type (veg/non-veg): ").lower()

                if food_type not in ["veg", "non-veg"]:
                    print(Fore.RED + "Invalid food type")
                    return

                half = int(input("Half price: "))
                full = int(input("Full price: "))

                if half <= 0 or full <= 0:
                    print(Fore.RED + "Price must be greater than 0")
                    return

                item = {
                    "name": name,
                    "type": food_type,
                    "price": {"half": half, "full": full}
                }

            elif category == "breads":
                price = int(input("Price: "))

                if price <= 0:
                    print(Fore.RED + "Price must be greater than 0")
                    return

                item = {"name": name, "price": price}

            else:
                half = int(input("Half price: "))
                full = int(input("Full price: "))

                if half <= 0 or full <= 0:
                    print(Fore.RED + "Price must be greater than 0")
                    return

                item = {
                    "name": name,
                    "price": {"half": half, "full": full}
                }

            quantity = Validation.opening_qty()


            if category == "breads":
                inventory_data["inventory"].append({
                    "name": name,
                    "category": category,
                    "available_qty": quantity
                })
            else:
                inventory_data["inventory"].append({
                    "name": name,
                    "category": category,
                    "available_half_qty": quantity
                })

            data["menu"][category].append(item)
            ReadWrite.write_json(data,Path.food_item_path)
            
            ReadWrite.write_json(inventory_data,Path.inventory_data_path)

            print(Fore.GREEN + "Item added successfully")

        except ValueError:
            print(Fore.RED + "Price must be a number")


    @staticmethod
    def delete_item():
        
        data = ReadWrite.read(Path.food_item_path)
        inventory_data = ReadWrite.read(Path.inventory_data_path)

        category = input(Fore.BLUE + "Category (starters/main_course/breads/drinks/desserts): ").strip().lower()

        if category not in data["menu"]:
            print(Fore.RED + "Invalid category")
            return

        items = data["menu"][category]

        print(Fore.LIGHTYELLOW_EX + "\nAvailable items:")
        for item in items:
            print("-", item["name"])

        name_to_delete = input(Fore.BLUE + "Item name to delete: ").strip().lower()

        for item in items:
            if item["name"].strip().lower() == name_to_delete:
                items.remove(item) 

                inventory_items = inventory_data["inventory"]
                for inventory in inventory_items[:]: 
                    if (inventory["name"].strip().lower() == name_to_delete and inventory["category"] == category):
                        inventory_items.remove(inventory)

                ReadWrite.write_json(data, Path.food_item_path)
                ReadWrite.write_json(inventory_data, Path.inventory_data_path)

                print(Fore.GREEN + "Item deleted from menu and inventory successfully")
                return

        print(Fore.RED + "Item not found")


    @staticmethod
    def update_item(email):
        data = ReadWrite.read(Path.food_item_path)
        inventory_data = ReadWrite.read(Path.inventory_data_path)

        category = input(Fore.BLUE + "Category (starters/main_course/breads/drinks/desserts): ").strip().lower()

        if category not in data["menu"]:
            print(Fore.RED + "Invalid category")
            return

        items = data["menu"][category]
        inventory_items = inventory_data["inventory"]

        print(Fore.LIGHTYELLOW_EX + "\nAvailable items:")
        for item in items:
            print("-", item["name"])

        search_name = input(Fore.BLUE + "\nItem name to update: ").strip().lower()

        for item in items:
            if item["name"].strip().lower() == search_name:

                old_name = item["name"] 

                print(Fore.BLUE + "\n1. Update Name")
                print(Fore.BLUE + "2. Update Price")

                if category in ["starters", "main_course"]:
                    print(Fore.BLUE + "3. Update Type (veg / non-veg)")

                choice = Validation.menu_choice()

                if choice == 1:
                    new_name = input(Fore.BLUE + "New name: ").strip().title()

                    if not new_name:
                        print(Fore.RED + "Name cannot be empty")
                        return

                    item["name"] = new_name

                    for inv in inventory_items:
                        if (inv["name"].strip().lower() == old_name.strip().lower()and inv["category"] == category):
                            inv["name"] = new_name
                            break

                elif choice == 2:
                    try:
                        if isinstance(item["price"], dict):
                            print(Fore.CYAN + "1. Update Half Price")
                            print(Fore.CYAN + "2. Update Full Price")
                            print(Fore.CYAN + "3. Update Both")

                            price_choice = Validation.menu_choice()

                            if price_choice == 1:
                                item["price"]["half"] = int(input(Fore.LIGHTYELLOW_EX + "New half price: "))

                            elif price_choice == 2:
                                item["price"]["full"] = int(input(Fore.LIGHTYELLOW_EX + "New full price: "))

                            elif price_choice == 3:
                                item["price"]["half"] = int(input(Fore.LIGHTYELLOW_EX + "New half price: "))
                                item["price"]["full"] = int(input(Fore.LIGHTYELLOW_EX + "New full price: "))
                            else:
                                print(Fore.RED + "Invalid choice")
                                return
                        else:
                            item["price"] = int(input(Fore.LIGHTYELLOW_EX + "New price: "))

                    except ValueError as e:
                        print(Fore.RED + "Invalid price")
                        ReadWrite.log_error(Logs.update_item, str(e), email, Module.update)
                        return

                elif choice == 3 and category in ["starters", "main_course"]:
                    while True:
                        new_type = input(Fore.BLUE + "New type (veg/non-veg): ").strip().lower()

                        if new_type in ["veg", "v"]:
                            item["type"] = "veg"
                            break
                        elif new_type in ["non-veg", "nonveg", "n"]:
                            item["type"] = "non-veg"
                            break
                        else:
                            print(Fore.RED + "Invalid type. Enter veg or non-veg.")
                else:
                    print(Fore.RED + "Invalid option")
                    return
                
                ReadWrite.write_json(data, Path.food_item_path)
                ReadWrite.write_json(inventory_data, Path.inventory_data_path)

                print(Fore.GREEN+"Menu item & inventory updated successfully")
                return

        print(Fore.RED + "Item not found")

    
