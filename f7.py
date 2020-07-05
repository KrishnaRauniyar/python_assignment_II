# Create a list of tuples of first name, last name, and age for your friends and colleagues. If you don't know the age, put in None. Calculate the average age, skipping over any None values. Print out each name, followed by old or young if they are above or below the average age.

my_input = ["krishna", "kavir", "nabin", "james"]
my_input1 = ["rauniyar", "ramanava", "pakka", "sikkar"]
my_input2 = [23, 24, 22, None]

# zip to list the tuples
zipped = list(zip(my_input, my_input1, my_input2))
print(zipped)

av = [zi[2] for zi in zipped]
av_without_none = list(filter(None, av))
average = sum(av_without_none) / len(av_without_none)
print(average)

# remaining




