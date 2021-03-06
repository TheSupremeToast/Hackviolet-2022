import os
import json
import random
import string
import hashlib

# import login.py
import login

# import twilio for phone authentication
# NOTE: you must install twilio (pip3 install twilio)
from twilio.rest import Client

# import dotenv to load environment variables
# NOTE: you must install dotenv (pip install dotenv)
from dotenv import load_dotenv
load_dotenv()

# get twilio accound sid and auth token from .env
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
phone_number = os.getenv('TWILIO_PHONE_NUMBER')

client = Client(account_sid, auth_token)
    
#
# random authentication code generator
#
def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


#
# text 2-factor code to user
#
def text_code(user_phone):
    # generate 2 factor code and sms content 
    code = id_generator()
    response = "Your 2-Factor Verification code: " + code
    
    # get user profile data from json file
    # with open ('user_data.json', 'r') as read_file:
    #     users = json.load(read_file)
    # user_phone = login.account_login()

    # check if phone number contains an extension
    # if it doesn't add '+1'
    # TODO - does not check if number is valid, won't be done for hackathon
    if user_phone != False:
        extension = '+1'
        if extension in user_phone:
            True
        else:
            user_phone = "+1" + user_phone 
        
        # send user text message
        # NOTE: DOES NOT WORK WITHOUT A VALID PHONE NUMBER
        message = client.messages.create(
            # send text with verification code
            body= response,
            from_= phone_number,
            to= user_phone)
        # print(message.sid)
        
        # encrypt 2 factor code
        encoded = hashlib.sha256(code.encode()).hexdigest()
        with open('temp.txt', 'w') as file:
            file.write(encoded)

# if phone value is false, exit and print an error code
    else:
        print("Exit with error code 1")

# testing
# text_code()
