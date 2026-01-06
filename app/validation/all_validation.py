from app.domain.read_write import ReadWrite
from app.model.logs_path import Logs
from colorama import Fore , init
init(autoreset=True)

class Validation:
    @staticmethod
    def menu_choice():
        choice=input(Fore.WHITE+"Please Enter Your Choice: ").strip()
        if choice.isdigit():
            return int(choice)
        else:
            print(Fore.RED+"Please Enter Number Only.")
    @staticmethod
    def name():
        name=input(Fore.WHITE+"Please Enter Your Name: ").strip()
        if name.isalpha():
            return name
        else:
            print(Fore.RED+"Please Enter Valid Name.")
    @staticmethod
    def contact(email,module):
        while True:
            try:
                contact =int(input(Fore.WHITE+"Please Enter Your Contact: "))
                if len(str(contact)) == 10:
                    return contact       
                else:
                    print(Fore.RED+"Invalid contact! Enter 10 digit number.")
            except Exception as e:
                    print(Fore.RED + "Invalid Contact Number.")
                    path = Logs.contact
                    ReadWrite.log_error(path, str(e), email, module)

    @staticmethod
    def email(module):
        while True: 
            try:
                email = input(Fore.WHITE + "Please Enter your email: ")

                if "@" in email and "." in email:
                    return email
                else:
                    print(Fore.RED + "Invalid Email. Please try again.")

            except Exception as e:
                print(Fore.RED + "Something went wrong.")
                path = Logs.email
                ReadWrite.log_error(path, str(e), email, module)

    @staticmethod
    def experience(email,module):
        while True:
            try:
                years= int(input(Fore.WHITE+"Please Enter Your Exprience (in years): "))
                if years < 0:
                    print(Fore.RED+"Experience cannot be negative.")
                elif years > 50:
                    print(Fore.RED+"Experience seems to high.")
                else:
                    return years
            except ValueError as e:
                print(Fore.RED+"Please Enter Numbers Only.")
                path=Logs.experience 
                ReadWrite.log_error(path,str(e),email,module)  
    @staticmethod
    def password(email,module):
        while True:
            try:
                password = input(Fore.WHITE+"Enter password: ")
                confirm_password = input(Fore.WHITE+"Confirm password: ")
                if len(password) < 8:
                    print(Fore.RED+"Minimum 8 characters required.")    
                elif password != confirm_password:
                    print(Fore.RED+"Passwords do not match.")
                else:
                    return password
            except Exception as e:
                print(Fore.RED+"Something went wrong.")
                path=Logs.password
                ReadWrite.log_error(path,str(e),email,module)     
                   
                        


                
