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
    self.var_directRight_value = 0
    self.var_directLeft_value = 0
    self.var_powerRight_value = 0
    self.var_powerLeft_value = 0
    self.var_reverseRight_value = 0
    self.var_reverseLeft_value = 0
    

    self.taskbar = Frame(self.frame)
    self.taskbar.config(bg=rgb2hex(38, 38, 38), highlightbackground=rgb2hex(38, 38, 38), width=1024, height=34)
    self.taskbar.grid(row=0, column=0, sticky=(N, S, E, W))
    self.taskbar.isgridded = True
    self.taskbar.columnconfigure(1, weight=1)

    self.home_button = Button(self.taskbar, image=self.home_icon, command=go_home)
    self.home_button.grid(row=0, column=0, sticky=(E, W))
    self.home_button.config(width=34, height=34)
    self.home_button.config(bg=rgb2hex(38, 38, 38), highlightbackground=rgb2hex(60, 60, 60), relief=FLAT, activebackground=rgb2hex(38, 38, 38), borderwidth = 0)

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

    self.joystick_visual = Canvas(self.home, width=300, height=300)
    self.joystick_visual.grid(row = 0, column = 0, sticky = (N, W))
    self.joystick_visual.config(bg=rgb2hex(60, 60, 60), borderwidth=0, highlightthickness=0, relief=RIDGE)

    self.joystick_visual_densicolor = PhotoImage(file="RaspberryPI/images/Home/JoystickGraphDensityColor.png")
    self.joystick_visual_background = PhotoImage(file="RaspberryPI/images/Home/JoystickGraphBackground.png")
    self.joystick_visual_graph_head = PhotoImage(file="RaspberryPI/images/Home/JoystickGraphHead.png")
    self.joystick_visual_buttondown = PhotoImage(file="RaspberryPI/images/Home/JoystickGraphButtonDown.png")
    
    self.i0 = self.joystick_visual.create_image(0, 0, anchor=NW, image=self.joystick_visual_densicolor)
    
    self.r1 = self.joystick_visual.create_rectangle(99, 4, 150, 20, fill=rgb2hex(60, 60, 60),outline=rgb2hex(60, 60, 60))
    self.r2 = self.joystick_visual.create_rectangle(150, 4, 200, 20, fill=rgb2hex(60, 60, 60),outline=rgb2hex(60, 60, 60))

    self.r3 = self.joystick_visual.create_rectangle(279, 99, 296, 150, fill=rgb2hex(60, 60, 60),outline=rgb2hex(60, 60, 60))
    self.r4 = self.joystick_visual.create_rectangle(279, 150, 296, 200, fill=rgb2hex(60, 60, 60),outline=rgb2hex(60, 60, 60))

    self.a1 = self.joystick_visual.create_arc(36, 36, 263, 263, start=90, extent=100, fill=rgb2hex(60, 60, 60),outline=rgb2hex(60, 60, 60))
    self.a2 = self.joystick_visual.create_arc(36, 36, 263, 263, start=350, extent=100, fill=rgb2hex(60, 60, 60),outline=rgb2hex(60, 60, 60))
    
    self.i1 = self.joystick_visual.create_image(0, 0, anchor=NW, image=self.joystick_visual_background)
    self.i2 = self.joystick_visual.create_image(0, 0, anchor=NW,image=self.joystick_visual_graph_head)
    
    self.tilt_value = Label(self.sensors, height=1, width=8, textvariable=self.tilt_value_text, anchor=(W))
    self.tilt_value.place(x=10, y=40)

    self.pan_value = Label(self.sensors, height=1, width=8, textvariable=self.pan_value_text, anchor=(W))
    self.pan_value.place(x=82, y=40)

    self.rot_value = Label(self.sensors, height=1, width=8, textvariable=self.rot_value_text, anchor=(W))
    self.rot_value.place(x=10, y=10)

    self.button_value = Label(self.sensors, height=1, width=8, textvariable=self.button_value_text, anchor=(W))
    self.button_value.place(x=82, y=10)
    
    self.directRight_value = Label(self.sensors, height=1, width=8, textvariable=self.directRight_value_text, anchor=(W))
    self.directRight_value.place(x=82, y=70)
    
    self.directLeft_value = Label(self.sensors, height=1, width=8, textvariable=self.directLeft_value_text, anchor=(W))
    self.directLeft_value.place(x=10, y=70)
    
    self.powerRight_value = Label(self.sensors, height=1, width=8, textvariable=self.powerRight_value_text, anchor=(W))
    self.powerRight_value.place(x=82, y=100)
    
    self.powerLeft_value = Label(self.sensors, height=1, width=8, textvariable=self.powerLeft_value_text, anchor=(W))
    self.powerLeft_value.place(x=10, y=100)
    
    self.reverseRight_value = Label(self.sensors, height=1, width=8, textvariable=self.reverseRight_value_text, anchor=(W))
    self.reverseRight_value.place(x=82, y=130)
    
    self.reverseLeft_value = Label(self.sensors, height=1, width=8, textvariable=self.reverseLeft_value_text, anchor=(W))
    self.reverseLeft_value.place(x=10, y=130)

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

