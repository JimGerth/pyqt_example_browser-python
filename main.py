from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl


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
h_layout.addWidget(QPlainTextEdit("address"))

button_view.setLayout(h_layout)

v_layout.addWidget(button_view)

window.setLayout(v_layout)
window.show()

app.exec_()