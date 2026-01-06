from app.model.json_file import Path
import json
from colorama import Fore , init,Style
init(autoreset=True)

food_json_path=Path.food_item_path

class Food_menu():
    @staticmethod
    def food_items():
        with open(food_json_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        print(Fore.BLUE+"=" * 70)
        print(Fore.YELLOW+f"{data['restaurant_name']:^70}")
        print(Fore.LIGHTYELLOW_EX+f"{data['location']:^70}")
        print(Fore.BLUE+"=" * 70)

        menu = data["menu"]

        for category in ["starters", "main_course"]:
            items = menu[category]

            for food_type in ["veg", "non-veg"]:
                print(Fore.YELLOW+f"\n{category.replace('_', ' ').upper()} - {food_type.upper():^40}")
                print(Fore.RED+"-" * 70)
                print(Fore.GREEN+f"{'ID':<5}{'ITEM NAME':<25}{'HALF':<10}{'FULL'}")
                print(Fore.RED+"-" * 70)

                for item in items:
                    if item["type"] == food_type:
                        print(
                            Fore.BLUE+f"{item['id']:<5}"
                            f"{item['name']:<25}"
                            f"₹{item['price']['half']:<9}"
                            f"₹{item['price']['full']}"
                        )

        print(Fore.GREEN+f"\n{'BREADS':^70}")
        print(Fore.RED+"-" * 70)
        print(Fore.GREEN+f"{'ID':<5}{'ITEM NAME':<35}{'PRICE'}")
        print(Fore.RED+"-" * 70)

        for item in menu["breads"]:
            print(Fore.BLUE+f"{item['id']:<5}{item['name']:<35}₹{item['price']}")

        print(Fore.GREEN+f"\n{'DRINKS':^70}")
        print(Fore.RED+"-" * 70)
        print(Fore.GREEN+f"{'ID':<5}{'ITEM NAME':<25}{'HALF':<10}{'FULL'}")
        print(Fore.RED+"-" * 70)

        for item in menu["drinks"]:
            print(
                Fore.BLUE+f"{item['id']:<5}"
                f"{item['name']:<25}"
                f"₹{item['price']['half']:<9}"
                f"₹{item['price']['full']}"
            )

        print(Fore.GREEN+f"\n{'DESSERTS':^70}")
        print(Fore.RED+"-" * 70)
        print(Fore.GREEN+f"{'ID':<5}{'ITEM NAME':<25}{'HALF':<10}{'FULL'}")
        print(Fore.RED+"-" * 70)

        for item in menu["desserts"]:
            print(
                Fore.BLUE+f"{item['id']:<5}"
                +Fore.BLUE+f"{item['name']:<25}"
                +Fore.BLUE+f"₹{item['price']['half']:<9}"
                f"₹{item['price']['full']}"
            )

        print(Fore.LIGHTYELLOW_EX+"=" * 70)
        print(Fore.LIGHTMAGENTA_EX+"[ THANK YOU FOR VISITING ]".center(70))
        print(Fore.LIGHTYELLOW_EX+"=" * 70)

