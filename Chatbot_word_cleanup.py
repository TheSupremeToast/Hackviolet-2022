from nltk import pos_tag
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

specialChars = """'~:+[\@^{%(-"*|,&<`}._=]!>;?#$)/"""

def clean(str) -> str:
    returnString = ""
    for i in range(len(str)):
        if(str[i] not in specialChars):
            returnString += str[i]
    return returnString 

def stemlem(str) -> list :
    #Stemmatization
    tokens = word_tokenize(str)
    ##python -m nltk.downloader all
    ##in command prompt installs averaged_perceptron_tagger needed for pos_tag
    tokens = pos_tag(tokens)

    #Lemmatization
    lem_tool = WordNetLemmatizer() 
    lem_tokens = []
    for t,s in tokens:
        #v = verb, j = adjective, r = adverb
        if(s.startswith('V') or s.startswith('R') or s.startswith('J')) :
            try :
                lem_tokens.append(lem_tool.lemmatize(t,pos=s[0].lower()))
            except :
                lem_tokens.append(t)
        else :
            lem_tokens.append(t)
    return lem_tokens

def askCleanString(str: str) -> list:
    ##nltk.download('punkt')
    str = clean(str)
    li = stemlem(str)
    print("Your cleaned reply is",li)
    return li
