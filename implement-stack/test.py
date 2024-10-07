from option2 import IntStack
import unittest

class Test(unittest.TestCase):
    def test_push(self):
        s = IntStack()
        s.push(1)
        s.push(2)
        self.assertEqual(s.head.data, 2)
    
    def test_pop(self):
        s = IntStack()
        s.push(1)
        s.push(2)
        s.push(3)
        s.push(4)
        self.assertEqual(s.pop(), 4)
        self.assertEqual(s.pop(), 3)
        s.pop()
        s.pop()
        self.assertTrue("Stack is empty" in str(s.pop()))

    def test_peek(self):
        s = IntStack()
        s.push(1)
        s.push(2)
        s.push(3)
        s.push(4)
        self.assertEqual(s.peek(), 4)
        s.pop()
        s.pop()
        self.assertEqual(s.peek(), 2)
        s.pop()
        s.pop()
        self.assertTrue("Stack is empty" in str(s.peek()))
    
    def test_size(self):
        s = IntStack()
        s.push(1)
        s.push(2)
        self.assertEqual(s.size(), 2)
        s.pop()
        s.pop()
        self.assertEqual(s.size(), 0)

if __name__ == "__main__":
    unittest.main()