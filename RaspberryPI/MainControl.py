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
except BaseException as e:
  print("loool didnt work")

ARDUINO_ADDR = 0x15
running = True

class App:

  def __init__(self, master):
    frame = Frame(master)
    frame.pack()
    print("TestERUS")
    self.tilt_value_text = StringVar()
    self.pan_value_text = StringVar()
    self.rot_value_text = StringVar()
    self.button_value_text = StringVar()
    self.directRight_value_text = StringVar()
    self.directLeft_value_text = StringVar()
    self.powerRight_value_text = StringVar()
    self.powerLeft_value_text = StringVar()
    self.reverseRight_value_text = StringVar()
    self.reverseLeft_value_text = StringVar()
    
    
    self.exit_button = Button(root, text="X", fg="black", command=software_exit, width=1, height=1)
    self.exit_button.place(x=70, y=10)
    self.update_button = Button(root, text="U", fg="black", command=software_update, width=1, height=1)
    self.update_button.place(x=10, y=10)
    self.tilt_value = Label(root, height=1, width=4, textvariable = self.tilt_value_text)
    self.tilt_value.place(x=10, y=200)
    
    self.pan_value = Label(root, height=1, width=4, textvariable = self.pan_value_text)
    self.pan_value.place(x=70, y=200)
    
    self.rot_value = Label(root, height=1, width=4, textvariable = self.rot_value_text)
    self.rot_value.place(x=10, y=150)
    
    self.button_value = Label(root, height=1, width=4, textvariable = self.button_value_text)
    self.button_value.place(x=70, y=150)
    try:
      value = bus.read_byte(I2C_Arduino_Joystick)
    except BaseException as e:
      value = "ERR"
    self.tilt_value_text.set(value)

print("RemoteControl.py was sucessfully started")

def software_exit(*args):
  running = False
  thread.start_new_thread(os.system, ("sudo python RaspberryPI/Startup.py",))
  exit()
  
def software_update(*args):
  running = False
  thread.start_new_thread(os.system, ("sudo python RaspberryPI/Updater.py",))
  exit()


def getData(reg):
  value = 0
  try:
      bus.write_byte(I2C_Arduino_Joystick, reg)
      value = bus.read_byte(I2C_Arduino_Joystick)
    except BaseException as e:
      value = "ERR"
   return value


def workerThread():
  #global bus, I2C_Arduino_Joystick
  print("Blupsebaer")
  while 1:
    app.tilt_value_text.set(getData(0))
    app.pan_value_text.set(getData(1))
    app.button_value_text.set(getData(2))
    app.rot_value_text.set(getData(3))
    #app.tilt_value_text.set(getData(6))
    time.sleep(0.1)
    
root = Tk()
app = App(root)
root.title("MainControl")
root.config(bg="green")
root.bind('<F4>',software_exit) #http://effbot.org/tkinterbook/tkinter-events-and-bindings.htm    key bindings
root.bind('<F5>',software_update)
root.attributes('-fullscreen', True)

thread.start_new_thread(workerThread,())


root.mainloop()





