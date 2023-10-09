import sys
from PyQt5.QtGui import QApplication

def main():

    app = QApplication(sys.argv)
    w = QBushButton()
    w.setText("Quit")
    w.clicked.connect(app.quit)
    w.show()
    app.exec_()
