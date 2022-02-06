import subprocess
import account
import login
import phone_auth


# initialization order
# 
# - account.py - create_account()
# - login.py - account_login() -> calls phone_auth.py - text_code(phone_number)
# - login.py - two_factor_check()
# - todolist.jar 
# - ...

# account.py functions are called individually
# login.py functions must be called individually
# phone_auth.py functions must be called

################################################## 

#
# Account creation and login
#

# Prompt for account creation
if input('Do you want to create and account? (Y/n) ') == 'Y':
    account.create_account()
print('\n')

# Prompt Login
# login.account_login()
print('\n')
# prompt for two factor code
# login.two_factor_check()
print('\n')

#################################################

#
# Run jar file to initialize todo list
#

# call todolist.jar
# NOTE: java must be installed
subprocess.call(['java', '-jar', 'todolist.jar'])

# TODO - somewhere around here encrypt json from java

#################################################

#
# Initialize chatbot functionality here
#

# TODO 
# initialize python calls for chatbot here
# @ lily





#################################################

# END FILE
