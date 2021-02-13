#Code created by Inventing Phoenix
#1 FEB 2021
from machine import Pin # For accessing these pins using the Pin class of the machine module 
import time # Time module helps in creating delays

led= Pin(25,Pin.OUT)  # The Pin is assigned and the mode of the pin is set in this command 


while True:     # While True is used to creating a loop that will never end
   led.high()     #  .high()  will set the pin to the high logic level
   time.sleep(1)  #   time.sleep(1) will create an delay of 1 seconds. Time can be changed inside the bracket.
   led.low()      #  .low() will set the pin to the low logic level
   time.sleep(1)
   
#Thank you for watch this Video Please subricbe the channel and click on the bell icon.
   

 