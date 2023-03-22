#  ECIE 3101 Section 1 Semester 2 Session 22/23
#  Group member:
#  ABDULLAH FARHAN BIN ABD NASIR (2013219)
#  MUHAMMAD NABIL ARRASYID (2011093)
#  IMAN IRMANISYA BIN BAKRI (1715123)
#
#
#  Practice for Chapter 0
# This code is to calculate the greatest common divisor of two numbers inputed by the user

# method to compute gcd ( Loops )

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

# Greatest Common Divisor (GCD)

a = int(input('input number for a: '))
b = int(input('input number for b: '))
gcd = computegcd(a, b)
print("The GCD of", a, "and", b, "is : ", gcd)

#Least Common Multiple (LCM)

lcm = (a * b) / gcd
print("The LCM of", a, "and", b, "is : ", lcm)



