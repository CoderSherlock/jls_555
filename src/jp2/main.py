import numpy as np
import cv2
import pywt


data = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]], dtype=np.int)
print(data)

coeffs = pywt.dwt2(data, 'haar')
print coeffs

a, (b,c,d)=coeffs
d = np.array([[0,0],[0,-8]], dtype=np.float)
coeffs = (a, (b,c,d))
print coeffs

recover = pywt.idwt2(coeffs, 'haar')
print recover

image = cv2.imread("../../img/basel2.bmp")
height, width = image.shape[0], image.shape[1]

def dwt_control(image, level):
    dwt(image)


def dwt(data):
    return pywt.dwt2(data, 'haar')
