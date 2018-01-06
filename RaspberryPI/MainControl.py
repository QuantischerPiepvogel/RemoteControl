import thread
import Tkinter as tk
import os

print("RemoteControl.py was sucessfully started")
#cool
def software_exit(*args):
  
  exit()
  
def software_update(*args):
  
  thread.start_new_thread(os.system, ("sudo python RaspberryPI/Updater.py",))
  exit()
  
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
