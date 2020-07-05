# Write a binary search function. It should take a sorted sequence and the item it is looking for. It should return the index of the item if found. It should return -1 if the item is not found.


def binary_search(l, n):
    lb = sorted(l)
    if n in lb:
        return list.index(lb, n)
    else:
        return -1
print(binary_search([2,1,6,8,9], 5))