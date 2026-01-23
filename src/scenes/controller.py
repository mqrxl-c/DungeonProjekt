import tkinter as tk
from .menu import StartPage, Placeholder

## https://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter

class Controller(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        ## sets window info and Size
        self.geometry("400x400")
        self.resizable(False, False)
        self.title("Dungeon Game")

        ## Container for Frames
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)

        self.rooms = []
        self.frames = {}

        ## get Frames and add to self.frames
        for F in (StartPage, Placeholder):
            frame = F(parent=self.container, controller=self)
            self.frames[frame.name] = frame

            # puts frame on same position, at same size as window
            frame.place(relwidth=1, relheight=1, relx=0, rely=0, anchor="nw")

        self.show_frame("StartPage")

    def get_rooms(self, room_list):
        '''Takes a list of rooms and adds them to frames'''
        for room in room_list:
            self.frames[room.name] = room
            # puts room frame on same position, at same size as window
            room.place(relwidth=1, relheight=1, relx=0, rely=0, anchor="nw")

            self.rooms.append(room)

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

    def next_room(self, index):
        '''Shows the room at given index'''
        if index < len(self.rooms):
            ## updates player health for next room
            self.rooms[index].player_health.set(
                "Player Health: " + str(self.rooms[index].player.health))
            self.show_frame("Room "+str(index+1))
        else:
            self.show_frame("StartPage")