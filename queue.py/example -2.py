from collections import deque

queue = deque()

queue.append(5)
queue.append(15)
queue.append(25)
queue.append(35)
queue.append(45)

print("Queue:", list(queue))

queue.popleft()
queue.popleft()

print("After Dequeue:", list(queue))

queue.append(55)
queue.append(65)

print("Final Queue:", list(queue))