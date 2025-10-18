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
        Returns a new sorted list.
        """
        # Base case: a list of 0 or 1 is already sorted.
        # Return a copy to ensure immutability.
        if len(data) <= 1:
            return data[:]

        # 1. Divide
        mid = len(data) // 2
        
        # 2. Conquer (Recursively sort)
        left_half = Sorter.merge(data[:mid], comparator)
        right_half = Sorter.merge(data[mid:], comparator)

        # 3. Combine (Merge)
        merged = []
        i, j = 0, 0 # Pointers for left and right halves

        while i < len(left_half) and j < len(right_half):
            # Use the comparator to decide which element to add
            if comparator(left_half[i], right_half[j]):
                merged.append(left_half[i])
                i += 1
            else:
                merged.append(right_half[j])
                j += 1

        # Add any remaining elements
        merged.extend(left_half[i:])
        merged.extend(right_half[j:])
        
        return merged

    @staticmethod
    def insertion(data: List[Any], comparator: Callable[[Any, Any], bool]) -> List[Any]:
        """
        Sorts the list using the insertion sort algorithm.
        Returns a new sorted list.
        """
        # Create a copy to avoid modifying the original list
        arr = data[:] 
        
        # Start from the second element
        for i in range(1, len(arr)):
            key = arr[i] # The element to be inserted
            j = i - 1    # Start comparing with the element before it

            # Move elements that are "greater" (per comparator) 
            # than key one position ahead
            while j >= 0 and comparator(key, arr[j]):
                arr[j + 1] = arr[j]
                j -= 1
            
            # Place the key in its correct sorted position
            arr[j + 1] = key
            
        return arr

    @staticmethod
    def bubble(data: List[Any], comparator: Callable[[Any, Any], bool]) -> List[Any]:
        """
        Sorts the list using the bubble sort algorithm.
        Returns a new sorted list.
        """
        # Create a copy to avoid modifying the original list
        arr = data[:]
        n = len(arr)

        for i in range(n):
            swapped = False
            # Last i elements are already in place
            for j in range(0, n - i - 1):
                # Swap if the next element should come before the current one
                if comparator(arr[j + 1], arr[j]):
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
            
            # If no swaps, list is sorted
            if not swapped:
                break
                
        return arr

    @staticmethod
    def sort(data: List[Any], comparator: Callable[[Any, Any], bool], method: str = "merge") -> List[Any]:
        """
        Sorts the list using the specified algorithm.
        Dispatches to the correct sort method.
        """
        # Normalize method name
        method_name = method.lower().strip()
        
        if method_name == 'merge':
            return Sorter.merge(data, comparator)
        elif method_name == 'insertion':
            return Sorter.insertion(data, comparator)
        elif method_name == 'bubble':
            return Sorter.bubble(data, comparator)
        else:
            raise ValueError(f"Unknown sort method: {method}")