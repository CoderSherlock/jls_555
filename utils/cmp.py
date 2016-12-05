import cv2
import numpy as np
import math
import sys
from matplotlib import pyplot as plt

imga = cv2.imread(sys.argv[1])
imgb = cv2.imread(sys.argv[2])

print(imgb)

if(imga.shape != imgb.shape):
    print("Wrong images, not from same origin")
    exit(0)

imgdiff = np.zeros((imga.shape[0],imga.shape[1],3), np.uint8)
count = 0
error = 0
for i in range(0, imga.shape[0]):
    for j in range(0, imga.shape[1]):
        for k in range(0, 3):
            #print imga[i][j][k], imgb[i][j][k], error
            try:
                imgdiff[i][j][k] = abs(int(imga[i][j][k])-int(imgb[i][j][k]))
                error += abs(int(imga[i][j][k])-int(imgb[i][j][k]))
                count +=1
                time.sleep(1)
            except Exception as e:
                continue

print(error, count)
print((float(error)/count))


plt.subplot(131),plt.imshow(cv2.cvtColor(imga, cv2.COLOR_BGR2RGB),'gray'),plt.title('origin')
plt.subplot(132),plt.imshow(cv2.cvtColor(imgb, cv2.COLOR_BGR2RGB),'gray'),plt.title('after en/de')
plt.subplot(133),plt.imshow(cv2.cvtColor(imgdiff, cv2.COLOR_BGR2RGB),'gray'),plt.title('diff')

plt.show()
