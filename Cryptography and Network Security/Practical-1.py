# Caesar Cypher Encryption and Decryption

# Encryption
def encrypt(text, s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    return result

# Decryption
def decrypt(text, s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if (char < 'A' or char > 'Z'):
            result += chr((ord(char) - s - 97) % 26 + 97)
        elif (char < 'a' or char > 'z'):
            result += chr((ord(char) - s - 65) % 26 + 65)
        else:
            result = "Invalid Input"  
    return result

# User Case
print("1. Decryption Using Brute Force")
print("2. Encryption")
print("3. Decryption Using Key")

sc = int(input("Enter the value: "))
# For Brute Force Decryption
if sc == 1:
    text = input("Enter the text: ")
    for i in range(26):
        print("Shift " + str(i) + ": " + decrypt(text, i))

#For Encryption
elif sc == 2:
    text = input("Enter the text: ")
    #Convert Text without spaces
    text = text.replace(" ", "")
    s = int(input("Enter the shift: "))
    print("Shift : " + str(s))
    print("Cipher: " + encrypt(text, s))

#For Decryption Using Key
elif sc == 3:
    text = input("Enter the text: ")
    s = int(input("Enter the shift: "))
    print("Shift : " + str(s))
    print("Decrypted Test: " + decrypt(text, s))
else:
    print("Invalid Input")