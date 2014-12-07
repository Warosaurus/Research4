#!/usr/bin/env python

class Node:
    # n = next node
    # d = data (object)
    # p = previous*
    def __init__(self, d=None, n=None): #initilization with default values
        self.d = d
        self.n = n
    
    def setData(self, d):
        self.d = d
    
    def getData(self):
        return self.d
    
    def setNext(self, n):
        self.n = n
    
    def getNext(self):
        return self.n

class linked_list:
    def __init__(self):
        self.head = None
        self.count = 0
        
    def is_Empty(self):
        return 1 if self.count == 0 else 0
    
    def add(self, d):
        node = Node(d)
        if (self.is_Empty()):
            self.head = node
        else:
            self.last_Node().n = node
        self.count = self.count + 1
        
    def last_Node(self):
        lastNode = None
        if self.is_Empty() != 1:
            lastNode = self.head
            while lastNode.n is not None:
                lastNode = lastNode.n
        return lastNode
    
    def remove_node(self, d):
        if not self.is_Empty():
            found = False
            count = 0
            node = self.head
            prevNode = None
            nextNode = None
            while !found and count <= self.count:
                if node.d == d:
                    found = True
                else:
                    node = node.n
                    count = count + 1
            if found:
                                                
    
    def print_list(self):
        nextNode = None
        if not self.is_Empty():
            ret = {}
            nextNode = self.head
            for pos in range(self.count):
                ret[pos] = nextNode.d
                nextNode = nextNode.n
            for key, val in ret.iteritems():
                print "{}: {}".format(key, val)
        
if __name__ == "__main__":
    link = linked_list()
    link.add(2)
    link.add(10)
    link.print_list()