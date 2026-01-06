from app.model.json_file import Path
import json
import datetime
import uuid

class ReadWrite:

    @staticmethod
    def read():
        path=Path.staff_data_path
        with open(path, "r") as f:
            data = json.loads(f.read())
            return data
    @staticmethod
    def write_json(data):
        with open(Path.staff_data_path, "w") as file:
            json.dump(data, file, indent=4)

    @staticmethod
    def log_error(path, message, email, module):
        with open(path, "a") as file:
            file.write(f"Email={email} | {datetime.datetime.now()} | Module={module} | "f"ERROR_ID={uuid.uuid4().hex[:8]} - {message}\n")
