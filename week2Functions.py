# Week 2 - Functions
# This script provides two simple functions
# The first function accepts a number and prints
# out the OU cheer that number of times

def functionBoomer(n):
    for i in range(n):
        print("Boomer")
        print("Sooner")
        

# Notice there is not a return on this function
# Every function does not need a return function
# But a function without a return does return None

cheer = int(input("How many times do you want to see the cheer? "))

functionBoomer(cheer)


# What about a function that returns a result?


def functionMath(x, y):
    rtnProd = x * y
    rtnSum = x + y
    return(rtnProd, rtnSum)

print(functionMath(2, 5))
