from app.model.json_file import Path
from app.domain.read_write import ReadWrite
from colorama import Fore, Style, init
init(autoreset=True)

class Food_menu:

    @staticmethod
    def food_items():
        data=ReadWrite.read(Path.food_item_path) 

        print(Fore.CYAN + "=" * 70)
        print(Fore.YELLOW + Style.BRIGHT + f"{data['restaurant_name']:^70}")
        print(Fore.LIGHTWHITE_EX + f"{data['location']:^70}")
        print(Fore.CYAN + "=" * 70)

        menu = data["menu"]

        for category in ["starters", "main_course"]:
            items = menu[category]

            for food_type in ["veg", "non-veg"]:
                title = f"{category.replace('_', ' ').upper()} - {food_type.upper()}"
                color = Fore.GREEN if food_type == "veg" else Fore.LIGHTRED_EX

                print("\n" + color + Style.BRIGHT + title.center(70))
                print(Fore.WHITE + "-" * 70)
                print(Fore.YELLOW + f"{'ITEM NAME':<35}{'HALF':<15}{'FULL'}")
                print(Fore.WHITE + "-" * 70)

                for item in items:
                    if item["type"] == food_type:
                        print(
                            Fore.LIGHTCYAN_EX +
                            f"{item['name']:<35}"
                            f"₹{item['price']['half']:<14}"
                            f"₹{item['price']['full']}"
                        )

        print("\n" + Fore.MAGENTA + Style.BRIGHT + "BREADS".center(70))
        print(Fore.WHITE + "-" * 70)
        print(Fore.YELLOW + f"{'ITEM NAME':<45}{'PRICE'}")
        print(Fore.WHITE + "-" * 70)

        for item in menu["breads"]:
            print(
                Fore.LIGHTCYAN_EX +
                f"{item['name']:<45}"
                f"₹{item['price']}"
            )

        print("\n" + Fore.BLUE + Style.BRIGHT + "DRINKS".center(70))
        print(Fore.WHITE + "-" * 70)
        print(Fore.YELLOW + f"{'ITEM NAME':<35}{'HALF':<15}{'FULL'}")
        print(Fore.WHITE + "-" * 70)

        for item in menu["drinks"]:
            print(
                Fore.LIGHTCYAN_EX +
                f"{item['name']:<35}"
                f"₹{item['price']['half']:<14}"
                f"₹{item['price']['full']}"
            )

        print("\n" + Fore.LIGHTMAGENTA_EX + Style.BRIGHT + "DESSERTS".center(70))
        print(Fore.WHITE + "-" * 70)
        print(Fore.YELLOW + f"{'ITEM NAME':<35}{'HALF':<15}{'FULL'}")
        print(Fore.WHITE + "-" * 70)

        for item in menu["desserts"]:
            print(
                Fore.LIGHTCYAN_EX +
                f"{item['name']:<35}"
                f"₹{item['price']['half']:<14}"
                f"₹{item['price']['full']}"
            )

        print(Fore.CYAN + "=" * 70)
        print(Fore.LIGHTGREEN_EX + Style.BRIGHT + "[ THANK YOU FOR VISITING ]".center(70))
        print(Fore.CYAN + "=" * 70)
