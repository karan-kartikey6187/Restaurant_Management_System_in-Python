import uuid
from app.validation.all_validation import Validation
from app.model.error_module import Module
from colorama import Fore , init
init(autoreset=True)
class Staff:
    @staticmethod
    def register():
        """Registers a new staff or admin user.""" 
        module=Module.register
        print(Fore.BLUE+"<>"*15)
        print(Fore.LIGHTYELLOW_EX+">>>>>>>Registration Menu<<<<<<")
        print(Fore.BLUE+"<>"*15)
        id = uuid.uuid4().hex[:7]
        name = Validation.name()
        email = Validation.email(module)
        contact = Validation.contact(email,module)
        experience = Validation.experience(email,module)
        password = Validation.password(email,module)
        role = "Staff"
        print(Fore.GREEN+"Registation Successfull.")
        return {
            "id": id,
            "name": name,
            "email": email,
            "contact": contact,
            "experience": experience,
            "password": password,
            "role": role
        }
