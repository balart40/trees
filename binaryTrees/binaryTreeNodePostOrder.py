# Implementation Of Binary Tree
# Implementation of Binary Tree Node
# By Francisco Eduardo Balart Sanchez
# http://www.codeskulptor.org/#user42_rTHaZaNUvesxdqa_20.py
import math
import random

tree =["A","B","C","E","F","G","H","L","","I","J","","","","D","","","","","","","M","","",""]

#tree =["A","B","C","E","F","G","H","L","","I","J","","","","D","","","","","","","","","","","","","","","M",""]
#       |   |_v_|   |_____V_____|   |____________V__________|  |_______________________v______________________|
#    2^0=1   2^1=4     2^2=4                   2^3 = 8                                2^4 = 16
#
#							  A             -----1
#					       /     \          
#						  B       C         -----2
#                        /  \     / \
#                       E    F   G    H     -----4
#                      / \   /\  /\   / \
#                      L  @ I J  @@   @  D   -----8
#        			  /\    /\/\         /\
#					 @ @    @@@@         M @ -----16
#										 /\
#										 @@

class BinaryTree:
    """
    Simple Binary Tree Clas
    """
    def __init__(self, file):
        self._nodes = []
        self._postOrderPath = []
        self.createTree(file)
    def __str__(self):
        return "Class Binary Tree: \n"  \
              +"With nodes: "+str(self._nodes)+"\n"
    def createTree(self, file):
        queue = []
        queue.append(BinaryTreeNode(file.pop(0)))
        while queue!=[]:            
            currentNode = queue.pop(0)
            left = file.pop(0)
            if (left == ""):
                left = BinaryTreeNode(None)
            else:
                left = BinaryTreeNode(left)
                queue.append(left)
            right = file.pop(0)
            if (right == ""):
                right = BinaryTreeNode(None)
            else:
                right = BinaryTreeNode(right)
                queue.append(right)
            if (len(self._nodes) !=0):
                found = False
                for node in self._nodes:
                    if currentNode._value == node._value:
                        node._leftChild = left
                        node._rightChild = right
                        found = True
                if (found == False):
                    currentNode._leftChild = left
                    currentNode._rightChild = right
                    self._nodes.append(currentNode)
                    if left._value != None:
                        self._nodes.append(left)
                    if right._value != None:
                        self._nodes.append(right)
            elif (len(self._nodes) ==0):
                currentNode._leftChild = left
                currentNode._rightChild = right
                self._nodes.append(currentNode)
                if left._value != None:
                    self._nodes.append(left)
                if right._value != None:
                    self._nodes.append(right)
    def travelPostOrder(self, node ):
        currentNode = node
        if currentNode._value != None:
            self.travelPostOrder(currentNode._leftChild)
            self.travelPostOrder(currentNode._rightChild)
            self._postOrderPath.insert(0,currentNode._value)
        return self._postOrderPath
        
class BinaryTreeNode:
    """
    Simple Binary Tree Node Class.
    """
    def __init__(self, value, left=None, right=None):
        self._value = value
        self._leftChild = left
        self._rightChild = right
        self._visited = False
    def __str__(self):
        """
        Return human readable state
        """
        return "Class BinaryTreeNode: "+"\n" \
              +"Value: "+str(self._value)+"\n" \
              +"Left Child:	"+str(self._leftChild)+"\n" \
              +"Right Child: "+str(self._rightChild)+"\n" \
              +"Visited state:  "+str(self._visited)+"\n"
    # functions of the BinaryTreeNode                           
    def getChilds(self):        
        return (self._leftChild,self._rightChild)
    def insertRightChild(self, btn):
        self._rightChild = btn
    def insertLeftChild(self, btn):
        self._leftChilf = btn
    def visited(self):
        self._visited = True
    def unvisited(self):
        self._visited = False
        
print "The tree length "+str(len(tree))+"\n"        
AbinaryTree = BinaryTree(tree)
print "The tree Nodes \n"
print [node._value for node in AbinaryTree._nodes]
for node in AbinaryTree._nodes:
    print "\nnode value: "+str(node._value)
    print "left: "+str(node._leftChild._value)
    print "right: "+str(node._rightChild._value)
PostOrder = AbinaryTree.travelPostOrder(AbinaryTree._nodes[0])
print "\nPost Order traversal\n"
print [node for node in PostOrder]
