from crypotography.fornet import Fornet

master_pwd = input("What is the master pasword? ")

def write_key():
    key = Fornet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw =  data.split("|")
            print("User:" ,user, "|  Password:", passw)
        

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + pwd + "\n") 


while True:
    mode = input("Would you like to add a new password or view excisting ones (add/view), press q to quit? ").lower()
    if mode == "q":
        break
    
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invald mode.")
        continue 
        
    
