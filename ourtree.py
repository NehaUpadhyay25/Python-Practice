__author__ = 'zjb'

class BTNode:
    __slots__ = ('data','left','right')

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BTree:
    __slots__ = ('root')

    def __init__(self):
        self.root = None

    def traverse_inorder(self):
        self.traverse_inorder_from(self.root)

    def traverse_inorder_from(self,node):
        if node is None:
            return
        self.traverse_inorder_from(node.left)
        # do the thing here
        print(node.data,end=' ')
        self.traverse_inorder_from(node.right)

    def traverse_postorder(self):
        self.traverse_postorder_from(self.root)

    def traverse_postorder_from(self,node):
        if node is None:
            return
        self.traverse_postorder_from(node.left)
        self.traverse_postorder_from(node.right)
        # do the thing here
        print(node.data,end=' ')

    # preorder is also a thing

def main():
    a = BTNode('1')
    b = BTNode('2')
    c = BTNode('+')
    c.left = a
    c.right = b
    three = BTNode('3')
    two = BTNode('2')
    minus = BTNode('-')
    minus.left = three
    minus.right = two
    root = BTNode('*')
    root.left = c
    root.right = minus
    tree = BTree()
    tree.root = root

    tree.traverse_inorder()
    print()
    tree.traverse_postorder()

if __name__ == '__main__':
    main()


