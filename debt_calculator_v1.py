from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class DebtCalculator(QMainWindow):
    def __init__(self):
        """initialize"""
        super(DebtCalculator, self).__init__()
        self.setGeometry(210, 90, 1500, 900)  # set window
        self.setWindowTitle("Debt Calculator")  # set title
        self.initUI()

    def initUI(self):
        """things that will be on the screen"""
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Debt Calculator")
        self.label.move(50, 50)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Submit")
        self.b1.clicked.connect(self.clicker)

    def clicker(self):
        self.label.setText("your pressed the button")
        self.update()

    def update(self):
        """Auto adjust the window if there is a change. Need to call if something changes on window"""
        self.label.adjustSize()


def window():
    app = QApplication(sys.argv)
    win = DebtCalculator()

    win.show()
    sys.exit(app.exec_())


window()
