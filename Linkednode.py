class Node:

    __slots__ = ("value", "link")

    def __init__(self, value, link=None):
        self.value=value
        self.link=link

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return "LinkedNode(" + repr(self.value) + ", " +repr(self.link) + ")"


def main():
    node=Node( 1, Node( "two",( Node( 3.0 ) ) ) )
    n = node
    while n != None:
        print( n.value )
        n=n.link
    print()
    print( node )
    print( repr( node ) )


if __name__ == "__main__":
    main()