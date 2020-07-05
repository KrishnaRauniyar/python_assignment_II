#  Create a tuple with your first name, last name, and age. Create a list,
# people, and append your tuple to it. Make more tuples with the corresponding information from your friends # and append them to the list. Sort the list. When you learn about sort method, you can use the key parameter to sort by any field in the tuple, first name, last name, or age.


my_input = "Krishna Rauniyar 23"
my_input1 = "Nabin Pakka 22"
my_input3 = "Ramita Gurung 23"

my_tuple = tuple(map(str, my_input.split(' ')))
my_tuple1 = tuple(map(str, my_input1.split(' ')))
my_tuple3 = tuple(map(str, my_input3.split(' ')))

people = []
people.append(my_tuple)
people.append(my_tuple1)
people.append(my_tuple3)
print("List of tuples : ", people)
# sort through last name
people.sort(key=lambda tup: tup[1])
print("List of tuples after sorting : ", people)