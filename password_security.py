import time
import os

users = {"Abdullah Azzam Olcay":"qwerty",
         "Muhammed Asım Olcay":"123456789"}

# user = {name:password...}

user_name = input("Enter your name:\n")

if user_name in users.keys():
    print("Your name is correct\\/\n")
    time.sleep(2)
    print("Welcome...")
    time.sleep(2)
    user_password = input("Enter your password:\n")
    if user_password == users[user_name]:
        print("Your password is correct")
        time.sleep(2)
        print("You entered your account")
        os.system("espeak 'Welcome to your account {}' -s 160".format(user_name))
    else:
        print("Your password is not true")
        os.system("espeak 'Your password is not true' -s 160")
else:
    print("Your name is absent in this website")
    os.system("espeak 'Your name is absent in this website' -s 160")