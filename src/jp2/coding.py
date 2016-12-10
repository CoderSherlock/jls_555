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

    def estimateSize(self):
        fileSize = 0
        # print(len(self.encodeDict))
        fileSize += 8*16
        largestBits = 0
        for i in self.encodeDict.keys():
            largestBits = len(self.encodeDict[i]) if len(self.encodeDict[i]) > largestBits else largestBits

        fileSize += len(self.encodeDict)*(largestBits+16)
        fileSize += len(self.bflow)
        print("Esitmated Size is {0} Kbs".format(float(fileSize)/8/1024))

    def write2File(self, filename="outstream.jp2"):
        self.buildtree()
        self.encode()
        out = file(filename, 'wb')
        for i in range(0, len(self.bflow), 16):
            if len(self.bflow[i:i+16]) < 16:

                print int(self.bflow[i:i+16], 2)
            print "{0:b}".format(int(self.bflow[i:i+16], 2))
            out.write(struct.pack(">H", int(self.bflow[i:i+16], 2)))
        out.close()

    def readFile(self, filename="outstream.jp2"):
        inf = file(filename, 'rb')
        content =inf.read()
        print content



if __name__ == "__main__":
    raw_stream = [100, 199, 15, 10, 10, 131, 0, -1, 1, 2, -2, 0, 0, -1, 0]
    driver = huffman(raw_stream)
    # print driver.data
    # print driver.codeDict
    # driver.buildtree()
    # print driver.encodeDict
    # driver.encode()
    # print driver.bflow
    # print len(driver.bflow)

    # driver.estimateSize()
    # driver.write2File()
    # driver.readFile()
    # for i in driver.listofNode:
    #    print i
