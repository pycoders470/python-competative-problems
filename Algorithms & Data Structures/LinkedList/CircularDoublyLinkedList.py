"""
Circular Doubly Linked List (Node) example with forward and backward traversal.

This module defines a `CircularDoubleLinkedList` node class and demonstrates
linking nodes so that:
- Each node has both `next` and `prev` pointers
- The last node's `next` points back to the head (circular forward)
- The head's `prev` points to the last node (circular backward)

This enables traversal in both directions around the circle.

Pseudocode (Node & Circular Traversal):
    class CNode:
        data
        next = None
        prev = None

    # build circular doubly linked list
    head = CNode(7)
    head.next = CNode(8)
    head.next.prev = head
    ... link remaining nodes ...
    tail.next = head
    head.prev = tail

    # forward traversal (start from head)
    current = head
    start = head
    print(current.data)
    current = current.next
    while current != start:
        print(current.data)
        current = current.next

    # backward traversal (start from tail)
    current = tail
    start = tail
    print(current.data)
    current = current.prev
    while current != start:
        print(current.data)
        current = current.prev

Key Features:
- Combines benefits of doubly linked list (bi-directional) and circular list
- No null pointers; every node is connected
- Supports efficient insertion/deletion from both ends
- Requires careful linking to maintain circular structure

Time Complexity:
    - Traversal (one loop forward or backward): O(n)
Space Complexity:
    - O(n) for n nodes
"""

class CircularDoubleLinkedList:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None



node1 = CircularDoubleLinkedList(7)
node2 = CircularDoubleLinkedList(8)
node3 = CircularDoubleLinkedList(3)
node4 = CircularDoubleLinkedList(5)

node1.prev = node4
node1.next = node2
node2.next = node3
node2.prev = node1
node3.next = node4
node3.prev = node2
node4.next = node1
node4.prev = node3

print("Traversing forward ----> ")
startnode = node1
currentnode = node1
print(currentnode.data, end=',')
currentnode = currentnode.next

while currentnode!=startnode:
    print(currentnode.data, end=',')
    currentnode=currentnode.next
print('x.......................x......................x')
print("Traversing backward ------->")
startnode = node4
currentnode = node4
print(currentnode.data,end=',')
currentnode = currentnode.prev 

while currentnode!=startnode:
    print(currentnode.data, end=',')
    currentnode=currentnode.prev


