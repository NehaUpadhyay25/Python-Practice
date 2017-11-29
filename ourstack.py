__author__ = 'zjb'

from collections import namedtuple

StackNode = namedtuple('StackNode',('data', 'next'))

class OurStack:
    __slots__ = ('top')


    def __init__(self):
        '''
        actually not pointless.
        :return:
        '''
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self,item):
        '''
        :param item: Any data object
        :return: None
        '''
        newnode = StackNode(item,self.top)
        self.top = newnode

    def pop(self):
        '''
        Removes top of stack and returns it
        :pre: stack is not empty
        :return: data inside top of stack
        '''
        saveme = self.top.data
        self.top = self.top.next
        return saveme

def main():
    '''
    some test cases
    :return:
    '''
    stack = OurStack()
    stack.push('dishes')
    stack.push('kids')
    thing = stack.pop()
    print(thing)
    while not stack.is_empty():
        print(stack.pop())

if __name__ == '__main__':
    main()
