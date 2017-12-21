from unittest import TestCase
from min_heap import MinHeap


class TestMinHeap(TestCase):
    def test_pop(self):
        init = [1, 2, 3, 4, 5, 6, 7]
        heap = MinHeap(init)
        r = heap.pop()
        self.assertEqual(r, 1)
        self.assertEqual(heap.values, [2, 4, 3, 7, 5, 6])

    def test_push(self):
        init = [2, 7, 9, 5]
        heap = MinHeap(init)
        heap.push(1)
        self.assertEqual(heap.values, [1, 2, 9, 7, 5])
