class IntStack:
    class Node:
        def __init__(self, data, next):
            self.data = data
            self.next = next

    def __init__(self):
        self.head = None
        self.depth = 0

    def push(self, data):
        temp = self.Node(data, self.head)
        self.head = temp
        self.depth += 1

    def pop(self):
        if self.head is None:
            return Exception("Stack is empty")
        temp = self.head
        self.head = self.head.next
        self.depth -= 1
        return temp.data

    def peek(self):
        if self.head is None:
            return Exception("Stack is empty")
        return self.head.data
        
    def size(self):
        return self.depth
        