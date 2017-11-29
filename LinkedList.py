from Linkednode import Node

class LinkedList:

    __slots__ = ("head", "tail")

    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        result = "Linked List : ["
        current = self.head
        while current is not None:
            result += " " + str(current.value) + " "
            current = current.link
        result += "]"
        return result

    def isEmpty(self):
        return self.head == None

    def prepend(self, value):
        newNode = Node(value, None)
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
        else:
            newNode.link = self.head
            self.head = newNode

    def append(self, value):
        newNode = Node(value, None)
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.link = newNode
            self.tail = newNode

    def get(self, index):
        current = self.head
        for n in range(index):
            current = current.link
        return print("Get = " +str(current.link))

    def put(self, index, value):
        current = self.head
        for n in range(index):
            current = current.link
        current.value = value

    def insertBefore(self, index, value):
        if index == 0:
            self.prepend(value)
        else:
            current = self.head
            for n in range(index-1):
                current = current.link
            current.link = Node(value, current.link)

    def insertAfter(self, index, value):
        if index == 0:
            self.prepend(value)
        else:
            current = self.head
            for n in range(index):
                current = current.link
            current.link = Node(value, current.link)

    def find(self, value):
        current = self.head
        index = 0
        while current is not None:
            if current.value == value:
                return print("Find = " +str(index))
            else:
                current = current.link
                index += 1
        return -1

    def length(self):
        current = self.head
        length = 0
        while current is not None:
            current = current.link
            length += 1
        return print("Length = " +str(length))

def main():
    l = LinkedList()
    print(l)
    l.append(11)
    print(l)
    l.append(7)
    print(l)
    l.prepend(13)
    print(l)
    l.insertAfter(0, 6)
    print(l)
    l.insertAfter(3,9)
    print(l)
    l.insertAfter(2,8)
    print(l)
    l.get(4)
    l.put(4, 12)
    print(l)
    l.insertAfter(4, 15)
    print(l)
    l.find(15)
    l.length()

if __name__=="__main__":
    main()