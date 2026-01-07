import uuid
from app.validation.all_validation import Validation
from app.model.user import User_model
from app.model.error_module import Module
from colorama import Fore , init
init(autoreset=True)
class Staff:
    @staticmethod
    def register():
        stud=User_model()
        """Registers a new staff or admin user.""" 
        module=Module.register
        print(Fore.BLUE+"<>"*15)
        print(Fore.LIGHTYELLOW_EX+">>>>>>>Registration Menu<<<<<<")
        print(Fore.BLUE+"<>"*15)
        stud.id = uuid.uuid4().hex[:7]
        stud.name = Validation.name()
        stud.email = Validation.email(module)
        stud.contact = Validation.contact(stud.email,module)
        stud.experience = Validation.experience(stud.email,module)
        stud.password = Validation.password(stud.email,module)
        stud.role = "Staff"
        print(Fore.GREEN+"Registation Successfull.")
        return stud.__dict__
