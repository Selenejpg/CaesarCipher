import art
from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)

def startup():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    
    if direction == "encode" or direction == "decode":
    
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))

        caesar(text, shift, direction)   
    
    else:
        print("Invalid input")

def caesar(plain_text, shift_amount, cypher_direction):     
    word = ""
    
    for char in plain_text:
        if char in alphabet:
            position_alphabet = alphabet.index(char)  
            
            if cypher_direction == "encode":
                shifted_position = (position_alphabet + shift_amount) % 26 
            elif cypher_direction == "decode":
                shifted_position = (position_alphabet - shift_amount) % 26 
                
            encrypted_letters = alphabet[shifted_position] 
            word += encrypted_letters
        else:
            word += char  
             
    print(f"The {cypher_direction}d text is {word}")
    rerun = input("Would you like to restart the programm? Type 'yes' or 'no' to answer ") 

    if rerun == "yes":
        startup()
    else:
        print("Thank you for using Caesar Cipher!")
    
startup()


    