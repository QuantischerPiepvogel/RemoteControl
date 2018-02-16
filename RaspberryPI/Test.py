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

RGB = [0, 0, 0]

sleeptime = 0.0025
counter = 0
fadetime = 1530

while GPIO.input(33) == GPIO.LOW:
  
  print(counter)    
  
  if counter <= 255:
    RGB[0] = 255
    RGB[1] = counter
    RGB[2] = 0
  elif counter <= 510:
    RGB[0] = 510-counter
    RGB[1] = 255
    RGB[2] = 0
  elif counter <= 765:
    RGB[0] = 0
    RGB[1] = 255
    RGB[2] = counter-510
  elif counter <= 1020:
    RGB[0] = 0
    RGB[1] = 1020-counter
    RGB[2] = 255
  elif counter <= 1275:
    RGB[0] = counter-1020
    RGB[1] = 0
    RGB[2] = 255
  elif counter <= 1530:
    RGB[0] = 255
    RGB[1] = 0
    RGB[2] = 1530-counter
  
  RGB[0] = RGB[0]*2
  
  
  writeRow(ROT)
  time.sleep(sleeptime*RGB[0]/(RGB[0]+RGB[1]+RGB[2]))
  writeRow(GRUEN)
  time.sleep(sleeptime*RGB[1]/(RGB[0]+RGB[1]+RGB[2]))
  writeRow(BLAU)
  time.sleep(sleeptime*RGB[2]/(RGB[0]+RGB[1]+RGB[2]))
  writeRow(ROT)
  time.sleep(sleeptime*RGB[0]/(RGB[0]+RGB[1]+RGB[2]))
  writeRow(GRUEN)
  time.sleep(sleeptime*RGB[1]/(RGB[0]+RGB[1]+RGB[2]))
  writeRow(BLAU)
  time.sleep(sleeptime*RGB[2]/(RGB[0]+RGB[1]+RGB[2]))
  writeRow(ROT)
  time.sleep(sleeptime*RGB[0]/(RGB[0]+RGB[1]+RGB[2]))
  writeRow(GRUEN)
  time.sleep(sleeptime*RGB[1]/(RGB[0]+RGB[1]+RGB[2]))
  writeRow(BLAU)
  time.sleep(sleeptime*RGB[2]/(RGB[0]+RGB[1]+RGB[2]))
  writeRow(ROT)
  time.sleep(sleeptime*RGB[0]/(RGB[0]+RGB[1]+RGB[2]))
  writeRow(GRUEN)
  time.sleep(sleeptime*RGB[1]/(RGB[0]+RGB[1]+RGB[2]))
  writeRow(BLAU)
  time.sleep(sleeptime*RGB[2]/(RGB[0]+RGB[1]+RGB[2]))
    
  counter += 1
  
  if counter > fadetime:
    
    counter = 0;

print("STOPPED")
