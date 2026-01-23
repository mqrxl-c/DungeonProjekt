from scenes.controller import Controller
from src.room import Room
from player import Player
from monster import Monster


if __name__ == "__main__":
    player = Player("Name")

    controller = Controller()

    room_list = []

    for i in range(5):
        room = Room(parent=controller.container, controller=controller, index=i, player=player, monster=Monster("Name"))
        room_list.append(room)

    controller.get_rooms(room_list)
    controller.show_frame("StartPage")

    controller.mainloop()