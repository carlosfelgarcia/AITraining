'''
Created on Aug 3, 2018

@author: User
'''
import cv2
import numpy as np
import matplotlib.pyplot as ptl


img = cv2.imread('Utils/watch.jpg', cv2.IMREAD_GRAYSCALE)

# with CV2
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#With matplolib
# ptl.imshow(img, cmap='gray', interpolation='bicubic')
# ptl.show()

#Save
cv2.imwrite('Utils/watchGray.jpg', img)