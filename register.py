'''
Diana Flores
'''

import json

def firstPart():
    #Setting up my token
    token = "ed5facd58009cc61842f923d8df3f62c"
    
    #Making a dictionary
    dict = {"token": token,"github": "https://github.com/dianaflowerss/code2040-TechAssessment"}
    
    #Using POST
    myAPI = requests.post("http://challenge.code2040.org/api/register", json=dict)
    print(myAPI.text)
    return token
    
def main():
    token = firstPart()
    
main()
