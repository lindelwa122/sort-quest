from typing import List, Callable, Any, Optional
import math

class NotFoundError(Exception):
    """Custom exception raised when an element is not found in a search."""
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
    def linear(data: List[Any], target: Any, comparator: Callable[[Any, Any], bool]) -> int:
        """
        Performs a linear search through the list.

        Iterates through the list using a custom comparator function to find the target.
        Returns the index of the first found element.

        Args:
            data: A list of elements to search through.
            target: The element to find.
            comparator: A function that takes two elements (list_element, target)
                        and returns True if they match.

        Returns:
            int: The index of the first found element.

        Raises:
            NotFoundError: If the target is not found in the list.
        """
        # Linear search iterates through the list, checking each element sequentially.
        # This handles the complexity requirements (O(n) worst case, O(1) best case).
        for index, element in enumerate(data):
            # Use the custom comparator function as required by the assignment
            # The comparator checks if the current list element matches the target
            if comparator(element, target):
                # Return the index immediately upon the first match.
                return index

        # If the loop completes without finding a match (this handles empty lists as well),
        # raise the custom NotFoundError exception with the descriptive message.
        raise NotFoundError(f"{target} was not found")

    # =====================
    # BINARY SEARCH (Implementation left as 'pass' as per your original code)
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