# ECIE 3101 Section 1 Semester 2 Session 22/23
# Group Name: Group-Hensem-lab
# Group member:
# ABDULLAH FARHAN BIN ABD NASIR (2013219)
# MUHAMMAD NABIL ARRASYID (2011093)
# IMAN IRMANISYA BIN BAKRI (1715123)
# Ahmad Zal Hasmi Bin Ahmad Jafry (2012991)
# Muhammad Adzim Bin Rosly (2013413)
#
# Binary Tree Sort and Height
# Task 5b & 5c

class Node:
    def __init__(self, value):
        self.value = value
        self.index_key = None
        self.left = None
        self.right = None

    def deepestBranch(self):
        if self.value is None:
            print('The Deepest Branch is 0')
            return None

        depth = 1
        leftHeight = self.deepestBranch(self.left)
        rightHeight = self.deepestBranch(self.right)
        deepest_path = max(leftHeight, rightHeight) + depth

        print('The Deepest Branch is', deepest_path)
        return None

def keyying_index(node,value):
    ans = [ord(c) for c in value]
    print(ans[0])
    node.index_key = ans[0]
    return ans[0]

def insertSort(node,value):
    index = keyying_index(node,value)
    print(node.index_key)
    # if binary search tree is empty, create a new node and declare it as root
    if node is None or index is None:
        node.index_key = index
        return Node(value)

    else:
        if node.index_key is index:
            return node
        elif index > node.index_key:
            # if new Value is greater than value of data in root, add it to right subtree and proceed recursively
            node.right = insertSort(node.right, value)
        else:
            # if newValue is less than value of data in root, add it to left subtree and proceed recursively
            node.lift = insertSort(node.left, value)
        return node

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



root = Node('Haziman Sairin')

insertSort(root,'Zikri Hakim')
insertSort(root,'Jameel Majdi')
insertSort(root,'Raniya Waleed')
insertSort(root,'Syukri Talib')
insertSort(root,'Saif al-Din')
insertSort(root,'Nuqman Aliff')
insertSort(root,'Amir Suad')
insertSort(root,'Abd al-Karim Mumtaz')
insertSort(root,'Dania Izzah')
insertSort(root,'Zharif Aiman')
insertSort(root,'Sharifa Harun')
insertSort(root,'Fuad Najma')

printPreorder(root)
print()
printInorder(root)
print()
printPostorder(root)
print()
root.deepestBranch()