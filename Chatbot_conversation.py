#Since Chatbot_conversation.py is the main driver (see init.py for more), 
#the other related files are imported here and executed as one
import Chatbot_word_cleanup as cleanup
import Chatbot_utilities as util
import Chatbot_file_editor as io
import re, random

#Dialogue
#each pair is an array of [x,y] where 
#x is an array of keywords to trigger action,
#y is an array of responses
#r for regular expression
pairs =[
    [
        r".*subtask.*",
        ["What number task should this new subtask fall under?",
        "This new subtask should go under what task number?"]
    ],
    [
        r".*add.*",
        ["What task should I add to your TODO list?",
        "I'm ready! Let's add a task to your TODO list.",
        "What task am I adding?"]
    ],
    [
        r".*delete.*|.*remove.*|.*trash.*",
        ["What task number should I remove?",
        "What is the number of the task to be deleted?"]

    ],
    [
        r".*search.*until.*|.*get.*until.*",
        ["Get tasks until what date and time?"]
    ],
    [
        r".*search.*name.*|.*get.*name.*",
        ["What would you like to search today?",
        "I can help with that! What would you like to search?",
        "Let me help you find what you're looking for!",
        "Type some key words so I know what to search!"]  
    ],
    [
        r".*search.*|.*get.*",
        ["What would you like to search today?",
        "I can help with that! What would you like to search?",
        "Let me help you find what you're looking for!",
        "Type some key words so I know what to search!"]  
    ],
    [
        r".*count.*|.*stats.*|.*statistics.*",
        ["Sure! Let's see some statistics about your tasks."]
    ],
    [
        r".*list.*|.*due.*|.*TODO list.*",
        ["Here's your TODO list!",
        "What's due on your list?"]
    ],
    [
        r".*tasks?.*|.*options?.*|.*choices?.*|.*help.*",
        ["You can:\nadd task\nadd subtask\nremove task\nsearch task by name\nsearch task by date\nview stats\nlist tasks"]
    ]
]

#follows up on chatline with additional info if required
#writes to command file to communicate with TODO list
def decideAction(i: int):
    ret_string = ""
    if(i == 0):
        task_num = input("Task number: ")
        ret_string = "create subtask " + task_num
    elif(i == 1):
        task_name = input("Task name: ")
        task_datetime = util.requestDate()
        ret_string = "create task " + task_name + " " + task_datetime
    elif(i == 2):
        task_num = input("Task number: ")
        ret_string = "delete task " + task_num
    elif(i == 3):
        task_datetime = input("Date and time to search: ")
        ret_string = "search task " + task_datetime
    elif(i == 4):
        task_name = input("Task name to search: ")
        ret_string = "search task " + task_name
    elif(i == 5):
        print("Did you mean: search by name | search by datetime | get list of tasks ?")
    elif(i == 6):
        ret_string = "stats"
    elif(i == 7):
        ret_string = "display list"
    elif(i == 8):
        #help menu; not a command
        pass
    else:
        ret_string = "ERROR: Could not determine action."
    callOutWriter(ret_string+"\n")

#Initializes Outwriter object from Chatbot_file_editor.py and updates commands.txt
def callOutWriter(str: str):
    writer = io.Outwriter("commands.txt")
    writer.writeToFile(str)
    writer.closeFile()

#Converts a list of lemmatized keywords to a single string for regex
def arrToString(arr):
    ret_string = ""
    for a in arr:
        ret_string += a
    return ret_string

#override respond function in nltk to take in array of keywords
def reply(str):
        # check each pattern
        idx = 0
        for (pattern, response) in pairs:
            match = re.match(pattern, str)

            # did the pattern match?
            if match:
                resp = random.choice(response)  # pick a random response
                return resp, idx
            idx += 1

#override converse function in nltk to get user input and convert to array of cleaned words
def conversation(quit="quit"):
    user_input = input("Type quit to exit ")
    if(user_input != quit) :
        arr = cleanup.askCleanString(user_input)
        s = arrToString(arr)
        chatline, act = reply(s)
        print(chatline)
        decideAction(act)
        conversation()