from app.menu.all_menu import Menu
from app.auth.staff_registation import Staff
from app.domain.read_write import ReadWrite
from app.model.json_file import Path
from app.auth.login import Login
json_file=Path.staff_data_path

class Main():
    all_data=[]
    def __init__(self):
        self.json_file=json_file
        ReadWrite.write(self,json_file)
        self.all_data=ReadWrite.read(self)
    def option(self):
        while True:
            choice=Menu.main_menu(self)
            if choice==1:
                Login.login_user(self,self.all_data) 
            elif choice==2:
                ob=Staff()
                data=ob.to_dict()
                self.all_data.append(data)
                ReadWrite.write_json(self,self.all_data)
            elif choice==3:
                break   
             




        
