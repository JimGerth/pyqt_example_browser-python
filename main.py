from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl


app = QApplication([])

web_view = QWebEngineView()
web_view.setUrl(QUrl('https://www.google.com'))

window = QWidget()

layout = QVBoxLayout()
layout.addWidget(web_view)
layout.addWidget(QTextEdit())

window.setLayout(layout)
window.show()

app.exec_()