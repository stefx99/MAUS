from PyQt5.QtWidgets import QApplication,QDialog,QPushButton,QLabel,QFileDialog,QVBoxLayout
import sys
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap

class Window(QDialog):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Window"
        self.left = 500
        self.top = 200
        self.width = 300
        self.height = 300

        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)

        vbox = QVBoxLayout()
        self.btn = QPushButton("Browse image")
        self.btn.clicked.connect(self.browseImage)

        vbox.addWidget(self.btn)

        # self.label = QLabel("Cao bato")
        # vbox.addWidget(self.label)

        self.setLayout(vbox)
        self.show()

    def browseImage(self):
        fname = QFileDialog.getOpenFileName(self,"Open File","c\\","Image files (*.jpg *.png)")
        imagePath = fname[0]
        pixmap = QPixmap(imagePath)
        self.label.setPixmap(QPixmap(pixmap))
        self.resize(pixmap.width(),pixmap.height())

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())