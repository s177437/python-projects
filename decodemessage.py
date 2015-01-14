'''
Created on 14. jan. 2015

@author: stianstrom
'''
alphabetcipher={'a':'d','b':'e','c':'f','d':'g','e':'h','f':'i','g':'j','h':'k','i':'l','j':'m','k':'n','l':'o','m':'p','n':'q','o':'r','p':'s','q':'t','r':'u','s':'v','t':'w','u':'x','v':'y','w':'z','x':'a','y':'b','z':'c',}
def encryptSentence(sentence):
   # words=sentence.split(" ") 
    encryptedSentence = ""
    lowercasesentance=sentence.lower()
    words= list(lowercasesentance)
    for word in words :  
       newletter=encryptLetter(word)
       encryptedSentence+=newletter
    return encryptedSentence

def decryptSentence(sentence):
   # words=sentence.split(" ") 
    decryptedSentence = ""
    lowercasesentance=sentence.lower()
    words= list(lowercasesentance)
    for word in words :  
       newletter=decryptLetter(word)
       decryptedSentence+=newletter
    return decryptedSentence
        

def decryptLetter(character):
    for letter, decodedletter in alphabetcipher.items() :
        if(character == decodedletter): 
            return letter
        elif(character==' '): 
            return ' '
            
def encryptLetter(character):
    for letter, decodedletter in alphabetcipher.items(): 
        if(character==letter) :
            return decodedletter
        elif(character==" "): 
            return " "


#Testcomment
testString=encryptSentence("the cake is a lie")
print testString

         
    
    
