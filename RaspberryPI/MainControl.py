import thread
import Tkinter as tk
import os

print("RemoteControl.py was sucessfully started")

def software_exit(*args):
  
  exit()
  
def software_update(*args):
  
  thread.start_new_thread(os.system, ("sudo python RaspberryPI/Updater.py",))
  exit()
  
root = tk.Tk()
root.title("MainControl")
root.bind('<Escape>',software_exit)
root.bind('<Enter>',software_update)
root.bind
root.attributes('-fullscreen', fullscreen)
root.mainloop()

#frame.width = 100
#frame.height = 100

#bottomframe = Frame(root)
#bottomframe.pack( side = BOTTOM )

#exit_button = Button(frame, text="X", fg="black", command="software_exit()", width=50, height=50)
#exit_button.place(10, 10)

#update_button = Button(frame, text="U", fg="black", command="software_update()", width=50, height=50)
#update_button.place(60, 10)
