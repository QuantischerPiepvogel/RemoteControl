# info: https://www.youtube.com/watch?v=FV7eiqN01hc

import os, thread

os.system("git pull")
print("RemoteControl was updated")
thread.start_new_thread(os.system, ("sudo python RaspberryPI/MainControl.py",))
exit()
