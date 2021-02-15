# This code is created by Inventing Phoneix
# 1 FEB 2021
from machine import Pin,PWM #This will help you access these pins using the Pin class of the machine module
                            # and PWM class of the machine module 
import time                 #This module will you create delays 
 
pwm = PWM(Pin(15))          # Pin number 15 has been assigned to our LED and it as also initated as PWM pin

pwm.freq(1000)              # tells Raspberry Pi Pico how often to switch the power between on and off for the LED.

# the duty cycle tells the LED for how long it should be turned ON each time. 
# For Raspberry Pi Pico in MicroPython,this can range from 0 to 65025. 65025 would be 100% of the time, so the LED would stay bright.
# A value of around 32512 would indicate that it should be on for half the time.

while True:
    for duty in range(0,65025,5000): # for every duty cycle from the range 0 to 65025,
                                           #every cycle 5000 PWM values will be added
        pwm.duty_u16(duty)           # PWM value will be shown in the output
        time.sleep(1)                      # delay 1 second
        
	for duty in range(65025, 0, -5000):    # for every duty cycle from the range 65025 to 0,
                                           #every cycle 5000 PWM values will be deducted
		pwm.duty_u16(duty)                 # PWM value will be shown in the output
		time.sleep(1)
		
#Thank you for watching the video! Please subscribe to our youtube channel and click on the bell notification
