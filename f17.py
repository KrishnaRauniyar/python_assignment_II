#  Write a program that serves as a basic calculator. It asks for two numbers, then it asks for an operator. Gracefully deal with input that doesn't cleanly convert to numbers. Deal with division by zero errors.


num1=int(input('Enter first number : '))
num2=int(input('Enter second number : '))
operator=input('Enter operator : ')
if operator=='+':
    print('sum of {} and {} : {}'.format(num1,num2,(num1+num2)))
elif operator=='-':
    print('subtraction of {} and {} : {}'.format(num1,num2,(num1-num2)))
elif operator=='*':
    print('multiplication of {} and {} : {}'.format(num1,num2,(num1*num2)))
elif operator=='/':
    try:
        print('Division of {} and {} : {}'.format(num1,num2,(num1/num2)))
    except:
        print('Divisor can not be Zero')
else:
    print('You did not enter any operator.')