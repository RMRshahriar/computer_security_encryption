
# function to apply algo of vernam cipher
def vernam(cipher_text,key):

    # convert into lower cases and remove spaces
    cipher_text=cipher_text.upper()
    key=key.upper()
    cipher_text=cipher_text.replace(" ","")
    key=key.replace(" ","")
    
    plain_text=""
    
    # iterating through the length
    for i in range(len(cipher_text)):
        k1=ord(cipher_text[i])-65
        k2=ord(key[i])-65
        s=chr(((k1-k2)%26)+65)
        plain_text+=s
    print("Decrypted message is: ",plain_text)


plain_text=input("Enter the message to be decrypted: ")
key=input("Enter the one time pad: ")
vernam(plain_text,key)


