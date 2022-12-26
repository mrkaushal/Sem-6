# Caesar Cypher Encryption and Decryption

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

text = input("Enter the text: ")
for i in range(26):
    print("Shift " + str(i) + ": " + decrypt(text, i))