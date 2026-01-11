from app.domain.read_write import ReadWrite
from app.model.json_file import Path
from app.model.colors import Color

class TableManager:
    @staticmethod
    def manage_tables():
        print(Color.YELLOW+"\n")
        print(Color.BRIGHT_BLUE+"=" * 50)
        print(Color.YELLOW+"MANAGE TABLES")
        print(Color.BRIGHT_BLUE+"=" * 50)
        
        while True:
            print(Color.WHITE+"\n1. View All Tables")
            print(Color.WHITE+"2. Add New Table")
            print(Color.WHITE+"3. Remove Table")
            print(Color.WHITE+"0. Back")
            print(Color.BRIGHT_BLUE+"-" * 50)
            
            choice = TableManager.get_int(Color.BRIGHT_BLUE+"Enter choice: "+Color.YELLOW)
            if choice == 0:
                return
            
            if choice == 1:
                TableManager.view_tables()
            elif choice == 2:
                TableManager.add_table()
            elif choice == 3:
                TableManager.remove_table()
            else:
                print(Color.RED+"Invalid option!")
            
            input(Color.YELLOW+"\nPress Enter..."+Color.WHITE)

    @staticmethod
    def get_tables():
        tables_data = ReadWrite.read(Path.tables_data_path)
        return tables_data if isinstance(tables_data, list) else tables_data.get("tables", [])

    @staticmethod
    def save_tables(tables):
        ReadWrite.write_json(tables, Path.tables_data_path)

    @staticmethod
    def get_int(prompt):
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print(Color.RED+"Enter valid number!")

    @staticmethod
    def view_tables():
        tables = TableManager.get_tables()
        if not tables:
            print(Color.RED+"No tables found!")
            return
        
        print(Color.YELLOW+"\nALL TABLES:")
        print(Color.BRIGHT_BLUE+"-" * 45)
        print(Color.WHITE+f"{'ID':<5} {'Name':<6} {'Capacity':<8} {'Status'}")
        print(Color.BRIGHT_BLUE+"-" * 45)
        
        for table in tables:
            tid = table.get('table_id', 'N/A')
            tname = table.get('table_name', 'N/A')
            capacity = table.get('capacity', 'N/A')
            status = table.get('status', 'N/A')
            status_color = Color.GREEN if status == "free" else Color.RED
            print(Color.WHITE+f"{tid:<5} {tname:<6} {capacity:<8} "+status_color+status)
        print(Color.BRIGHT_BLUE+"-" * 45)

    @staticmethod
    def add_table():
        tables = TableManager.get_tables()
        next_id = max([t.get('table_id', 0) for t in tables], default=0) + 1
        next_name = f"T{next_id}"
        
        print(Color.YELLOW+"\nADD NEW TABLE")
        print(Color.BRIGHT_BLUE+"-" * 25)
        print(Color.CYAN+f"AUTO: ID={next_id} | Name={next_name}")
        
        while True:
            capacity_input = input(Color.BRIGHT_BLUE+f"Capacity (2/4/6/8): "+Color.YELLOW).strip()
            if capacity_input in ['2', '4', '6', '8']:
                capacity = int(capacity_input)
                new_table = {"table_id": next_id, "table_name": next_name, "capacity": capacity, "status": "free"}
                tables.append(new_table)
                TableManager.save_tables(tables)
                print(Color.GREEN+f"✓ {next_name} (Cap: {capacity}) ADDED!")
                break
            print(Color.RED+"Only 2, 4, 6, 8 allowed!")

    @staticmethod
    def remove_table():
        tables = TableManager.get_tables()
        if not tables:
            print(Color.RED+"No tables!")
            return
        
        TableManager.view_tables()
        
        tid = TableManager.get_int(Color.BRIGHT_BLUE+"Enter Table ID to remove: "+Color.YELLOW)
        table_to_remove = next((t for t in tables if t.get('table_id') == tid), None)
        
        if not table_to_remove:
            print(Color.RED+"Table not found!")
            return
        
        table_name = table_to_remove.get('table_name')
        print(Color.YELLOW+f"\nRemove {table_name}? (Cap: {table_to_remove.get('capacity')})")
        
        while True:
            confirm = input(Color.RED+"(Y/N): "+Color.YELLOW).lower().strip()
            if confirm == 'y':
                tables = [t for t in tables if t.get('table_id') != tid]
                TableManager.save_tables(tables)
                print(Color.GREEN+f"✓ {table_name} REMOVED!")
                break
            elif confirm == 'n':
                print(Color.YELLOW+"Cancelled.")
                break
            else:
                print(Color.RED+"Enter Y or N only!")

