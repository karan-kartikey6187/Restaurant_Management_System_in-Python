from app.model.json_file import Path
import json
import datetime
import uuid

class ReadWrite:

    @staticmethod
    def read():
        """Loads and returns JSON data from file."""
        path=Path.staff_data_path
        with open(path, "r") as f:
            data = json.loads(f.read())
            return data
    @staticmethod    
    def read_inventory():
        inventory_path=Path.inventory_data_path    
        with open(inventory_path, "r") as f:
             inventory_data = json.load(f)
             return inventory_data

    @staticmethod
    def write_inventory(inventory_data):
        inventory_path=Path.inventory_data_path    
        with open(inventory_path, "w") as f:
            json.dump(inventory_data, f, indent=4)    

    @staticmethod
    def write_json(data):
        """Writes JSON data to given file path."""
        with open(Path.staff_data_path, "w") as file:
            json.dump(data, file, indent=4)
    @staticmethod
    def read_food_data():
        path=Path.food_item_path
        with open(path, "r") as f:
            data = json.loads(f.read())
            return data  
    @staticmethod
    def write_json_food(data):
        with open(Path.food_item_path, "w") as file:
            json.dump(data, file, indent=4)          

    @staticmethod
    def log_error(path, message, email, module):
        """Stores log messages in a log file."""
        with open(path, "a") as file:
            file.write(f"Email={email} | {datetime.datetime.now()} | Module={module} | "f"ERROR_ID={uuid.uuid4().hex[:8]} - {message}\n")
