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
        # Copy of the data
        arr = data[:]
        
        # Helper function to merge two sorted sublists
        def merge_helper(left: List[Any], right: List[Any]) -> List[Any]:
            result = []
            i = j = 0
            
            # Merge elements from both lists while comparing with the comparator
            while i < len(left) and j < len(right):
                if comparator(left[i], right[j]):
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            
            # Append remaining elements from left sublist (if any)
            while i < len(left):
                result.append(left[i])
                i += 1
            
            # Append remaining elements from right sublist (if any)
            while j < len(right):
                result.append(right[j])
                j += 1
            
            return result
        
        # Recursive merge sort function
        def merge_sort_recursive(arr: List[Any]) -> List[Any]:
            # Base case: lists with 0 or 1 element are already sorted
            if len(arr) <= 1:
                return arr
            
            # Divide the list into two halves
            mid = len(arr) // 2
            left = arr[:mid]
            right = arr[mid:]
            
            # Recursively sort both halves
            left_sorted = merge_sort_recursive(left)
            right_sorted = merge_sort_recursive(right)
            
            # Merge the sorted halves
            return merge_helper(left_sorted, right_sorted)
        
        # Perform merge sort and return the result
        return merge_sort_recursive(arr)

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

