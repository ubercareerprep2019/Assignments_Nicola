import sys

#Part A
class Stack:
    def __init__(self):
        self.stack = []
        self.minimum = sys.maxint
    def push(self, value):
        self.stack.append(value)
        if value < self.stack.top():
            self.minimum = value
    def pop(self):
        i = len(self.stack) - 1
        if myStack.isEmpty():
            print("Stack is empty. Can't pop.")
        else:
            return self.stack.pop(i)
    def top(self):
        return self.stack[len(self.stack)-1]
    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False
    def size(self):
        return len(self.stack)
    def min(self):
        return self.minimum

myStack = Stack()
myStack.push(15)
print("Top of Stack: ", myStack.top())
print("Stack Size: ", myStack.size())
myStack.push(-134)
print("Top of Stack: ", myStack.top())
print("Stack Size: ", myStack.size())
print("Popping: ", myStack.pop())
print("Top of Stack: ", myStack.top())
print("Stack Size: ", myStack.size())
print("Popping: ", myStack.pop())
print("Stack Size: ", myStack.size())




#Part B

class Queue:
    def __init__(self):
        self.queue = Stack()
    def enqueue(self, value):
        self.queue.push(value)
    def dequeue(self):
        return self.queue
