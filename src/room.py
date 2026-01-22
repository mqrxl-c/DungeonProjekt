import tkinter as tk

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

        self.init_screen()

    def init_screen(self):
        ## Inits and Packs all Widgets for Frame

        ## Room Title
        label = tk.Label(self, text=self.name)
        label.pack(side="top", fill="x", pady=10)

        ## Monster Health
        monster_label = tk.Label(self, textvariable=self.monster_health)
        monster_label.pack(side="top", fill="x", pady=10)

        ## Buttons
        button1 = tk.Button(self, text="Test", command=self.test)
        button1.pack()

        button2 = tk.Button(self, text="Attack", command=self.test_health)
        button2.pack()

    def test(self):
        self.controller.next_room(self.index + 1)

    def test_health(self):
        self.monster.health -= 10
        self.monster_health.set("Monster Health: " + str(self.monster.health))
