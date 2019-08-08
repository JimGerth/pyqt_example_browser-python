from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QAction
from Browser import Browser


class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setCentralWidget(Browser())
        self.setWindowTitle('Browser')
        self._setup_actions()
        self._setup_menu_bar()

    def _setup_actions(self):
        self._print_action = QAction('Print')
        self._print_action.setShortcut('Ctrl+P')
        self._print_action.triggered.connect(self._print)

        self._about_action = QAction('About')
        self._about_action.triggered.connect(self._about)

    def _setup_menu_bar(self):
        self._menu_bar = self.menuBar()

        self._file_menu = self._menu_bar.addMenu('File')
        self._file_menu.addAction(self._print_action)

        self._help_menu = self._menu_bar.addMenu('Help')
        self._help_menu.addAction(self._about_action)

    def _print(self):
        print('printing...')
        self.centralWidget().grab().save('image.png')

    def _about(self):
        print('made by Jim Gerth')