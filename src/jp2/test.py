import pywt

def dwt(data):
    print data
    return pywt.dwt2(data, 'haar')


a = [[4, 4, 3, 3], [4, 4, 3, 3], [2, 2, 1, 1], [2, 2, 1, 1]]
print dwt(a)
