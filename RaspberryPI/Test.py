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

LEDValues = [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0]

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
fadetime = 1530

while GPIO.input(33) == GPIO.LOW:
  
  print(counter)
  
  for l in range(0, 255):
    
    for g in range(0, 8):
      
      if counter <= 255:
        
        LEDValues[g*3+1] = 0
        LEDValues[g*3+2] = 0
        
        if l <= counter:
          
          LEDValues[g*3] = 1
          
        else:
          
          LEDValues[g*3] = 0
          
      elif counter <= 510:
        
        LEDValues[g*3] = 255
        LEDValues[g*3+2] = 0
        
        if l+255 <= counter:
          
          LEDValues[g*3+1] = 255
          
        else:
          
          LEDValues[g*3+1] = 0
          
      elif counter <= 765:
        
        LEDValues[g*3+1] = 255
        LEDValues[g*3+2] = 0
        
        if l+765 >= counter:
          
          LEDValues[g*3] = 1
          
        else:
          
          LEDValues[g*3] = 0
        
    writeRow(LEDValues)
    time.sleep(0.00005)
    
  
  #writeRow(GRUEN)
  #time.sleep(0.01*counter/fadetime)
  #writeRow(ROT)
  #time.sleep(0.01*(fadetime-counter)/fadetime)
    
  counter += 1
  
  if counter > fadetime:
    
    counter = 0;

print("STOPPED")
