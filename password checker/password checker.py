cp = "SwearWord420" 
#correct password (cp)

change = ""
#initialise change variable

#ask user for password
print("Password?")

#input guessed password(gp)
gp = input()

#line break
print(" ")

#is the guessed password correct??
if gp == cp:

    #greet
    print("Yippie it is you.")


    #until user gives a valid answer:
    while change != "y" and change != "n" :
    
        # ask to change password
        print("Would you like to change the password?(y/n)")
        change = str(input())

    #if yes
    if change == "y":
        print("Whoopsy dasies i can't, i dont know how to edit files yet")

#when everything is done or user gets password incorect
print("You have been booted off this program. bye bye.")
    
    
    
