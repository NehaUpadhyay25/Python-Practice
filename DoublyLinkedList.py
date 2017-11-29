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

    def prepend(self, value):
        new_node = Node(value, self.head, None)

        if self.head is not None:
            self.head.prev = new_node

        self.head = new_node

    def insertAfter(self,prevNode, value):
        if prevNode is None:
            print("Node can't be none")
            return

        new_node = Node(value)

        self.head.link = Node(value, self.head.link, self.head)

        if new_node.link is not None:
            new_node.link.prev = new_node

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



def main():
    l = DoublyLinkedList()
    print(l)
    l.append(80)
    print(l)
    l.prepend(5)
    print(l)
    l.prepend(6)
    print(l)
    l.prepend("xyz")
    print(l)
    l.prepend("abc")
    print(l)
    l.insertAfter(l.head.link,9)
    print(l)
    l.append(15)
    print(l)
    l.append(25)
    print(l)


if __name__=="__main__":
    main()