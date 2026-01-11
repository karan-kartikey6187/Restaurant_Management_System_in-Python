from app.domain.read_write import ReadWrite
from app.model.json_file import Path
import re
from datetime import datetime
from app.model.colors import Color

class Order_Take:

    @staticmethod
    def input_booking_id():
        while True:
            booking_id = input(Color.BRIGHT_BLUE+"Enter booking id (6 chars): "+Color.YELLOW).strip().upper()

            if booking_id == "":
                print(Color.RED+"Booking id cannot be empty.")
                continue

            if re.fullmatch(r"[A-F0-9]{6}", booking_id) is None:
                print(Color.RED+"Invalid booking id. Example: A1B2C3")
                continue

            return booking_id

    @staticmethod
    def input_item_name(inventory_list):
        while True:
           item_name = input(Color.BRIGHT_BLUE+"\nEnter item name: "+Color.YELLOW).strip()

           if not item_name:
               print(Color.RED+"Item name cannot be empty.")
               continue

           if not re.fullmatch(r"[A-Za-z]+(?: [A-Za-z]+)*", item_name):
               print(Color.RED+"Item name must contain only letters and single spaces.")
               continue

           item_name = item_name.title()

           found_item = next((item for item in inventory_list if item.get("name") == item_name), None)
           if not found_item:
               print(Color.RED+"Item not found in inventory.")
               continue

           return found_item

    @staticmethod
    def input_size_if_needed(found_item):
        if found_item.get("category") != "breads" and "available_half_qty" in found_item:
            while True:
                size = input(Color.BRIGHT_BLUE+"Half or Full: "+Color.YELLOW).strip().lower()
                if size in ("half", "full"):
                    return size
                print(Color.RED+"Please enter 'half' or 'full' only.")
        return "none"

    @staticmethod
    def input_quantity():
        while True:
            try:
                qty = int(input(Color.BRIGHT_BLUE+"Enter quantity: "+Color.YELLOW))
                if qty <= 0:
                    print(Color.RED+"Quantity must be greater than 0.")
                    continue
                return qty
            except ValueError:
                print(Color.RED+"Quantity must be a number.")

    @staticmethod
    def take_order():

        booking_id = Order_Take.input_booking_id()

        reservations_data = ReadWrite.read(Path.reservations_data_path)
        if not reservations_data or "reservations" not in reservations_data:
            print(Color.RED+"Reservations data not found.")
            return

        reservations_list = reservations_data["reservations"]
        matched_reservation = next(
            (r for r in reservations_list
             if r.get("reservation_id") == booking_id and r.get("status") == "booked"),
            None
        )

        if matched_reservation is None:
            print(Color.RED+"No table booked with this booking id.")
            return

        customer_name = matched_reservation.get("customer_name", "N/A")
        table_id = matched_reservation.get("table_id")
        table_name = matched_reservation.get("table_name", "N/A")
        booking_date = matched_reservation.get("date", "N/A")
        booking_slot = matched_reservation.get("time_slot", "N/A")

        print(Color.GREEN+f"Booking found: {Color.CYAN}{table_name} | {booking_date} | {booking_slot}")
        print(Color.YELLOW+f"Customer: {Color.CYAN}{customer_name}")

        orders_data = ReadWrite.read(Path.orders_data_path)
        if not orders_data:
            orders_data = {"orders": []}
        if "orders" not in orders_data:
            orders_data["orders"] = []

        already = next((o for o in orders_data["orders"] if o.get("reservation_id") == booking_id), None)
        if already is not None:
            print(Color.YELLOW+f"Order already exists for this booking id (Order ID: {Color.CYAN}{already.get('order_id')}).")
            return

        inventory_data = ReadWrite.read(Path.inventory_data_path)
        if not inventory_data or "inventory" not in inventory_data:
            print(Color.RED+"Inventory data not found.")
            return

        inventory_list = inventory_data["inventory"]
        if not inventory_list:
            print(Color.RED+"No items available in inventory.")
            return

        order_items = []

        while True:
            print(Color.YELLOW+"\nAvailable Items:")
            for item in inventory_list:
                print(Color.CYAN+"- " + item.get("name", ""))

            found_item = Order_Take.input_item_name(inventory_list)
            size = Order_Take.input_size_if_needed(found_item)
            qty = Order_Take.input_quantity()

            category = found_item.get("category")

            if category == "breads":
                if found_item.get("available_half_qty", 0) < qty:
                    print(Color.RED+"\nNot enough stock available")
                    print(Color.YELLOW+f"Available: {found_item.get('available_half_qty', 0)}")
                    continue
                found_item["available_half_qty"] -= qty
                print(Color.CYAN+f"Remaining stock: {found_item['available_half_qty']}")

            elif "available_half_qty" in found_item:
                required_qty = qty if size == "half" else qty * 2
                if found_item.get("available_half_qty", 0) < required_qty:
                    print(Color.RED+"\nNot enough stock available")
                    print(Color.YELLOW+f"Available (half units): {found_item.get('available_half_qty', 0)}")
                    continue
                found_item["available_half_qty"] -= required_qty
                print(Color.CYAN+f"Remaining stock (half units): {found_item['available_half_qty']}")

            else:
                if found_item.get("available_qty", 0) < qty:
                    print(Color.RED+"\nNot enough stock available")
                    print(Color.YELLOW+f"Available: {found_item.get('available_qty', 0)}")
                    continue
                found_item["available_qty"] -= qty
                print(Color.CYAN+f"Remaining stock: {found_item['available_qty']}")

            existing_item = next(
                (i for i in order_items
                 if i["item_name"] == found_item.get("name")
                 and i["size"] == (size if size else "none")),
                None
            )

            if existing_item:
                existing_item["quantity"] += qty
            else:
                order_items.append({
                    "item_name": found_item.get("name"),
                    "category": category,
                    "size": size if size else "none",
                    "quantity": qty
                })

            ReadWrite.write_json(inventory_data, Path.inventory_data_path)
            print(Color.GREEN+"\nItem added successfully")

            while True:
                more = input(Color.BRIGHT_BLUE+"Add more items? (y/n): "+Color.YELLOW).strip().lower()
                if more in ("y", "n"):
                    break
                print(Color.RED+"Please enter only y or n.")

            if more == "n":
                break

        if not order_items:
            print(Color.RED+"No items added. Order cancelled.")
            return

        current_datetime = datetime.now().strftime("%Y-%m-%d %I:%M %p")
        
        new_order = {
            "order_id": len(orders_data["orders"]) + 1,
            "reservation_id": booking_id,
            "customer_name": customer_name,
            "table_id": table_id,
            "table_name": table_name,
            "order_datetime": current_datetime, 
            "order_status": "pending",
            "items": order_items
        }

        orders_data["orders"].append(new_order)
        ReadWrite.write_json(orders_data, Path.orders_data_path)

        print(Color.GREEN+f"\nOrder placed successfully (Booking ID: {Color.CYAN}{booking_id})")
        print(Color.GREEN+f"Order Time: {Color.CYAN}{current_datetime}")
