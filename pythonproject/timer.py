# Import necessary modules
from threading import Timer
import time
import tkinter as tk
from tkinter import *
from datetime import datetime

import winsound

# Creating a window
window = Tk()
window.geometry('600x600')  # Set window size
window.title('PythonGeeks')  # Set title

head = Label(window, text="Countdown Clock and Timer", font=('Calibri', 15))
head.pack(pady=20)

# Define variables
hour = StringVar()
minute = StringVar()
second = StringVar()
count = IntVar()
check = IntVar()

# Labels and Entry fields
Label(window, text="Enter time in HH:MM:SS", font=('bold')).pack()
Entry(window, textvariable=hour, width=30).pack()
Entry(window, textvariable=minute, width=30).pack()
Entry(window, textvariable=second, width=30).pack()

# Checkbox
Checkbutton(window, text='Check for Music', variable=check).pack()

# Label for countdown display
countdown_label = Label(window, text="", font=('bold', 20))
countdown_label.pack()

# Function to handle countdown
def countdown():
    try:
        # Convert input time to seconds
        t = int(hour.get()) * 3600 + int(minute.get()) * 60 + int(second.get())
        
        while t >= 0:
            mins, secs = divmod(t, 60)
            display = f'{mins:02d}:{secs:02d}'
            
            countdown_label.config(text=display)  # Update label
            window.update()
            time.sleep(1)
            
            t -= 1

        countdown_label.config(text="Time-Up")
        
        # Display notification
        toast = ToastNotifier()
        toast.show_toast("Notification", "Timer is Off", duration=5, threaded=True)

        # Play beep sound if checked
        if check.get() == 1:
            winsound.Beep(440, 1000)

    except ValueError:
        countdown_label.config(text="Invalid Input!")

# Button to start countdown
Button(window, text="Set Countdown", command=countdown, bg='yellow').place(x=260, y=230)

# Display current time
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
Label(window, text=f"Current Time: {current_time}", font=('bold', 12)).pack()

# Run main loop
window.mainloop()
