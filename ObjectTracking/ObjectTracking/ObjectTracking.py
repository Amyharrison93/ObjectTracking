#!/usr/bin/env python
import numpy as np
import cv2 as cv 

intCamLoc = 0
try:
    objCam = cv.VideoCapture(intCamLoc, cv.CAP_DSHOW)
except:
    objCam = "Error: Camera not found"
    print(objCam)

state, arryFrameOld = objCam.read()
arryFrameBlank = arryFrameOld-arryFrameOld

#highlights moving objects using background subtraction
def BkgSubtractMOG(arryFrame):
    subtractor = cv.createBackgroundSubtractorMOG()
    arryMask = subtractor.apply(arryFrame)
    return arryMask

#highlights countours in an image
def Contours(arryFrame):
    contours, hierarchy = cv.findContours(
        arryFrame,  
        cv.RETR_EXTERNAL, 
        cv.CHAIN_APPROX_NONE)

    if len(contours > 0):
        return contours
    else:
        return 0
        print("No contours detected")

while (objCam != "Error: Camera not found"):

    # image capture and preprocessing
    state, arryFrameRaw = objCam.read()
    arryFrame = cv.cvtColor(arryFrameRaw, cv.COLOR_BGR2GRAY)
    arryFrame = cv.GaussianBlur(arryFrame, (3,3), 2)


    if arryFrameOld != arryFrameBlank:
        arryMask = BkgSubtractMOG(arryFrame)
        arryContours = Contours(arryMask)
   
        if Contours != 0:
            intObjects = 0
            arryBounds = np.zeros(len(arryContours)+1)
            #for each list find bounds. Note: 0 is X 1 is Y
            for intObjects in range(0, len(arryContours)):
                arryBounds[intObjects] = (
                    arryContours[intObjects][0].min,    # X1
                    arryContours[intObjects][0].max,    # X2
                    arryContours[intObjects][1].min,    # Y1
                    arryContours[intObjects][1].max)    # Y2

                #draw box around each moving object
                cv.rectangle(arryFrameRaw, 
                             (arryContours[intObjects][0].min, arryContours[intObjects][1].min),
                             (arryContours[intObjects][0].max,  arryContours[intObjects][1].max),
                             (255,0,0))

    #save previous frame
    arryFrameOld = arryFrame
    cv.waitKey(1)