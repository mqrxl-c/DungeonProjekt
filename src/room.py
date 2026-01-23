import tkinter as tk
import tkinter.font as tkFont
import time

from src.utils import clear_frame

class Room(tk.Frame):
    def __init__(self, parent, controller, index, player, monster):
        tk.Frame.__init__(self, parent)

        ## base Info
        self.name = "Room " + str(index + 1)
        self.controller = controller
        self.index = index

        ## references
        self.player = player
        self.monster = monster ## needed?

        ## mit StringVar kann man den Lable Text updaten
        self.monster_health = tk.StringVar()
        self.monster_health.set("Monster Health: " + str(self.monster.health))
        self.player_health = tk.StringVar()
        self.player_health.set("Player Health: " + str(self.player.health))

        self.text = tk.StringVar()

        self.action_frame = tk.Frame(self)
        self.action_frame.place(relx=0.1, rely=0.8, relwidth=0.8, height=100)
        self.text_frame = tk.Frame(self)
        self.action_frame.place(relx=0.1, rely=0.8, relwidth=0.8, height=100)

        self.init_screen()

    def init_screen(self):
        ## Inits and Packs all Widgets for Frame

        ## Room Title
        label = tk.Label(self, text=self.name, font=tkFont.Font(
            family="Times New Roman", size=20, weight="bold"))
        label.place(relx=0.5, rely=0.05, anchor="n")

        ## Monster Health
        monster_label = tk.Label(self, textvariable=self.monster_health)
        monster_label.place(rely=0.2, relx=0.1, anchor="w")

        player_label = tk.Label(self, textvariable=self.player_health)
        player_label.place(rely=0.2, relx=0.9, anchor="e")

        text_label = tk.Label(self.text_frame, textvariable=self.text)
        button = tk.Button(self.text_frame, text="Continue", command=self.show_actions)
        button.place(rely=0.9, relx=0.5, anchor="s")
        self.text.set("text")
        text_label.place(rely=0.5, relx=0.5, relwidth=1, anchor="center")

        ## Buttons
        run_button = tk.Button(self.action_frame, text="Run", command=self.run)
        attack_button = tk.Button(self.action_frame, text="Attack", command=self.attack)

        run_button.place(rely=0.5, relx=0.45, anchor="e", width=80)
        attack_button.place(rely=0.5, relx=0.55, anchor="w", width=80)

        self.show_actions()

    def attack(self):
        if self.monster.take_damage(self.player.return_strength()):
            self.monster_health.set("Monster Health: " + str(self.monster.health))
            self.show_text("Player Attacked Monster")
        else:
            ## monster died
            self.monster_health.set("Monster Health: 0")
            self.room_completed()

    def show_actions(self):
        print("actions")
        self.action_frame.tkraise()

    def show_text(self, text):
        print("text")
        self.text.set(text)
        self.text_frame.tkraise()

    def run(self):
        self.player.take_damage(10)
        self.room_completed()

    def room_completed(self):
        clear_frame(self)

        label = tk.Label(self, text="Room: " + str(self.index + 1) +" completed!")
        label.pack(side="top", fill="x", pady=10)

        monster_label = tk.Label(self, textvariable=self.monster_health)
        monster_label.pack(side="top", fill="x", pady=10)

        button = tk.Button(self, text="Next Room", command=self.next_room)
        button.pack()

    def next_room(self):
        self.controller.next_room(self.index + 1)
