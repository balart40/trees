# Implementation Of Binary Tree
# Implementation of Binary Tree Node

import math
import random

tree =["A","B","C","E","F","G","H","L","","","","I","J","","","","","","","","D","M","","",""]
#
#							A
#					       / \
#						  B   C
#                        /\   /\
#                       E  F G  H
#                      /  /\      \
#                      L I  J      D
#        						   /
#								  M
#

class BinaryTree:
    """
    Simple Binary Tree Clas
    """
    def __init__(self, file):
        self._nodes = []
        self._postOrderPath = []
        self.createTree(self._nodes, file)
    def __str__(self):
        return "Class Binary Tree: \n"  \
              +"With nodes: "+str(self._nodes)+"\n"
    def createTree(self, nodes, file):
        queue = []
        queue.append(file.pop(0))
        while queue!=[]:
            currentNode = queue.pop(0)
            if currentNode == None:
                continue
            #print currentNode
            #print file
            left = file.pop(0)
            if left == "":
                left = None
            queue.append(left)
            right = file.pop(0)
            if right == "":
                right = None
            queue.append(right)
            node = BinaryTreeNode(currentNode,left,right)
            self._nodes.append(node)
    def travelPostOrder(self):
        currentNode = self._nodes.pop(0)
        self._postOrderPath.append(currentNode)
        queue = []
        queue.append(currentNode)
        while queue != []:
            currentNode = queue.pop(0)
            print "current Node\n"+str(currentNode)
            for nodes in currentNode.getChilds():
                queue.append(nodes)
                self._postOrderPath.append(nodes)
                
        return reverse(self._postOrderPath)
                
            
        #for child in self.nodes:
            
        
class BinaryTreeNode:
    """
    Simple Binary Tree Node Class.
    """
    def __init__(self, value, left, right):
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
        
AbinaryTree = BinaryTree(tree)
#for node in AbinaryTree._nodes:
#    print node
PostOrder =     AbinaryTree.travelPostOrder()
for node in PostOrder:
    print node._value
    
    
