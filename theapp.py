import os
import sys

try :
    userSelect = float(input("Hey! Welcome To My Little Encryption/Decryption APP. \nPlease Select(1.Encrypt 2.Decrypt): "))
    
    if userSelect == 1 :
        encryptWord = input("\n\nPlease enter your words to encrypt: ")
        encryptPass = input("Please enter your password to encrypt: ")

        def encrypt (encryptedWord, encryptPass) :
            myCmd = 'echo ' + encryptedWord + ' | openssl enc -k ' + encryptPass + ' -aes-256-cbc -base64 -out "Encrypted Words.txt"'
            os.system(myCmd)
        encrypt(encryptWord, encryptPass)

        filename = "Encrypted Words.txt"
        READ = "r"
        with open(filename, mode = READ) as myDataFile :
            firstline = myDataFile.readline()
                        
        if firstline == "" :
            print("\n\nOOPS! Seems file is empty. something went wrong so please report!.")
            myDataFile.close()
        else :
            print("\n\nDone! Your Encrypted Words Saved Into `Encrypted Words.txt` File!")
            myDataFile.close()

    elif userSelect == 2 :
        decryptWord = input("\n\nPlease enter your words to decrypt: ")
        decryptPass = input("Please enter your password to decrypt: ")

        def decrypt (decryptedWord, decryptPass) :
            myCmd = 'echo ' + decryptedWord + ' | openssl enc -d -k ' + decryptPass + ' -aes-256-cbc -base64 -out "Decrypted Words.txt"'
            os.system(myCmd)
        decrypt(decryptWord, decryptPass)

        filename = "Decrypted Words.txt"
        READ = "r"
        with open(filename, mode = READ) as myDataFile :
            firstline = myDataFile.readline()
                        
        if firstline == "" :
            print("\n\nOOPS! Seems file is empty. maybe you typed worng password.")
            myDataFile.close()
        else :
            print("\n\nDone! Your Decrypted Words Saved Into `Decrypted Words.txt` File!")
            myDataFile.close()

except ValueError:
    print("Hey! Just Type 1 or 2")
except :
    fullerror = sys.exc_info()[0]
    print(f"I found an error!\nReport it as: {fullerror}") 


print("\n\nThanks for using my app!\nCreated by Esmail EL BoB under GNU GPL V3")