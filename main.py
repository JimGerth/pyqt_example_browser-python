from PyQt5.QtWidgets import *
from Browser import Browser


app = QApplication([])

browser = Browser()
browser.show()

app.exec_()