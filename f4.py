#  Create a list. Append the names of your colleagues and friends to it. Has the id of the list changed?
#  Sort the list.
#  What is the first item on the list? What is the second item on the list?

# no id of list is not changed
def checkId(string):
    arr = []
    print("The is before append: ", id(arr))
    for i in range(len(string)):
        arr.append(string[i])
        print("The id after append", id(arr))
        arr.sort()
    return print("The two names are {}".format(arr[0:2]))

print(checkId(["rahul", "krishna", "pakka", "gaurav", "anil", "ramita"]))
print("The id before and after append remains the same")

