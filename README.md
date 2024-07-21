# 20-20-20 Tkinter Timer Application

## Overview

Using what I have learned about Tkinter from the 100 Days of Python course by Dr. Angela Yu, I decided to make a simple timer that can help you with the 20-20-20 rule.
- A message box every 20 minutes will pop up, prompting you to look away for 20 seconds and afterward reset again to 20 minutes of work. 
- I wanted to make this timer as it would be useful for me, who often works long hours on my computer and wanted a way to remind me to take care of my eyes, whilst at the same time practicing my coding skills. 

## Features

- Timer GUI with work and break cycles
- Start and reset functionality
- Pop-up with a sound notification to announce the end of work and break cycles

## Prerequisites

To run this application, you need to have at least Python 3.11 installed on your computer. You can download Python from [python.org](https://www.python.org/downloads/).

## How to Run

1. **Clone the Repository**: 
   - Open your terminal or command prompt.
   - Navigate to the directory where you want to clone the repository.
   - Run the following command:
     ```shell
     git clone https://github.com/nfalck/20_20_20_timer.git
     ```

2. **Navigate to the Project Folder**:
   - Change the directory to the project folder:
     ```shell
     cd 20_20_20_timer
     ```

3. **Install Dependencies**:
   - The application uses the tkinter library, which is included with Python.
   
4. **Run the Application**:
   - Execute the following command to start the application:
     ```shell
     python main.py
     ```

5. **Interact with the Application**:
   - Click on the "Start Timer" button in order to start the timer.
   - Click on the "Reset Timer" button in order to reset it. 

6. **Notifications**:
   - The timer will alternate between work and break intervals, prompting you every 20 minutes to follow the 20-20-20 rule for eye care.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments
- Inspired by the 20-20-20 rule for eye care during computer use.
- Used a video by [Codemy.com](https://www.youtube.com/watch?v=djDcVWbEYoE) to learn how to add sound.
- Used StackOverflow - [Post 1](https://stackoverflow.com/questions/51014756/changing-color-of-buttons-in-tkinter-works-on-windows-but-not-mac-osx) and [Post 2](https://stackoverflow.com/questions/1854/how-to-identify-which-os-python-is-running-on) to solve the tkinter button issue on MacOS.
- Used the skills that I learned from the Pomodoro Timer project in "100 Days of Code: The Complete Python Pro Bootcamp for 2023" by Dr. Angela Yu
