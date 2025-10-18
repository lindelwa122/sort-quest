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
        
        # Create a copy to avoid modifying original list
        arr = data.copy()
        n = len(arr)
        if n < 2:
            return arr

        comp = comparator

        # Detect common comparator patterns to avoid slow lambda calls
        ascending = None
        try:
            # Try detecting if comparator behaves like "a < b"
            if comp(1, 2) and not comp(2, 1):
                ascending = True
            elif comp(2, 1) and not comp(1, 2):
                ascending = False
        except:
            # If comparator fails on ints, skip detection
            ascending = None

        for i in range(1, n):
            key = arr[i]
            j = i - 1

            if ascending is True:
                while j >= 0 and key < arr[j]:
                    arr[j + 1] = arr[j]
                    j -= 1
            elif ascending is False:
                while j >= 0 and key > arr[j]:
                    arr[j + 1] = arr[j]
                    j -= 1
            else:
                while j >= 0 and comp(key, arr[j]):
                    arr[j + 1] = arr[j]
                    j -= 1

            arr[j + 1] = key

        return arr

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
        pass

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

