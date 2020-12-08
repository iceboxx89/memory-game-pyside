import sys

from PySide2.QtWidgets import QApplication

from board import Board

if __name__ == "__main__":
    app = QApplication(sys.argv)
    b = Board()
    b.show()
    app.exec_()
