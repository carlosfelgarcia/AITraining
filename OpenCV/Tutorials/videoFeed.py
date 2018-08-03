'''
Created on Aug 3, 2018

@author: User
'''
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

# Read a file
# cv2.VideoCapture(<Filepath>)

# Codec
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('Utils/output.avi', fourcc, 20.0, (640, 480))

while True:
    # Video feed
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Write output
    out.write(frame)
    
    # show video
    cv2.imshow('gray', gray)
    cv2.imshow('frame', frame)
    
    # Break the while True
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
out.release()
cv2.destroyAllWindows()
