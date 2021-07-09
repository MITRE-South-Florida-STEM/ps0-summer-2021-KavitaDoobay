import math
# 1. Ask the user to enter a number "x"
x=int(input("Enter number x: "))


# 2. Ask the user to enter a number "y"
y=int(input("Enter number y: "))

# 3. Prints out the number "x" raised to the power "y"
p = x**y
print("x**y = " + str(p))

# 4. Prints out the log (base 2) of "x"
print("log(x) = " + str(math.log2(x)))
