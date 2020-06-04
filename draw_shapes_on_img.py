import cv2

img = cv2.imread('/home/igor-bond/Pictures/testing.png',1)

img = cv2.line(img,(0,0),(255,255),(0,255,0),10)
img = cv2.arrowedLine(img,(0,255),(255,255),(255,0,0),10)
img = cv2.rectangle(img,(500,255),(620,375),(0,0,255),5)
img = cv2.circle(img,(560,315),60,(0,255,0),-1)
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img,'OpenCV',(100,500),font,4,(255,255,255))
#img = cv2.circle(img,(100,500),1,(0,255,0),-1)

cv2.imshow('image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
