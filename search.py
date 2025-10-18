from typing import List, Callable, Any


class NotFoundError(Exception):
    pass


class Search:
    """
    A collection of static search algorithms.

    Each method takes:
        - data: list of elements to search in
        - target: element to find
        - comparator: function(a, b) -> bool indicating equality or ordering

    All methods return the index of the found element, or raise NotFoundError.
    """

    @staticmethod
    def linear(data: List[Any], target: Any, comparator: Callable[[Any, Any], bool]) -> Any:
        """
        Performs a linear search through the list using a custom comparator.

        Returns the index of the found element.
        Raises NotFoundError if not found.
        """
        if not data:
            raise NotFoundError(f"{target} was not found")

        for index, item in enumerate(data):
            if comparator(item, target):
                return index

        raise NotFoundError(f"{target} was not found")
