from app.model.json_file import Path
import json
import os
import datetime
import uuid
class ReadWrite:

    def read(self):
        self.path_json=Path.staff_data_path
        with open(Path.staff_data_path, "r") as f:
            return json.loads(f.read())

    def write_json(self,data):
        with open(self.path_json,'w') as file:
                    file.write(json.dumps(data,indent=4))

    def write(self,path): 
        if not os.path.exists(path):
            with open(path, "w") as f:
                f.write("[]")    
    @staticmethod               
    def log_error(path, message):
        with open(path, "a") as file:
            file.write(f"{datetime.datetime.now()} | ERROR_ID={uuid.uuid4().hex[:8]} - {message}\n")                    