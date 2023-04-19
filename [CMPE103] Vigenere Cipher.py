#Pierre Victor T. Zurbito
#BSCPE 1-4
#Object Oriented Programming

#Importing sys that can halt the program should None be the data form
import sys
#Defining a class that encrypts the message
def vigenere(message, keyword):
    #Turns the message and keyword into uppercase letters
    message_uppercase=message.upper()
    keyword_uppercase=keyword.upper()
    #Strips the spaces on the letters should there be any
    message_stripped=message_uppercase.replace(" ","")
    keyword_stripped=keyword_uppercase.replace(" ","")
    #Generates the keyword to be in the same length as message, should they not be equivalent
    keyword_match=keyword_stripped*(len(message_stripped)//len(keyword_stripped)+1)
    keyword_match=keyword_match[:len(message_stripped)]
    #Sets a variable for the encrypted message
    encrypted_message=""
    #Starting the encryption process
    for i in range(len(message_stripped)):
        #Checks if all the characters of the message is alphabet
        if message_stripped[i].isalpha():
            #Converts the alphabets of the message into numeric equivalent
            message_numbered=ord(message_stripped[i])-65
            #Converts the key into numeric equivalents
            keyword_numbered=ord(keyword_match[i])-65


#Asking the user for a message to encrypt as well as a desired keyword
message = input("Please input a desired message to encrypt:")
keyword = input("Please input a desired keyword:")
encrypted_message=vigenere(message, keyword)

#Prompting the program to end if the encrypted message results to None
