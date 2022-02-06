import json
import hashlib
import getpass

#
# add to existing json file
#
def write_json(new_data, filename='user_data.json'):
    with open(filename, 'r+') as file:
        #load existing data into dictionary
        file_data = json.load(file)
        # join new_data with file_data inside users
        file_data['users'].append(new_data)
        # set current position in file
        file.seek(0)
        # convert back to json
        json.dump(file_data, file, indent = 4)


#
# Create an account and store it in a json file
#
def create_account():
    print('Create account:')
    username = input('Enter a username: ')
    flag = False 
    while not flag:
        # take user password and check they typed correctly
        password = getpass.getpass('Enter desired password: ')
        password_confirm = getpass.getpass('Retype password: ')
        if password != password_confirm:
            print('\nPasswords did not match.\nPlease reenter your password.\n')
        else:
            flag = True 
    phone = input('Enter your phone number: ')
    
    # encode password into sha256
    encoded_password = hashlib.sha256(password.encode()).hexdigest()
    # return(username, phone, encoded_password.hexdigest())

    # define the json file to be added to user_data.json
    data = {
        'username': username,
        'phone': phone,
        'password': encoded_password 
    }
    json_string = json.dumps(data)
    write_json(data)


# test call the account create function
# user_data = create_account()
