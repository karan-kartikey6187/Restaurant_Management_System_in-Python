from app.model.json_file import Path
import json
import datetime
import uuid

class ReadWrite:
    @staticmethod
    def read(path):
        """Loads and returns JSON data from file."""
        with open(path, "r") as f:
            data = json.loads(f.read())
            return data
        
    @staticmethod
    def write_json(data,path):
        """Writes JSON data to given file path."""
        with open(path, "w") as file:
            json.dump(data, file, indent=4)         

    @staticmethod
    def log_error(path, message, email, module):
        """Stores log messages in a log file."""
        with open(path, "a") as file:
            file.write(f"Email={email} | {datetime.datetime.now().strftime("%d-%m-%Y %H:%M %p")} | Module={module} | "f"ERROR_ID={uuid.uuid4().hex[:8]} - {message}\n")
