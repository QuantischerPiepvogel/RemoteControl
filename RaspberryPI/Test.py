import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setup(18, GPIO.OUT) #Clock
GPIO.setup(16, GPIO.OUT) #Latch
GPIO.setup(12, GPIO.OUT) #Data

def shiftOne(bool):
  print("Set to: " + str(bool))
  GPIO.output(12, bool)
  time.sleep(0.01)
  GPIO.output(18, GPIO.HIGH)
  time.sleep(0.01)
  GPIO.output(16, GPIO.HIGH)
  time.sleep(0.01)
  GPIO.output(18, GPIO.LOW)
  GPIO.output(16, GPIO.LOW)
  time.sleep(0.01)

while True:
  shiftOne(GPIO.HIGH)
  time.sleep(0.5)
  shiftOne(GPIO.LOW)
  time.sleep(0.5)
