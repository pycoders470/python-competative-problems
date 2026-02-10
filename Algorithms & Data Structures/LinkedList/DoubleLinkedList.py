"""
Doubly Linked List (Node) example with forward and backward traversal.

This module defines a `DoubleLinkedList` node class and demonstrates linking
nodes to traverse in both directions.

Pseudocode (Node & Traversal):
    class DNode:
        data
        next = None
        prev = None

    # link nodes
    head = DNode(3)
    head.next = DNode(7)
    head.next.prev = head

    # forward traversal
    current = head
    while current is not None:
        print(current.data)
        current = current.next

    # backward traversal (start from tail)
    current = tail
    while current is not None:
        print(current.data)
        current = current.prev

Time Complexity:
    - Traversal/search: O(n)
Space Complexity:
    - O(n) for n nodes
"""

class DoubleLinkedList:
    def __init__(self, data):
        self.data = data
        self.next = None 
        self.prev = None

node1 = DoubleLinkedList(3)
node2 = DoubleLinkedList(7)
node3 = DoubleLinkedList(5)
node4 = DoubleLinkedList(9)

node1.next = node2
node2.next = node3
node2.prev = node1
node3.next = node4
node3.prev = node2
node4.prev = node3

print('Forward traversing--->')
currentnode = node1
while currentnode:
    print(currentnode.data, end=',')
    currentnode = currentnode.next
print('null')

print("backward traversing---->")
currentnode = node4
while currentnode:
    print(currentnode.data, end= ',')
    currentnode = currentnode.prev 
print('null')
