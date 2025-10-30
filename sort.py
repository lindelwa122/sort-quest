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
         if len(data) <= 1:
            return data.copy()
        
        # Spliting array 
        mid = len(data) // 2
        left = Sorter.merge(data[:mid], comparator)
        right = Sorter.merge(data[mid:], comparator)
        
        # Merge 
        return Sorter._merge_halves(left, right, comparator)
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
         arr = data.copy()
        
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            
            while j >= 0 and not comparator(arr[j], key):
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        
        return arr
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
          arr = data.copy()
        n = len(arr)
        
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
               
                if not comparator(arr[j], arr[j + 1]):
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
            if not swapped:
                break
        
        return arr
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
          method = method.lower()
    
    if method == "merge":
        return Sorter.merge(data, comparator)
    if method == "insertion":
        return Sorter.insertion(data, comparator)
    if method == "bubble":
        return Sorter.bubble(data, comparator)
    
    raise ValueError(f"Unknown sort method: {method}. Use 'merge', 'insertion', or 'bubble'.")
        pass

