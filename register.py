'''
Diana Flores
email: dicflore@ucsc.edu or dianaf@hughes.net
Code 2040 Technical Assessment
'''
#Required imports
import json
import requests
import iso8601
import datetime


def firstPart():
    #Setting up my token
    token = "ed5facd58009cc61842f923d8df3f62c"
    
    #Making a dictionary
    dict = {"token": token,"github": "https://github.com/dianaflowerss/code2040-TechAssessment"}
    
    #Using POST
    myAPI = requests.post("http://challenge.code2040.org/api/register", json=dict)
    print(myAPI.text)
    return token

def secondPart(token):
    #Dictionary for my token
    tokenDic = {"token": token}

    #Imputs the string
    strResult = requests.post("http://challenge.code2040.org/api/reverse", json=tokenDic)

    strText = strResult.text

    #Reverse the string
    reverseString = strText[::-1]

    #Use POST for the reversed string
    strDict = {"token": token, "string": reverseString}
    stringValue = requests.post("http://challenge.code2040.org/api/reverse/validate", json=strDict)
    print(stringValue.text)

def thirdPart(token):
    
    tokenDic = {"token": token}
    
#Gets the needle and haystack dictionary
    needleRes = requests.post("http://challenge.code2040.org/api/haystack", json=tokenDic)
    haystackDict = json.loads(needleRes.text)
    
    haystack = haystackDict['haystack']
    needle = haystackDict['needle']
    
    for index in range(len(haystack)):
        if haystackDict['needle'] == haystack[index]:
            needle = index
            break;
        
        
    needleDic = {"token": token, "needle": needle}
    needleVal = requests.post("http://challenge.code2040.org/api/haystack/validate", json=needleDic)
    print(needleVal.text)

def fourthPart(token):
    tokenDic = {"token": token}
    pay = requests.post("http://challenge.code2040.org/api/prefix", json=tokenDic)

    prefix = json.loads(pay.text)
    string = prefix["array"]

    arrayN = []

    for word in string:
        if prefix['prefix'] not in word:
            arrayN.append(word)
    
    #Using POST
    load = {'token': token, 'array': arrayN}
    end = requests.post("http://challenge.code2040.org/api/prefix/validate", json=load)
    print (end.text)

#One thing that I had trouble with was setting up the iso8601 into my Python
def fifthPart(token):
    tokenDic = {"token": token}
    dates = requests.post("http://challenge.code2040.org/api/dating", json=tokenDic)
    dateN = json.loads(dates.text)

    #Making the datestamp seconds
    day = str(dateN["datestamp"])
    seconds = str(dateN["interval"])
    convert = datetime.timedelta(seconds=int(seconds))

    parseDate = iso8601.parse_date(day)
    newTime = parseDate + convert

    dateUp = newTime.strftime("%Y-%m-%dT%H:%M:%SZ")

    #Using POST
    newDate = {"token": token, "datestamp": dateUp}
    dVal = requests.post("http://challenge.code2040.org/api/dating/validate", json=newDate)
    print(dVal.text)

 #I made a main so it would be easier to organize all of the challenge sections   
def main():
    token = firstPart()
    secondPart(token)
    thirdPart(token)
    fourthPart(token)
    fifthPart(token)
    
main()
