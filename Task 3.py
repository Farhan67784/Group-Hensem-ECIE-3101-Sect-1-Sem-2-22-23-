# ECIE 3101 Section 1 Semester 2 Session 22/23
# Group Name: Group-Hensem-lab
# Group member:
# ABDULLAH FARHAN BIN ABD NASIR (2013219)
# MUHAMMAD NABIL ARRASYID (2011093)
# IMAN IRMANISYA BIN BAKRI (1715123)
# Ahmad Zal Hasmi Bin Ahmad Jafry (2012991)
# Muhammad Adzim Bin Rosly (2013413)
#
#

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self,):
        self.head = None

    def push(self, data):     #Push means add an element at the start or the front end of the list
        NewNode = Node(data)
        NewNode.next = self.head
        self.head = NewNode
        del NewNode

    def pop(self):       #Pop means remove the first element located at the start of the list
        TempNode = self.head
        if TempNode is None:   #check if List is empty or the list is underflow
            print("Cannot Do That Sorry.", "The List is Empty")
            return None
        else:
            self.head = TempNode.next    # set the next link as the head & delete the last header
        del TempNode

    def enqueue(self,data): #Enqueue means add to the end of the list
        #if there are no prior element in the list, it will becomes the first in the list
        current = self.head
        if current is None:
            self.push(data)
        else:             # otherwise, it will be added at the end of list
            NewNode = Node(data)
            while current.next:
                current = current.next
            current.next = NewNode

        del current

    def dequeue(self):  #Dequeue means remove at the start of the list
        #self.pop()
        TempNode = self.head
        if TempNode is None:
            print("Cannot Do That Sorry.", "The List is Empty")
            return None
        else:
            self.head = TempNode.next
        del TempNode

    def reverse(self):  # Reverse the arrangement of the list to display from last to first by inverting the pointers
        current = self.head
        prev = None
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next

        self.head = prev

    def display_list(self):   # display the content of the list
        current = self.head
        if current is None:
            print("The List is empty")
        else:
            while current:
                print(current.data, end=" ")
                current = current.next
                if current:
                    print("-->", end=" ")
        print()
        del current

    def count(self):      # count the number of elements inside the list, returns an integer
        current = self.head
        ans = 0
        if current is None:
            print("The list is Empty because The number of elements is ", ans)
            return None
        else:
            while current:
                ans +=1
                current = current.next
            return ans


# An External Function to convert the given parameter of a linked list
# & convert it into an array
    def convertToArray(self, listA):
        new_array = arr.array('u')
        length = listA.count()
        #print(length)

        current = self.head
        if current is None:
            print("List is empty")
            return None
        else:
            while current:
                new_array.append(current.data)
                current = current.next
            # deleting the linked list by deleting the head so it cannot
            # be located
            self.head = None
            return new_array    # return the elements as an array

    def reverseList(self, listA, listB):
        # Reverse the arrangement of the list to display from last to first by inverting the pointers
        current = self.head
        prev = None
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

        current = self.head
        Node_list = Node(current.data)
        while current.next:
            current = current.next
        current.next = Node_list




#The Main Body

import array as arr   # importing the python module for array

#Task 3a
listA = LinkedList()
listA.push('P')
listA.push('Y')
listA.enqueue('T')
listA.enqueue('H')
listA.push('O')
listA.enqueue('N')
listA.display_list()
print(listA.count())

listA.pop()
listA.dequeue()
listA.pop()
listA.display_list()
print(listA.count())

#Task 3b
listA = LinkedList()
listA.push('I')
listA.enqueue('L')
listA.enqueue('O')
listA.enqueue('V')
listA.enqueue('E')
listA.push('C')
listA.push('O')
listA.push('D')
listA.push('I')
listA.push('N')
listA.push('G')
listA.display_list()

arrayA = listA.convertToArray(listA)
print(arrayA)
listA.display_list()

#TASK 3c
listA = LinkedList()
listB = LinkedList()
listA.push('I')
listA.enqueue('A')
listA.enqueue('M')
listA.push('A')
listA.enqueue('M')
listA.enqueue('U')
listA.enqueue('S')
listA.enqueue('L')
listA.enqueue('I')
listA.enqueue('M')
listA.display_list()

listA.reverse()
listA.reverseList(listA,listB)
listA.display_list()
listB.display_list()