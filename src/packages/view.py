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
        self.layout = QtWidgets.QGridLayout()
        self.layout.addWidget(self.tree, 0, 0)
        self.layout.addWidget(self.pageView, 0, 1)

        # Menu Bar
        self.menuBar = QtWidgets.QMenuBar()
        #self.menuBar.addMenu()


        # End of menu bar


        # Layout add
        self.layout.setMenuBar(self.menuBar)
        self.setLayout(self.layout)
        self.setWindowTitle(self.tr("MAUS"))






