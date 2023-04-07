#!/usr/bin/python3
import cipher_logo
def ceaser(text, shift, direction):
    new_text = ""
    for ch in text:
        if ch in alphabet:
            if direction == "encode":
                count = 0
                while alphabet[count] != ch:
                    count += 1
                new = count + shift
                new_text += alphabet[new]
            elif direction == "decode":
                count = 25
                while alphabet[count] != ch:
                    count += 1
                new = count - shift
                new_text += alphabet[new]
            else:
                print("Incorrect input. Type encode or decode")
        else:
            new_text += ch
    print(f"The {direction}d text is {new_text}")

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
print(cipher_logo.logo)
cont = True
while cont != False:
    direction = input("Type 'encode' to encrypt and 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 25
    ceaser(text, shift, direction)
    i = input("Do you want to continue? Type 'yes' to continue and 'no' to stop:  ").lower()
    if i == "yes":
        cont = True
    else:
        cont = False
