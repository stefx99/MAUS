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
        self.tree.setMaximumWidth(180)

        self.pageView = QtWidgets.QAbstractScrollArea()


        # Setting up and add to layout
        self.layout = QtWidgets.QHBoxLayout()

        self.layout.addWidget(self.tree)
        self.layout.addWidget(self.pageView)

        # Menu Bar//////

        self.mainMenu = QtWidgets.QMenuBar()

        # End of menu bar


        # Layout add

        self.createMenus()
        self.setLayout(self.layout)
        self.setWindowTitle(self.tr("MAUS"))
        self.layout.setMenuBar(self.mainMenu)


    def createMenus(self):

        self.actionNewProject = QtWidgets.QAction("New", None)
        self.actionNewProject.triggered.connect(self.tree.addNode)

        

        self.filemenu = self.mainMenu.addMenu("File")
        self.helpmenu = self.mainMenu.addMenu("Help")
        self.helpmenu.addAction(self.actionNewProject)

        self.filemenu.addAction(self.actionNewProject)

        self.filemenu.addAction(self.actionNewProject)
        self.filemenu.addAction(self.actionNewProject)




