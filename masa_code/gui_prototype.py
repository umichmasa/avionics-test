import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
#from csv_reader import Warning
import os,sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap




class App(QWidget):


    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 button - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 1920
        self.height = 1080
        self.initUI()


    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

##############################################################

        #label = QLabel()
        #pixmap = QPixmap("C:\\Desktop\\masa_code\\p&id.png")
        #label.setPixmap(pixmap)


        #image = QtGui.QLabel(self)
        #image.setGeometry(50, 40, 250, 250)
        #pixmap = QtGui.QPixmap("C:\\Desktop\\masa_code\\p&id.png")
        #image.setPixmap(pixmap)
        #image.show()

 #   def InitWindow(self):
  #      self.label = QLabel(self)
   #     self.label.setPixmap(QPixmap('p&id.png'))
    #    self.label.setGeometry(60, 50, 800, 400)
     #   self.setWindowIcon(QtGui.QIcon("p&id.png"))
      #  self.setWindowTitle(self.title)
       # self.setGeometry(self.top, self.left, self.width, self.height)

        #label = QLabel(self)
        #pixmap = QPixmap('image.jpeg')
        #label.setPixmap(pixmap)
        # Optional, resize window to image size
        #self.resize(pixmap.width(), pixmap.height())

##############################################################

        button = QPushButton('PyQt5 button', self)
        button.setToolTip('This is an example button')
        button.move(10, 10)
        button.clicked.connect(self.on_click)

        button = QPushButton('PyQt5 button', self)
        button.setToolTip('This is an example button')
        button.move(10, 40)
        button.clicked.connect(self.on_click)

        button = QPushButton(self)
        button.move(150, 700)
        #button.setStyleSheet("background-color:transparent;border:0;")
        button.resize(30, 70)
        button.clicked.connect(self.on_click)

        button = QPushButton('PyQt5 button', self)
        button.setToolTip('This is an example button')
        button.move(10, 10)
        button.clicked.connect(self.on_click)



        self.show()


    @pyqtSlot()
    def on_click(self):
        print('button is pushed my dude')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
