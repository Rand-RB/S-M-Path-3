#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 11:47:16 2020

@author: ranood
"""
#smile detection with open cv
import cv2
#xml file "the trained model"
smaile_trained_model=cv2.CascadeClassifier("haarcascade_smile.xml")
#read the image
img=cv2.imread("aaa.jpg")
#change the input to gray
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#detect smiles
smile=smaile_trained_model.detectMultiScale(gray,1.8,10)
#draw rectangle around smiles
for (x,y,w,h)in smile:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,135,0),2)

#display output
cv2.imshow("smile detected:",img)
cv2.waitKey(0)
cv2.distroyAllWindows()    
