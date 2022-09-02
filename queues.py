from collections import deque
# https://www.bigocheatsheet.com/

# Queue implementation in Python
class Queue:

    def __init__(self):
        self.queue = []

    # Add an element
    def enqueue(self, item):
        self.queue.append(item)

    # Remove an element
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop()

    # Display  the queue
    def display(self):
        print(self.queue)

    def size(self):
        return len(self.queue)


# class Dqueue:
    
#     def __init__(self):
#         self.buffer = deque()
    
#     def enqueue(self, val):
#         self.buffer.appendleft(val)
        
#     def dequeue(self):
#         return self.buffer.pop()
    
#     def is_empty(self):
#         return len(self.buffer)==0
    
#     def size(self):
#         return len(self.buffer)


if __name__ == '__main__':

    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)

    q.display()

    q.dequeue()
    q.dequeue()

    print("After removing an element")
    q.display()

    r = deque()

    r.appendleft(5)
    r.appendleft(8)
    r.appendleft(27)

    r.pop()

    # pq = Dqueue()

    # pq.enqueue({
    #     'company': 'Wall Mart',
    #     'timestamp': '15 apr, 11.01 AM',
    #     'price': 131.10
    # })
    # pq.enqueue({
    #     'company': 'Wall Mart',
    #     'timestamp': '15 apr, 11.02 AM',
    #     'price': 132
    # })
    # pq.enqueue({
    #     'company': 'Wall Mart',
    #     'timestamp': '15 apr, 11.03 AM',
    #     'price': 135
    # })

    # print(pq.buffer)

    # print(pq.size())

    # print(pq.dequeue())



