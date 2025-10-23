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
        
        
        if len(data) <= 1:
            return data
        
        mid = len(data) // 2
        left = Sorter.merge(data[:mid], comparator)
        right = Sorter.merge(data[mid:], comparator)
        merged = []
        i = 0
        j = 0
        while i < len(left) and j < len(right):
            if comparator(left[i], right[j]):
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged

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

