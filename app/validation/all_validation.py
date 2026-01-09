from app.domain.read_write import ReadWrite
from app.model.logs_path import Logs
from app.model.pattern import Pattern
from colorama import Fore , init
import getpass
import re
init(autoreset=True)

class Validation:
    @staticmethod
    def menu_choice():
        while True:
            choice=input(Fore.WHITE+"Please Enter Your Choice: ").strip()
            if choice.isdigit():
                return int(choice)
            else:
                print(Fore.RED+"Please Enter Number Only.")

    @staticmethod
    def opening_qty():
        while True:
            qty=input("Opening stock Quantity(half): ")
            if qty.isdigit():
                return int(qty)
            else:
                print(Fore.RED+"Please Enter Number Only.")           

    @staticmethod
    def name():
          while True:
               name = input(Fore.WHITE+"Please enter your full name: ").strip()
                
               if re.fullmatch(Pattern.name_pattern, name) and 2 <= len(name) <= 50:
                     return name
               else:
                   print(Fore.RED + "Invalid name. Only letters, spaces, hyphens and apostrophes allowed.")

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
                email = input(Fore.WHITE + "Please Enter Your Email: ").strip().lower()
                if re.fullmatch(Pattern.email_pattern, email):
                    return email
                else:
                    print(Fore.RED + "Invalid Email. Please try again.")
            except Exception as e:
                print(Fore.RED + "Something went wrong.")
            
                ReadWrite.log_error(Logs.email, str(e), email, module)

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

                ReadWrite.log_error(Logs.experience,str(e),email,module)  

    @staticmethod
    def password(email,module):
        while True:
            try:
                password = getpass.getpass(Fore.WHITE+"Enter password: ")
                confirm_password = getpass.getpass(Fore.WHITE+"Confirm password: ")

                if len(password) < 8:
                    print(Fore.RED+"Minimum 8 characters required.")

                elif " " in password:
                    print(Fore.RED+"Do Not Give Space in Passwords.")

                elif len(password) > 20:
                    print(Fore.RED + "Password should be between 8 and 20 characters.")    

                elif password != confirm_password:
                    print(Fore.RED+"Passwords do not match.") 

                else:
                    return password
            except Exception as e:
                print(Fore.RED+"Something went wrong.")
                ReadWrite.log_error(Logs.password,str(e),email,module)     
                   
                        


                
