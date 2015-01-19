'''
Created on 14. jan. 2015

bisectionsearch.py
@author: Stian Strom Anderssen s177437
@course MS015A
The script use a dictionarylist where all the letters has a corresponding shift 3 letter. 
On a later point, it could be nice to implement a method that generated the decrypted alphabet based on a shift number 
you send as a parameter. The dictionary is hardcoded at this point.   
This script has four defs:
encryptLetter - Takes a letter as a parameter, encrypts it, and returns it.   
decryptLetter- Takes a letter as a paramter, decrypts it, and returns it. 
encryptSentence - Takes a sentence as a parameter and sends it to encryptLetter to encrypt the Letter, 
It takes the letter returned and adds it to the encrypted sentence 
decryptSentence- Takes a sentence as a paramter and sends it to decryptLetter to decrypt the letter. 
It takes the letter returned, and adds it to the decrypted sentence. 

'''
alphabetcipher={'a':'d','b':'e','c':'f','d':'g','e':'h','f':'i','g':'j','h':'k','i':'l','j':'m','k':'n','l':'o','m':'p','n':'q','o':'r','p':'s','q':'t','r':'u','s':'v','t':'w','u':'x','v':'y','w':'z','x':'a','y':'b','z':'c',}
def encryptSentence(sentence):
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


msg = raw_input("Your message to encode? ")
if len(msg)>0 : 
    secret=encryptSentence(msg)
    print"The encoded messsage is: ", secret
        
secret = raw_input("Your message to decode?")
if len(secret)>0 :
    msg=decryptSentence(secret)
    print "The decoded message is: ", msg
    

         
    
    
