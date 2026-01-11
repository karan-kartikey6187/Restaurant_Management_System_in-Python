from app.domain.read_write import ReadWrite
from app.model.json_file import Path
from datetime import datetime
from collections import Counter
from app.validation.all_validation import Validation
from app.model.colors import Color

class Reports:
    @staticmethod
    def view_reports():
        while True:
            print(Color.YELLOW+"\n")
            print(Color.BRIGHT_BLUE+"=" * 50)
            print(Color.YELLOW+"             VIEW REPORTS")
            print(Color.BRIGHT_BLUE+"=" * 50)
            print(Color.WHITE+"1. Today Summary")
            print(Color.WHITE+"2. Total Sales")
            print(Color.WHITE+"3. Top Items")
            print(Color.WHITE+"4. Pending Orders")
            print(Color.WHITE+"0. Back to Menu")
            print(Color.BRIGHT_BLUE+"=" * 50)
            
            try:
                choice = Validation.menu_choice()
                
                if choice == 0:
                    print(Color.YELLOW+"\n" * 2)
                    break
                
                orders_data = ReadWrite.read(Path.orders_data_path)
                orders = orders_data.get("orders", []) if orders_data else []
                
                if not orders:
                    print(Color.RED+"\nNo orders data available.")
                    input(Color.YELLOW+"\nPress Enter...")
                    continue
                
                if choice == 1:
                    Reports.today_summary(orders)
                elif choice == 2:
                    Reports.total_sales(orders)
                elif choice == 3:
                    Reports.top_items(orders)
                elif choice == 4:
                    Reports.pending_orders(orders)
                else:
                    print(Color.RED+"\nInvalid option!")
                
                input(Color.YELLOW+"\nPress Enter...")
                
            except Exception as e:
                print(Color.RED+"\nError occurred. Press Enter...")
                input()

    @staticmethod
    def today_summary(orders):
        today = datetime.now().strftime("%Y-%m-%d")
        today_orders = [o for o in orders if o.get("order_datetime", "").startswith(today)]
        total = len(today_orders)
        paid = sum(1 for o in today_orders if o.get("order_status") == "paid")
        revenue = sum(o.get("total_amount", 0) for o in today_orders if o.get("order_status") == "paid")
        
        print(Color.YELLOW+"\nTODAY SUMMARY:")
        print(Color.BRIGHT_BLUE+"-" * 40)
        print(Color.WHITE+f"Total Orders Today:      {total}")
        print(Color.WHITE+f"Paid Orders Today:       {paid}")
        print(Color.CYAN+f"Revenue Today:           ₹{revenue:,.0f}")
        print(Color.WHITE+f"Pending Today:           {total - paid}")

    @staticmethod
    def total_sales(orders):
        paid_orders = [o for o in orders if o.get("order_status") == "paid"]
        total_revenue = sum(o.get("total_amount", 0) for o in paid_orders)
        avg_value = total_revenue / len(paid_orders) if paid_orders else 0
        
        print(Color.YELLOW+"\nTOTAL SALES REPORT:")
        print(Color.BRIGHT_BLUE+"-" * 40)
        print(Color.WHITE+f"Total Paid Orders:       {len(paid_orders)}")
        print(Color.CYAN+f"Total Revenue:           ₹{total_revenue:,.0f}")
        print(Color.CYAN+f"Average Order Value:     ₹{avg_value:,.0f}")

    @staticmethod
    def top_items(orders):
        """FIXED: Now counts ACTUAL QUANTITY (Rasmalai 3, Buttermilk 2)"""
        item_quantity = Counter()
        
        for order in orders:
            for item in order.get("items", []):
                name = item.get("item_name", "Unknown")
                qty = item.get("quantity", 1) 
                item_quantity[name] += qty 
        
        print(Color.YELLOW+"\nTOP SELLING ITEMS (by Quantity):")
        print(Color.BRIGHT_BLUE+"-" * 45)
        print(Color.WHITE+f"{'Rank':<5} {'Item Name':<20} {'Qty'}")
        print(Color.BRIGHT_BLUE+"-" * 45)
        
        if item_quantity:
            top_items_list = item_quantity.most_common(5)
            for i, (item, total_qty) in enumerate(top_items_list, 1):
                print(Color.WHITE+f"{i:<5} {item[:19]:<20} "+Color.GREEN+f"{total_qty:>3}")
        else:
            print(Color.RED+"No items data available.")

    @staticmethod
    def pending_orders(orders):
        pending = [o for o in orders if o.get("order_status") == "pending"]
        
        print(Color.RED+"\nPENDING ORDERS REPORT:")
        print(Color.BRIGHT_BLUE+"-" * 40)
        print(Color.WHITE+f"Total Pending Orders:    {len(pending)}")
        
        if pending:
            print(Color.YELLOW+"\nRecent Pending Orders:")
            print(Color.BRIGHT_BLUE+"-" * 40)
            for order in pending[:3]:
                order_id = order.get('order_id', 'N/A')
                table = order.get('table_name', 'N/A')
                booking_id = order.get('reservation_id', 'N/A')
                print(Color.WHITE+f"Order {order_id:<3} | Table {table:<4} | {booking_id}")

