#  ECIE 3101 Section 1 Semester 2 Session 22/23
#  Group Name: Group HENSEM
#  Group member:
#  ABDULLAH FARHAN BIN ABD NASIR (2013219)
#  MUHAMMAD NABIL ARRASYID (2011093)
#  IMAN IRMANISYA BIN BAKRI (1715123)
#  Ahmad Zal Hasmi Bin Ahmad Jafry (2012991)
#  Muhammad Adzim Bin Rosly (2013413)
#
#  TASK 1d.
#  This Program is to calculate the length of hypotenuse of a right-angled triangle.
#  The other 2 length are taken as inputs from the user.
#
import math


def get_length(step):
    print("Input length", step, ": ")
    ans = float(input())

    return ans

def get_hypotenuse(a,b):
    ans = (a*a) + (b*b)
    return math.sqrt(ans)

print("This program is to calculate the length of hypotenuse of a right-angled triangle.")
print("Please input the lengths of 2 sides of the triangle")

a = get_length(1)
b = get_length(2)

print("For length a: ",a)
print("For length b: ",b)

c ='{0:.4g}'.format(get_hypotenuse(a,b))
print("Given the lengths, The Hypotenuse is ", c)

