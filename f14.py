# Write a function that reads a CSV file. It should return a list of dictionaries, using the first row as key names, and each subsequent row as values for those keys. For the data in the previous example it would return: [{'name': 'George', 'address': '4312 Abbey Road', 'age': 22}, {'name': 'John', 'address': '54 Love Ave', 'age': 21}]


import csv

header=['name', 'address', 'age']
data = [{'name': 'George', 'address': '4312 Abbey Road', 'age': 22},
        {'name':'John', 'address': '54 Love Ave', 'age': 21}]
filename='file13.csv'
def store_data(file_name,rows):
    file=open(file_name,'w')
    filewriter = csv.DictWriter(file,fieldnames=header)
    filewriter.writeheader()
    filewriter.writerows(rows)
    file.close()
store_data(filename,data)
print('Input data : ',data)
print('your data is stored to ',filename,' file.')