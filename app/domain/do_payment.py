import re
from datetime import datetime
from app.domain.read_write import ReadWrite
from app.model.json_file import Path
from app.model.colors import Color

class DoPayment:

    @staticmethod
    def input_booking_id():
        while True:
            booking_id = input(
                Color.CYAN + "Enter booking id (6 chars): " + Color.RESET
            ).strip().upper()

            if booking_id == "":
                print(Color.RED + "Booking id cannot be empty." + Color.RESET)
                continue

            if re.fullmatch(r"[A-F0-9]{6}", booking_id) is None:
                print(Color.RED + "Invalid booking id. Example: A1B2C3" + Color.RESET)
                continue

            return booking_id

    @staticmethod
    def input_payment_method():
        while True:
            method = input(
                Color.CYAN + "Payment method (cash/upi/card): " + Color.RESET
            ).strip().lower()

            if method in ("cash", "upi", "card"):
                return method

            print(Color.RED + "Please enter cash, upi, or card only." + Color.RESET)

    @staticmethod
    def get_item_price(menu_data, item_name, size):
        menu = menu_data.get("menu", {})

        for category_items in menu.values():
            for menu_item in category_items:
                if menu_item.get("name") == item_name:
                    price_data = menu_item.get("price", {})

                    if isinstance(price_data, dict):
                        if size in price_data:
                            return price_data[size]
                        return price_data.get("full", price_data.get("half", 0))
                    return price_data
        return 0

    @staticmethod
    def print_bill_table(rows, total):
        print("\n" + Color.YELLOW + "-" * 55 + Color.RESET)
        print(Color.BOLD + Color.BLUE + "No  Item                    Qty  Price  Amt" + Color.RESET)
        print(Color.YELLOW + "-" * 55 + Color.RESET)

        i = 0
        while i < len(rows):
            r = rows[i]
            name = str(r["name"])[:18]
            qty = str(r["qty"])
            price = str(r["price"])
            amt = str(r["amount"])

            line = (
                Color.WHITE +
                f"{str(i+1).ljust(3)} {name.ljust(18)} {qty.rjust(3)} " +
                Color.BRIGHT_GREEN +
                f"{price.rjust(6)} {amt.rjust(6)}" +
                Color.RESET
            )
            print(line)
            i += 1

        print(Color.YELLOW + "-" * 55 + Color.RESET)
        print(Color.BOLD + Color.BRIGHT_GREEN + f"TOTAL: Rs {total:.0f}" + Color.RESET)
        print(Color.YELLOW + "-" * 55 + Color.RESET)

    @staticmethod
    def do_payment():
        booking_id = DoPayment.input_booking_id()

        orders_data = ReadWrite.read(Path.orders_data_path)
        if not orders_data or "orders" not in orders_data:
            print(Color.RED + "Orders data not found." + Color.RESET)
            return

        food_data = ReadWrite.read(Path.food_item_path)
        if not food_data or "menu" not in food_data:
            print(Color.RED + "Food items data not found." + Color.RESET)
            return

        reservations_data = ReadWrite.read(Path.reservations_data_path)
        if not reservations_data or "reservations" not in reservations_data:
            print(Color.RED + "Reservations data not found." + Color.RESET)
            return

        orders_list = orders_data["orders"]
        reservations_list = reservations_data["reservations"]

        booked_res = None
        for r in reservations_list:
            if r.get("reservation_id") == booking_id and r.get("status") == "booked":
                booked_res = r
                break

        if booked_res is None:
            print(Color.RED + "No active table booking found with this booking id." + Color.RESET)
            return

        order_found = None
        for o in orders_list:
            if o.get("reservation_id") == booking_id:
                order_found = o
                break

        if order_found is None:
            print(Color.RED + "No food order found for this booking id." + Color.RESET)
            return

        if order_found.get("order_status") == "paid":
            print(Color.YELLOW + "This order is already paid." + Color.RESET)
            return

        items = order_found.get("items", [])
        if not items:
            print(Color.RED + "Order has no items." + Color.RESET)
            return

        bill_rows = []
        total = 0

        for it in items:
            name = it.get("item_name")
            size = it.get("size", "none")
            qty = it.get("quantity", 0)

            if not name or qty <= 0:
                continue

            price = DoPayment.get_item_price(food_data, name, size)
            amount = price * qty
            total += amount

            bill_rows.append({
                "name": name,
                "size": size,
                "qty": qty,
                "price": price,
                "amount": amount
            })

        if not bill_rows:
            print(Color.RED + "No valid bill items found." + Color.RESET)
            return

        gst = total * 0.05
        grand_total = total + gst

        print(
            Color.BOLD + Color.BRIGHT_BLUE +
            f"\nBooking: {booked_res.get('table_name')} | "
            f"Date: {booked_res.get('date')} | "
            f"Slot: {booked_res.get('time_slot')}" +
            Color.RESET
        )

        DoPayment.print_bill_table(bill_rows, grand_total)
        print(Color.GREEN + f"GST (5%): Rs {gst:.0f}" + Color.RESET)

        confirm = input(
            Color.CYAN + "Proceed to payment? (y/n): " + Color.RESET
        ).strip().lower()

        if confirm != "y":
            print(Color.YELLOW + "Payment cancelled." + Color.RESET)
            return

        method = DoPayment.input_payment_method()

        order_found["order_status"] = "paid"
        order_found["payment_method"] = method
        order_found["paid_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        order_found["total_amount"] = grand_total

        booked_res["status"] = "completed"
        booked_res["completed_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        ReadWrite.write_json(orders_data, Path.orders_data_path)
        ReadWrite.write_json(reservations_data, Path.reservations_data_path)

        print(
            Color.BOLD + Color.BRIGHT_MAGENTA +
            f"\nPayment successful! Booking ID: {booking_id}" +
            Color.RESET
        )
        print(
            Color.BOLD + Color.BRIGHT_GREEN +
            f"Grand Total: Rs {grand_total:.0f} ({method.upper()})" +
            Color.RESET
        )
