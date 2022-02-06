# Hackviolet-2022  
### By: Lily Chiang, James DeLoach, and Patrick Dewey  
  
---  
  
### Project for the Virginia Tech Hackviolet 2022 Hackathon:  
  
## Secure TODO list with chatbot interface  

---

## Security:  
1) Individual account and login system  
2) sha256 password encryption  
3) Sms two-factor authentication system powered by twlio  
4) sha256 encrypted two-facor authentication code
   
5) TODO - encrypt user todo list data  
  
---  

## TODO List Features:  
1)  


---

## Chatbot Features:  
1)  Python implementation; takes user requests and determines desired commands to execute on TODO List
2)  User input cleanup using nltk stemming and lemmatization
3)  Robust natural language processing with regex
4)  Versatile date and time parsing
5)  Uses Outwriter class to log decisions as commands to a txt file for TODO List to execute

---  
## Usage Instructions:  
1) Clone repository  
2) Set up personal twilio account
3) get twlio sid, auth token, and phone number, then rename example.env to .env and fill in your information  
4) make sure twilio and dotenv are installed via pip
5) run 'python init.py' in your terminal and follow instructions from there