def getData(reg, addr):
  value = 0
  try:
    bus.write_byte(addr, reg)
    value = bus.read_byte(addr)
  except BaseException as e:
    value = "ERR"
  return value


def workerThread():
  
  while running:
    try:
      app.var_tilt_value = getData(0, I2C_Arduino_Joystick)
      app.var_pan_value = getData(1, I2C_Arduino_Joystick)
      app.var_button_value = getData(3, I2C_Arduino_Joystick)
      app.var_rot_value = getData(2, I2C_Arduino_Joystick)
      app.var_directRight_value = getData(2, I2C_Arduino_Joystick)
      app.var_directLeft_value = getData(2, I2C_Arduino_Non_Joystick)
      app.var_powerRight_value = getData(2, I2C_Arduino_Joystick)
      app.var_powerLeft_value = getData(2, I2C_Arduino_Non_Joystick)
      app.var_reverseRight_value = getData(2, I2C_Arduino_Joystick)
      app.var_reverseLeft_value = getData(2, I2C_Arduino_Non_Joystick)
    except:
      print('Unexpected error:', sys.exc_info()[0])
      
    try:
      app.tilt_value_text.set("tilt: " + str(app.var_tilt_value))
      app.pan_value_text.set("pan: " + str(app.var_pan_value))
      app.button_value_text.set("button: " + str(app.var_button_value))
      app.rot_value_text.set("rot: " + str(app.var_rot_value))
      app.directRight_value_text.set("dr: " + str(app.var_directRight_value))
      app.directLeft_value_text.set("dl: " + str(app.var_directLeft_value))
      app.powerRight_value_text.set("pr: " + str(app.var_powerRight_value))
      app.powerLeft_value_text.set("pl: " + str(app.var_powerLeft_value))
      app.reverseRight_value_text.set("rr: " + str(app.var_reverseRight_value))
      app.reverseLeft_value_text.set("rl: " + str(app.var_reverseLeft_value))
    except:
      print('Unexpected error:', sys.exc_info()[0])
      
    try:
      w = app.var_tilt_value
      if w > 50:
        w = 50
      app.joystick_visual.coords(app.r1, 99, 4, 100 + w, 20)
    except:
      print('Unexpected error:', sys.exc_info()[0])
      
    try:
      w = 100 - app.var_tilt_value
      if w > 50:
        w = 50
      app.joystick_visual.coords(app.r2, 200 - w, 4, 200, 20)
    except:
      print('Unexpected error:', sys.exc_info()[0])
      
    try:
      w = 100 - app.var_pan_value
      if w > 50:
        w = 50
      app.joystick_visual.coords(app.r3, 279, 99, 296, 100 + w)
    except:
      print('Unexpected error:', sys.exc_info()[0])
      
    try:
      w = app.var_pan_value
      if w > 50:
        w = 50
      app.joystick_visual.coords(app.r4, 279, 200 - w, 296, 200)
    except:
      print('Unexpected error:', sys.exc_info()[0])
      
    try:
      w = app.var_rot_value * 2
      if w > 100:
        w = 100
      app.joystick_visual.itemconfigure(app.a1, start=190 - w, extent=w)
    except:
      print('Unexpected error:', sys.exc_info()[0])
      
    try:
      w = 200 - (app.var_rot_value * 2)
      if w > 100:
        w = 100
      app.joystick_visual.itemconfigure(app.a2, start=350, extent=w)
    except:
      print('Unexpected error:', sys.exc_info()[0])
      
    try:
      if app.var_button_value < 50:
        app.joystick_visual.itemconfigure(app.i2, image=app.joystick_visual_graph_head)
      else:
        app.joystick_visual.itemconfigure(app.i2, image=app.joystick_visual_buttondown)
      app.joystick_visual.coords(app.i2, app.var_tilt_value - 50, 50 - app.var_pan_value)
    except:
      print('Unexpected error:', sys.exc_info()[0])
      
    try:
      bus.write_byte(I2C_Arduino_Joystick, 11)
      bus.write_byte(I2C_Arduino_Joystick, app.var_pan_value)
      bus.write_byte(I2C_Arduino_Joystick, 12)
      bus.write_byte(I2C_Arduino_Joystick, app.var_pan_value)
    except:
      print('Unexpected error:', sys.exc_info()[0])
    time.sleep(0.05)
    
    
root = Tk()
app = App(root)
root.title("MainControl")
root.bind('<F4>',software_exit) #http://effbot.org/tkinterbook/tkinter-events-and-bindings.htm    key bindings
root.bind('<F5>',software_update)
root.attributes('-fullscreen', True)

thread.start_new_thread(workerThread,())

root.mainloop()
