from app.domain.read_write import ReadWrite
from app.model.json_file import Path
from app.model.colors import Color

class View_Orders:

    @staticmethod
    def view_orders():
        orders_data = ReadWrite.read(Path.orders_data_path)
        if not orders_data or "orders" not in orders_data:
            print(Color.RED+"\nNo orders found."+Color.YELLOW)
            return

        orders = orders_data.get("orders", [])
        if not orders:
            print(Color.RED+"\nNo orders found."+Color.YELLOW)
            return

        print(Color.BRIGHT_BLUE+"=" * 45)
        print(Color.YELLOW+"             VIEW ORDERS")
        print(Color.BRIGHT_BLUE+"=" * 45)

        for order in orders:
            print(Color.BRIGHT_BLUE+"\nOrder ID      : " + Color.CYAN+str(order.get("order_id", "N/A")))
            print(Color.BRIGHT_BLUE+"Booking ID    : " + Color.CYAN+str(order.get("reservation_id", "N/A")))
            print(Color.BRIGHT_BLUE+"Table         : " + Color.CYAN+str(order.get("table_name", "N/A")))
            
            order_datetime = order.get("order_datetime", "N/A")
            if order_datetime != "N/A" and " " in order_datetime:
                parts = order_datetime.split(" ")
                order_date = parts[0]     
                order_time = " ".join(parts[1:]) 
            else:
                order_date = "N/A"
                order_time = "N/A"
            
            print(Color.BRIGHT_BLUE+"Order Date    : " + Color.CYAN+str(order_date))
            print(Color.BRIGHT_BLUE+"Order Time    : " + Color.CYAN+str(order_time))

            status = str(order.get("order_status", "unknown")).lower()
            status_display = status.upper()
            
            status_color = Color.GREEN if status == "paid" else Color.RED if status == "cancelled" else Color.YELLOW
            print(Color.BRIGHT_BLUE+"Order Status  : " + status_color+status_display)

            print(Color.BRIGHT_BLUE+"-" * 60)
            print(Color.YELLOW+"Items:")
            print(Color.WHITE+f"{'No':<4} {'Item Name':<22} {'Qty':<6} {'Size':<8} {'Category':<12}")
            print(Color.BRIGHT_BLUE+"-" * 60)

            items = order.get("items", [])
            if not items:
                print(Color.RED+"No items.")
            else:
                for idx, item in enumerate(items, start=1):
                    item_name = str(item.get("item_name", "N/A"))[:21] 
                    qty = str(item.get("quantity", 0))
                    size_display = str(item.get("size", "none"))
                    if size_display == "none":
                        size_display = "N/A"
                    category = str(item.get("category", "N/A"))[:11]
                    
                    print(
                        Color.WHITE+f"{idx:<4} " 
                        + Color.CYAN+f"{item_name:<22} "
                        + Color.GREEN+f"{qty:<6} "
                        + Color.MAGENTA+f"{size_display:<8} "
                        + Color.YELLOW+f"{category:<12}"
                    )
            print(Color.BRIGHT_BLUE+"-" * 60)

        input(Color.YELLOW+"\nPress Enter to continue..."+Color.WHITE)
