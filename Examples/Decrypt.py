from cryptography.fernet import Fernet

key = Fernet.generate_key()

# Instance the Fernet class with the key

fernet = Fernet(key)
encMessage= input("Encrypt Txt :- ")
encMessage =encMessage.encode('utf-8') 

decMessage = fernet.decrypt(encMessage).decode()

print("decrypted string: ", decMessage)
