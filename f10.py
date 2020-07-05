# Write a function that takes camel-cased strings (i.e. ThisIsCamelCased), and converts them to snake case (i.e. this_is_camel_cased). Modify the function by adding an argument, separator, so it will also convert to the kebab case (i.e.this-is-camel-case) as well.

def change_case(str):
    res = [str[0].lower()]
    for c in str[1:]:
        if c in ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
            res.append('_')
            res.append(c.lower())
        else:
            res.append(c)

    return ''.join(res)


str = "ThisIsCamelCased"
print(change_case(str))
