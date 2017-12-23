import Tkinter as tk
import os

print("RemoteControl.py was sucessfully started")

def software_exit():
  
  software_update()
  exit()
  
  #if messagebox.askokcancel("Question","Do you want to update the program before closing?"):
    
    #software_update()
    
  #else:
    
    #if messagebox.askokcancel("Question","Do you really want to close the program?"):
    
      #exit()
  
def software_update():
  
  os.system("sudo python RaspberryPI/Updater.py")
  exit()
  
  #if messagebox.askokcancel("Question","Do you really want to update the program?"):
    
    
    #os.system("sudo python RaspberryPI/Updater.py")
    
    #exit()

#class FullScreenApp(object):
    #def __init__(self, master, **kwargs):
        #self.master=master
        #pad=3
        #self._geom='200x200+0+0'
        #master.geometry("{0}x{1}+0+0".format(
            #master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
        #master.bind('<Escape>',self.toggle_geom)            
    #def toggle_geom(self,event):
        #geom=self.master.winfo_geometry()
        #print(geom,self._geom)
        #self.master.geometry(self._geom)
        #self._geom=geom
  
root = tk.Tk()
root.title("MainControl")
root.bind('<Escape>',software_exit)
#app=FullScreenApp(root)
root.bind
#root.attributes('-fullscreen', True)
root.mainloop()
#frame.pack()

#frame.width = 100
#frame.height = 100

#bottomframe = Frame(root)
#bottomframe.pack( side = BOTTOM )

#exit_button = Button(frame, text="X", fg="black", command="software_exit()", width=50, height=50)
#exit_button.place(10, 10)

#update_button = Button(frame, text="U", fg="black", command="software_update()", width=50, height=50)
#update_button.place(60, 10)

#root.mainloop()

print("RemoteControl.py was sucessfully started")
