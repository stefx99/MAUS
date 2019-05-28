from PySide2 import QtWidgets, QtCore, QtGui
import random
import sys

from src.model.Node import Node
from src.packages.HierarchyTreeModel import HierarchyTreeModel
from src.packages.HierarchyTreeView import HierarchyTreeView
from src.packages.TextEdit import Window
from src.packages.PreviewPage import PreviewPage


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Treeview
        self.rootNode = Node('ROOT')
        self.treeModel = HierarchyTreeModel(self.rootNode)

        self.tree = HierarchyTreeView()
        self.tree.setModel(self.treeModel)
        self.tree.setMaximumWidth(180)

        #self.pageView = QtWidgets.QAbstractScrollArea()


        # Setting up and add to layout
        self.layout = QtWidgets.QHBoxLayout()
        self.layout.addWidget(self.tree)
        #self.layout.addWidget(self.pageView)

        # Menu Bar//////

        self.mainMenu = QtWidgets.QMenuBar()

        # End of menu bar

        # PREVIEWPAGEEE

        self.block = QtWidgets.QWidget()
        self.block.setAutoFillBackground(True)
        p = self.block.palette()
        p.setColor(self.block.backgroundRole(), randomColor())
        self.block.setPalette(p)
        self.block.setFixedHeight(800)
        self.block.setFixedWidth(1000)
        self.preview = QtWidgets.QScrollArea()
        self.preview.setWidget(self.block)

        # End preview


        self.toolBar = QtWidgets.QToolBar()
        self.initUI()

        # Layout add
        self.layout.addWidget(self.preview)
        self.layout.addWidget(self.toolBar)
        self.createMenus()
        self.setLayout(self.layout)
        self.setWindowTitle(self.tr("MAUS"))
        self.layout.setMenuBar(self.mainMenu)


    def createMenus(self):

        self.actionNewProject = QtWidgets.QAction("New", None)
        self.actionNewProject.triggered.connect(self.tree.addNode)

        self.actionExit = QtWidgets.QAction("Exit", None)
        self.actionExit.triggered.connect(self.close_application)



        self.filemenu = self.mainMenu.addMenu("File")
        self.helpmenu = self.mainMenu.addMenu("Help")
        self.helpmenu.addAction(self.actionNewProject)

        self.filemenu.addAction(self.actionExit)

        self.filemenu.addAction(self.actionNewProject)
        self.filemenu.addAction(self.actionNewProject)

    def close_application(self):
        sys.exit()

    def initUI(self):
            # boldAction =
            # italicAction =
            # underlineAction =

        boldLetter = QtWidgets.QAction(QtGui.QIcon("src/media/b.png"), "Bold", self)
        boldLetter.setShortcut("Ctrl+B")
        boldLetter.setStatusTip("Podebljava slovo/a")
            # boldLetter.clicked.connect(boldAction)

        italicLetter = QtWidgets.QAction(QtGui.QIcon("src/media/i.png"), "Italic", self)
        italicLetter.setShortcut("Ctrl+I")
        italicLetter.setStatusTip("Kosi slovo/a")
            # italicLetter.clicked.connect(italicAction)

        underlineLetter = QtWidgets.QAction(QtGui.QIcon("src/media/u.png"), "Underline", self)
        underlineLetter.setShortcut("Ctrl+U")
        underlineLetter.setStatusTip("Podvlaci slovo/a")
            # underlineLetter.clicked.connect(underlineAction)




        self.toolBar.addAction(boldLetter)
        self.toolBar.addAction(italicLetter)
        self.toolBar.addAction(underlineLetter)


        #self.toolBar.setGeometry(300, 300, 300, 300)

########################################
def randomColor():
    r = lambda: random.randint(0, 255)
    g = lambda: random.randint(0, 255)
    b = lambda: random.randint(0, 255)
    return ('#%02X%02X%02X' % (r(), g(), b()))