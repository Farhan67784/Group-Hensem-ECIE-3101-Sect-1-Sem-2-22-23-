# ECIE 3101 Section 1 Semester 2 Session 22/23
# Group Name: Group-Hensem-lab
# Group member:
# ABDULLAH FARHAN BIN ABD NASIR (2013219)
# MUHAMMAD NABIL ARRASYID (2011093)
# IMAN IRMANISYA BIN BAKRI (1715123)
# Ahmad Zal Hasmi Bin Ahmad Jafry (2012991)
# Muhammad Adzim Bin Rosly (2013413)
#
# Binary Tree
# Task 5a
class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

def printPreorder(node):
    if node:
        print("-->",node.value, end=" ")
        printPreorder(node.left)
        printPreorder(node.right)

def printInorder(node):
    if node:
        printInorder(node.left)
        print("-->",node.value, end=" ")
        printInorder(node.right)

def printPostorder(node):
    if node:
        printPostorder(node.left)
        printPostorder(node.right)
        print("-->",node.value, end=" ")



root = Node(2)
root.left = Node(3)
root.right = Node(7)
root.left.left = Node(1)
root.right.left = Node(6)
root.left.right = Node(4)
root.left.right.left = Node(5)
root.right.right = Node(8)

printPreorder(root)
print()
printInorder(root)
print()
printPostorder(root)
