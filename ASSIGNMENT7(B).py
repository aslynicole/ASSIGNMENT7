# Program 2: Password validator

import re # import regular expressions
import shutil
class bcolors: # colors for fonts
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
columns = shutil.get_terminal_size().columns
print (bcolors.HEADER+"Create your Password".center(columns))
print( bcolors.OKBLUE+ "The password is only valid if all criteria are met:" +bcolors.OKCYAN)
print ('a. Greater than 15 letters')
print ('b. Have at least one capital letter')
print ('c. Have at least one number')
print ('d. Have at least one special character (!@#$%^&*()_+ etc)\n'+ bcolors.ENDC)

# def password function that checks if the password is valid and invalid
def password():
          userPassword = input("Please enter a valid password: ")
          val = True 
          while val:  # loop for the password
              if (len(userPassword)<15): # for the length of password
                  print("Password length should be greater than 15")     
                  break 
              elif not re.search("[a-z]",userPassword): # for the lowercase
                  print("You need at least one lower case letter")
                  break
              elif not re.search("[A-Z]",userPassword): # for the uppercase
                  print("You need at least one upper case character")
                  break
              elif not re.search("[0-9]",userPassword): # for the numbers
                  print("You need at least one number")
                  break
              elif not re.search("[$@%#_&^!*+?]",userPassword): # for the special characters
                  print("You need at least one special character [ex:$@%#_&^!*+?]")
                  break
              elif re.search("\s",userPassword): # for the space
                  print("You cannot have blank spaces in your password")
                  break
              else:
                  print(bcolors.OKGREEN+"Valid Password"+ bcolors.ENDC)
                  val = False 
                  break
          if val: 
              print(bcolors.FAIL+"Invalid Password" + bcolors.ENDC)
              password()
# call for the function:
password()