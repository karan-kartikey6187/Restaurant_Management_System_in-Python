import uuid
from app.validation.all_validation import Validation
from app.model.user import User_model
from app.model.error_module import Module
from app.model.role_model import Role
from app.model.colors import Color

class Staff:
    @staticmethod
    def register():
        stud=User_model()
        """Registers a new staff or admin user.""" 
        print(Color.BRIGHT_BLUE+"<>"*15)
        print(Color.YELLOW+">>>>>>Registration Menu<<<<<<")
        print(Color.BRIGHT_BLUE+"<>"*15)
        stud.id = uuid.uuid4().hex[:7]
        stud.name = Validation.name()
        stud.email = Validation.email(Module.register)
        stud.contact = Validation.contact(stud.email,Module.register)
        stud.experience = Validation.experience(stud.email,Module.register)
        stud.password = Validation.password(stud.email,Module.register)
        stud.role = Role.staff
        print(Color.GREEN+"Registration Successful.")
        return stud.__dict__
