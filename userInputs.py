seedChoice = 1


print("Enter a 1, 2, or 3: ")
seedChoice = int(input())

# check the seedChoice variable for reasonablness
if (seedChoice < 1 or seedChoice > 3):
	exit("Value not in range.")


# Now do something about it...
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

# Ask the user how many 1s and 0s to generate...

# In a big loop (100? 1000? a million?) generate that number of 1s and 0s...
#	get the mean and stddev of every pass
#	get the cummulative mean of means and mean of stddevs for all passes

# Store these


# Then ask for the user to enter that same number of 1s and 0s and check to 
# see if that sequence's streak mean and stddev all within what you know to
# be random..  Declaer the sequence as random or not random...



