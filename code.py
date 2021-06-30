import argparse #as agphraser
import cv2 #opencv
import numpy as np #to process fast

#argphraser section
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())
img = cv2.imread(args["image"])
#used to test without argphraser
# img = cv2.imread('input/TextDocument.png')
#Converting an image to gray scale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh1 = cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
#Return a new array
kernel = np.ones((3, 3), np.uint8)
imgMorph = cv2.erode(thresh1, kernel, iterations = 1)
#to crop words
contours, hierarchy = cv2.findContours(imgMorph,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#iterating&saving
i=1
for cnt in contours:
    x,y,w,h = cv2.boundingRect(cnt)

    if w>10 and w<100 and h>10 and h<100:
        cv2.imwrite("Words/NAME_{}.png".format((i)),thresh1[y:y+h,x:x+w])
        i=i+1
#preview the image and close
cv2.imshow('Preview',imgMorph)
cv2.waitKey(0)
cv2.destroyAllWindows()