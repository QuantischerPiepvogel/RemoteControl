import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setup(18, GPIO.OUT) #Clock
GPIO.setup(16, GPIO.OUT) #Latch
GPIO.setup(12, GPIO.OUT) #Data
GPIO.setup(33, GPIO.IN)


def addRGB(r, g, b):
  shiftOne(b)
  time.sleep(0.01)
  shiftOne(g)
  time.sleep(0.01)
  shiftOne(r)
  time.sleep(0.01)

def refresh():
  GPIO.output(16, GPIO.HIGH)
  GPIO.output(16, GPIO.LOW)

def shiftOne(bool):
  GPIO.output(12, bool)
  GPIO.output(18, GPIO.HIGH)
  time.sleep(0.001)
  GPIO.output(18, GPIO.LOW)

while GPIO.input(33) == GPIO.LOW:
  addRGB(0,0,0)
  refresh()
  time.sleep(1)
  addRGB(1,0,0)
  refresh()
  time.sleep(1)
  addRGB(0,1,0)
  refresh()
  time.sleep(1)
  addRGB(0,0,1)
  refresh()
  time.sleep(1)
  addRGB(1,1,0)
  refresh()
  time.sleep(1)
  addRGB(0,1,1)
  refresh()
  time.sleep(1)
  addRGB(1,0,1)
  refresh()
  time.sleep(1)
  addRGB(1,1,1)
  refresh()
  time.sleep(1)

  #shiftOne(GPIO.HIGH)
  #shiftOne(GPIO.LOW)
  #refresh()
  #time.sleep(0.1)
  #shiftOne(GPIO.LOW)
  #refresh()
  #time.sleep(0.1)

print("STOPPED")
