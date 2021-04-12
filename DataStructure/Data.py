#!/usr/bin/python3

"""
@description -> binaryTree: datastructure which contains values
                represents nodes connected by edges is a non linear
                datastructure

                Properties:
                    - One node is represented as Root Node
                    - Each other node associated with other one parent node
                    - Each node can have an arbitrary child node number

"""

class Node:

    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

def print_in_order(node):

    if node is None:
        return

    print_in_order(node.left)
    print(node.value)
    print_in_order(node.right)




root = Node(2) # that's the root
root.left = Node(5)
root.right = Node(6)

print_in_order(root)
