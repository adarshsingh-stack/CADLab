class Stack:
    def __init__(self, capacity):
        self.stack = []
        self.capacity = capacity

    def push(self, item):
        if len(self.stack) >= self.capacity:
            return "Stack Overflow"
        self.stack.append(item)
        return item

    def pop(self):
        if len(self.stack) == 0:
            return "Underflow"
        return self.stack.pop()

    def peek(self):
        if len(self.stack) == 0:
            return None
        return self.stack[-1]

    def reverse(self):
        temp = []
        while len(self.stack) > 0:
            temp.append(self.stack.pop())
        self.stack = temp

    def copy_stack(self):
        new_stack = Stack(self.capacity)
        for i in self.stack:
            new_stack.push(i)
        return new_stack

    def search(self, value):
        if value in self.stack:
            return self.stack[::-1].index(value) + 1
        return -1

    def clear(self):
        self.stack = []

    def display(self):
        print(self.stack)


s1 = Stack(10)

s1.push(5)
s1.push(15)
s1.push(25)
s1.push(35)
s1.push(45)

s1.display()

print("Top:", s1.peek())

print("Search 25:", s1.search(25))

s2 = s1.copy_stack()

print("Copied Stack:")
s2.display()

s1.reverse()

print("Reversed Stack:")
s1.display()

print("Pop:", s1.pop())
print("Pop:", s1.pop())

s1.display()

s1.clear()

print("After clear:")
s1.display()