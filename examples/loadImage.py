#!/usr/bin/python
from pcf8833 import lcd

#Load the LCD driver
myLcd = lcd.Driver()

#Load teh image to the LCD
myLcd.loadImage("./images/testImg.jpg")

print "Done. You should see now a test image in the LCD."

