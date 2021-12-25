class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, val):
        new_node = Node(val)
        if self.tail == None and self.head == None:
            self.tail = self.head = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def printQueue(self):
        curr = self.head
        while (curr != None):
            print(curr.value)
            curr = curr.next

    def dequeue(self) -> 'Optional[int]':
        if self.tail != None:
            val = self.head.value
            self.head = self.head.next
            return val
        else:
            return None


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.printQueue()
print(q.dequeue())
