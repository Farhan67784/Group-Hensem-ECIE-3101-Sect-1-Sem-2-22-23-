#  ECIE 3101 Section 1 Semester 2 Session 22/23
#  Group member:
#  ABDULLAH FARHAN BIN ABD NASIR (2013219)
#  MUHAMMAD NABIL ARRASYID (2011093)
#  IMAN IRMANISYA BIN BAKRI (1715123)
#  Ahmad Zal Hasmi Bin Ahmad Jafry (2012991)
#  Muhammad Adzim Bin Rosly (2013413)
#
# Practice for Task 2
# 2a. Create 2 functions countOdd() and countEven() that counts the even and odd numbers in the list. (3m)
# 2b. Create a function that swaps 2 elements in the list using their index number. (3m)

#NODE CLASS
class Node:
    #CONSTUCTOR
    def __init__(self, data=None, link=None):
        self.data = data
        self.link = link

    def setLink(self, link):
        self.link = link

    def getData(self):
        return self.data

    def getNext(self):
        return self.link

    def updateData(self, data):
        self.data = data


#LINKED LIST CLASS
class LL:
    #LL CONSTRUCTOR
    def __init__(self):
        self.head = None

    #ADD A NODE TO THE START OF THE LIST
    def addToStart(self,data):
        tempNode = Node(data)
        tempNode.setLink(self.head)
        self.head = tempNode
        del tempNode

     # ADD A NODE TO THE END OF THE LIST
    def addToEnd(self, data):
        current = self.head
        if current is None:
            self.addToStart(data)
        else:
            tempNode = Node(data)
            while current.getNext():
                current = current.getNext()
            current.setLink(tempNode)
            del tempNode
        del current


        # DISPLAY THE LINKED LIST
    def displayList(self):
        current = self.head
        if current is None:
            print("List is empty")
        else:
            while current:
                print(current.getData(), end=" ")
                current = current.getNext()
                if current:
                    print("-->", end=" ")
        print()
        del current

    # GET THE LENGTH
    def length(self):
        current = self.head
        if current is None:
            return 0
        else:
            count = 0
            while current:
                count += 1
                current = current.getNext()
            return count

    # COUNT THE ODD NUMBERS IN THE LINKED LIST
    def count_odd(self):
        current = self.head
        count = 0
        while current:
            if current.getData() %2 !=0:
                count += 1
            current = current.getNext()
        return count

    # COUNT THE EVEN NUMBERS IN THE LINKED LIST
    def count_even(self):
        current = self.head
        count = 0
        while current:
            if current.getData() %2 ==0:
                count += 1
            current = current.getNext()

        return count

    def display_even(self):
        current = self.head
        while current:
            if current.getData() % 2 == 0:
                print(current.getData(), end=" ")
            current = current.getNext()
        print()
        self.displayList()
        del current

    def display_odd(self):
        current = self.head
        while current:
            if current.getData() % 2 != 0:
                print(current.getData(), end=" ")
            current = current.getNext()
        print()
        del current


    def swap(self, num1, num2):
        current = self.head
        #IDENTIFY IF THE INDEX IN WITHIN THE LIST'S SIZE
        if current is None:
            print("List is empty")
        elif num1 > self.length() or num2 > self.length():
            print("Error! Index is beyond the size of list!")
            return None
        else:
            #FINDING THE CORESPONDING NODES

            c, d = 0, 0
            # Searching for the first node
            while c != num1:
                current = current.getNext()
                c+=1
            temp1 = current.getData()
            print("At Index:", c, ", The Data is:", current.getData())

            # Searching for the second node
            current = self.head
            while d != num2:
                current = current.getNext()
                d+=1
            temp2 = current.getData()
            print("At Index:", d, ", The Data is:", current.getData())

            # SWAPPING THE DATA VALUES INSIDE THE NODE
            current = self.head
            c, d = 0, 0
            # swapping the data by searching and updating the node
            while c != num1:
                current = current.getNext()
                c += 1
            current.updateData(temp2)

            current = self.head
            while d != num2:
                current = current.getNext()
                d += 1
            current.updateData(temp1)


list = LL()
list.addToStart(10)
list.addToStart(20)
list.addToStart(45)
list.addToStart(35)
list.addToStart(15)

list.displayList()

print("There are",list.count_odd(), "Odd Numbers in the List")
print("The odd numbers are:")
list.display_odd()
print("There are",list.count_even(), "Even Numbers in the List")
print("The even numbers are:")
list.display_even()

list.addToStart(30)
list.addToStart(40)
list.displayList()

print("There are",list.count_odd(), "Odd Numbers in the List")
print("The odd numbers are:")
list.display_odd()
print("There are",list.count_even(), "Even Numbers in the List")
print("The even numbers are:")
list.display_even()

list.swap(1,5)
list.displayList()

list.swap(2,3)
list.displayList()

list.swap(7,4)
list.displayList()