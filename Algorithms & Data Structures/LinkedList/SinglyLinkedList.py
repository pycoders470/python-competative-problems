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

def Traverse(startnode):
    """
    Traverse and print the linked list from `startnode`.

    Pseudocode:
        current = startnode
        while current is not None:
            print(current.data)
            current = current.next

    Prints nodes in a single line separated by arrows and ends with 'null'.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    currentnode = startnode
    while currentnode:
        print(currentnode.data, end=' -> ')
        currentnode = currentnode.next
    print('null')

def LowestElement(startnode):
    """
    Return the smallest value stored in the linked list starting at `startnode`.

    Pseudocode:
        min_val = startnode.data
        current = startnode
        while current is not None:
            if current.data < min_val:
                min_val = current.data
            current = current.next
        return min_val

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    currentnode = startnode
    lowestvalue = startnode.data
    while currentnode:
        if currentnode.data < lowestvalue:
            lowestvalue = currentnode.data
        currentnode = currentnode.next
    return lowestvalue

def DeleteNode(startnode, nodetodelete):
    """
    Delete `nodetodelete` from the list starting at `startnode` and return
    the possibly-updated head.

    Pseudocode (delete by node reference):
        if startnode == nodetodelete:
            return startnode.next
        current = startnode
        while current.next is not None and current.next != nodetodelete:
            current = current.next
        if current.next is None:
            # nodetodelete not found
            return startnode
        current.next = current.next.next
        return startnode

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if startnode == nodetodelete:
        return startnode.next
    currentnode = startnode
    # find the node whose next is the node to delete
    while currentnode.next and currentnode.next != nodetodelete:
        currentnode = currentnode.next
    # not found
    if currentnode.next is None:
        return startnode
    # bypass the node to delete
    currentnode.next = currentnode.next.next
    return startnode

def InsertNode(startnode, newnode, position):
    """
    Insert `newnode` into the list at 1-based `position` and return the head.

    Pseudocode:
        if position == 1:
            newnode.next = head
            return newnode
        current = head
        for i in range(position-2):
            current = current.next
        newnode.next = current.next
        current.next = newnode
        return head

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if position == 1:
        newnode.next = startnode
        return newnode
    currentnode = startnode
    for i in range(position - 2):
        if currentnode is None:
            break
        currentnode = currentnode.next
    if currentnode is None:
        # position out of bounds; append to end
        return startnode
    newnode.next = currentnode.next
    currentnode.next = newnode
    return startnode

if __name__ == '__main__':
    node1 = SinglyLinkedList(3)
    node2 = SinglyLinkedList(7)
    node3 = SinglyLinkedList(1)
    node4 = SinglyLinkedList(9)

    node1.next = node2
    node2.next = node3
    node3.next = node4

    print("Original list:")
    Traverse(node1)
    print("Lowest element in linked list:", LowestElement(node1))

    print('\nAfter deleting node with value 7:')
    node1 = DeleteNode(node1, node2)
    Traverse(node1)

    print('\nAfter inserting 40 at position 2:')
    newnode = SinglyLinkedList(40)
    node1 = InsertNode(node1, newnode, 2)
    Traverse(node1)
