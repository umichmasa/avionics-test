from PyQt5 import QtGui, QtCore, QtWidgets

class Window(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.label = QtWidgets.QLabel(self)
        self.label.setSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        self.label.resize(1920, 1080)
        self.label.setContentsMargins(0, 0, 0, 0);
        self.pixmap = QtGui.QPixmap("p&id.png")
        self.label.setPixmap(self.pixmap)
        self.label.setMinimumSize(1, 1)
        self.label.installEventFilter(self)
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.label)

    def eventFilter(self, source, event):
        if (source is self.label and event.type() == QtCore.QEvent.Resize):
            self.label.setPixmap(self.pixmap.scaled(
                self.label.size(), QtCore.Qt.KeepAspectRatio))
        return super(Window, self).eventFilter(source, event)

if __name__ == '__main__':

    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    window.resize(1920, 1080)
    sys.exit(app.exec_())


