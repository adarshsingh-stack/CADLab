class Queue:
    def __init__(self, size):
        self.queue = []
        self.size = size
        self.front = -1
        self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return self.rear == self.size - 1

    def enqueue(self, data):
        if self.is_full():
            print("Queue is Full")
        else:
            if self.front == -1:
                self.front = 0
            self.rear += 1
            if self.rear < len(self.queue):
                self.queue[self.rear] = data
            else:
                self.queue.append(data)
            print(data, "inserted into queue")

    def dequeue(self):
        if self.is_empty():
            print("Queue is Empty")
        else:
            data = self.queue[self.front]
            if self.front == self.rear:
                self.front = -1
                self.rear = -1
            else:
                self.front += 1
            print(data, "removed from queue")
            return data

    def display(self):
        if self.is_empty():
            print("Queue is Empty")
        else:
            print("Queue elements are:")
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=" ")
            print()

q = Queue(5)

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)

q.display()

q.dequeue()
q.dequeue()

q.display()

q.enqueue(60)
q.enqueue(70)

q.display()