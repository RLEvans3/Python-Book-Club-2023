# Is it random?  An analysis of ones and zeros
# Elizabeth Chaney in 2023 Python Book Club


import random
 
print("Enter a 1, 2, or 3: ")
seedChoice = int(input())
 
# check the seedChoice variable for reasonablness
if (seedChoice < 1 or seedChoice > 3):
        exit("Value not in range.")
 
#Were going to have to eventually activate these seeds to generate the 1s and 0s
if seedChoice == 1:
        print(seedChoice)
        print("Enter a seed as an integer:")
        seed = int(input())
 
if seedChoice == 2:
        print(seedChoice)
        print("Using built-in seeding from computer.")
        # Nothing to do
 
if seedChoice == 3:
        print(seedChoice)
        print("Go get an external seed from the internet")
 
print("\nHow many 1s and 0s are in the string?")
stringLength = int(input())
 
print("\nHow many simulations do you want to run?")
monteSim = int(input())
 
# Outer loop of Monte Carlo sim
for simCounter in range(monteSim):
        print(simCounter+1) #corrected for base 0 counting for the user
 
        # Prepare for the inner loop that generates 1s and 0s  
        userString = []
        firstValue = random.randint(0,1)
        userString.append(firstValue)
 
        stringOrigin = 1
       
        # Inner loop that generates 1s and 0s
        streakCounter = []
        currentStreak = 1
 
        while stringOrigin <= stringLength-1:
                nextValue = random.randint(0,1)
                currentValue = userString[-1]
                userString.append(nextValue)
                #firstValue = userString[0]
                #currentValue = userString[-1]
                print(f"Values (c,n): {currentValue}, {nextValue}")
 
#increment the streakCountuntil the next value is different then and only #then add the streakCount to the list.
 
                if currentValue == nextValue:
                        currentStreak += 1
 
                else:
                        streakCounter.append(currentStreak)
                        currentStreak = 1
 
                stringOrigin += 1
 
        #add final streak to streakCounter
        streakCounter.append(currentStreak)
 
        print("string:", userString)
        print("length of streaks:", streakCounter)
