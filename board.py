import json
import ssl
from urllib import request
from PySide2.QtWidgets import QWidget, QGridLayout

from tile import Tile


class Board(QWidget):
    def __init__(self, parent=None):
        super(Board, self).__init__(parent)
        with request.urlopen("https://dog.ceo/api/breeds/image/random/1", context=ssl.SSLContext()) as f:
            obj = json.loads(f.read())
            # with request.urlopen(obj["message"][0], context=ssl.SSLContext()) as _img:
            #     print(_img.read())
        num_images = 3
        self._layout = QGridLayout(self)
        self._layout.setSpacing(2)
        for row in range(num_images):
            for col in range(num_images):
                self._layout.addWidget(Tile(row + 1, col + 1, obj["message"][0], parent=self), row + 1, col + 1)
        self.setLayout(self._layout)
        self.resize(800, 600)