import thread
from Tkinter import *
import os
import smbus
import time
import smbus


bus = smbus.SMBus(1)
I2C_Arduino_Joystick = 0x08
I2C_Arduino_Non_Joystick = 0x09
try:

  bus.write_byte(I2C_Arduino_Joystick, 0xFF)
  bus.write_byte(I2C_Arduino_Non_Joystick, 0xFF)

except BaseException as e:
  
  print("loool didnt work")

ARDUINO_ADDR = 0x15
running = True

class App:
  def __init__(self, master):
    frame = Frame(master)
    frame.pack()
    self.exit_button = Button(root, text="X", fg="black", command=software_exit, width=1, height=1)
    self.exit_button.place(x=70, y=10)
    self.update_button = Button(root, text="U", fg="black", command=software_update, width=1, height=1)
    self.update_button.place(x=10, y=10)
    self.tilt_value = Text(root, height=2, width=4)
    self.tilt_value.place(x=10, y=100)
    self.tilt_value.insert(END, "tilt\n")
    try:
      value = bus.read_byte(I2C_Arduino_Non_Joystick)
    except BaseException as e:
      value = "ERR"
    self.tilt_value.insert(END,  value)

print("RemoteControl.py was sucessfully started")

def software_exit(*args):
  running = False
  thread.start_new_thread(os.system, ("sudo python RaspberryPI/Startup.py",))
  exit()
  
def software_update(*args):
  running = False
  thread.start_new_thread(os.system, ("sudo python RaspberryPI/Updater.py",))
  exit()

def workerThread(*args):
  global bus, ARDUINO_ADDR
  while running:
    bus.write_byte(ARDUINO_ADDR, 10)
    pan = bus.read_byte_data(ARDUINO_ADDR)
    bus.write_byte(ARDUINO_ADDR, 11)
    tilt = bus.read_byte_data(ARDUINO_ADDR)
    bus.write_byte(ARDUINO_ADDR, 12)
    bus.write_byte(ARDUINO_ADDR, tilt)
    time.sleeep(0.1)

root = Tk()
app = App(root)
root.title("MainControl")
root.config(bg="green")
root.bind('<F4>',software_exit) #http://effbot.org/tkinterbook/tkinter-events-and-bindings.htm    key bindings
root.bind('<F5>',software_update)
root.attributes('-fullscreen', True)
root.mainloop()
