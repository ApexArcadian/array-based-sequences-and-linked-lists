"""
Singly Linked List - Abstract Data Type Implementation

A singly linked list is a dynamic data structure composed of nodes where each node 
stores data and a reference to the next node. The list maintains pointers to the 
head and tail of the list, and tracks the number of elements.
"""


class Node:
    """Represents a single node in the linked list."""
    
    def __init__(self, data):
        """
        Initialize a node with data.
        
        Args:
            data: The data to store in the node
        """
        self.data = data
        self.next = None


class SinglyLinkedList:
    """
    A singly linked list implementation that supports dynamic insertion,
    deletion, and traversal operations.
    """
    
    class EmptyListException(Exception):
        """Raised when operations are performed on an empty list."""
        pass
    
    class NodeNotFoundException(Exception):
        """Raised when a specified node is not found."""
        pass
    
    def __init__(self):
        """Initialize an empty singly linked list."""
        self.__head = None
        self.__tail = None
        self.__count = 0
    
    def build_forward_list(self, iterable):
        """
        Build the list by adding elements in forward order (append to tail).
        
        Args:
            iterable: An iterable of elements to add to the list
        """
        for item in iterable:
            self.__append(item)
    
    def build_backward_list(self, iterable):
        """
        Build the list by adding elements in reverse order (insert at head).
        
        Args:
            iterable: An iterable of elements to add to the list
        """
        for item in iterable:
            self.__prepend(item)
    
    def __append(self, value):
        """
        Append a value to the end of the list.
        
        Args:
            value: The value to append
        """
        new_node = Node(value)
        if self.__head is None:
            self.__head = self.__tail = new_node
        else:
            self.__tail.next = new_node
            self.__tail = new_node
        self.__count += 1
    
    def __prepend(self, value):
        """
        Prepend a value to the beginning of the list.
        
        Args:
            value: The value to prepend
        """
        new_node = Node(value)
        new_node.next = self.__head
        self.__head = new_node
        if self.__tail is None:
            self.__tail = new_node
        self.__count += 1
    
    def insert_after(self, after_value, new_value):
        """
        Insert new_value after the first node containing after_value.
        
        Args:
            after_value: The value to search for
            new_value: The value to insert
            
        Raises:
            EmptyListException: If the list is empty
            NodeNotFoundException: If after_value is not found in the list
        """
        if self.__head is None:
            raise SinglyLinkedList.EmptyListException()
        
        current = self.__head
        while current and current.data != after_value:
            current = current.next
        
        if current is None:
            raise SinglyLinkedList.NodeNotFoundException()
        
        new_node = Node(new_value)
        new_node.next = current.next
        current.next = new_node
        if current == self.__tail:  # if inserted at end of list
            self.__tail = new_node  # re-route the tail pointer
        self.__count += 1
    
    def remove(self, value):
        """
        Remove the first node containing value.
        
        Args:
            value: The value to remove
            
        Raises:
            EmptyListException: If the list is empty
            NodeNotFoundException: If value is not found in the list
        """
        if self.__head is None:
            raise SinglyLinkedList.EmptyListException()
        
        current = self.__head
        previous = None
        while current and current.data != value:
            previous = current
            current = current.next
        
        if current is None:
            raise SinglyLinkedList.NodeNotFoundException()
        
        if previous is None:
            self.__head = current.next  # remove first node
        else:
            previous.next = current.next  # remove an interior node
        
        if current == self.__tail:
            self.__tail = previous  # remove the last node
        
        self.__count -= 1
    
    def display(self):
        """Print the contents of the list in forward order."""
        current = self.__head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements))
    
    def display_reverse(self):
        """Print the contents of the list in reverse order using recursion."""
        def _reverse_recursive(node):
            return _reverse_recursive(node.next) + [node.data] if node else []
        
        print(" <- ".join(map(str, _reverse_recursive(self.__head))))
    
    def __iter__(self):
        """
        Enable iteration over node data.
        
        Yields:
            The data stored in each node
        """
        current = self.__head
        while current:
            yield current.data
            current = current.next
    
    def __len__(self):
        """
        Return the number of nodes in the list.
        
        Returns:
            The count of nodes in the list
        """
        return self.__count
