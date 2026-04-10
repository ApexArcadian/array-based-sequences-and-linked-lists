"""
Main program demonstrating the SplitEvensOdds class.

This program creates a SinglyLinkedList with mixed integers and splits 
the list into two separate lists: one containing even numbers and one 
containing odd numbers, by manipulating node pointers.
"""

from singly_linked_list import SinglyLinkedList, Node


class SplitEvensOdds(SinglyLinkedList):
    """
    A derived class from SinglyLinkedList that provides a method to split
    a list into two lists: one containing even numbers and one containing
    odd numbers, using pointer manipulation.
    """
    
    def split(self):
        """
        Split the current list into two separate lists based on even/odd values.
        
        The original list is emptied by redirecting all nodes to either the
        evens or odds list. This is done by manipulating node pointers rather
        than creating new nodes.
        
        Returns:
            tuple: A tuple of (evens_list, odds_list) where:
                - evens_list: SplitEvensOdds containing all even numbers
                - odds_list: SplitEvensOdds containing all odd numbers
        """
        evens_list = SplitEvensOdds()
        odds_list = SplitEvensOdds()
        
        # Access private attributes of the current list
        current = self._SinglyLinkedList__head
        
        # Initialize tracking variables for both lists
        evens_head = None
        evens_tail = None
        odds_head = None
        odds_tail = None
        evens_count = 0
        odds_count = 0
        
        # Traverse the original list and reroute pointers
        while current:
            if current.data % 2 == 0:  # Even number
                if evens_head is None:
                    evens_head = current
                else:
                    evens_tail.next = current
                evens_tail = current
                evens_count += 1
            else:  # Odd number
                if odds_head is None:
                    odds_head = current
                else:
                    odds_tail.next = current
                odds_tail = current
                odds_count += 1
            
            current = current.next
        
        # Clean up tail pointers for the new lists
        if evens_tail:
            evens_tail.next = None
        if odds_tail:
            odds_tail.next = None
        
        # Assign the constructed lists to the new SinglyLinkedList objects
        evens_list._SinglyLinkedList__head = evens_head
        evens_list._SinglyLinkedList__tail = evens_tail
        evens_list._SinglyLinkedList__count = evens_count
        
        odds_list._SinglyLinkedList__head = odds_head
        odds_list._SinglyLinkedList__tail = odds_tail
        odds_list._SinglyLinkedList__count = odds_count
        
        # Empty the current list
        self._SinglyLinkedList__head = None
        self._SinglyLinkedList__tail = None
        self._SinglyLinkedList__count = 0
        
        return evens_list, odds_list
    
    def display(self):
        """Display the list with 'Head -> ' prefix for clarity."""
        current = self._SinglyLinkedList__head
        print("Head -> ", end="")
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        if elements:
            print(" -> ".join(elements) + " -> None")
        else:
            print(" -> None")


def main():
    """Demonstrate the SplitEvensOdds functionality."""
    
    # Create a SplitEvensOdds list and populate it with sample data
    split_list = SplitEvensOdds()
    split_list.build_forward_list([1, 24, 3, 4, 5, 6, 67, 8, 15, 14, 13, 12, 11, 100, 9, 9000])
    
    # Display the original list
    print("Original list:")
    split_list.display()
    
    # Split the list into evens and odds
    evens_list, odds_list = split_list.split()
    
    # Display the evens list
    print("\nEvens list:")
    evens_list.display()
    
    # Display the odds list
    print("\nOdds list:")
    odds_list.display()
    
    # Display the original list (should be empty)
    print("\nOriginal list after split:")
    split_list.display()


if __name__ == "__main__":
    main()
