import cv2 as cv
import numpy as np

#Take a image/You can replace also
image = cv.imread("test_image.jpeg")

#Convert it into Gray
gray = cv.cvtColor(src=image, code=cv.COLOR_RGB2GRAY)

#Blur The gray image using medianBlur methid
blur = cv.medianBlur(src=gray, ksize=1)

#Now we will detect edge of the image we made gray using adaptive threshold
edge = cv.adaptiveThreshold(src=blur, maxValue=255, adaptiveMethod=cv.ADAPTIVE_THRESH_MEAN_C,
                            thresholdType=cv.THRESH_BINARY, blockSize=9, C=10)

#We'll add effects to image using bilateral filter for more good results
effects = cv.bilateralFilter(src=image, d=9, sigmaColor=9, sigmaSpace=7)

#We'll combine both coloured and edge image
#Actually we're masking edges(edge) on colored image(effects)
cartoon_image = cv.bitwise_or(src1=effects, src2=effects, mask=edge)

# We'll be able to show our results
cv.imshow("Original", image)
cv.imshow("Cartoon", cartoon_image)
cv.waitKey(0)
cv.destroyAllWindows()