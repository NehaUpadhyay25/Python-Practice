__author__ = 'zjb'

class ListNode:
    __slots__ = ('data','next')
    def __init__(self,data,next):
        self.data = data
        self.next = next
    def __str__(self):
        return "Node contains " + str(self.data)

class OurList:
    __slots__ = ('head', 'tail')

    def __init__(self):
        self.head = None
        self.tail = None

    def add_last(self,item):
        newnode = ListNode(item,None)
        if self.tail is None:
            self.head = newnode
        else:
            self.tail.next = newnode
        self.tail = newnode

    def add_first(self,item):
        newnode = ListNode(item,None)
        newnode.next = self.head
        self.head = newnode
        if self.tail is None:
            self.tail = self.head

    def remove_first(self):
        '''
        :pre: head is not None
        :return:
        '''
        self.head = self.head.next
        if self.head is None:
            self.tail = None

    def insert(self,item,ind):
        '''
        This function is OK but takes O(n) time.
        Often we will already be examining the list to decide where to put the new item
        :pre: the index is actually within the list
        :param item:
        :param ind:
        :return:
        '''
        finger = self.head
        for _ in range(ind):
            finger = finger.next
        newnode = ListNode(item,finger.next)
        finger.next = newnode

    def start(self):
        return self.head


    def value_of(self,finger):
        return finger.data

    def next(self,finger):
        return finger.next

    def insert_after(self,finger,item):
        newnode = ListNode(item,finger.next)
        finger.next = newnode

    #def insert_before(self,finger,item):
        # not like that, you can't
        # maybe two pointers?
        # or, doubly-linked list


