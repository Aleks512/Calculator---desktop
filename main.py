import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QPushButton, QLabel, \
    QGridLayout, QLineEdit

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
}

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.buttons = {}
        self.setWindowTitle('Super Calculatrice')
        # set up main layout and fix it to window
        self.main_layout = QGridLayout(self)

        # set up input and result window
        self.result_and_adit = QLineEdit("0")

        # add it to main layout with coordinates
        self.main_layout.addWidget(self.result_and_adit, 0, 0, 1, 4)

        # create all BUTTONS

        for key, value in BUTTONS.items():
            button = QPushButton(key)
            self.main_layout.addWidget(button, *value) #tupple unpacking
            # create dico of buttons to connect them to slots
            self.buttons[key] = button





if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Calculator()
    win.show()
    sys.exit(app.exec())


