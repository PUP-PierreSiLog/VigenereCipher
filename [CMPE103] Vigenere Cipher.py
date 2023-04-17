#Pierre Victor T. Zurbito
#BSCPE 1-4
#Object Oriented Programming

#Importing sys that can halt the program should None be the data form
import sys
#Defining a class that encrypts the message
def vigenere(message, keyword):

#Asking the user for a message to encrypt as well as a desired keyword
message = input("Please input a desired message to encrypt:")
keyword = input("Please input a desired keyword:")
encrypted_message=vigenere(message, keyword)
