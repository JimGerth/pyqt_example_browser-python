from PyQt5.QtWidgets import *
from Window import Window


app = QApplication([])

window = Window()
window.show()

app.exec_()