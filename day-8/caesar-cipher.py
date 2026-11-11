alphabet = list("abcdefghijklmnopqrstuvwxyz")
def caesar_cipher(direction, message, shift):
    if direction.lower() == "decode":
        shift *= -1
    new_message = ""
    for part in message:
        if part.isalpha():
            shifted = alphabet.index(part) + shift
            
            shifted %= len(alphabet)
            new_message += alphabet[shifted]
        else:
            new_message += part
    
    print(f"Here is your {direction}d result: {"".join(new_message)}")
    
    return "".join(new_message)
    
def encrypt(message, shift):
    new_message = ""
    for part in message:
        shifted = alphabet.index(part) + shift
        
        shifted %= len(alphabet)
        new_message += alphabet[shifted]
    
    print(new_message)
    return "".join(new_message)
    
def decrypt(message, shift):
    deciphered = ""
    for part in message:
        unshifted = alphabet.index(part) - shift
        unshifted %= len(alphabet)
        deciphered += alphabet[unshifted]
    print(f"Deciphered: {deciphered}")
    return deciphered

should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    while direction.lower() != 'encode' and direction.lower() != 'decode':
        print("Invalid direction choice")
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

    msg = input("Type your message:\n")
    shft = int(input("Type the shift number:\n"))
    caesar_cipher(direction, msg, shft)
    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
    if restart == "no":
        should_continue = False
        print("Goodbye")
