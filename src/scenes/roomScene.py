from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QLabel, QGridLayout, QHBoxLayout, QVBoxLayout, QPushButton
from PyQt6.QtGui import QColor, QPalette, QFont


class Color(QWidget):
    def __init__(self, color):
        super().__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)

class RoomScene(QWidget):
    def __init__(self, window=None, count=None):
        super().__init__(window)

        ## window reference
        self.window = window

        ## Vertical Layout
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        self.title = QLabel("Room " + str(count))

        self.room_info = QVBoxLayout()

        self.main_layout.addLayout(self.room_info)

        self.main_layout.addWidget(Color("Black"))
        self.main_layout.addWidget(Color("Black"))
        self.main_layout.addWidget(Color("Black"))

        ## scene dem MainWindow hinzufügen
        self.window.add_scene(self)

        self.init_header()
        self.actions()

    def init_header(self):

        ## Title Erstellen und zu dem Layout hinzufügen
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title.setFont(QFont(self.window.title_font, 20))

        self.player_hp = QLabel("Player HP: " + str(100))

        self.room_info.addWidget(self.title)
        self.room_info.addWidget(self.player_hp)

        divider = QLabel("+" + "-"*125 + "+")
        divider.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.room_info.addWidget(divider)

    def actions(self):
        run_button = QPushButton("Run")
        attack_button = QPushButton("Attack")

        self.action_layout = QHBoxLayout()
        self.action_layout.addWidget(attack_button)
        self.action_layout.addWidget(run_button)

        self.main_layout.addLayout(self.action_layout)