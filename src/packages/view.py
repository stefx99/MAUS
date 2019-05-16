from PySide2 import QtWidgets, QtCore, QtGui


from src.model.Node import Node
from src.packages.HierarchyTreeModel import HierarchyTreeModel
from src.packages.HierarchyTreeView import HierarchyTreeView

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Treeview
        self.rootNode = Node('ROOT')
        self.treeModel = HierarchyTreeModel(self.rootNode)

        self.tree = HierarchyTreeView()
        self.tree.setModel(self.treeModel)
        self.tree.show()
        self.pageView = QtWidgets.QAbstractScrollArea()


        # Setting up and add to layout
        self.layout = QtWidgets.QHBoxLayout()

        self.layout.addWidget(self.tree)
        self.layout.addWidget(self.pageView)

        # Menu Bar//////

        self.mainMenu = QtWidgets.QMenuBar()

        self.filemenu = self.mainMenu.addMenu("File")
        self.helpmenu = self.mainMenu.addMenu("Help")

        self.filemenu.addAction("New")
        self.filemenu.addAction("Open")
        self.filemenu.addAction("Save")
        self.filemenu.addAction("Exit")
        # fileMenu.addMenu("File")
        # viewMenu.addMenu("View")
        # editMenu.addMenu("Edit")
        # helpMenu.addMenu("Help")

        #self.menuBar.addMenu()\



        # End of menu bar


        # Layout add
        #self.layout.setMenuBar(self.mainBar)


        self.setLayout(self.layout)
        self.setWindowTitle(self.tr("MAUS"))
        self.layout.setMenuBar(self.mainMenu)


    def createMenus(self):
        pass

        # fileMenu = menuBar().addMenu(tr("&File"))

    # fileMenu.addAction(Act)
    #
    # fileMenu.addAction(openAct)
    #
    # fileMenu.addAction(saveAct)
    # fileMenu.addAction(printAct)
    #
    # fileMenu.addSeparator()
    #
    # fileMenu.addAction(exitAct)
    #
    # editMenu = menuBar().addMenu(tr("&Edit"))
    # editMenu.addAction(undoAct)
    # editMenu.addAction(redoAct)
    # editMenu.addSeparator()
    # editMenu.addAction(cutAct)
    # editMenu.addAction(copyAct)
    # editMenu.addAction(pasteAct)
    # editMenu.addSeparator()
    #
    # helpMenu = menuBar().addMenu(tr("&Help"))
    # helpMenu.addAction(aboutAct)
    # helpMenu.addAction(aboutQtAct)
    #

