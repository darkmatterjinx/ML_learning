import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('moonlanding.png',0) #直接读为灰度图像
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)

#取绝对值：将复数变化成实数
#取对数的目的为了将数据变化到较小的范围（比如0-255）
s1 = np.log(np.abs(f))
s2 = np.log(np.abs(fshift))
plt.subplot(221),plt.imshow(s1,'gray'),plt.title('original')
plt.subplot(222),plt.imshow(s2,'gray'),plt.title('center')

cf = np.fft.ifft2(f)
print(cf)
cfshift = np.fft.ifftshift(fshift)
plt.subplot(223),plt.imshow(img,'gray'),plt.title('original')
plt.show()
