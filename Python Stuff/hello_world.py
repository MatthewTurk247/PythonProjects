print("Hello world!")

fibRange = input("How many Fibonacci numbers do you want generated? ")
print("First {} numbers of the Fibonacci Sequence:".format(fibRange))

if int(fibRange) > 0:
    for num in range(1, int(fibRange)):
        fib = (((1 + 5**(1/2))/2)**num - ((1 - 5**(1/2))/2)**num)/5**(1/2)
        print(round(fib))