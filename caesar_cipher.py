# Create a function encrypt_caesar(text: str, shift: int) -> str that encrypts a message using the Caesar Cipher.

# Only encrypt alphabetic characters (ignore digits, spaces, punctuation).
# Maintain case (uppercase/lowercase).
# The alphabet should wrap around (e.g., 'z' with shift 2 → 'b').
# The shift can be positive or negative.

def ceasar_cipher(str, shift):
    res = ''
    for i in range(len(str)):
        if(str[i].isalpha()):
            newChar = chr(ord(str[i]) + shift)
            res += newChar
        else:
            res += str[i]
    return res

print(ceasar_cipher("Hello, World!", 3) )     # "Khoor, Zruog!"
