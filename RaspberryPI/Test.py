import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setup(18, GPIO.OUT) #Clock
GPIO.setup(16, GPIO.OUT) #Latch
GPIO.setup(12, GPIO.OUT) #Data


def addRGB(r, g, b):
  shiftOne(r)
  shiftOne(g)
  shiftOne(b)

def refresh():
  GPIO.output(16, GPIO.HIGH)
  GPIO.output(16, GPIO.LOW)

def shiftOne(bool):
  GPIO.output(12, bool)
  GPIO.output(18, GPIO.HIGH)
  GPIO.output(18, GPIO.LOW)

while True:
  shiftOne(GPIO.HIGH)
  time.sleep(0.5)
  shiftOne(GPIO.LOW)
  time.sleep(0.5)
