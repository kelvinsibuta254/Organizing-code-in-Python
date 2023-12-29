def new_user():
    confirm = "N"
    while confirm != "Y":#Continues while the user does not enterY
        username = input("Enter thename of the user to add: ")#Takes user input and assigns it to a variableCalls the Linux command sudo adduserwith the provided variable as the usernameafter the while loop exits

        print("Use the username '" + username + "'? (Y/N)")
        confirm = input().upper()
        os.system("sudo adduser " + username)#Calls the Linux command sudo adduserwith the provided variable as the usernameafter the while loop exits

    new_user
