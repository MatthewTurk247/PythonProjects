# Ask the user to input thier name and assign it to a variable named name

num1, num2 = input('Enter 2 numbers: ').split()

sum = int(num1) + int(num2)

difference = int(num1) - int(num2)

product = int(num1) * int(num2)

quotient = int(num1) / int(num2)

remainder = int(num1) % int(num2)

print('{} + {} = {}'.format(num1, num2, sum))
print('{} - {} = {}'.format(num1, num2, difference))
print('{} + {} = {}'.format(num1, num2, product))
print('{} / {} = {}'.format(num1, num2, quotient))
print('{} % {} = {}'.format(num1, num2, remainder))

#kilmoeters = miles * 1.60934
#Enter Miles

miles = input('Enter miles ')

kilometres = float(miles) * 1.60934

if float(miles) == 1.0:
    print('{} mile = {} kilometres'.format(miles, kilometres))
else:
    print('{} miles = {} kilometres'.format(miles, kilometres))



calc1, operator, calc2 = input('Enter calculation').split()

calc1 = float(calc1)
calc2 = float(calc2)

if operator == "+":
    print("{} + {} = {}".format(calc1, calc2, calc1 + calc2))
elif operator == "-":
    print("{} - {} = {}".format(calc1, calc2, calc1 - calc2))
elif operator == "*":
    print("{} * {} = {}".format(calc1, calc2, calc1 * calc2))
elif operator == "/":
    print("{} / {} = {}".format(calc1, calc2, calc1 / calc2))
elif operator == "%":
    print("{} % {} = {}".format(calc1, calc2, calc1 % calc2))
else:
    print("WHAT ARE YOU DOING")

birthday_age = eval(input("Enter age"))
if (birthday_age > 0) and (birthday_age < 19):
    print("important")
elif int(birthday_age) == 21 or int(birthday_age) == 50 or int(birthday_age) == 65:
    print("important")
else:
    print("ha ha")

student_age = input("Enter your age, student")

student_age = int(student_age)

if student_age == 5:
    print("Go to kindergarten")
elif student_age > 5 and student_age <= 17:
    print("Go to grades 1 thorugh 12")
else:
    print("Go to college")