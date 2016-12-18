import cv2
import numpy as np
import math
import sys
from matplotlib import pyplot as plt



class cmp:
    def __init__(self, aname, bname):
        self.imga = cv2.imread(aname)
        self.imgb = cv2.imread(bname)
        print self.imga, self.imgb

        if(self.imga.shape != self.imgb.shape):
            print("Wrong images, not from same origin")
            exit(0)

    def errorrate(self):
        self.error = 0
        self.count = 0
        for i in range(0, self.imga.shape[0]):
            for j in range(0, self.imga.shape[1]):
                for k in range(0, 3):
                    try:
                        self.error += abs(int(self.imga[i][j][k])-int(self.imgb[i][j][k]))
                        self.count +=1
                    except Exception as e:
                        continue

        print(self.error, self.count)
        print((float(self.error)/self.count))
     
    def diffimage(self):
        imgdiff = np.zeros((self.imga.shape[0],self.imga.shape[1],3), np.uint8)
        for i in range(0, self.imga.shape[0]):
            for j in range(0, self.imga.shape[1]):
                for k in range(0, 3):
                    try:
                        imgdiff[i][j][k] = abs(int(self.imga[i][j][k])-int(self.imgb[i][j][k]))
                    except Exception as e:
                        continue

        plt.subplot(131),plt.imshow(cv2.cvtColor(self.imga, cv2.COLOR_BGR2RGB),'gray'),plt.title('origin')
        plt.subplot(132),plt.imshow(cv2.cvtColor(self.imgb, cv2.COLOR_BGR2RGB),'gray'),plt.title('after en/de')
        plt.subplot(133),plt.imshow(cv2.cvtColor(imgdiff, cv2.COLOR_BGR2RGB),'gray'),plt.title('diff')

        plt.show()



if __name__ == "__main__":
    c = cmp(sys.argv[1], sys.argv[2])
    c.errorrate()
    c.diffimage()




