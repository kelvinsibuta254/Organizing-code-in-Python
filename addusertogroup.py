def add_user_to_group():
    username = input("Enter the name of the user that you wantto addto agroup: ")#Takesthe name of the user that you want to work with
    output = subprocess.Popen('groups', stdout=subprocess.PIPE).communicate()[0]#Performs the groupscommand and saves the result to a variable, which is output later for the user to select from

    print("Enter a list of groups to add the user to")#Takes the list of groups that the user should be added to
    print("The list should be separatedby spaces, for example:\r\n group1 group2 group3")
    print("The available groups are:\r\n " + output)
    chosenGroups = input("Groups: ")

    output = output.split(" ")#Splits the string from the previous section into an array
    chosenGroups = chosenGroups.split(" ")#Splits the string from the previous section into an array

    print("Add To:")
    found = True
    groupString = ""

    for grp in chosenGroups:#For each member of the chosen Groups array
        for existingGrp in output:#For each member of the output array
            if grp == existingGrp:#If the members exist in both groups
                found = True
                print("-Existing Group : " + grp)
                groupString= groupString + grp + ","
        if found == False:
            print("-New Group : " + grp)#Prints whether the script createsa new group or usesan existing group when the user is added

            groupString = groupString + grp + ","
        else:
            found = False

groupString = groupString[:-1] + " "#Removes the final comma (,) and adds a space at the endof the line
confirm = ""
while confirm != "Y" and confirm != "N" :#The whileloopends only if the user enters Y or N
    print("Add user '" + username + "' to thesegroups? (Y/N)")
    confirm = input().upper()#Takes user input and stores it in the variable confirm
if confirm == "N":
    print("User '" + username + "' not added")
elif confirm == "Y":
    os.system("sudo usermod -aG " + groupString + username)
    print('"User '" + username + '" added)#If  the user entered Y, calls the Linux Command sudo usermod –aGwith the groups and the user that you created earlier
#The whileloop exits if the user enters n, N, y, or Y. The input.upper() converts the user input to upper case.

def install_or_remove_packages():
    iOrR= ""
    while iOrR!= "I" and iOrR!= "R":
        print("Would you like to install or remove packages? (I/R)")
        iOrR= input().upper()
        if iOrR == "I":
            iOrR= "install" #Checks whether the user wants to install or remove packages
        elif iOrR == "R":
            iOrR= "remove"
print("Entera list of packages to install")
print("The list should be separated by spaces, for example:")#Describes how the input should be formatted

print(" package1package2package3")
print("Otherwise, input 'default' to " + iOrR + " the default packages listed in this program")
packages = input().lower()
if packages == "default":# Installs the default list of packages for the script if the user specifies default
    packages = defaultPackages
    if iOrR == "install":
        os.system("sudo apt-get install " + packages)#Calls the Linux command sudo apt-get installwith the packages that you specified

elif iOrR == "remove":
    while True:
        print("Purge files after removing? (Y/N)")
        choice = input().upper()#Changes the user input into uppercase so that it can be compared
        if choice == "Y":
            os.system("sudo apt-get --purge " +iOrR + " " + packages)#Calls the Linux command sudo apt-get –-purge removewith the packages that youspecified

            break
        elif choice == "N":
            os.system("sudo apt-get " + iOrR + "" + packages)#Calls the Linux command sudo apt-get remove with the packages that you specified
            break
    os.system("sudo apt autoremove")#Calls the Linux command sudo apt autoremove, which removes any old package files(if they exist)

    def clean_environment():
        os.system("sudo apt-get autoremove")#Removes dependencies that were installed with applications and are no longer used by anything on the system

        os.system("sudo apt-get autoclean")#Cleans obsolete deb-packages
    #Used together,these two Linux commands are a good way to maintain an up-to-date and clean environment.

    def update_environment():
        os.system("sudo apt-get update")#Updates the package lists for packages that must be upgraded, and also for new packages that were recently added to the repositories
        os.system("sudo apt-get upgrade")#Updates the current OS, Note:This commanddoesnot upgrade the OSto a higher version. For example,if you run the command on Debian V8, it will notget Debian V9
        os.system("sudo apt-get dist-upgrade")#Downloads and installs updates for all installed packages






