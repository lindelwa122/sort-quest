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
        arr = data[:]  # work on a copy to keep immutability
        temp = [None] * len(arr)  # pre-allocate temp list once (performance gain)

        def merge_sort(start: int, end: int):
            if end - start <= 1:
                return

            mid = (start + end) // 2
            merge_sort(start, mid)
            merge_sort(mid, end)

            # Merge two sorted halves (in-place using temp)
            i, j, k = start, mid, start
            while i < mid and j < end:
                if comparator(arr[i], arr[j]):
                    temp[k] = arr[i]
                    i += 1
                else:
                    temp[k] = arr[j]
                    j += 1
                k += 1

            # Copy remaining elements
            while i < mid:
                temp[k] = arr[i]
                i += 1
                k += 1
            while j < end:
                temp[k] = arr[j]
                j += 1
                k += 1

            # Copy back to arr
            arr[start:end] = temp[start:end]

        merge_sort(0, len(arr))
        return arr

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

