#################
#guess my number#
#################
import random,time

#settings: you can edit this here!_________

min_guesses = 4 #minumum guesses that can be given (def: 4)
max_guesses = 8 #maximum guesses that can be given (def: 8)

min_number = 1 #minimum number that can be chosen (def: 1)
max_number = 20 #maximum number that be chosen (def: 20)

#settings end______________________________


#initialise the variables

gc = 0 #guess counter

gl = random.randint( min_guesses , max_guesses ) #guesses left

cn = random.randint( min_number , max_number ) #correct number 

g = None #user guess

#tell the user the range of values and the amount of guesses they have

print("Hello! We have a guessing game featuring numbers and confusion. Intrested?") #contextual content

time.sleep(2) #allow user to read before shoving next text in face

print("We have picked a number between " + str(min_number) + " and " + str(max_number))
print("You have " + str(gl) + " attempts. Go.")


#Silly loop

while True: #until break

    try:
        g = int(input())
    except:
        print("Try using a digits guess.")
        continue
    
    gc = gc + 1
    
    if g == cn:
        break

#if guess was correct, this bottom part of the loop wont run
    
    #take away 1 guess(cus its wrong)
    gl = gl - 1
    if gl == 0:
        break
    
#if user still has guesses but wrong, tell user if their guess is higher or lower
#and the amount of times they can guess again
    
    if g > cn:
        print("High. You can guess " + str(gl) + " more time(s).")
    else:
        print("Low. You can guess " + str(gl) + " more time(s).")
        
#repeat loop until break


#when no more silly loop: if they lost tell them the right answer, if they won, tell them how fast they got it.
if g == cn:
    print("Yippie! you got it in " + str(gc) +" guesses.")
else:
    print("You failed. It was " + str(cn) + ".")
        
    
