class Deque:
    def __init__(self, size):
        self.front = -1
        self.rear = -1
        self.size = size
        self.queue_list = [None] * size

    def isFull(self):
        return (self.front == 0 and self.rear == self.size - 1) or (self.rear + 1 == self.front)

    def isEmpty(self):
        return self.front == -1

    def EnqueueFront(self, val):
        if self.isFull():
            print("Deque is full")
        else:
            if self.isEmpty():  # Empty deque
                self.front = 0
                self.rear = 0
            elif self.front == 0:  # Wrap around
                self.front = self.size - 1
            else:
                self.front -= 1
            self.queue_list[self.front] = val

    def EnqueueRear(self, val):
        if self.isFull():
            print("Deque is full")
        else:
            if self.isEmpty():  # Empty deque
                self.front = 0
                self.rear = 0
            elif self.rear == self.size - 1:  # Wrap around
                self.rear = 0
            else:
                self.rear += 1
            self.queue_list[self.rear] = val

    def DequeueFront(self):
        if self.isEmpty():
            print("Deque has no elements")
            return None
        else:
            rem = self.queue_list[self.front]
            self.queue_list[self.front] = None
            if self.front == self.rear:  # Only one element
                self.front = -1
                self.rear = -1
            elif self.front == self.size - 1:  # Wrap around
                self.front = 0
            else:
                self.front += 1
            return rem

    def DequeueRear(self):
        if self.isEmpty():
            print("Deque has no elements")
            return None
        else:
            rem = self.queue_list[self.rear]
            self.queue_list[self.rear] = None
            if self.front == self.rear:  # Only one element
                self.front = -1
                self.rear = -1
            elif self.rear == 0:  # Wrap around
                self.rear = self.size - 1
            else:
                self.rear -= 1
            return rem

    def peekFront(self):
        if self.isEmpty():
            print("Deque has no elements")
            return None
        return self.queue_list[self.front]

    def peekRear(self):
        if self.isEmpty():
            print("Deque has no elements")
            return None
        return self.queue_list[self.rear]


# Usage
deque = Deque(int(input("Enter the size of deque: ")))
print("1-EnqueueFront, 2-EnqueueRear, 3-DequeueFront, 4-DequeueRear, 5-PeekFront, 6-PeekRear, 7-Empty, 8-Full, 9-Exit")

while True:
    cas = int(input())

    match cas:
        case 1:
            deque.EnqueueFront(int(input("Enter the element to enqueue at front: ")))
            print(deque.queue_list)
        case 2:
            deque.EnqueueRear(int(input("Enter the element to enqueue at rear: ")))
            print(deque.queue_list)
        case 3:
            print("Dequeued from Front:", deque.DequeueFront())
            print(deque.queue_list)
        case 4:
            print("Dequeued from Rear:", deque.DequeueRear())
            print(deque.queue_list)
        case 5:
            print("Peek Front:", deque.peekFront())
        case 6:
            print("Peek Rear:", deque.peekRear())
        case 7:
            print("Deque is Empty:", deque.isEmpty())
        case 8:
            print("Deque is Full:", deque.isFull())
        case 9:
            break
