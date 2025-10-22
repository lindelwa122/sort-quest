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
        arr = data.copy()  # Do not modify original list
        n = len(arr)
        
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                # If elements are out of order per comparator, swap
                if not comparator(arr[j], arr[j + 1]):
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
            # Optimization: stop if already sorted
            if not swapped:
                break
        return arr

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

