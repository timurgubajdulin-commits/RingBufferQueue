import unittest
from script import RingBufferQueue


class TestRingBufferQueue(unittest.TestCase):

    def test_enqueue(self):
        queue = RingBufferQueue(3)
        queue.enqueue(10)
        self.assertEqual(queue.to_list(), [10])

    def test_dequeue(self):
        queue = RingBufferQueue(3)
        queue.enqueue(1)
        queue.enqueue(2)

        result = queue.dequeue()

        self.assertEqual(result, 1)
        self.assertEqual(queue.to_list(), [2])

    def test_peek(self):
        queue = RingBufferQueue(3)
        queue.enqueue(7)
        queue.enqueue(8)

        self.assertEqual(queue.peek(), 7)

    def test_is_empty(self):
        queue = RingBufferQueue(3)

        self.assertTrue(queue.is_empty())

        queue.enqueue(1)

        self.assertFalse(queue.is_empty())

    def test_is_full(self):
        queue = RingBufferQueue(2)

        queue.enqueue(1)
        queue.enqueue(2)

        self.assertTrue(queue.is_full())

    def test_size(self):
        queue = RingBufferQueue(3)

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
    unittest.main()