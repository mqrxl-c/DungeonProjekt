import sys
import time

import tkinter as tk

from scenes.window import Window
from room import Room
from monster import Monster
from player import Player

if __name__ == "__main__":

    # Create main window
    root = tk.Tk()
    root.geometry("400x200")

    # Create a frame
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")

    # Add some widgets to the frame
    label = tk.Label(frame, text="Hello, Tkinter!")
    label.pack(pady=10)
    button = tk.Button(frame, text="Click Me")
    button.pack(pady=10)


    # Function to clear all widgets in the frame
    def clear_frame():
        for widget in frame.winfo_children():
            widget.destroy()


    # Add a button to clear the frame
    clear_button = tk.Button(root, text="Clear Frame", command=clear_frame)
    clear_button.pack(pady=20)

    root.mainloop()
