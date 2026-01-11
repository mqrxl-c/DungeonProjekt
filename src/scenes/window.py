from PyQt6.QtGui import QFontDatabase
from PyQt6.QtWidgets import QMainWindow, QStackedWidget

from src.utils import get_project_root

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(640, 480)

        self.scenes = QStackedWidget()
        self.setCentralWidget(self.scenes)

        self.title_font = ""

        root = get_project_root()
        font = QFontDatabase.addApplicationFont(str(root) + "/src/assets/StitchWarrior.ttf")

        ## check ob die Schrift richtig geladen wurde
        if font < 0:
            print("Error: Font ID not found")
        else:
            font_name = QFontDatabase.applicationFontFamilies(font)
            self.title_font = font_name[0]

    def add_scene(self, scene):
        self.scenes.addWidget(scene)

    def go_to_scene(self, scene):
        self.scenes.setCurrentWidget(scene)