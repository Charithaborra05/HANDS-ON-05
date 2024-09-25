from typing import TypeVar, List, Optional

T = TypeVar('T')

class Heap:
    def __init__(self, arr: List[T]) -> None:
        self.heap: List[T] = arr
        self.build_min_heap()
    
    def insertElement(self, value: T) -> None:
        self.heap.append(value)
        self._bubble_up(len(self.heap) - 1)
    
    def _bubble_up(self, i: int) -> None:
        parent = (i - 1) >> 1
        while i > 0 and self.heap[i] < self.heap[parent]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            i = parent
            parent = (i - 1) >> 1

    def heapify(self, n: int, i: int) -> None:
        smallest = i
        left = (i << 1) + 1
        right = (i << 1) + 2

        if left < n and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < n and self.heap[right] < self.heap[smallest]:
            smallest = right
        
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.heapify(n, smallest)

    def build_min_heap(self) -> None:
        n = len(self.heap)
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(n, i)

    def get_root(self) -> Optional[T]:
        return self.heap[0] if self.heap else None
    
    def pop(self) -> Optional[T]:
        if not self.heap:
            return None
        root_value = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.heapify(len(self.heap), 0)
        return root_value
    
    def size(self) -> int:
        return len(self.heap)


if __name__ == '__main__':
    # Example usage
    arr = [50, 20, 30, 10, 15, 5, 25]
    heap = Heap(arr)
    print(f'Min Heap: {heap.heap}')

    heap.insertElement(2)
    print("Heap after inserting 2:", heap.heap)

    root = heap.get_root()
    print(f'Root element: {root}')

    popped_value = heap.pop()
    print(f'Heap after popping root ({popped_value}): {heap.heap}')
