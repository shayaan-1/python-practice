
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
