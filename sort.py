from typing import List, Callable, Any

class Sorter:
    """
    A sorting utility class providing multiple sorting algorithms.
    
    Each method is static and takes:
        - data: a list of elements to sort
        - comparator: a function that compares two elements
          and returns True if the first should come before the second.
    """

    @staticmethod
    def merge(data: List[Any], comparator: Callable[[Any, Any], bool]) -> List[Any]:
        """
        Sorts the list using the merge sort algorithm.
        
        Args:
            data (List[Any]): The list to sort.
            comparator (Callable[[Any, Any], bool]): Comparison function.
            
        Returns:
            List[Any]: A new sorted list.
        """
        pass

    @staticmethod
    def insertion(data: List[Any], comparator: Callable[[Any, Any], bool]) -> List[Any]:
        """
        Sorts the list using the insertion sort algorithm.
        
        Args:
            data (List[Any]): The list to sort.
            comparator (Callable[[Any, Any], bool]): Comparison function.
            
        Returns:
            List[Any]: A new sorted list.
        """
        pass

    @staticmethod
    def bubble(data: List[Any], comparator: Callable[[Any, Any], bool]) -> List[Any]:
        """
        Sorts the list using the bubble sort algorithm.
        
        Args:
            data (List[Any]): The list to sort.
            comparator (Callable[[Any, Any], bool]): Comparison function.
            
        Returns:
            List[Any]: A new sorted list.
        """
        # Handle empty or single-element lists
        if len(data) <= 1:
            return data[:]
        
        # Create a copy to avoid modifying the original list
        result = data[:]
        n = len(result)
        
        # Flag to optimize for already sorted lists
        swapped = True
        
        # Keep track of last swap position to optimize range
        last_swap = n - 1
        
        while swapped:
            swapped = False
            next_last_swap = 0
            
            # Only iterate up to the last swap position from previous pass
            for i in range(last_swap):
                # If the elements are in wrong order, swap them
                if not comparator(result[i], result[i + 1]):
                    result[i], result[i + 1] = result[i + 1], result[i]
                    swapped = True
                    next_last_swap = i
            
            # Update last swap position for next pass
            last_swap = next_last_swap
            
            # If no swaps occurred, list is sorted
            if not swapped:
                break
        
        return result

    @staticmethod
    def sort(data: List[Any], comparator: Callable[[Any, Any], bool], method: str = "merge") -> List[Any]:
        """
        Sorts the list using the specified algorithm.
        
        Args:
            data (List[Any]): The list to sort.
            comparator (Callable[[Any, Any], bool]): Comparison function.
            method (str): Sorting algorithm ('merge', 'insertion', or 'bubble').
            
        Returns:
            List[Any]: A new sorted list.
            
        Raises:
            ValueError: If an unknown sort method is provided.
        """
        pass

