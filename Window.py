from PyQt5.QtWidgets import QMainWindow
from Browser import Browser


class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setCentralWidget(Browser())