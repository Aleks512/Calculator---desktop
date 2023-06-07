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
        self.result_and_edit = QLineEdit("0")

        # add it to main layout with coordinates
        self.main_layout.addWidget(self.result_and_edit, 0, 0, 1, 4)

        # create all BUTTONS

        for key, value in BUTTONS.items():
            button = QPushButton(key)
            self.main_layout.addWidget(button, *value) #tupple unpacking
            #eliminer les "=" et "C"  de self.buttons[key] = button
            if key not in ["=", "C"]:
            # connect button
                button.clicked.connect(self.button_pressed)
            self.buttons[key] = button
        self.buttons["C"].clicked.connect(self.clear_result) # say that this method 'clear_result' is called when connect signal is broadcasted
        self.buttons["="].clicked.connect(self.compute_result)

    def clear_result(self):
        self.result_and_edit.setText("0")

    def compute_result(self):
        try:
            result = eval(self.result_and_edit.text().replace("x", "*"))
        except SyntaxError: #error like "120jdkskn" and then "=" in lineedit
            return # do nothing, stop the method
        self.result_and_edit.setText(str(result))

    def button_pressed(self):
        if self.result_and_edit.text() == "0":
            self.result_and_edit.clear()
        # print(self.sender().text()) self.sender => selon le btn on recuperer <PySide6.QtWidgets.QPushButton(0x26aa67ccd70) at 0x0000026AA6F68D40> et ave le texte() on recuperer le key de b
        button_number = self.sender().text() # self.sender().text() recupere le widget en texte qui a declanché la méthode
        capture_text = self.result_and_edit.text()

        self.result_and_edit.setText(capture_text + button_number)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Calculator()
    win.show()
    sys.exit(app.exec())


