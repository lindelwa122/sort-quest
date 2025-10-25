from typing import List, Callable, Any, Optional
import math

class NotFoundError(Exception):
    pass


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
        for i, item in enumerate(data):
            if comparator(item, target):
                return i
        return -1
        pass

    # =====================
    # BINARY SEARCH
    # =====================
    @staticmethod
    def binary(data: List[Any], target: Any, comparator: Callable[[Any, Any], int]) -> Any:
        """
        Performs binary search on a sorted list.
        
        The comparator should return:
            - 0 if a == b
            - negative if a < b
            - positive if a > b
        Returns the index of the found element, or -1 if not found.
        """
        pass

