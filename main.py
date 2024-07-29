import customtkinter
from PIL import Image
import math
import pygame

# Background color of the timer window
background_color = "#2c2f35"

# Text color and font for labels and text displayed
text_color = "#ffce7b"
font_name = "Lexend"

# Initialize the timer variable (will store the timer's current state)
timer = None

# Initialize the reps variable (will keep track of timer cycles)
reps = 0

# Initialize the sound mixer
pygame.mixer.init()


class MainApplication(customtkinter.CTk):
    """
    This class represents the main application of the timer. It manages the user interface and timer functionality,
    including starting and resetting the timer.
    """
    def __init__(self):
        # Initialize the window and its settings
        customtkinter.CTk.__init__(self)
        self.title("20-20-20 Timer")
        self.configure(bg=background_color)
        self.font_title = customtkinter.CTkFont(family=font_name, size=30, weight="bold")
        self.font_timer = customtkinter.CTkFont(family=font_name, size=25, weight="bold")
        self.font_button = customtkinter.CTkFont(family=font_name, size=15, weight="normal")
        self.font_label = customtkinter.CTkFont(family=font_name, size=15, weight="bold")

        # Variable to track whether the timer is running or not
        self.timer_running = False

        #  Layout of the timer program with title, timer and buttons
        self.timer_title = customtkinter.CTkLabel(self, text="20-20-20 Timer", text_color=text_color,
                                                  fg_color="transparent", font=self.font_title, padx=220)
        self.timer_title.grid(row=0, column=0, columnspan=3)

        # Button that will start the timer
        self.timer_label = customtkinter.CTkLabel(self, text="00:00", text_color=text_color, fg_color="transparent",
                                                  font=self.font_timer)
        self.timer_label.grid(row=2, column=0, columnspan=3, pady=30)

        self.start_button = customtkinter.CTkButton(self, text="Start", fg_color="#d0ed87", text_color="#2c2f35",
                                                    command=self.start_timer, width=100, font=self.font_button,
                                                    hover_color="#76c776")
        self.start_button.grid(row=3, column=0, pady=10)

        # To get space between the buttons and be able to center the eye image
        self.space_label = customtkinter.CTkLabel(self, fg_color="transparent")
        self.space_label.grid(row=3, column=1, pady=10)

        # Button that will reset the timer
        self.reset_button = customtkinter.CTkButton(self, text="Reset", fg_color="#c63958", text_color="#2c2f35",
                                                    command=self.reset_timer, width=100, font=self.font_button,
                                                    hover_color="#990000")
        self.reset_button.grid(row=3, column=2, pady=10)

        # An image of an eye
        self.eye_image = customtkinter.CTkImage(light_image=Image.open("eye.png"),
                                                dark_image=Image.open("eye.png"),
                                                size=(80, 80))
        self.eye = customtkinter.CTkLabel(self, image=self.eye_image, text="")
        self.eye.grid(row=3, column=1, pady=20)

    def open_breakwindow(self):
        break_window = customtkinter.CTkToplevel(self)
        break_window.title("BREAK TIME")
        break_window.resizable(False, False)
        break_window.attributes('-topmost', True)
        break_image = customtkinter.CTkImage(light_image=Image.open("Breaktime.png"),
                                             dark_image=Image.open("Breaktime.png"), size=(300, 200))
        break_image_label = customtkinter.CTkLabel(break_window, image=break_image, text="")
        break_image_label.grid(row=0, column=1, pady=20)

        def close_breakwindow():
            break_window.destroy()
            break_window.update()
            self.count_down(break_sec)

        def close_breakwindow_cancel():
            break_window.destroy()
            break_window.update()
            self.reset_timer()

        break_label = customtkinter.CTkLabel(break_window, text="It's break time now! Look away at least 6 "
                                                                "meters away for 20 seconds.", font=self.font_label,
                                             fg_color="transparent", text_color="#F8F8FF")
        break_label.grid(row=1, column=0, columnspan=3)
        breakspace_label = customtkinter.CTkLabel(break_window, fg_color="transparent", text=" ")
        breakspace_label.grid(row=2, column=1, pady=10)
        break_ok_button = customtkinter.CTkButton(break_window, text="OK", command=close_breakwindow,
                                                  text_color="#2c2f35", fg_color="#d0ed87", font=self.font_button,
                                                  hover_color="#76c776", width=100)
        break_ok_button.grid(row=2, column=0, padx=10, pady=10)
        break_cancel_button = customtkinter.CTkButton(break_window, text="CANCEL", command=close_breakwindow_cancel,
                                                      text_color="#2c2f35", fg_color="#c63958", font=self.font_button,
                                                      hover_color="#990000", width=100)
        break_cancel_button.grid(row=2, column=2, padx=10, pady=10)

    def open_workwindow(self):
        work_window = customtkinter.CTkToplevel(self)
        work_window.title("WORK TIME")
        work_window.resizable(False, False)
        work_window.attributes('-topmost', True)
        work_image = customtkinter.CTkImage(light_image=Image.open("Worktime.png"),
                                            dark_image=Image.open("Worktime.png"), size=(300, 200))
        work_image_label = customtkinter.CTkLabel(work_window, image=work_image, text="")
        work_image_label.grid(row=0, column=1, pady=20)

        def close_workwindow():
            work_window.destroy()
            work_window.update()
            self.count_down(work_sec)

        def close_workwindow_cancel():
            work_window.destroy()
            work_window.update()
            self.reset_timer()

        work_label = customtkinter.CTkLabel(work_window, text="Good job! It's work time now!", font=self.font_label,
                                            fg_color="transparent", text_color="#F8F8FF")
        work_label.grid(row=1, column=0, columnspan=3)
        workspace_label = customtkinter.CTkLabel(work_window, fg_color="transparent", text=" ")
        workspace_label.grid(row=2, column=1, pady=10)

        work_ok_button = customtkinter.CTkButton(work_window, text="OK", command=close_workwindow, text_color="#2c2f35",
                                                 fg_color="#d0ed87", font=self.font_button, hover_color="#76c776",
                                                 width=100)
        work_ok_button.grid(row=2, column=0)
        work_cancel_button = customtkinter.CTkButton(work_window, text="CANCEL", command=close_workwindow_cancel,
                                                     text_color="#2c2f35", fg_color="#c63958", font=self.font_button,
                                                     hover_color="#990000", width=100)
        work_cancel_button.grid(row=2, column=2)

    def play(self):
        # To play notification at pop-up
        pygame.mixer.music.load("notificationsound.mp3")
        pygame.mixer.music.play(loops=0)

    def count_down(self, count):
        # Calculate minutes and seconds
        count_min = math.floor(count / 60)
        count_sec = count % 60

        # Formatting where the seconds are displayed with leading zeros
        if count_sec < 10:
            count_sec = f"0{count_sec}"

        # Update the timer label to show the countdown time
        self.timer_label.configure(text=f"{count_min}:{count_sec}")

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
        work_min = 20
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
            # Play the notification sound
            self.play()
            # Makes the application pop up, and you cannot click outside of it
            self.attributes("-topmost", True)
            self.focus_force()
            # Message that pops up when break is done
            self.open_workwindow()
        # Equal reps are break cycles
        else:
            # Play the notification sound
            self.play()
            # Makes the application pop up, and you cannot click outside of it
            self.attributes("-topmost", True)
            self.focus_force()
            # Message that pops up when work is done
            self.open_breakwindow()

    def reset_timer(self):
        # Cancel the current countdown if there is any
        self.after_cancel(timer)
        # Restore timer label back to 00:00 and remove focus from window
        self.attributes('-topmost', False)
        self.timer_label.configure(text="00:00")
        # Reset the total cycles to 0
        global reps
        reps = 0


if __name__ == "__main__":
    # Create an instance of the MainApplication class and start the main event loop
    app = MainApplication()
    app.mainloop()
