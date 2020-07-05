# Write an if statement to determine whether a variable holding a year
# is a leap year.

year = 2000

if year % 400 == 0 and year % 4 == 0:
    print("{} is a leap year".format(year))

else:
    print("{} is not a leap year".format(year))