from PySide2 import QtWidgets, QtCore, QtGui

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Treeview
        self.treeView = QtWidgets.QTreeView()
        self.pageView = QtWidgets.QAbstractScrollArea()


        # Setting up and add to layout
        self.layout = QtWidgets.QGridLayout()
        self.layout.addWidget(self.treeView, 0, 0)
        self.layout.addWidget(self.pageView, 0, 1)

        # Menu Bar
        self.menuBar = QtWidgets.QMenuBar()
        #self.menuBar.addMenu()


        # End of menu bar


        # Layout add
        self.layout.setMenuBar(self.menuBar)
        self.setLayout(self.layout)
        self.setWindowTitle(self.tr("MAUS"))






