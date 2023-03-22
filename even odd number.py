# ECIE 3101 Section 1 Semester 2 Session 22/23
# Group member:
# ABDULLAH FARHAN BIN ABD NASIR (2013219)
# MUHAMMAD NABIL ARRASYID (2011093)
# IMAN IRMANISYA BIN BAKRI (1715123)


# Practice for Chapter 0
# Program to display all the numbers from 0 to 50 and determine whether it is an odd or even number

num = 50
lst_even = []
lst_odd = []

for i in range(0, num+1):
    print(i)

for i in range(0, num+1):
    if i%2 == 0:
        lst_even.append(i)
    else:
        lst_odd.append(i)

print("The even numbers are:", lst_even)
print("The odd numbers are:", lst_odd)

