# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 09:36:06 2023

@author: Celine
"""

import win32api, win32con
import sched, time, os


# Specify the duration of the programme
duration_hour = 10


# define the lag for each loop, here is every 9.5 minutes
time_lag = 4.5

# Transform the time lag under secs
routine = int(time_lag*60)

# Transform the end time under seconds
secs = time.time() + duration_hour*60*60

# Define how many rounds of the programme
time_end = int((secs-time.time())/routine)+1


# Define the Start time
starttime = time.time()
x = 0

# Point out the times active 'ctrl'
y = 0

# Show the starting information
print("Program will run:", time_end, "times | Start at:", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),"| End estimated at:",time.strftime("%Y-%m-%d %H:%M:%S", 
      time.localtime(secs)),"| Program duration:", duration_hour, "hours", sep=" ")


for x in range(0, time_end):
    current_posit = win32api.GetCursorPos()
    
    # win32api.SetCursorPos((current_posit[0] + 100 ,current_posit[1] + 1))
    # win32api.SetCursorPos((current_posit[0] - 100 ,current_posit[1] + 1))
    
        
    time.sleep(routine)
    
    if current_posit == win32api.GetCursorPos() or x == 0:
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,current_posit[0],current_posit[1],0,0)
        y = y + 1
    
    x = x + 1
    
    print("N:",x,"|Active times:", y,"times |Program active pct", int((y/x) * 100),"% |Time now:",time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
          "|Time passed:",int(((time.time()-starttime)/60)/60),"h",int(((time.time()-starttime)/60)%60),"m",int((time.time()-starttime)%60),"|Your Working time around: ", 
          (x-y+1)*time_lag, "mins |Program working time around:", y*time_lag, "mins", sep = " ")

print("Program runs:",x,"times | Program active times: ", y, "times | Activity pct", int((1-y/x) * 100),"% | End Time:",time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
      " | Total time passed:",int(((time.time()-starttime)/60)/60),"h",int(((time.time()-starttime)/60)%60),"m",int((time.time()-starttime)%60), " | Your Working hour around: ", 
      int((x-y+1)*time_lag/60), "hours | Program working hour around:", duration_hour-int((x-y+1)*time_lag/60), "hours", sep = " ")
