# Find a package in the Python standard library for dealing with JSON. Import the library module and inspect the attributes of the module. Use the help function to learn more about how to use the module. Serialize a dictionary mapping 'name' to your name and 'age' to your age, to a JSON string. Deserialize the JSON back into Python.


import json

class Show_json:
    def json_error(self):
        methods = ['__init__', '__reduce__']
        attribute = ['msg', 'doc', 'pos', 'lineno', 'colno']
        print('Methods : ', methods)
        print('Attribute : ', attribute)

    def json_decoder(self):
        methods = ['__init__', 'decode', 'raw_decode']
        attribute = ['*', 'object_hook', 'parse_float', 'parse_int', 'parse_constant', 'strict', 'object_pairs_hook']
        print('Methods : ', methods)
        print('Attribute : ', attribute)

    def json_encoder(self):
        methods = ['__init__', 'default', 'encode', 'iterencode']
        attribute = ['*', 'skipkeys', 'ensure_ascii', 'check_circular', 'allow_nan', 'sort_keys', 'indent',
                     'separators', 'default']
        print('Methods : ', methods)
        print('Attribute : ', attribute)

    def json_function(self):
        json_func = ['dump', 'dumps', 'load', 'loads']
        print('FUNCTION : ', json_func)


print('Welcome to Json')
print('The josn package contains three Class : ')
print('press the key to see more :')
print('1 for JSONDecodeError')
print('2 for JSONDecoder')
print('3 for JSONEncoder')
print('4 for FUNCTIONS')
code = int(input())
error = Show_json()
if code == 1:
    error.json_error()
elif code == 2:
    error.json_decoder()
elif code == 3:
    error.json_encoder()
elif code == 4:
    error.json_function()
else:
    print('Please enter correct key : ')

print('Convertion of dictionary to json:')
dictionary = {'name': 'Krishna Rauniyar', 'address': 'Banasthali', 'age': 23}
result = json.dumps(dictionary)
print('Json of dictionary : ', result)