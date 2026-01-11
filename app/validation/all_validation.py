from app.domain.read_write import ReadWrite
from app.model.logs_path import Logs
from app.model.pattern import Pattern
from app.model.colors import Color
import getpass
import re

class Validation:
    @staticmethod
    def menu_choice():
        while True:
            choice=input(Color.BRIGHT_BLUE+"Please Enter Your Choice: "+Color.YELLOW)
            if choice.isdigit():
                return int(choice)
            else:
                print(Color.RED+"Please Enter Number Only."+Color.YELLOW)

    @staticmethod
    def opening_qty():
        while True:
           qty=input(Color.BRIGHT_BLUE+"Opening stock Quantity(half): "+Color.YELLOW)
           if qty.isdigit():
               return int(qty)
           else:
               print(Color.RED+"Please Enter Number Only."+Color.YELLOW)         

    @staticmethod
    def name():
         while True:
              name = input(Color.BRIGHT_BLUE+"Please enter your full name: "+Color.YELLOW).strip()
              
              if re.fullmatch(Pattern.name_pattern, name) and 2 <= len(name) <= 50:
                 return name
              else:
                  print(Color.RED+"Invalid name. Only letters, spaces, hyphens and apostrophes allowed."+Color.YELLOW)

    @staticmethod
    def contact(email,module):
        while True:
            try:
                contact =int(input(Color.BRIGHT_BLUE+"Please Enter Your Contact: "+Color.YELLOW))
                if len(str(contact)) == 10:
                    return contact       
                else:
                    print(Color.RED+"Invalid contact! Enter 10 digit number."+Color.YELLOW)
            except Exception as e:
                    print(Color.RED+"Invalid Contact Number."+Color.YELLOW)
                    path = Logs.contact
                    ReadWrite.log_error(path, str(e), email, module)

    @staticmethod
    def email(module):
        while True: 
            try:
                email = input(Color.BRIGHT_BLUE+"Please Enter Your Email: "+Color.YELLOW).strip().lower()
                if re.fullmatch(Pattern.email_pattern, email):
                    return email
                else:
                    print(Color.RED+"Invalid Email. Please try again."+Color.YELLOW)
            except Exception as e:
                print(Color.RED+"Something went wrong."+Color.YELLOW)
                
                ReadWrite.log_error(Logs.email, str(e), email, module)

    @staticmethod
    def experience(email,module):
        while True:
            try:
                years= int(input(Color.BRIGHT_BLUE+"Please Enter Your Exprience (in years): "+Color.YELLOW))
                if years < 0:
                    print(Color.RED+"Experience cannot be negative."+Color.YELLOW)
                elif years > 50:
                    print(Color.RED+"Experience seems to high."+Color.YELLOW)
                else:
                    return years
            except ValueError as e:
                print(Color.RED+"Please Enter Numbers Only."+Color.YELLOW)

                ReadWrite.log_error(Logs.experience,str(e),email,module)  

    @staticmethod
    def password(email,module):
        while True:
            try:
                password = getpass.getpass(Color.BRIGHT_BLUE+"Enter password: "+Color.YELLOW)
                confirm_password = getpass.getpass(Color.BRIGHT_BLUE+"Confirm password: "+Color.YELLOW)

                if len(password) < 8:
                    print(Color.RED+"Minimum 8 characters required."+Color.YELLOW)

                elif " " in password:
                    print(Color.RED+"Do Not Give Space in Passwords."+Color.YELLOW)

                elif len(password) > 20:
                    print(Color.RED+"Password should be between 8 and 20 characters."+Color.YELLOW)    

                elif password != confirm_password:
                    print(Color.RED+"Passwords do not match."+Color.YELLOW) 

                else:
                    return password
            except Exception as e:
                print(Color.RED+"Something went wrong."+Color.YELLOW)
                ReadWrite.log_error(Logs.password,str(e),email,module)          
