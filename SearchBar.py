from PyQt5.QtWidgets import *
import re


class SearchBar(QLineEdit):
    def keyPressEvent(self, e):
        super().keyPressEvent(e)
        if e.key() == 0x01000004:
            print('enter pressed')
            is_url = re.match('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', self.text())
            if not is_url:
                print('enter a valid url!')
            else:
                print('loading {}...'.format(self.text()))