'''
Ovde je kod za horizontalni Meni sa listom padajucih elemenata i dugmica.
'''

from PySide2 import QtWidgets, QtCore, QtGui

class MenuBar(QtWidgets.QMainWindow):

    def __init__(self):
        self.menuBar = MenuBar

    def setMenuBar(self):
        mainMenu = self.menuBar()
        fileMenu = self.addMenu("File")
        viewMenu = self.addMenu("View")
        editMenu = self.addMenu("Edit")
        helpMenu = self.addMenu("Help")
