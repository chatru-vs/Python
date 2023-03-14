import cv2
# specify the path to image
image1 = cv2.imread('C:\image\demo.png')
Window_name ='original image'
#displaying the orginal image
cv2.imshow(Window_name,image1)
#convert the image from one color space to another
grey_img = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
invert = cv2.bitwise_not(grey_img)
#image smoothing
blur = cv2.GaussianBlur(invert,(21, 21), 0)
invertedblur = cv2.bitwise_not(blur)
sketch = cv2.divide(grey_img, invertedblur, scale=256.0)
#save the converted image to specified path
cv2.imwrite("C:\image\demo1.png", sketch)
#Reading an image in default mode
image=cv2.imread("C:\image\demo1.png")
Window_name = 'sketch image'
#displaying the sketch image
cv2.imshow(Window_name, image)
cv2.waitkey(0)
cv2.destroyAllWindows()
