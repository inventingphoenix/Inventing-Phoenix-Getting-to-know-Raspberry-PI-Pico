# This code Created by Inventing Phoenix
# 1 FEB 2021
from machine import Pin #This will help you access these pins using the Pin class of the machine module:
import time             #This module will you create delays 
IR = Pin(2, Pin.IN)     #The Pin is assigned for the component and the pin mode is set to input
led= Pin(16,Pin.OUT)    #The Pin is assigned for the component and the pin mode is set to output


while True:             # This loop will run forever
   y= IR.value()        # The digital input values are read by IR sensor and stored in a variable y
   if y!= 0 :           # if y is not equal to zero (ie if Digital value is one )
      led.low()         # Turn off the LED (ie set the pin to the low logic level)
      #time.sleep(1)     # for one second 
   else:
      led.high()        #Turn on the LED (ie set the pin to the High logic level)
      #time.sleep(1)
      
#Thank you for watching the video! Please subscribe to our youtube channel and click on the bell notification
 