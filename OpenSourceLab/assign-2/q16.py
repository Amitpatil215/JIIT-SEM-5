# Program to get letter count in a text file

# explit function to return the letter count
def letterFrequency(fileName, letter):
	# open file in read mode
	file = open(fileName, 'r')

	# store content of the file in a variable
	text = file.read()

	# using count()
	return text.count(letter)


# call the function and display the letetr count
print(letterFrequency('gfg.txt', 'g'))
