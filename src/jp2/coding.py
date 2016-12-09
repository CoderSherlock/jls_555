import sys
import os
import struct


class node:
    def __init__(self, right=None, left=None, parent=None, weight=0, charcode=None):
        self.right = right
        self.left = left
        self.parent = parent
        self.weight = weight
        self.charcode = charcode
    
class huffman:





if __name__ == "__main__":
    f = open("test.dat", 'wb')
    f.write(struct.pack('i', 0))
    f.write(struct.pack('i', 128))
    f.write(struct.pack('i', 255))
    f.write(struct.pack('i', 3000))
    f.close()
