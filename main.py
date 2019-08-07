from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
import re


class AddressBar(QLineEdit):
    def keyPressEvent(self, e):
        super().keyPressEvent(e)
        if e.key() == 0x01000004:
            print('enter pressed')
            is_url = re.match('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', self.text())
            if not is_url:
                print('enter a valid url!')
            else:
                print(f'loading {self.text()}...')

app = QApplication([])

web_view = QWebEngineView()
web_view.setUrl(QUrl('https://www.google.com'))

window = QWidget()

button_view = QWidget()

v_layout = QVBoxLayout()
v_layout.addWidget(web_view)

h_layout = QHBoxLayout()

h_layout.addWidget(QPushButton(text="back"))
h_layout.addWidget(QPushButton(text="load"))

address_bar = AddressBar("address")

h_layout.addWidget(address_bar)

button_view.setLayout(h_layout)

v_layout.addWidget(button_view)

window.setLayout(v_layout)
window.show()

app.exec_()