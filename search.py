from typing import List, Callable, Any, Optional
import math

class NotFoundError(Exception):
    def __init__(self, message="Element not found"):
        self.message = message
        
    def __repr__(self):
        return f"NotFoundError('{self.message}')"

    def __eq__(self, other):
        """Allows test comparisons with other NotFoundError objects."""
        if isinstance(other, NotFoundError):
            return self.message == other.message
        return False

    def __bool__(self):
        """Allows checking if the result is NOT NotFoundError."""
        return False


class Search:
    """
    A collection of static search algorithms.

    Each method takes:
        - data: list of elements to search in
        - target: element to find
        - comparator: function(a, b) -> bool indicating equality or ordering

    All methods return the index of the found element, or -1 if not found.
    """

    # =====================
    # LINEAR SEARCH
    # =====================
    @staticmethod
    def linear(data: List[Any], target: Any, comparator: Callable[[Any, Any], bool]) -> Any:
        """
        Performs a linear search through the list.
        Returns the index of the target, or -1 if not found.
        """
        
        if not data:
            raise NotFoundError("List is empty.")
            
        for index, item in enumerate(data):
        
            if comparator(item, target):
                return index
        
        raise NotFoundError(f"Target '{target}' not found in the list.")
    # =====================
    # BINARY SEARCH
    # =====================
    @staticmethod
    def binary(data: List[Any], target: Any, comparator: Callable[[Any, Any], int]) -> Any:

        if not data:
            raise NotFoundError("List is empty.")

        left, right = 0, len(data) - 1

        while left <= right:
            # Calculate mid point
            mid = (left + right) // 2
            comparison_result = comparator(data[mid], target)

            if comparison_result == 0:
                return mid
            
            elif comparison_result < 0:
                left = mid + 1
            
            else: 
                right = mid - 1
        
        raise NotFoundError(f"Target '{target}' not found in the list.")
