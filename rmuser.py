import os
def remove_user():
    confirm = "N"
    while confirm != "Y":#Continues while the user does not enterY

        username = input("Enter the name of the user to remove: ")#Takes user input and assigns it to a variable
        print("Remove the user : '" + username + "'? (Y/N)")
        confirm = input().upper()
        os.system("sudo userdel -r " + username)#Calls the Linux command sudo userdel -r with the provided variable as the usernameafter the while loop exits
    remove_user()