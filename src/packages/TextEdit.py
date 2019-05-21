import sys
from PySide2 import QtWidgets


class Window(QtWidgets.QWidget):

    def __init__(self):

        super().__init__()
        self.setWindowTitle("Text Editor")
        self._counter = 1
        self.initUI()

    def initUI(self):

        currentPage = QtWidgets.QPushButton(str(self._counter))

        nextPage = QtWidgets.QPushButton(">")
        # nextPage.clicked.connect(self,getNextPage)

        prevPage = QtWidgets.QPushButton("<")
        # prevPage.clicked.connect(self,getPreviousPage)

        reviewEdit = QtWidgets.QTextEdit()

        grid = QtWidgets.QGridLayout()

        grid.setSpacing(20)
        grid.addWidget(reviewEdit, 1, 1, 30, 3)
        grid.addWidget(prevPage,63,1)
        grid.addWidget(nextPage,63,3)
        grid.addWidget(currentPage,63,2)


    def get_counter(self):

        return self._counter

    def set_counter(self,counter):

        self._counter = counter
