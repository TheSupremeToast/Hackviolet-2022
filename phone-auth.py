import os
import json
import random
import string


# import twilio for phone authentication
from twilio.rest import Client

# import dotenv to load environment variables
from dotenv import load_dotenv
load_dotenv()

# get twilio accound sid and auth token from .env
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')

client = Client(account_sid, auth_token)

# get user profile data from json file
with open ('user_data.json', 'r') as read_file:
    users = json.load(read_file)
# get user phone number from json
user_phone = users['phone']


# authentication code generator
def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
code = id_generator()
response = "Your 2-Factor Verification code: " + code

# send user text message
message = client.messages.create(
    # send text with verification code
    body= response,
    from_= '+19034818989',
    to= user_phone)

print(message.sid)
