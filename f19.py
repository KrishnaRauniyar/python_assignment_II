# Write a Python class to find validity of a string of parentheses, '(', ')', '{', '}', '[' and ']. These brackets must be close in the correct order, for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid

class Check_validity:
    def baracket(self,bra):
        count=0
        for i in bra:
            if((i=='(')|(i=='{')|(i=='[')):
                count+=1
            else:
                count-=1
        if count==0:
            return "Valid"
        else:
            return "Invalid"
my_input=input('Enter brackets : ')
obj=Check_validity()
print('Output : ',obj.baracket(my_input))