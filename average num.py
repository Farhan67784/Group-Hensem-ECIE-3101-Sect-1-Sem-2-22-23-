#  ECIE 3101 Section 1 Semester 2 Session 22/23
#  Group member:
#  ABDULLAH FARHAN BIN ABD NASIR (2013219)
#  MUHAMMAD NABIL ARRASYID (2011093)
#  IMAN IRMANISYA BIN BAKRI (1715123)
#  Ahmad Zal Hasmi Bin Ahmad Jafry (2012991)
#
#  Practice for Chapter 0
#  This Program is to prompt the user for several numbers and calculate the sum and average of th inputed number

def average(x):
    avg = sum(x)/len(x)
    return avg

# creating an empty list
lst = []

# number of elements as input
print("The program is designed to calculate the sum and average from a list of inputs")

n = int(input("Please enter the desired number of elements : "))

print("Enter the elements inside the list one by one:-")
# iterating till the range
for i in range(0, n):
    element = int(input())
    lst.append(element)  # adding the element

print("The values inside the list are:")
print(lst)

ans = average(lst)
print("The Sum of the list: ", sum(lst))
print("The Average of list: ", ans)

