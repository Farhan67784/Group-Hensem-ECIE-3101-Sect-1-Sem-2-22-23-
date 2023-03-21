# This code is to calculate the greatest common divisor of two numbers inputed by the user

# method to compute gcd ( Loops )
# Greatest Common Divisor (GCD)
def computegcd(x, y):
    global ans
    if x > y:
        small = y
    else:
        small = x

    for i in range(1, small + 1):
        if (x % i == 0) and (y % i == 0):
            ans = i

    return ans


a = int(input('input a: '))
b = int(input('input b: '))
gcd = computegcd(a, b)
print("The gcd of", a, "and", b, "is : ", gcd)

#Least Common Multiple (LCM)

lcm = (a * b) / gcd
print("The LCM is:", lcm)



