from Linkednode import Node

class Stack:

    __slots__="top"

    def __init__(self):
        self.top=None

    def __str__(self):
        result = "Stack[ "
        n = self.top
        while n != None:
            result += "" + str(n.value)
            n = n.link
        result += " ]"
        return result

    def isEmpty(self):
        return self.top == None

    def push(self, value):
        self.top = Node(value, self.top)

    def pop(self):
        result = self.top.value
        self.top = self.top.link
        return result

def main():
    s = Stack()
    print(s)
    s.push(5)
    s.push("xyz")
    s.push(8)
    print(s)

    while not s.isEmpty():
        print("Popped item is " +str(s.pop()))

if __name__ == "__main__":
    main()



