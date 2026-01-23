import tkinter as tk
import tkinter.font as tkFont

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Dungeon Adventure", font=tkFont.Font(
            family="Times New Roman", size=20, weight="bold"))
        label.place(relx=0.5, rely=0.1, anchor="n")

        button1 = tk.Button(self, text="Start Rooms Test",
                                command=lambda: controller.next_room(0))
        button1.place(relx=0.5, rely=0.5, anchor="center")

        self.name = "StartPage"


class Placeholder(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is the start page")
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Start Rooms Test",
                                command=lambda: controller.show_frame(
                                    "Room 1"))
        button1.pack()

        self.name = "Placeholder"