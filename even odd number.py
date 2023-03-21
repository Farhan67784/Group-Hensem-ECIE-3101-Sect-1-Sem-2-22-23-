# Program to display all the numbers from 0 to 50 and determine whether it is an odd or even number

num = 50

for i in range(0, num+1):
    print(i)

for i in range(0, num+1):
    if i%2 == 0:
        print(i,' is even number')
    else:
        print(i,' is odd number')