__author__ = 'zjb'

from collections import namedtuple

# this doesn't work.
#QueueNode = namedtuple('QueueNode',('data', 'next'))

class QueueNode:
    __slots__ = ('data','next')
    def __init__(self,data,next):
        self.data = data
        self.next = next
    def __str__(self):
        return "Node contains " + str(self.data)

class OurQueue:
    __slots__ = ('head', 'tail')

    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self,item):
        newnode = QueueNode(item,None)
        if self.tail is None:
            self.head = newnode
        else:
            self.tail.next = newnode
        self.tail = newnode

    def dequeue(self):
        '''
        :pre: head is not None
        :return:
        '''
        self.head = self.head.next
        if self.head is None:
            self.tail = None

def main():
    q = OurQueue()
    q.enqueue('Abhishek')
    print(q.head)
    print(q.tail)
    q.enqueue('Anil')
    print(q.head)
    print(q.tail)
    while q.head is not None:
        q.dequeue()
        print(q.head)

main()
