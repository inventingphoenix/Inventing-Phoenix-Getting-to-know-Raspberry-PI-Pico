# This code Created by Inventing Phoenix
# 1 FEB 2021
from machine import Pin, PWM, ADC # This will help you access these pins using the Pin class of the machine module
                                  # and PWM and ADC class of the machine module. ADC class will help us use analog pins
import time

pwm = PWM(Pin(15))                # Pin number 15 has been assigned to our LED and it as also initated as PWM component
adc = ADC(Pin(26))                # Pin number 26 has been assigned to our potentiometer and its initated as analog component

pwm.freq(1000)                    # tells Raspberry Pi Pico how often to switch the power between on and off for the LED.

while True:                       # runs the loop forever 
	duty = adc.read_u16()         # analog values read by the analog pin assigned to the potentiometer will be save in duty variable
	print(duty)                   # will print the analog value on the screen
	pwm.duty_u16(duty)            # will pass one the analog value to the LED as a PWM input 
	time.sleep(1)                 # delay for 1 second

#Thank you for watching the video! Please subscribe to our youtube channel and click on the bell notification
