from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl


app = QApplication([])
web_view = QWebEngineView()
web_view.setUrl(QUrl('https://www.google.com'))
web_view.show()
app.exec_()