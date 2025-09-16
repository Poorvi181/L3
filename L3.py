#Basic utility function-2
import cv2
import numpy as np
t= cv2.imread("tomatoes.png")
cv2.imshow("tomatoes",t)
cv2.waitKey(0)

a=cv2.cvtColor(t,cv2.COLOR_BGR2GRAY)
cv2.imshow("grayscale",a)
cv2.waitKey(0)

(row,col)=t.shape[0:2] #Extracts only height (row) and width (column).
for i in range(row):
    for j in range(col):
        t[i,j]=sum(t[i,j])*0.33

cv2.imshow("tomatoes3",t)
cv2.waitKey(0)

c=cv2.imread("borderimg.jpg")
(rows,cols)=t.shape[0:2]
d=cv2.getRotationMatrix2D((cols/2,rows/2),angle=45,scale=1)
e=cv2.warpAffine(c,d,(rows,cols))
cv2.imwrite("rotatedimg.jpg",e)

#Canny edge detection.

p=cv2.imread("Pika.png")
f=cv2.Canny (p,100,200)
cv2.imwrite("edgeimg.jpg",f)
g=np.zeros_like(p)#Create a black color image.
g[f!=0]=[45, 45,140]
cv2.imwrite("redimg.jpg",g)

hsv=cv2.cvtColor(p,cv2.COLOR_BGR2HSV)
cv2.imshow("hsvclr",hsv)
cv2.waitKey(0)

cv2.destroyAllWindows()
