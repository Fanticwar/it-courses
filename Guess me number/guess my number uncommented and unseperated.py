import random,time
min_guesses = 4 
max_guesses = 8 
min_number = 1 
max_number = 20 
gc = 0 
gl = random.randint( min_guesses , max_guesses ) 
cn = random.randint( min_number , max_number ) 
g = None 
print("Hello! We have a guessing game featuring numbers and confusion. Intrested?") 
time.sleep(2) 
print("We have picked a number between " + str(min_number) + " and " + str(max_number))
print("You have " + str(gl) + " attempts. Go.")
while True:
    try:
        g = int(input())
    except:
        print("Try using a digits guess.")
        continue
    gc = gc + 1
    if g == cn:
        break
    gl = gl - 1
    if gl == 0:
        break
    if g > cn:
        print("High. You can guess " + str(gl) + " more time(s).")
    else:
        print("Low. You can guess " + str(gl) + " more time(s).")
if g == cn:
    print("Yippie! you got it in " + str(gc) +" guesses.")
else:
    print("You failed. It was " + str(cn) + ".")
        
    
