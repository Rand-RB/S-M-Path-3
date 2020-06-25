# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
""" 
#wibsite URL "https://en.wikipedia.org/wiki/Animal"

#import urllib package 
import urllib as ub
URL="https://en.wikipedia.org/wiki/Animal"
#open URL by using urlopen function
content=ub.request.urlopen(URL)

#decoding string "converts the set of bytes back to the original string"
for line in content:
    decode=line.decode("utf_8")
    print(decode)












