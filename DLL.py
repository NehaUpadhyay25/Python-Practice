class Node:

    __slots__ = ("value", "link", "prev")

    def __init__(self, value, link=None, prev=None):
        self.value=value
        self.link=link
        self.prev=prev

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return "LinkedNode(" + repr(self.value) + ", " +repr(self.link) + ", " +repr(self.prev)+ ")"

class DoublyLinkedList:

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

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return

        current = self.head

        while current.link is not None:
            current = current.link

        current.link = Node(value, None, current)
        return

    def removeBeginning(self):
        self.head = self.head.link
        self.head.prev = None

    def removeMiddle(self,index):
        current = self.head

        for n in range(index):
            current = current.link

        if current.link == None:
            current.prev.link = current.link

        else:
            current.prev.link = current.link
            current.link.prev = current.prev

def main():
    l = DoublyLinkedList()
    l.append(3)
    l.append(1)
    l.append(5)
    l.append(2)
    l.append(99)
    l.append(88)
    l.append(77)
    l.append(66)
    print(l)
    l.removeMiddle(3)
    print(l)
    l.removeBeginning()
    print(l)
    l.removeMiddle(5)
    print(l)

if __name__=="__main__":
    main()