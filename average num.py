# This is a sample Python script.
def average(x):
    avg = sum(x)/len(x)
    return abs(avg)

# creating an empty list
lst = []

# number of elements as input
n = int(input("Please enter number of elements : "))

print("Enter the elements inside the list one by one:-")
# iterating till the range
for i in range(0, n):
    element = int(input())
    lst.append(element)  # adding the element

print("The value inside the list are:")
print(lst)

ans = average(lst)
print("Average of list: ", ans)

