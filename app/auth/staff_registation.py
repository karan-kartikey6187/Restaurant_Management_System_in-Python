import uuid
from app.validation.all_validation import Validation
class Staff:
    def __init__(self):
        print(">>>>>>>>>Registation Menu<<<<<<<<<<")
        self.id = uuid.uuid4().hex[:7]
        self.name = Validation.name(self)
        self.email = Validation.email(self)
        self.contact = Validation.contact(self)
        self.experience = Validation.experience(self)
        self.password = Validation.password(self)
        self.role = "Staff"
        print("Registation Successfull.")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "contact": self.contact,
            "experience": self.experience,
            "password":self.password,
            "role": self.role
        }
