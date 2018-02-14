import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setup(8, GPIO.OUT) #Clock
GPIO.setup(10, GPIO.OUT) #Latch
GPIO.setup(12, GPIO.OUT) #Data

def shiftOne(bool):
  print("Set to: " + bool)
  GPIO.output(12, bool)
  time.sleep(0.05)
  GPIO.output(8, GPIO.HIGH)
  time.sleep(0.05)
  GPIO.output(10, GPIO.HIGH)
  time.sleep(0.1)
  GPIO.output(8, GPIO.LOW)
  GPIO.output(10, GPIO.LOW)
  time.sleep(0.1)

while True:
  shiftOne(GPIO.HIGH)
  time.sleep(0.5)
  shiftOne(GPIO.LOW)
  time.sleep(0.5)
