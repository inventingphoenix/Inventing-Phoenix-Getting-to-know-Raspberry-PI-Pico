# code created by Inventing phoenix
# Feb,1,2021
from machine import ADC # ADC class will help us take analog reading
import time

temp_sensor = ADC(4)  # syntax to call the inbuilt temperature sensor

while True:

     temperature = temp_sensor.read_u16() # the data from the sensor will get stored in a variable temperature 
     to_volts = 3.3 / 65535               
     temperature = temperature * to_volts
     celsius_degrees = 27 - (temperature - 0.706) / 0.001721 # final calculations for celsius reading
     
     print(celsius_degrees) # prints the temperature reading in the shell
     time.sleep(1)     