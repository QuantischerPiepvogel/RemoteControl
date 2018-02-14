import time, os
import RPi.GPIO as GPIO

print("Starting up XD")

GPIO.setmode(GPIO.BOARD)
GPIO.setup(33, GPIO.IN)



while GPIO.input(33) == GPIO.LOW:
  
  time.sleep(0.5)

print("Button has been pressed")
os.system("sudo python RaspberryPI/MainControl.py")
