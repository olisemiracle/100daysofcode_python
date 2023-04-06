#!/usr/bin/python3
def encrypt(text, shift):
    new_text = ""
    for ch in text:
        if ch in alphabet:
            count = 0
            while alphabet[count] != ch:
                count += 1
            new = count + shift
            new_text += alphabet[new]
    print(f"The encoded text is {new_text}")
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
direction = input("Type 'encode' to encrypt and 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
encrypt(text, shift)
