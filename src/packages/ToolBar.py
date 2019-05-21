import sys
from PySide2 import QtGui, QtWidgets

class Example(QtWidgets.QMainWindow):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI():

        #boldAction =
        #italicAction =
        #underlineAction =


        boldLetter = QtWidgets.QAction(QtGui.QIcon("../media/b.png"),"Bold",self)
        boldLetter.setShortcut("Ctrl+B")
        boldLetter.setStatusTip("Podebljava slovo/a")
        #boldLetter.clicked.connect(boldAction)


        italicLetter = QtWidgets.QAction(QtGui.QIcon("../media/i.png"),"Italic",self)
        italicLetter.setShortcut("Ctrl+I")
        italicLetter.setStatusTip("Kosi slovo/a")
        #italicLetter.clicked.connect(italicAction)


        underlineLetter = QtWidgets.QAction(QtGui.QIcon("../media/u.png"),"Underline",self)
        underlineLetter.setShortcut("Ctrl+U")
        underlineLetter.setStatusTip("Podvlaci slovo/a")
        #underlineLetter.clicked.connect(underlineAction)


        toolBar = self.addToolBar('Menubar')
        toolBar.addAction(boldLetter)
        toolBar.addAction(italicLetter)
        toolBar.addAction(underlineLetter)

        self.setGeometry(300, 300, 300, 300)
        self.show()


def main():

    app = QtWidgets.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
