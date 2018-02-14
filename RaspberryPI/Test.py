import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setup(17, GPIO.OUT) #Clock
GPIO.setup(27, GPIO.OUT) #Latch
GPIO.setup(22, GPIO.OUT) #Data

def shiftOne(bool):
  GPIO.output(22, bool)
  time.sleep(0.05)
  GPIO.output(17, GPIO.HIGH)
  time.sleep(0.05)
  GPIO.output(27, GPIO.HIGH)
  time.sleep(0.1)
  GPIO.output(17, GPIO.LOW)
  GPIO.output(27, GPIO.LOW)
  time.sleep(0.1)

while True:
  shiftOne(GPIO.HIGH)
  time.sleep(0.5)
  shiftOne(GPIO.LOW)
  time.sleep(0.5)
