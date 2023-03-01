import unittest
from main import *

n1 = Node(5, None)
n2 = Node('a', n1)

stack = Stack()
stack.push('data1')
stack.push('data2')
stack.push('data3')

stack.pop()


class TestMain(unittest.TestCase):
    def test_Node(self):
        self.assertEqual(n1.data, 5)
        self.assertEqual(n2.data, 'a')
        self.assertEqual(n1.data, 5)
        self.assertEqual(n1.next_node, None)

    def test_Stack(self):
        self.assertEqual(stack.top.data, 'data2')
        self.assertEqual(stack.top.next_node.data, 'data1')
        self.assertEqual(stack.top.next_node.next_node, None)

    def test_pop(self):
        self.assertEqual(stack.top.data, 'data2')
