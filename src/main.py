import sys

from PyQt6.QtWidgets import QApplication, QWidget

from scenes.window import MainWindow
from scenes.roomScene import RoomScene

if __name__ == "__main__":
    print("Starting...")

    app = QApplication(sys.argv)

    window = MainWindow()

    room1 = RoomScene(window=window, count=1)
    room2 = RoomScene(window=window, count=2)

    window.go_to_scene(room1)
    window.show()

    app.exec()

