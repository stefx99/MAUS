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

        self.actionOpen = QtWidgets.QAction("Open", None) # Dodavanje dugmica
        self.actionOpen.triggered.connect(self.file_open)

        self.actionHelp = QtWidgets.QAction("Help", None)
        self.actionHelp.triggered.connect(self.helpWindow)

        self.actionAbout = QtWidgets.QAction("About", None)
        self.actionAbout.triggered.connect(self.aboutWindow)

        self.filemenu = self.mainMenu.addMenu("File")


        self.helpmenu = self.mainMenu.addMenu("Help")


        self.filemenu.addAction(self.actionExit)   # Dodavanje akcija na menubar
        self.filemenu.addAction(self.actionOpen)

        self.helpmenu.addAction(self.actionHelp)
        self.helpmenu.addAction(self.actionAbout)

    def close_application(self):
        sys.exit()

    def editor(self):

        self.textEdit = QtGui.QTextEdit()
        self.setCentralWidget(self.textEdit)


    def helpWindow(self):

        msgBox = QtWidgets.QMessageBox(self)
        msgBox.setWindowTitle(msgBox.tr("Help"))
        msgBox.setText('Cool message')
        msgBox.show();


    def aboutWindow(self):

        msgBox = QtWidgets.QMessageBox(self)
        msgBox.setWindowTitle(msgBox.tr("About"))
        msgBox.setText('Cool message #2')
        msgBox.show();



    def file_open(self): ### FILEOPEN KAO RADI, TREBAJU FUNKCIONALNOSTI

        fileOpen = QtWidgets.QFileDialog()

        fileOpen.setFileMode(QtWidgets.QFileDialog.ExistingFiles)

        if fileOpen.exec_():
            inFiles = fileOpen.selectedFiles()
        else:
            inFiles = []

        fileOpen.setParent(None)

        return inFiles

    """
        name = QtGui.QFileOpenEvent.openFile(self, 'Open File')
        file = open(name, 'r')

        self.editor()

        with file:
            text = file.read()
            self.textEdit.setText(text)
    """
    def file_save(self):
        name = QtGui.QFileDialog.getSaveFileName(self, 'Save File')
        file = open(name, 'w')
        text = self.textEdit.toPlainText()
        file.write(text)
        file.close()

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