from tkinter import ttk

class Room:
    def __init__(self, count, monster, player, window):
        self.name = "Room " + str(count)
        self.monster = monster
        self.player = player

        self.widgets = []
        self.init_screen(window)


    def init_screen(self, window):
        title = ttk.Label(window.frame, text=self.name)
        self.widgets.append(title)

    def room_loop(self):
        ## erste room info

        for widget in self.widgets:
            widget.pack()

        while self.monster.health > 0:
            ## angreifen oder fliehen
            pass

        ## monster tot
        self.player.regain_health(self.monster.return_damage_taken())
