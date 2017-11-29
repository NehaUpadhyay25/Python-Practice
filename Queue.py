from Linkednode import Node

class Queue:
    __slots__ = "front", "back"

    def __init__(self):
        self.front = None
        self.back = None

    def __str__(self):
        result = "Queue[ "
        n = self.front
        while n != None:
            result += "" + str(n.value)
            n = n.link
        result += " ]"
        return result

    def isEmpty(self):
        return self.front == None

    def push(self, value):
        newNode = Node(value, None)
        if self.isEmpty():
            self.front = newNode
        else:
            self.back.link = newNode
        self.back = newNode

    def pop(self):
        result = self.front.value
        self.front = self.front.link

        if self.front == None:
            self.back = None

        return result

def main():
    q = Queue()
    print(q)
    q.push(5)
    q.push("xyz")
    q.push(8)
    print(q)

    while not q.isEmpty():
        print("Popped item is " +str(q.pop()))

if __name__ == "__main__":
    main()