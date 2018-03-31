import thread
from Tkinter import *
import os
import smbus
import time
import smbus

running = True

bus = smbus.SMBus(1)
I2C_Arduino_Joystick = 0x08
I2C_Arduino_Non_Joystick = 0x09
try:
  bus.write_byte(I2C_Arduino_Joystick, 0xFF)
except BaseException as e:
  print("loool didnt work")

def rgb2hex(r,g,b):
  hex = "#{:02x}{:02x}{:02x}".format(r,g,b)
  return hex
  
class App:

  def __init__(self, master):
    
    self.frame = Frame(master)
    self.frame.pack()
    self.frame.config(bg=rgb2hex(60, 60, 60))
    self.frame.columnconfigure(0, weight=1, minsize=1024)
    self.frame.rowconfigure(0, weight=1, minsize=36)
    self.frame.rowconfigure(1, weight=1, minsize=564)

    
    self.home_icon=PhotoImage(file="RaspberryPI/images/Taskbar/Home_Icon.png")
    self.update_icon=PhotoImage(file="RaspberryPI/images/Taskbar/Update_Icon.png")
    self.exit_icon = PhotoImage(file="RaspberryPI/images/Taskbar/Exit_Icon.png")
    self.settings_icon = PhotoImage(file="RaspberryPI/images/Taskbar/Settings_Icon.png")
    self.sensors_icon = PhotoImage(file="RaspberryPI/images/Taskbar/Sensors_Icon.png")

    
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

    
    self.var_tilt_value = 0
    self.var_pan_value = 0
    self.var_rot_value = 0
    self.var_button_value = 0
    

    self.taskbar = Frame(self.frame)
    self.taskbar.config(bg=rgb2hex(38, 38, 38), highlightbackground=rgb2hex(38, 38, 38), width=1024, height=34)
    self.taskbar.grid(row=0, column=0, sticky=(N, S, E, W))
    self.taskbar.isgridded = True
    self.taskbar.columnconfigure(1, weight=1)

    self.home_button = Button(self.taskbar, image=self.home_icon, command=go_home)
    self.home_button.grid(row=0, column=0, sticky=(E, W))
    self.home_button.config(width=34, height=34)
    self.home_button.config(bg=rgb2hex(104, 104, 104), highlightbackground=rgb2hex(60, 60, 60), relief=FLAT, activebackground=rgb2hex(38, 38, 38), borderwidth = 0)

    self.sensors_button = Button(self.taskbar, image=self.sensors_icon, command=go_sensors)
    self.sensors_button.grid(row=0, column=1, sticky=(W))
    self.sensors_button.config(width=102, height=34)
    self.sensors_button.config(bg=rgb2hex(104, 104, 104), highlightbackground=rgb2hex(60, 60, 60), relief=FLAT,activebackground=rgb2hex(38, 38, 38), borderwidth=0)

    self.update_button = Button(self.taskbar, image=self.update_icon, command=software_update)
    self.update_button.grid(row=0, column=101, sticky=(E))
    self.update_button.config(width=34, height=34)
    self.update_button.config(bg=rgb2hex(104, 104, 104), highlightbackground=rgb2hex(60, 60, 60), relief=FLAT,activebackground=rgb2hex(38, 38, 38), borderwidth=0)

    self.settings_button = Button(self.taskbar, image=self.settings_icon, command=go_settings)
    self.settings_button.grid(row=0, column=102, sticky=(E))
    self.settings_button.config(width=34, height=34)
    self.settings_button.config(bg=rgb2hex(104, 104, 104), highlightbackground=rgb2hex(60, 60, 60), relief=FLAT,activebackground=rgb2hex(38, 38, 38), borderwidth=0)

    self.exit_button = Button(self.taskbar, image=self.exit_icon,command=software_exit)
    self.exit_button.grid(row=0, column=103, sticky=(E))
    self.exit_button.config(width=34, height=34)
    self.exit_button.config(bg=rgb2hex(104, 104, 104), highlightbackground=rgb2hex(60, 60, 60), relief=FLAT,activebackground=rgb2hex(38, 38, 38), borderwidth=0)

    
    self.home = Frame(self.frame)
    self.home.isgridded = True
    self.home.grid(row=1, column=0, sticky=(N, S, E, W))
    self.home.config(bg=rgb2hex(60, 60, 60))

    self.sensors = Frame(self.frame)
    self.sensors.isgridded = False
    self.sensors.config(bg=rgb2hex(60, 60, 60))

    self.settings = Frame(self.frame)
    self.settings.isgridded = False
    self.settings.config(bg=rgb2hex(60, 60, 60))

    
    self.tilt_value = Label(self.sensors, height=1, width=8, textvariable=self.tilt_value_text)
    self.tilt_value.place(x=10, y=40)

    self.pan_value = Label(self.sensors, height=1, width=8, textvariable=self.pan_value_text)
    self.pan_value.place(x=82, y=40)

    self.rot_value = Label(self.sensors, height=1, width=8, textvariable=self.rot_value_text)
    self.rot_value.place(x=10, y=10)

    self.button_value = Label(self.sensors, height=1, width=8, textvariable=self.button_value_text)
    self.button_value.place(x=82, y=10)

print("RemoteControl.py was sucessfully started")

def go_home(*args):

  app.home_button.config(bg=rgb2hex(38, 38, 38))
  app.sensors_button.config(bg=rgb2hex(104, 104, 104))
  app.settings_button.config(bg=rgb2hex(104, 104, 104))

  app.home.isgridded = True
  app.home.grid(row=1, column=0, sticky=(N, S, E, W))
  app.sensors.isgridded = False
  app.sensors.grid_forget()
  app.settings.isgridded = False
  app.settings.grid_forget()

def go_settings(*args):

  app.home_button.config(bg=rgb2hex(104, 104, 104))
  app.sensors_button.config(bg=rgb2hex(104, 104, 104))
  app.settings_button.config(bg=rgb2hex(38, 38, 38))

  app.home.isgridded = False
  app.home.grid_forget()
  app.sensors.isgridded = False
  app.sensors.grid_forget()
  app.settings.isgridded = True
  app.settings.grid(row=1, column=0, sticky=(N, S, E, W))

def go_sensors(*args):

  app.home_button.config(bg=rgb2hex(104, 104, 104))
  app.sensors_button.config(bg=rgb2hex(38, 38, 38))
  app.settings_button.config(bg=rgb2hex(104, 104, 104))

  app.home.isgridded = False
  app.home.grid_forget()
  app.sensors.isgridded = True
  app.sensors.grid(row=1, column=0, sticky=(N, S, E, W))
  app.settings.isgridded = False
  app.settings.grid_forget()

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
  while running:
    app.var_tilt_value = getData(0)
    app.var_pan_value = getData(1)
    app.var_button_value = getData(3)
    app.var_rot_value = getData(2)
    
    app.tilt_value_text.set("tilt: " + str(app.var_tilt_value))
    app.pan_value_text.set("pan: " + str(app.var_pan_value))
    app.button_value_text.set("button: " + str(app.var_button_value))
    app.rot_value_text.set("rot: " + str(app.var_rot_value))
    
    time.sleep(0.01)
    
    
root = Tk()
app = App(root)
root.title("MainControl")
root.bind('<F4>',software_exit) #http://effbot.org/tkinterbook/tkinter-events-and-bindings.htm    key bindings
root.bind('<F5>',software_update)
root.attributes('-fullscreen', True)

thread.start_new_thread(workerThread,())

root.mainloop()
