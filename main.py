import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QPushButton, QLabel, \
    QGridLayout

BUTTONS = {
    "C": (1, 0, 1, 1),
    "/": (1, 3, 1, 1),
    "7": (2, 0, 1, 1),
    "8": (2, 1, 1, 1),
    "9": (2, 2, 1, 1),
    "x": (2, 3, 1, 1),
    "4": (3, 0, 1, 1),
    "5": (3, 1, 1, 1),
    "6": (3, 2, 1, 1),
    "-": (3, 3, 1, 1),
    "1": (4, 0, 1, 1),
    "2": (4, 1, 1, 1),
    "3": (4, 2, 1, 1),
    "+": (4, 3, 1, 1),
    "0": (5, 0, 1, 2),
    ".": (5, 2, 1, 1),
    "=": (5, 3, 1, 1),
},

class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Super Calculatrice')
        main_layout = QGridLayout(self)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Calculator()
    win.show()
    sys.exit(app.exec())


