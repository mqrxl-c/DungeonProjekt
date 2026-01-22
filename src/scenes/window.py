import tkinter as tk


class Window:
    def __init__(self):
        self.root = tk.Tk()

        self.width = 800
        self.height = 600
        self.root.geometry(f"{self.width}x{self.height}")

        self.frame = tk.Frame(self.root)

        self.root.title("Dungeon Game")

        label = tk.Label(self.frame, text="Welcome to Dungeon Game")
        label.pack()

    def go_to_room(self, room):
        for widget in self.frame.winfo_children():
            widget.destroy()

        room.room_loop()