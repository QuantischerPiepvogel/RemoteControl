from Tkinter import *
import os

def software_exit():
  
  if messagebox.askokcancel("Question","Do you really want to close the program?"):
    
    exit()
  
def software_update():
  
  if messagebox.askokcancel("Question","Do you really want to update the program?"):
    
    
    os.system("cd RemoteControl")
    os.system("sudo python Updater.py")
    
    exit()
  

root = Tk()
frame = Frame(root)
frame.pack()

bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM )

exit_button = Button(frame, text="X", fg="black", command="software_exit()")
#exit_button.command(software_exit())
exit_button.width(50)
exit_button.height(50)
exit_button.place(10, 10)

update_button = Button(frame, text="U", fg="black", command="software_update()")
#update_button.command(software_update())
update_button.width(50)
update_button.height(50)
update_button.place(60, 10)

root.mainloop()

print("RemoteControl.py was sucessfully started")
