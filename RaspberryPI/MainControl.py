import thread
import Tkinter as tk
import os
import smbus
import time

bus = smbus.SMBus(1)
ARDUINO_ADDR = 0x15
running = True

print("RemoteControl.py was sucessfully started")
#cool
def software_exit(*args):
  running = False
  os.system("sudo python RaspberryPI/Startup.py")
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

root = tk.Tk()
root.title("MainControl")
root.bind('<F4>',software_exit) #http://effbot.org/tkinterbook/tkinter-events-and-bindings.htm    key bindings
root.bind('<F5>',software_update)
root.attributes('-fullscreen', True)
root.mainloop()

exit_button = Button(root, text="X", fg="black", command="software_exit", width=50, height=50)
exit_button.place(10, 10)

#update_button = Button(frame, text="U", fg="black", command="software_update()", width=50, height=50)
#update_button.place(60, 10)
