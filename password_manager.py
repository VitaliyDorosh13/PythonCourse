
#import lubrary Fernet for security
from cryptography.fernet import Fernet

#add a method where we generete random number and write 
''' 
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
'''
#loading key from file
def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

maaster_pwd = input("What is the master password? ")
key = load_key() + maaster_pwd.encode()
fer = Fernet(key)

#method where we can check existing password
def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User", user, "Password: ", fer.decrypt(passw.encode()).decode())
            

#the method gonna add a new password for user
def add():
    name = input("Account name: ")
    pwd = input("Password: ")

    with open('password.txt', 'a') as f:
        f.write( name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

#create a cycle
while True:

    #using input to chech the variacy of answer from costumer
    mode = input("What you like to add a new passwrd or view existing?, press q to quit ").lower()

    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode")
        continue