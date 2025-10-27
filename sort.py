from typing import List, Callable, Any

class Sorter:
    @staticmethod
    def _merge_halves(left: List[Any], right: List[Any], comparator: Callable[[Any, Any], bool]) -> List[Any]:
        result = []
        i = 0
        j = 0
        while i < len(left) and j < len(right):
            if comparator(left[i], right[j]):
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    @staticmethod
    def merge(data: List[Any], comparator: Callable[[Any, Any], bool]) -> List[Any]:
        if len(data) <= 1:
            return data
        
        mid = len(data) // 2
        left_half = Sorter.merge(data[:mid], comparator)
        right_half = Sorter.merge(data[mid:], comparator)
        
        return Sorter._merge_halves(left_half, right_half, comparator)


    @staticmethod
    def insertion(data: List[Any], comparator: Callable[[Any, Any], bool]) -> List[Any]:
        sorted_data = list(data)
        n = len(sorted_data)

        for i in range(1, n):
            key = sorted_data[i]
            j = i - 1

            # Shift elements that should come AFTER the key according to comparator
            while j >= 0 and comparator(key, sorted_data[j]):
                sorted_data[j + 1] = sorted_data[j]
                j -= 1

            sorted_data[j + 1] = key

        return sorted_data


    @staticmethod
    def bubble(data: List[Any], comparator: Callable[[Any, Any], bool]) -> List[Any]:
        sorted_data = list(data)
        n = len(sorted_data)
        
        for i in range(n - 1):
            swapped = False
            for j in range(n - 1 - i):
                # If the element at j should NOT come before the element at j+1, swap them.
                if not comparator(sorted_data[j], sorted_data[j+1]):
                    sorted_data[j], sorted_data[j+1] = sorted_data[j+1], sorted_data[j]
                    swapped = True
            
            if not swapped:
                break
                
        return sorted_data

    @staticmethod
    def sort(data: List[Any], comparator: Callable[[Any, Any], bool], method: str = "merge") -> List[Any]:
        method_lower = method.lower() # FIX: Handle case-insensitivity

        if method_lower == "merge":
            return Sorter.merge(data, comparator)
        elif method_lower == "insertion":
            return Sorter.insertion(data, comparator)
        elif method_lower == "bubble":
            return Sorter.bubble(data, comparator)
        else:
            raise ValueError(f"Unknown sort method: {method}. Must be 'merge', 'insertion', or 'bubble'.")