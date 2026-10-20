import string
import random

def password_generator():
    password = []
    letters = list(string.ascii_letters)
    digits = list(string.digits)
    symbols = list(string.punctuation)
    num_letters = False
    num_digits = False
    num_symbols = False
    
    while not check_validity(num_letters):
        num_letters = int(input("How many letters would you like in your password?"))
    while not check_validity(num_digits):
        num_digits = int(input("How many numbers would you like in your password?"))
    while not check_validity(num_symbols):
        num_symbols = int(input("How many symbols would you like in your password?"))
    
    random.shuffle(letters)
    random.shuffle(digits)
    random.shuffle(symbols)
    
    letter_slice = letters[0:num_letters:1]
    digit_slice = digits[0:num_digits:1]
    symbol_slice = symbols[0:num_symbols:1]
    
    print(f"Letters: {letter_slice}")
    print(f"Numbers: {digit_slice}")
    print(f"Symbols: {symbol_slice}")
    password = letter_slice + digit_slice + symbol_slice
    
    random.shuffle(password)
    return "".join(password)
    

def check_validity(input):
    while not isinstance(input,int):
        try:
            input = int(input)
        except ValueError:
            print("That's not a number, try again")
        
    return input


print(password_generator())