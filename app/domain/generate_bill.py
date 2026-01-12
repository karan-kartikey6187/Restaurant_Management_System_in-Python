import re
from datetime import datetime
from app.domain.read_write import ReadWrite
from app.model.json_file import Path
from app.model.colors import Color

class GenerateBill:

    @staticmethod
    def find_order(orders_data, identifier):
        orders = orders_data.get("orders", [])
        
        for order in orders:
            if order.get("reservation_id") == identifier["value"]:
                return order
        
        if identifier["type"] == "order_id":
            for order in orders:
                if order.get("order_id") == identifier["value"]:
                    return order
        
        return None

    @staticmethod
    def get_item_price(item_name, size, menu_data, inventory_data):
        menu = menu_data.get("menu", {})
        
        for category in menu.values():
            for item in category:
                if item.get("name", "").title() == item_name.title():
                    price_data = item.get("price", {})
                    
                    if isinstance(price_data, dict):
                        if size == "half":
                            return price_data.get("half", 0)
                        elif size == "full":
                            return price_data.get("full", 0)
                    else:
                        return price_data
        
        return 0

    @staticmethod
    def input_identifier():
        while True:
            val = input(Color.CYAN + "\nEnter Booking ID (6 chars) or Order ID (number): " + Color.RESET).strip().upper()

            if val == "":
                print(Color.RED + "Cannot be empty." + Color.RESET)
                continue

            if re.fullmatch(r"[A-F0-9]{6}", val):
                return {"type": "booking_id", "value": val}

            try:
                order_id = int(val)
                if order_id <= 0:
                    print(Color.RED + "ID must be greater than 0." + Color.RESET)
                    continue
                return {"type": "order_id", "value": order_id}
            except ValueError:
                print(Color.RED + "Invalid format. Use Booking ID (A1B2C3) or Order ID (1,2,3...)." + Color.RESET)

    @staticmethod
    def generate_bill():
        orders_data = ReadWrite.read(Path.orders_data_path)
        inventory_data = ReadWrite.read(Path.inventory_data_path)
        menu_data = ReadWrite.read(Path.food_item_path)

        if not orders_data or "orders" not in orders_data:
            print(Color.RED + "No orders found." + Color.RESET)
            return

        identifier = GenerateBill.input_identifier()
        order = GenerateBill.find_order(orders_data, identifier)

        if not order:
            print(Color.RED + "Order not found." + Color.RESET)
            return

        items = order.get("items", [])
        if not items:
            print(Color.RED + "No items in order." + Color.RESET)
            return

        subtotal = 0.0
        bill_items = []

        print(Color.YELLOW + "\nCalculating bill..." + Color.RESET)

        for item in items:
            item_name = item.get("item_name", "")
            size = item.get("size", "none")
            qty = item.get("quantity", 0)

            if qty <= 0 or not item_name:
                continue

            price = GenerateBill.get_item_price(item_name, size, menu_data, inventory_data)
            amount = price * qty

            bill_items.append({
                "name": item_name,
                "size": size,
                "qty": qty,
                "price": price,
                "amount": amount
            })
            subtotal += amount

        tax_rate = 0.05
        tax_amount = subtotal * tax_rate
        grand_total = subtotal + tax_amount

        order_date = order.get('order_date', datetime.now().strftime('%Y-%m-%d'))
        order_time = order.get('order_time', datetime.now().strftime('%I:%M %p'))

        print("\n" + Color.YELLOW + "=" * 60 + Color.RESET)
        print(Color.BOLD + Color.BRIGHT_YELLOW + f"  {menu_data.get('restaurant_name', 'FLAVORPOINT')} BILL" + Color.RESET)
        print(Color.CYAN + f"  {menu_data.get('location', 'Uttarakhand, India')}" + Color.RESET)
        print(Color.YELLOW + "=" * 60 + Color.RESET)

        print(Color.CYAN + f"Order ID      : {order.get('order_id', 'N/A')}" + Color.RESET)
        print(Color.CYAN + f"Booking ID    : {order.get('reservation_id', 'N/A')}" + Color.RESET)
        print(Color.CYAN + f"Customer      : {order.get('customer_name', 'N/A')}" + Color.RESET)
        print(Color.CYAN + f"Date & Time   : {order_date} {order_time}" + Color.RESET)

        print(Color.YELLOW + "-" * 60 + Color.RESET)

        for item in bill_items:
            print(
                Color.WHITE +
                f"{item['name']:<27} ({item['size']:<4}) x{item['qty']:2} " +
                Color.BRIGHT_GREEN +
                f"@Rs{item['price']:6.0f} = Rs{item['amount']:8.0f}" +
                Color.RESET
            )

        print(Color.YELLOW + "-" * 60 + Color.RESET)
        print(Color.GREEN + f"{'Subtotal                                    ':<44}: Rs{subtotal:10.0f}" + Color.RESET)
        print(Color.GREEN + f"{'GST @ 5%                                    ':<44}: Rs{tax_amount:10.0f}" + Color.RESET)
        print(Color.BOLD + Color.BRIGHT_GREEN + f"{'GRAND TOTAL                                 ':<44}: Rs{grand_total:10.0f}" + Color.RESET)
        print(Color.YELLOW + "=" * 60 + Color.RESET)

        print(Color.BRIGHT_MAGENTA + "\nBill generated successfully!" + Color.RESET)
