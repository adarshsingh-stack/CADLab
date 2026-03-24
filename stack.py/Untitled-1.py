class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if len(self.stack) == 0:
            return "Stack Underflow"
        return self.stack.pop()

    def peek(self):
        if len(self.stack) == 0:
            return "Stack is Empty"
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

    def display(self):
        if len(self.stack) == 0:
            print("Stack is Empty")
        else:
            print("Stack elements:", self.stack)


s = Stack()

s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)

s.display()

print("Top element:", s.peek())

print("Removed:", s.pop())
print("Removed:", s.pop())

s.display()

print("Stack size:", s.size())

print("Is Empty:", s.is_empty())

s.pop()
s.pop()
s.pop()

print("After removing all elements:")
s.display()

print("Is Empty:", s.is_empty())