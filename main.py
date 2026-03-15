import unittest
from io import StringIO
import sys


class RingBufferQueue:
    def __init__(self, capacity: int = 5):
        self._capacity = capacity
        self._data = [None] * capacity
        self._head = 0
        self._tail = 0
        self._count = 0

    def enqueue(self, value: int) -> None:
        if self.is_full():
            print("Предупреждение: очередь переполнена, элемент не добавлен.")
            return
        self._data[self._tail] = value
        self._tail = (self._tail + 1) % self._capacity
        self._count += 1

    def dequeue(self) -> int | None:
        if self.is_empty():
            return None
        value = self._data[self._head]
        self._data[self._head] = None
        self._head = (self._head + 1) % self._capacity
        self._count -= 1
        return value

    def peek(self) -> int | None:
        if self.is_empty():
            return None
        return self._data[self._head]

    def is_empty(self) -> bool:
        return self._count == 0

    def is_full(self) -> bool:
        return self._count == self._capacity

    def size(self) -> int:
        return self._count

    def to_list(self) -> list[int]:
        result = []
        index = self._head
        i = 0
        while i < self._count:
            result.append(self._data[index])
            index = (index + 1) % self._capacity
            i += 1
        return result


def main():
    queue = RingBufferQueue(3)

    print("is_empty:", queue.is_empty())
    print("is_full:", queue.is_full())
    print("size:", queue.size())
    print("peek:", queue.peek())
    print("dequeue:", queue.dequeue())
    print("to_list:", queue.to_list())

    queue.enqueue(1)
    print("enqueue(1):", queue.to_list())

    queue.enqueue(2)
    print("enqueue(2):", queue.to_list())

    queue.enqueue(3)
    print("enqueue(3):", queue.to_list())

    print("peek:", queue.peek())
    print("is_full:", queue.is_full())
    print("size:", queue.size())

    print("dequeue:", queue.dequeue())
    print("after dequeue:", queue.to_list())

    queue.enqueue(4)
    print("enqueue(4):", queue.to_list())

    queue.enqueue(5)

    print("dequeue:", queue.dequeue())
    print("dequeue:", queue.dequeue())
    print("dequeue:", queue.dequeue())
    print("dequeue:", queue.dequeue())
    print("is_empty:", queue.is_empty())


class TestRingBufferQueue(unittest.TestCase):
    def test_enqueue(self):
        queue = RingBufferQueue(3)
        queue.enqueue(10)
        self.assertEqual(queue.to_list(), [10])

    def test_dequeue(self):
        queue = RingBufferQueue(3)
        queue.enqueue(1)
        queue.enqueue(2)
        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.to_list(), [2])

    def test_peek(self):
        queue = RingBufferQueue(3)
        queue.enqueue(7)
        queue.enqueue(8)
        self.assertEqual(queue.peek(), 7)
        self.assertEqual(queue.to_list(), [7, 8])

    def test_is_empty(self):
        queue = RingBufferQueue(3)
        self.assertTrue(queue.is_empty())
        queue.enqueue(1)
        self.assertFalse(queue.is_empty())

    def test_is_full(self):
        queue = RingBufferQueue(2)
        self.assertFalse(queue.is_full())
        queue.enqueue(1)
        queue.enqueue(2)
        self.assertTrue(queue.is_full())

    def test_size(self):
        queue = RingBufferQueue(3)
        self.assertEqual(queue.size(), 0)
        queue.enqueue(1)
        queue.enqueue(2)
        self.assertEqual(queue.size(), 2)

    def test_to_list(self):
        queue = RingBufferQueue(3)
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        queue.dequeue()
        queue.enqueue(4)
        self.assertEqual(queue.to_list(), [2, 3, 4])


if __name__ == "__main__":
    main()
    unittest.main(argv=["first-arg-is-ignored"], exit=False)