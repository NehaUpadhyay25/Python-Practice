class Node:
    _slots_={"name","value","prev","next"}

    def __init__(self,name,value):
        self.name=name
        self.value=value
        self.next=None
        self.prev=None


