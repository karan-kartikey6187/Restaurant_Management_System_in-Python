from app.domain.read_write import ReadWrite

class Manage_item:
    @staticmethod
    def add_item():
        data = ReadWrite.read_food_data()

        category = input(
            "Category (starters/main_course/breads/drinks/desserts): "
        ).strip()

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
        category = input(
            "Category (starters/main_course/breads/drinks/desserts): "
        ).strip()

        if category not in data["menu"]:
            print("Invalid category")
            return

        name = input("Item name to delete: ").strip().lower()

        items = data["menu"][category]

        for item in items:
            item_name = item["name"].strip().lower()

            if item_name == name:
                items.remove(item)
                ReadWrite.write_json_food(data)
                print("Item deleted successfully")
                return

        print("Item not found")
