import time, os
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(33, GPIO.IN)

while GPIO.input(33) == GPIO.HIGH:

  time.sleep(0.5)
  
os.system("sudo python RaspberryPI/MainControl.py")
