import sys
import os
import struct


class Node:
    def __init__(self, right=None, left=None, parent=None, weight=0, charcode=None):
        self.right = right
        self.left = left
        self.parent = parent
        self.weight = weight
        self.charcode = charcode
    
    def __str__(self):
        return "Node\t{0}:{1}".format(self.charcode, self.weight)
    
class huffman:
    listofNode = []
    codeDict = {}
    encodeDict = {}
    head = None
    bflow = ""
    def __init__(self, raw_data=[]):
        self.data = raw_data
        for item in self.data:
            self.codeDict.setdefault(item, 0)
            self.codeDict[item] += 1
            
    def buildtree(self):
        for e in self.codeDict.keys():
            self.listofNode.append(Node(weight=self.codeDict[e], charcode=e))
        self.listofNode = self.sort(self.listofNode)

        listofNode = self.listofNode[:]
        while len(listofNode)!=1:
            a,b = listofNode[0], listofNode[1]
            new=Node()
            new.weight, new.left, new.right = a.weight + b.weight, a, b
            a.parent, b.parent = new, new
            listofNode.remove(a), listofNode.remove(b)
            listofNode.append(new)
            listofNode = self.sort(listofNode)
         
        self.head = listofNode[0]

        for e in self.listofNode:
            ep=e
            self.encodeDict.setdefault(e.charcode,"")
            while ep!=self.head:
                if ep.parent.left==ep:
                    self.encodeDict[e.charcode]="1"+self.encodeDict[e.charcode]
                else:
                    self.encodeDict[e.charcode]="0"+self.encodeDict[e.charcode]
                ep=ep.parent         
    
    def sort(self, listofNode):
        return sorted(listofNode,key=lambda node:node.weight)

    def encode(self):
        for i in self.data:
            self.bflow += self.encodeDict[i]



if __name__ == "__main__":
    raw_stream = [100, 100, 10, 10, 10, 10, 10, 10, 10, 0, 0, 0, 0, 0, 0]
    driver = huffman(raw_stream)
    # print driver.data
    print driver.codeDict
    driver.buildtree()
    print driver.encodeDict
    driver.encode()
    print driver.bflow
    print len(driver.bflow)
    # for i in driver.listofNode:
    #    print i