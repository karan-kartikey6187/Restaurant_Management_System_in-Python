from app.domain.read_write import ReadWrite
from app.model.logs_path import Logs

class Validation:
    def main_menu_choice(self):
        choice=input("Please Enter Your Choice: ").strip()
        if choice.isdigit():
            return int(choice)
        else:
            print("Please Enter Number Only.")

    def name(self):
        name=input("Please Enter Your Name: ")
        if name.isalpha():
            return name
        else:
            print("Please Enter Valid Name.")

    def contact(self):
        contact =int(input("Please Enter Your Contact: "))
        if len(str(contact)) == 10:
            return int(contact)        
        else:
            print("Invalid contact! Enter 10 digit number.")

    def email(self):
        email = input("Enter your email: ")
        if "@" in email and "." in email:
            return email
        else:
            print("Invalid Email")

    def experience(self):
        while True:
            try:
                years= int(input("Please Enter Your Exprience (in years): "))
                if years < 0:
                    print("Experience cannot be negative.")
                elif years > 50:
                    print("Experience seems to high.")
                else:
                    return years
            except ValueError as e:
                print("Please Enter Numbers Only.")
                path=Logs.experience 
                ReadWrite.log_error(path,str(e))  

    def password(self):
        while True:
            try:
                password = input("Enter password: ")
                confirm_password = input("Confirm password: ")
    
                if len(password) < 8:
                    print("Minimum 8 characters required.")
                elif not password.isalnum():
                    print("Use letters and numbers only.")
                elif password != confirm_password:
                    print("Passwords do not match.")
                else:
                    return password
            except Exception as e:
                print("Something went wrong.")
                path=Logs.password
                ReadWrite.log_error(path,str(e))     
                   
                        


                
