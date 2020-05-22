#!/usr/bin/env python
import numpy as np
import cv2 as cv 

intCamLoc = 0
try:
    objCam = cv.VideoCapture(intCamLoc, cv.CAP_DSHOW)
except:
    objCam = "Error: Camera not found"
    print(objCam)

while (objCam != "Error: Camera not found"):

    #capture image
    state, arryFrame = objCam.read()
    #reduce image
    arryFrame = 
