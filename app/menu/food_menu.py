from app.model.json_file import Path
import json
food_json_path=Path.food_item_path

class Food_menu():
    def food_items(self):
        with open(food_json_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        print("=" * 70)
        print(f"{data['restaurant_name']:^70}")
        print(f"{data['location']:^70}")
        print("=" * 70)

        menu = data["menu"]

        for category in ["starters", "main_course"]:
            items = menu[category]

            for food_type in ["veg", "non-veg"]:
                print(f"\n{category.replace('_', ' ').upper()} - {food_type.upper():^40}")
                print("-" * 70)
                print(f"{'ID':<5}{'ITEM NAME':<25}{'HALF':<10}{'FULL'}")
                print("-" * 70)

                for item in items:
                    if item["type"] == food_type:
                        print(
                            f"{item['id']:<5}"
                            f"{item['name']:<25}"
                            f"₹{item['price']['half']:<9}"
                            f"₹{item['price']['full']}"
                        )

        print(f"\n{'BREADS':^70}")
        print("-" * 70)
        print(f"{'ID':<5}{'ITEM NAME':<35}{'PRICE'}")
        print("-" * 70)

        for item in menu["breads"]:
            print(f"{item['id']:<5}{item['name']:<35}₹{item['price']}")

        print(f"\n{'DRINKS':^70}")
        print("-" * 70)
        print(f"{'ID':<5}{'ITEM NAME':<25}{'HALF':<10}{'FULL'}")
        print("-" * 70)

        for item in menu["drinks"]:
            print(
                f"{item['id']:<5}"
                f"{item['name']:<25}"
                f"₹{item['price']['half']:<9}"
                f"₹{item['price']['full']}"
            )

        print(f"\n{'DESSERTS':^70}")
        print("-" * 70)
        print(f"{'ID':<5}{'ITEM NAME':<25}{'HALF':<10}{'FULL'}")
        print("-" * 70)

        for item in menu["desserts"]:
            print(
                f"{item['id']:<5}"
                f"{item['name']:<25}"
                f"₹{item['price']['half']:<9}"
                f"₹{item['price']['full']}"
            )

        print("=" * 70)
        print("[ THANK YOU FOR VISITING ]".center(70))
        print("=" * 70)

