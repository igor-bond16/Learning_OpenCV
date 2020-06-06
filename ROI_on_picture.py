import cv2
#from matplotlib import pyplot as plt
import numpy as np 
 
#def mosaic(src, ratio=0.1):
#    small = cv2.resize(src, None, fx=ratio, fy=ratio, interpolation=cv2.INTER_NEAREST)
#    return cv2.resize(small, src.shape[:2][::-1], interpolation=cv2.INTER_NEAREST)

img = cv2.imread('/home/igor-bond/Desktop/soccer.jpg')
img2 = cv2.imread('/home/igor-bond/Pictures/insta.png')
#img[1350:1550,580:800] = [255,0,0]
#print(img.shape)
#print(img.size)
#print(img.dtype)
#img[143:180,536:635] = mosaic(img[143:180,536:635])
img,img2 =  cv2.resize(img,(512,512)),cv2.resize(img2,(512,512))
#b,g,r = cv2.split(img)
#img = cv2.merge((b,g,r))
#img = cv2.add(img,img2) 
img = cv2.addWeighted(img,.9,img2,.1,0)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#im_list = np.asarray(img)
#plt.imshow(im_list)
#plt.show()
