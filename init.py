import account
import login
import phone_auth


# initialization order
# 
# - account.py - create_account()
# - login.py - account_login() -> calls phone_auth.py - text_code(phone_number)
# - login.py - two_factor_check()
# - ... ? ... 

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
login.account_login()
print('\n')
# prompt for two factor code
login.two_factor_check()
print('\n')

#################################################

#
# Run jar files to initialize todo list
#

#TODO
# do java stuff here





# TODO - somewhere around here encrypt json from java

#################################################

#
# Initialize chatbot functionality here
#

# TODO 
# initialize python calls for chatbot here





# END FILE
print('0')
