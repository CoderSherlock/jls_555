import cv2
import sys
from matplotlib import pyplot as plt


img = cv2.imread(sys.argv[1])

print(img.shape)
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h,s,v=cv2.split(img2)

#plt.subplot(221),plt.imshow(h,'gray'),plt.title('blue')
#plt.subplot(222),plt.imshow(s,'gray'),plt.title('green')
#plt.subplot(223),plt.imshow(v,'gray'),plt.title('red')
#plt.subplot(224),plt.imshow(img,'gray'),plt.title('origin')

#plt.show()

img3 = cv2.cvtColor(cv2.merge((h,s,v)), cv2.COLOR_HSV2RGB)
cv2.imshow("res",img3)
#plt.imshow(img3)

cv2.imwrite(sys.argv[2], img)

#plt.show()
