from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtWidgets import QMdiArea
import random
import sys

from src.model.Node import Node
from src.packages.HierarchyTreeModel import HierarchyTreeModel
from src.packages.HierarchyTreeView import HierarchyTreeView
from src.packages.TextEdit import Window
from src.packages.PreviewPage import PreviewPage
from src.packages.bookView import bookView


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.rootNode = Node('ROOT')
        self.treeModel = HierarchyTreeModel(self.rootNode)

        self.tree = HierarchyTreeView()
        self.tree.setModel(self.treeModel)
        self.tree.setMaximumWidth(180)

        self.layout = QtWidgets.QHBoxLayout()
        self.layout.addWidget(self.tree)
        #self.layout.addWidget(self.pageView)

        self.mainMenu = QtWidgets.QMenuBar()

        self.preview = bookView()

        self.layout.addWidget(self.preview)
        self.createMenus()
        self.setLayout(self.layout)
        self.setWindowTitle(self.tr("MAUS"))

        self.layout.setMenuBar(self.mainMenu)

    def setMdiWidget(self,widget):
        self.mdiWidget = widget
        self.setCentralWidget(self.mdiWidget)

    def addToMdi(self,widget):
        self.mdiWidget.addTab(widget,"ime")

    def createMenus(self):

        self.actionNewWorkspace = QtWidgets.QAction("New Workspace",None)
        self.actionNewWorkspace.triggered.connect(self.createWorkspace)

        self.actionExit = QtWidgets.QAction("Exit", None)
        self.actionExit.triggered.connect(self.close_application)

        self.actionOpen = QtWidgets.QAction("Open", None)
        self.actionOpen.triggered.connect(self.file_open)

        self.actionHelp = QtWidgets.QAction("Help", None)
        self.actionHelp.triggered.connect(self.helpWindow)

        self.actionAbout = QtWidgets.QAction("About", None)
        self.actionAbout.triggered.connect(self.aboutWindow)

        self.filemenu = self.mainMenu.addMenu("File")
        self.helpmenu = self.mainMenu.addMenu("Help")

        self.filemenu.addAction(self.actionNewWorkspace)
        self.filemenu.addAction(self.actionOpen)
        self.filemenu.addAction(self.actionExit)

        self.helpmenu.addAction(self.actionHelp)
        self.helpmenu.addAction(self.actionAbout)

    def createWorkspace(self):
        pass

    def close_application(self):
        sys.exit()

    def editor(self):

        self.textEdit = QtGui.QTextEdit()
        self.setCentralWidget(self.textEdit)

    def helpWindow(self):

        msgBox = QtWidgets.QMessageBox(self)
        msgBox.setWindowTitle(msgBox.tr("Help"))
        msgBox.setText('Cool message')
        msgBox.show()

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
