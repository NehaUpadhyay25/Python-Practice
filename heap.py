__author__ = 'zjb'

class OurHeap:
    __slots__ = ('stuff','sz','topfn')

    def __init__(self,topfn):
        self.stuff = [None for _ in range(1000)]
        #self.stuff = []
        self.sz = 0
        self.topfn = topfn

    def par(self,ind):
        return (ind-1)//2

    def insert(self,val):
        self.stuff[self.sz] = val
        spot = self.sz
        while spot > 0 and self.topfn(self.stuff[spot], self.stuff[self.par(spot)]):
            self.stuff[spot], self.stuff[self.par(spot)] = self.stuff[self.par(spot)], self.stuff[spot]
            spot = self.par(spot)
        self.sz += 1

    def smallest(self,ind):
        lf = 2*ind + 1
        rt = 2*ind + 2
        if lf >= self.sz:
            return ind
        if rt >= self.sz:
            if self.topfn(self.stuff[ind],self.stuff[lf]):
                return ind
            else:
                return lf
            #return ind if self.stuff[ind] < self.stuff[lf] else lf
        # now we have to compare 3 things
        if self.topfn(self.stuff[lf], self.stuff[rt]):
            if self.topfn(self.stuff[ind], self.stuff[lf]):
                return ind
            else:
                return lf
        else:
            if self.topfn(self.stuff[ind], self.stuff[rt]):
                return ind
            else:
                return rt

    def remove(self):
        ret = self.stuff[0]
        self.sz -= 1
        self.stuff[0] = self.stuff[self.sz]
        loc = 0
        swaploc = self.smallest(loc)
        while loc != swaploc:
            self.stuff[loc],self.stuff[swaploc] = self.stuff[swaploc],self.stuff[loc]
            loc = swaploc
            swaploc = self.smallest(loc)
        return ret

def maxheap(o1,o2):
    return o1 > o2

def main():
    h = OurHeap(maxheap)
    h.insert(5)
    h.insert(2)
    h.insert(3)
    h.insert(9)
    h.insert(1)
    h.insert(7)
    h.insert(4)
    print(h.stuff[:h.sz])
    while h.sz > 0:
        print(h.remove())

if __name__ == '__main__':
    main()
