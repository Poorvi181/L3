#Basic utility function-2
import cv2
t= cv2.imread("tomatoes.png")
cv2.imshow("tomatoes",t)
cv2.waitKey(0)

a=cv2.cvtColor(t,cv2.COLOR_BGR2GRAY)
cv2.imshow("grayscale",a)
cv2.waitKey(0)


cv2.destroyAllWindows()