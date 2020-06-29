#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 10:53:39 2020

@author: ranood
"""
#face detection with open cv
import cv2
#xml file "the trained model"
Face_trained_model=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
#read the image
img=cv2.imread("/Users/ranood/Desktop/IMG_5336.JPG")
#change the input to gray 
gray_face=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#detect faces
face=Face_trained_model.detectMultiScale(gray_face,1.1,4)

#draw rectangle around faces
for (x,y,w,h)in face:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
    
    
#output displaying
cv2.imshow("img",img)
cv2.waitKey()   