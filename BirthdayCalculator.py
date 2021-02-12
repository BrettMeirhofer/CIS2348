# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


year = int(input("What is the current year?\n"))
month = int(input("What is the current month?\n"))
day = int(input("What is the current day?\n"))

birthyear = int(input("When is your birth year?\n"))
birthmonth = int(input("When is your birth month?\n"))
birthday = int(input("When is your birth day?\n"))

print("You are {} years old!".format(year-birthyear))

if(month == birthmonth and day == birthday):
    print("Happy birthday!")
