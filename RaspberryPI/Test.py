import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setup(18, GPIO.OUT) #Clock
GPIO.setup(16, GPIO.OUT) #Latch
GPIO.setup(12, GPIO.OUT) #Data
GPIO.setup(33, GPIO.IN)

def writeRow(values):
  
  for led in range(0, len(values)):
    
    shiftOne(values[len(values)-1-led])
    
  refresh()

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
  GPIO.output(18, GPIO.LOW)

#LEDValues = [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0]

AUS     = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
ROT     = [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0]
GELB    = [1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0]
GRUEN   = [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0]
CYAN    = [0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1]
BLAU    = [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1]
MAGENTA = [1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1]
WEISS   = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

sleeptime = 0.5
counter = 0

while GPIO.input(33) == GPIO.LOW:
  
  for t in range(0, 1000):
    
    writeRow(ROT)
    time.sleep(0.0001*t)
    writeRow(GRUEN)
    time.sleep(0.0001*(100-t))
    
  counter += 1
  
  if counter > 100:
    
    counter = 0;

print("STOPPED")
