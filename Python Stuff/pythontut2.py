import math
import random

for i in [3, 4, 5]:
    print("i Even? = {}".format(i % 2 == 0))

for i in range(21):
    if i % 2 != 0 :
        print("Odd? = {}".format(i))

fibRange = input("How many Fibonacci numbers do you want generated? ")
print("First {} numbers of the Fibonacci Sequence:".format(fibRange))

if int(fibRange) > 0:
    for num in range(1, int(fibRange)):
        fib = (((1 + 5**(1/2))/2)**num - ((1 - 5**(1/2))/2)**num)/5**(1/2)
        print(round(fib))
else:
    print("Don't")

your_float = input("Enter a float: ")

your_float = float(your_float)
print("Round to 2 decimales : {:.2f}".format(your_float))

investment = input("Enter your investment")
rate = input("Enter rate percentage e.g. 32")

investment = float(investment)
rate = float(rate) * 0.01

for year in range(10):
    investment += investment*rate
    if year == 9:
        print("At year {} your balance is: ${:.2f}".format(year, investment))

random_num = random.randrange(1, 51)

i = 1
while(i != random_num):
    i += 1
    print("The random value is:", random_num)

x = 1

# while x <= 20:
#     if i % 2 == 0:
#         i += 1
#         continue
#     if i == 15:
#         break
#     print("Odd: ", i)

tree_height = input("Enter tree length")
tree_height = int(tree_height)

spaces = tree_height - 1
hashes = 1

stump_spaces = tree_height - 1

while tree_height != 0:
    for i in range(spaces):
        print(' ', end="")
    for i in range(hashes):
        print('#', end="")

    print()
    spaces -= 1
    hashes += 2

    tree_height -= 1
for i in range(stump_spaces):
    print(' ', end="")

print("#")

something = input("Enter some value")

something += "Matthew"
print("{} + {:.2f}".format(something, 3.1415926535897932384626433832795028841971693993751058209749445))