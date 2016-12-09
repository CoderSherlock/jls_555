import sys
import cv2
import pywt
import numpy as np
from matplotlib import pyplot as plt


def print_file(img, h, w, name):
    f = open(name, "w")
    for i in range(0, h):
        for j in range(0, w):
            f.write(str(img[i][j])+"\n")
        f.write("")
    f.close()


def copy2(img, h, w):
    matrix = np.zeros((h, w), dtype=np.double)
    for i in range(0, h):
        for j in range(0, w):
            matrix[i][j] = img[i][j]
    return matrix

def copy3(img, h, w):
    matrix = np.zeros((h, w), dtype=np.int)
    for i in range(0, h):
        for j in range(0, w):
            matrix[i][j] = img[i][j]
    return matrix

def copyint(img, h, w):
    matrix = np.zeros((h, w), dtype=np.int)
    for i in range(0, h):
        for j in range(0, w):
            matrix[i][j] = int(img[i][j]+0.5)
    return matrix


def color_seperation(img):
    tmp = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
    return cv2.split(tmp)

def dwt(data):
    return pywt.dwt2(data, 'haar')


def dwt_control(image, h, w, level):
    print level

    lh, lw = h/(2**(level-1)), w/(2**(level-1))
    tmpdata = copy2(image, lh, lw)
    print lh, lw


    ill, (ilh, ihl, ihh) = dwt(tmpdata)
    # print(ll, lh, hl, hh)
    for i in range(0, lh/2):
        for j in range(0, lw/2):
            tmpdata[i][j] = ill[i][j]
    for i in range(0, lh/2):
        for j in range(lw/2, lw):
            tmpdata[i][j] = ilh[i][j-lw/2]
    for i in range(lh/2, lh):
        for j in range(0, lw/2):
            tmpdata[i][j] = ihl[i-lh/2][j]
    for i in range(lh/2, lh):
        for j in range(lw/2, lw):
            tmpdata[i][j] = ihh[i-lh/2][j-lw/2]

    for i in range(0, lh):
        for j in range(0, lw):
            image[i][j] = tmpdata[i][j]
    return image

def iwt(ll, lh, hl, hh):
    return pywt.idwt2((ll, (lh, hl, hh)), 'haar')

def iwt_control(image, h, w, level):
    print level
    lh, lw = h/(2**(level-1)), w/(2**(level-1))
    print lh, lw
    ill = np.zeros((lh/2, lw/2), dtype=np.double)
    ilh = np.zeros((lh/2, lw/2), dtype=np.double)
    ihl = np.zeros((lh/2, lw/2), dtype=np.double)
    ihh = np.zeros((lh/2, lw/2), dtype=np.double)

    for i in range(0, lh/2):
        for j in range(0, lw/2):
            ill[i][j] = image[i][j]
    for i in range(0, lh/2):
        for j in range(lw/2, lw):
            ilh[i][j-lw/2] = image[i][j]
    for i in range(lh/2, lh):
        for j in range(0, lw/2):
            ihl[i-lh/2][j] = image[i][j]
    for i in range(lh/2, lh):
        for j in range(lw/2, lw):
            ihh[i-lh/2][j-lw/2] = image[i][j]

    tmpdata = iwt(ill, ilh, ihl, ihh)
    for i in range(0, lh):
        for j in range(0, lw):
            image[i][j] = tmpdata[i][j]
    return image




def round_control(image, h, w, roun=3, op=0):
    tmpdata = image
    if op == 0:
        for i in range(0, roun):
            tmpdata = dwt_control(tmpdata, h, w, i+1)
    if op == 1:
        for i in range(0, roun):
            tmpdata = iwt_control(tmpdata, h, w, roun-i)
    return tmpdata



if __name__ == "__main__":
    operation   = sys.argv[1]
    tarimg      = sys.argv[2]
    retimg      = sys.argv[3]

    image = cv2.imread("../../img/basel2.bmp")
    height, width = image.shape[0], image.shape[1]

    ty, tu, tv = color_seperation(image)
    y = copy2(ty, height, width)
    u = copy2(tu, height, width)
    v = copy2(tv, height, width)    

    y = round_control(y, height, width, 3)
    u = round_control(u, height, width, 3)
    v = round_control(v, height, width, 3)

    plt.subplot(221),plt.imshow(y,'gray'),plt.title('y')
    plt.subplot(222),plt.imshow(u,'gray'),plt.title('u')
    plt.subplot(223),plt.imshow(v,'gray'),plt.title('v')

    plt.show()
    #print_file(y, height, width, "y.dat")
    #print_file(u, height, width, "u.dat")
    #print_file(v, height, width, "v.dat")
    
    y = copyint(y, height, width)
    u = copyint(u, height, width)
    v = copyint(v, height, width)

    print("saving")
    # print y,u,v
        
    # Test somthing
    cal = {}
    for i in range(0, height):
        for j in range(0, width):
            if y[i][j] in cal.keys():
                cal[y[i][j]] += 1
            else:
                cal[y[i][j]] = 1
    cal = sorted(cal.items(), key=lambda x: x[1])
    # print cal
    # End testing something


    # Save jp2 to bmp 
    
    #ha = np.zeros((height, width,3), np.uint16)
    #for i in range(0, height):
    #    for j in range(0, width):
    #            ha[i][j][0] = y[i][j]
    #            ha[i][j][1] = u[i][j]
    #            ha[i][j][2] = v[i][j]
    #cv2.imwrite("basel2jp2.jp2.bmp", ha)


    # Load jp2 from bmp/format

    #y, u, v = cv2.split(cv2.imread("basel2jp2.jp2.bmp"))
    #print("loading")
    #print y,u,v

    y = round_control(y, height, width, 3, 1)
    u = round_control(u, height, width, 3, 1)
    v = round_control(v, height, width, 3, 1)


    #print_file(y, height, width, "y.dat")
    #print_file(u, height, width, "u.dat")
    #print_file(v, height, width, "v.dat")

    #plt.subplot(221),plt.imshow(y,'gray'),plt.title('y')
    #plt.subplot(222),plt.imshow(u,'gray'),plt.title('u')
    #plt.subplot(223),plt.imshow(v,'gray'),plt.title('v')
    y = copy3(y, height, width)
    u = copy3(u, height, width)
    v = copy3(v, height, width)

    ha = cv2.merge((y,u,v))
    for i in range(0, height):
        for j in range(0, width):
            for k in range(0, 3):
                image[i][j][k] = ha[i][j][k]
    img = cv2.cvtColor(image, cv2.COLOR_YUV2RGB)
    plt.imshow(img)

    plt.show()

    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    cv2.imwrite(retimg, img)

