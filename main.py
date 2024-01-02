import tkinter as tk
from PIL import Image, ImageTk
import math
from tkinter import messagebox
import pygame

# Background color of the timer window
background_color = "#2c2f35"

# Text color and font for labels and text displayed
text_color = "#ffce7b"
font_name = "Comfortaa"

# Initialize the timer variable (will store the timer's current state)
timer = None

# Initialize the reps variable (will keep track of timer cycles)
reps = 0

# Initialize the sound mixer
pygame.mixer.init()

class MainApplication(tk.Tk):
    """
    This class represents the main application of the timer. It manages the user interface and timer functionality,
    including starting and resetting the timer.
    """
    def __init__(self):
        # Initialize the window and its settings
        tk.Tk.__init__(self)
        self.title("20-20-20 Timer")
        self.config(bg=background_color)

        # Variable to track whether the timer is running or not
        self.timer_running = False

        #  Layout of the timer program with title, timer and buttons
        self.timer_title = tk.Label(text="20-20-20 Timer", fg=text_color, bg=background_color, font=(font_name, 30), padx=220)
        self.timer_title.grid(row=0, column=0, columnspan=3)

        self.timer_label = tk.Label(text="00:00", fg=text_color, bg=background_color, font=(font_name, 25))
        self.timer_label.grid(row=2, column=0, columnspan=3, pady=30)

        # Button that will start the timer
        self.start_button = tk.Button(text="Start", highlightthickness=0, bg="#d0ed87", command=self.start_timer)
        self.start_button.grid(row=3, column=0, pady=10)

        # To get space between the buttons and be able to center the eye image
        self.space_label = tk.Label(bg=background_color)
        self.space_label.grid(row=3, column=1, pady=10)

        # Button that will reset the timer
        self.reset_button = tk.Button(text="Reset", highlightthickness=0, bg="#c63958", command=self.reset_timer)
        self.reset_button.grid(row=3, column=2, pady=10)

        # An image of a eye
        self.eye_image_open = Image.open("eye.png")
        self.eye_image = ImageTk.PhotoImage(self.eye_image_open)
        self.eye = tk.Label(image=self.eye_image, bg=background_color)
        self.eye.image = self.eye_image
        self.eye.grid(row=3, column=1, pady=20)

    def play(self):
        # To play notification at pop-up
        pygame.mixer.music.load("notification.mp3")
        pygame.mixer.music.play(loops=0)
    def count_down(self, count):
        # Calculate minutes and seconds
        count_min = math.floor(count / 60)
        count_sec = count % 60

        # Formatting where the seconds are displayed with leading zeros
        if count_sec < 10:
            count_sec = f"0{count_sec}"

        # Update the timer label to show the countdown time
        self.timer_label.config(text=f"{count_min}:{count_sec}")

        if count > 0:
            # To keep track of the timer
            global timer
            # Schedule the countdown for the next second
            timer = self.after(1000, self.count_down, count - 1)
        else:
            # Start a new timer cycle when the countdown reaches zero
            self.start_timer()


    def start_timer(self):
        # Variable to track timer cycles (work and break)
        global reps
        reps += 1

        # Durations of work and break time
        work_min = 1
        global work_sec
        work_sec = work_min * 60
        global break_sec
        break_sec = 20

        # Check what cycle it is and start countdown accordingly
        #  The first rep is always work and countdown of work time will start
        if reps == 1:
            self.count_down(work_sec)
        # Inequal reps are work cycles
        elif reps % 2 != 0:
            # Message that pops up when break is done
            if messagebox.askokcancel("Timer", "Break is up, time to work!"):
                # Countdown of work time will start
                self.count_down(work_sec)
        # Equal reps are break cycles
        else:
            # Play the notification sound
            self.play()
            # Message that pops up when work is done
            if messagebox.askokcancel("Timer", "Work time is up, look away for 20 seconds!"):
                # Countdown of break time will start
                self.count_down(break_sec)

    def reset_timer(self):
        # Cancel the current countdown if there is any
        self.after_cancel(timer)
        # Restore timer label back to 00:00
        self.timer_label.config(text="00:00")
        # Reset the total cycles to 0
        global reps
        reps = 0


if __name__ == "__main__":
    # Create an instance of the MainApplication class and start the main event loop
    app = MainApplication()
    app.mainloop()
