"""
Circular Linked List (Node) example and circular traversal.

This module defines a `CircularLinkedList` node class and demonstrates linking
nodes so that the last node points back to the head, enabling circular traversal.

Pseudocode (Node & Circular Traversal):
    class CNode:
        data
        next = None

    # build circular list
    head = CNode(3)
    head.next = CNode(7)
    head.next.next = CNode(5)
    tail.next = head  # close the circle

    # traverse once around the circle
    current = head
    start = head
    print(current.data)
    current = current.next
    while current != start:
        print(current.data)
        current = current.next

Time Complexity:
    - Traversal (one loop): O(n)
Space Complexity:
    - O(n) for n nodes
"""

class CircularLinkedList:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None



node1 = CircularLinkedList(3)
node2 = CircularLinkedList(7)
node3 = CircularLinkedList(5)
node4 = CircularLinkedList(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node1

currentnode = node1
startnode = node1
print(currentnode.data, end=',')
currentnode = currentnode.next
while currentnode != startnode:
    print(currentnode.data, end=',')
    currentnode = currentnode.next 
