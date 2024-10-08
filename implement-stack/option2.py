# OPTION 2 - IMPLEMENT STACK
# DO NOT SHARE

# 2. Implement a growable integer stack (without using container libraries like vector, list, etc.)
#    that satisfies the following requirements:

# `push` adds a given value to the top
# `pop`  returns and removes the value at the top
# `peek` returns the value at the top
# `size` returns the count of values

class IntStack:
    class Node:
        def __init__(self, data, next):
            self.data = data
            self.next = next


    def __init__(self):
        self.head = None
        self.depth = 0


    # Add a given value to the top
    def push(self, data):
        temp = self.Node(data, self.head)
        self.head = temp
        self.depth += 1


    # Return and remove the value at the top
    def pop(self):
        if self.head is None:
            return Exception("Stack is empty")
        temp = self.head
        self.head = self.head.next
        self.depth -= 1
        return temp.data


    # Returns the value at the top
    def peek(self):
        if self.head is None:
            return Exception("Stack is empty")
        return self.head.data


    # Returns the count of values    
    def size(self):
        return self.depth
        
