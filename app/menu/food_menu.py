from app.model.json_file import Path
from app.domain.read_write import ReadWrite
from app.model.colors import Color


class Food_menu:

    @staticmethod
    def food_items():
        data = ReadWrite.read(Path.food_item_path)

        print(Color.YELLOW + "=" * 70 + Color.RESET)
        print(Color.BOLD + Color.BRIGHT_YELLOW + f"{data['restaurant_name']:^70}" + Color.RESET)
        print(Color.CYAN + f"{data['location']:^70}" + Color.RESET)
        print(Color.YELLOW + "=" * 70 + Color.RESET)

        menu = data["menu"]

        for category in ["starters", "main_course"]:
            items = menu[category]

            for food_type in ["veg", "non-veg"]:
                title = f"{category.replace('_', ' ').upper()} - {food_type.upper()}"

                section_color = Color.GREEN if food_type == "veg" else Color.RED

                print("\n" + Color.BOLD + section_color + title.center(70) + Color.RESET)
                print(Color.YELLOW + "-" * 70 + Color.RESET)
                print(
                    Color.CYAN +
                    f"{'ITEM NAME':<35}{'HALF':<15}{'FULL'}" +
                    Color.RESET
                )
                print(Color.YELLOW + "-" * 70 + Color.RESET)

                for item in items:
                    if item["type"] == food_type:
                        print(
                            section_color +
                            f"{item['name']:<35}" +
                            Color.BRIGHT_GREEN +
                            f"₹{item['price']['half']:<14}₹{item['price']['full']}" +
                            Color.RESET
                        )

        print("\n" + Color.BOLD + Color.BRIGHT_BLUE + "BREADS".center(70) + Color.RESET)
        print(Color.YELLOW + "-" * 70 + Color.RESET)
        print(Color.CYAN + f"{'ITEM NAME':<45}{'PRICE'}" + Color.RESET)
        print(Color.YELLOW + "-" * 70 + Color.RESET)

        for item in menu["breads"]:
            print(
                Color.WHITE +
                f"{item['name']:<45}" +
                Color.BRIGHT_GREEN +
                f"₹{item['price']}" +
                Color.RESET
            )

        print("\n" + Color.BOLD + Color.BRIGHT_CYAN + "DRINKS".center(70) + Color.RESET)
        print(Color.YELLOW + "-" * 70 + Color.RESET)
        print(Color.CYAN + f"{'ITEM NAME':<35}{'HALF':<15}{'FULL'}" + Color.RESET)
        print(Color.YELLOW + "-" * 70 + Color.RESET)

        for item in menu["drinks"]:
            print(
                Color.WHITE +
                f"{item['name']:<35}" +
                Color.BRIGHT_GREEN +
                f"₹{item['price']['half']:<14}₹{item['price']['full']}" +
                Color.RESET
            )

        print("\n" + Color.BOLD + Color.BRIGHT_MAGENTA + "DESSERTS".center(70) + Color.RESET)
        print(Color.YELLOW + "-" * 70 + Color.RESET)
        print(Color.CYAN + f"{'ITEM NAME':<35}{'HALF':<15}{'FULL'}" + Color.RESET)
        print(Color.YELLOW + "-" * 70 + Color.RESET)

        for item in menu["desserts"]:
            print(
                Color.WHITE +
                f"{item['name']:<35}" +
                Color.BRIGHT_GREEN +
                f"₹{item['price']['half']:<14}₹{item['price']['full']}" +
                Color.RESET
            )

        print(Color.YELLOW + "=" * 70 + Color.RESET)
        print(Color.BOLD + Color.BRIGHT_MAGENTA + "[ THANK YOU FOR VISITING ]".center(70) + Color.RESET)
        print(Color.YELLOW + "=" * 70 + Color.RESET)
