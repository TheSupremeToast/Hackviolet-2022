import json
import hashlib
import getpass
import phone_auth


#
# login to account
#
def account_login():
    # read users json file
    username = input('Enter your username: ')
    with open ('user_data.json', 'r') as read_file:
        users = json.load(read_file)
    
    flag = False
    # iterate through json file to find desired username
    # then checks password
    i = 0
    for user in users['users']:
        if username == users['users'][i]['username']:
            pswd = getpass.getpass('Enter your password: ')
            pswd_encoded = hashlib.sha256(pswd.encode()).hexdigest()
            if pswd_encoded == users['users'][i]['password']:
                # get user phone number and send the 2 factor code
                phone = users['users'][i]['phone']
                phone_auth.text_code(phone)

            else:
                print('Incorrect Password.')
        i = i + 1 
    return 12


#
# 2 factor login check
#
def two_factor_check():
    with open('temp.txt') as file:
        code = file.read()

    auth_input = input('Enter your verification code: ')
    encoded = hashlib.sha256(auth_input.encode()).hexdigest()

    if encoded == code:
        print('You have successfully logged in')
        return True 
    else:
        print('Exit with error code 2')
        print(encoded)
        print(code)
    return False


# run functions, for testing purposes only
# account_login()
# two_factor_check()
