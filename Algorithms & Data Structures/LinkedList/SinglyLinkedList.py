"""
Singly Linked List (Node) example and forward traversal.

This module defines a simple `SinglyLinkedList` node class and shows how to
chain nodes to form a singly linked list and traverse it.

Pseudocode (Node & Traversal):
    class Node:
        data
        next = None

    # build nodes and link them
    head = Node(3)
    head.next = Node(7)
    head.next.next = Node(5)

    # traverse
    current = head
    while current is not None:
        print(current.data)
        current = current.next

Time Complexity:
    - Traversal: O(n)
Space Complexity:
    - O(n) for n nodes
"""

class SinglyLinkedList:
    def __init__(self,data):
        self.data = data 
        self.next = None
    
node1 = SinglyLinkedList(3)
node2 = SinglyLinkedList(7)
node3 = SinglyLinkedList(5)
node4 = SinglyLinkedList(9)

node1.next =  node2
node2.next = node3
node3.next = node4

currentnode = node1

while currentnode:
    print(currentnode.data, end=" ---> ")
    currentnode=currentnode.next
print("null")