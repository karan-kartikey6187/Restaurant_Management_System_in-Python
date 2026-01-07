from app.domain.read_write import ReadWrite
from app.model.error_module import Module
from app.model.logs_path import Logs
from colorama import Fore , init
init(autoreset=True)

class Manage_item:
    @staticmethod
    def add_item():
        data = ReadWrite.read_food_data()

        category = input(Fore.GREEN+"Category (starters/main_course/breads/drinks/desserts): ").strip()

        name = input("Item name: ").title()

        if category in ["starters", "main_course"]:
            food_type = input("Type (veg/non-veg): ")
            half = int(input("Half price: "))
            full = int(input("Full price: "))

            item = {
                "name": name,
                "type": food_type,
                "price": {"half": half, "full": full}
            }

        elif category == "breads":
            price = int(input("Price: "))
            item = {"name": name, "price": price}

        else:
            half = int(input("Half price: "))
            full = int(input("Full price: "))

            item = {
                "name": name,
                "price": {"half": half, "full": full}
            }

        data["menu"][category].append(item)
        ReadWrite.write_json_food(data)

        print("Item added successfully")

    @staticmethod
    def delete_item():
        data = ReadWrite.read_food_data()
        category = input(Fore.BLUE+"Category (starters/main_course/breads/drinks/desserts): ").strip()

        if category not in data["menu"]:
            print(Fore.RED+"Invalid category")
            return

        name = input(Fore.BLUE+"Item name to delete: ").strip().lower()

        items = data["menu"][category]

        for item in items:
            item_name = item["name"].strip().lower()

            if item_name == name:
                items.remove(item)
                ReadWrite.write_json_food(data)
                print(Fore.GREEN+"Item deleted successfully")
                return

        print(Fore.RED+"Item not found")

    @staticmethod
    def update_item(email):
        data = ReadWrite.read_food_data()
        category = input(Fore.BLUE+"Category (starters/main_course/breads/drinks/desserts): ").strip()

        if category not in data["menu"]:
            print(Fore.RED+"Invalid category")
            return

        items = data["menu"][category]

        print(Fore.LIGHTYELLOW_EX+"\nAvailable items:")
        for item in items:
            print("-", item["name"])

        name = input(Fore.BLUE+"\nItem name to update: ").strip().lower()

        for item in items:
            if item["name"].strip().lower() == name:

                print(Fore.BLUE+"\n1. Update Name")
                print(Fore.BLUE+"2. Update Price")
                print(Fore.BLUE+"3. Update Type (veg / non-veg)")
                choice = input(Fore.WHITE+"Choose option: ")

                if choice == "1":
                    item["name"] = input(Fore.BLUE+"New name: ").strip()

                elif choice == "2":
                        try:
                            if isinstance(item["price"], dict):
                                item["price"]["half"] = int(input(Fore.LIGHTYELLOW_EX+"New half price: "))
                                item["price"]["full"] = int(input(Fore.LIGHTYELLOW_EX+"New full price: "))
                            else:
                                item["price"] = int(input("New price: "))
                        except Exception as e:
                                print(Fore.RED+"Invalid Price.")
                                module=Module.update
                                path=Logs.update_item
                                ReadWrite.log_error(path,str(e),email,module)
                                

                elif choice == "3":
                    item["type"] = input(Fore.BLUE+"New type (veg/non-veg): ").strip()

                else:
                    print(Fore.RED+"Invalid option")
                    return

                ReadWrite.write_json_food(data)    

                print(Fore.GREEN+"Menu item updated successfully")
                return

        print(Fore.RED+"Item not found")
    
