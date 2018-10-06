import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
#from csv_reader import Warning



####### defining variables
#Warning w = createWarningList()
pressure = 101

##########################

class App(QWidget):


    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 button - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 1800
        self.height = 1200
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)


        button = QPushButton('PyQt5 button', self)
        button.setToolTip('This is an example button')
        button.move(10, 10)
        button.clicked.connect(self.on_click)

       # if pressure > 100:
        #        button.setStyleSheet("background-color: yellow")


        button = QPushButton('PyQt5 button', self)
        button.setToolTip('This is an example button')
        button.move(10, 40)
        button.clicked.connect(self.on_click)

        button = QPushButton('PyQt5 button', self)
        button.setToolTip('This is an example button')
        button.move(10, 70)
        button.clicked.connect(self.on_click)

        button = QPushButton('PyQt5 button', self)
        button.setToolTip('This is an example button')
        button.move(10, 100)
        button.clicked.connect(self.on_click)

        button = QPushButton('PyQt5 button', self)
        button.setToolTip('This is an example button')
        button.move(10, 130)
        button.clicked.connect(self.on_click)

        button = QPushButton('PyQt5 button', self)
        button.setToolTip('This is an example button')
        button.move(10, 160)
        button.clicked.connect(self.on_click)

        button = QPushButton('PyQt5 button', self)
        button.setToolTip('This is an example button')
        button.move(10, 190)
        button.clicked.connect(self.on_click)

        button = QPushButton('PyQt5 button', self)
        button.setToolTip('This is an example button')
        button.move(10, 220)
        button.clicked.connect(self.on_click)

        button = QPushButton('PyQt5 button', self)
        button.setToolTip('This is an example button')
        button.move(10, 250)
        button.clicked.connect(self.on_click)
        self.show()


    @pyqtSlot()
    def on_click(self):
        print('NUT NUT NUT NUT NUT')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

