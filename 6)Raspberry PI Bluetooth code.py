#code writen by Inventing Phoenix
# FEB/1/2021
from machine import UART,Pin # UART Stands for Universal asynchronus reciver and transmiter
                             # UART class will help us connect our Raspberry PI Pico to the HC-05 Bluetooth module
from time import sleep_ms

BT = UART(1,9600)            # the UART channel number to which the Bluetooth device is connected is mention allong with the baud rate

led= Pin(15,Pin.OUT)         # LED is connected to GPIO 15

while True:                  # 
    if BT.any() > 0:         # this conditional statement is used to check if the HC-05 is connected to any device
        data=BT.read(1)      # if the device is connected the data begin recived will be stored in data variable
        
        if "1" in data:      # if the data recived is 1 
            led.high()       # the LED is turned on 
        
        else:                # anything apart from 1 
            led.low()        # LED is turned off
            print(data)
        