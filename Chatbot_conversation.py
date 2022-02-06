import Chatbot_word_cleanup as cleanup
from nltk.chat.util import Chat, reflections
import re, random

""" reflections = {
  "i am"       : "you are",
  "i was"      : "you were",
  "i"          : "you",
  "i'm"        : "you are",
  "i'd"        : "you would",
  "i've"       : "you have",
  "i'll"       : "you will",
  "my"         : "your",
  "you are"    : "I am",
  "you were"   : "I was",
  "you've"     : "I have",
  "you'll"     : "I will",
  "your"       : "my",
  "yours"      : "mine",
  "you"        : "me",
  "me"         : "you" """

##each pair is an array of [x,y] where 
##x is an array of keywords to trigger action,
##y is an array of responses
##r for regular expression
pairs =[
    [
        r"add.*",
        ["What task should I add to your TODO list?",
        "I'm ready! Let's add a task to your TODO list.",
        "What task am I adding?"]
    ],
    [
        r"search.*until.*|get.*until.*",
        ["Get tasks until what date?"]
    ],
    [
        r"search.*|get.*",
        ["What would you like to search today?",
        "I can help with that! What would you like to search?",
        "Let me help you find what you're looking for!",
        "Type some key words so I know what to search!"]  
    ],
    [
        r"count.*|stats.*|statistics.*",
        ["Sure! Let's see some statistics about your tasks."]
    ],
    [
        r"list.*|due.*|TODO list.*",
        ["Here's your TODO list!",
        "What's due today?"]
    ],
    [
        r"tasks?|options?|choices?",
        ["Would you like to add a task, search for a task, or list all your tasks?"]
    ]
]

#override respond function in nltk to take in array of keywords
def reply(str):
        # check each pattern
        for (pattern, response) in pairs:
            match = re.match(pattern, str)

            # did the pattern match?
            if match:
                resp = random.choice(response)  # pick a random response
                return resp

#override converse function in nltk to get user input and convert to array of cleaned words
def conversation(quit="quit"):
    user_input = input("Type quit to exit ")
    if(user_input != quit) :
        print(reply(cleanup.askCleanString(user_input)))
        conversation()

conversation()