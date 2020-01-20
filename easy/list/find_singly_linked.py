'''find Nth element from the end of the singly-linked list. Not from Leetcode'''
import unittest


class LinkedList:
    class _Node:
        def __init__(self, data=None, next=None):
            self.data = data
            self.next = next

    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        new_node = self._Node(data)
        new_node.next = self.head
        self.head = new_node

    def get_last(self, N):
        '''get Nth node from the end of the list'''
        j = k = self.head
        counter = 0

        if not self.head:
            raise IndexError('Cannot index into an empty list')
        while k and counter < N:
            k = k.next
            counter += 1
        if not k and counter < N:
            raise IndexError(f'There is no {N}th node in the list')
        while k:
            j = j.next
            k = k.next

        return j


class TestStringMethods(unittest.TestCase):
    def setUp(self):
        self.list = LinkedList()
        self.list.insert(6)
        self.list.insert(5)
        self.list.insert(4)
        self.list.insert(3)
        self.list.insert(2)
        self.list.insert(1)
        self.list.insert(0)

    def test_simple_find(self):
        self.assertEqual(self.list.get_last(3).data, 4)

    def test_another_simple_find(self):
        self.assertEqual(self.list.get_last(6).data, 1)

    def test_finds_first_element(self):
        self.assertEqual(self.list.get_last(1).data, 6)

    def test_finds_last_element(self):
        self.assertEqual(self.list.get_last(7).data, 0)

    def test_find_in_empty(self):
        with self.assertRaises(IndexError):
            LinkedList().get_last(0)

    def test_out_of_bounds(self):
        with self.assertRaises(IndexError):
            self.list.get_last(42)


if __name__ == '__main__':
    unittest.main()
