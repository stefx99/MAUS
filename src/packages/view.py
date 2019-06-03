from PySide2 import QtWidgets, QtCore, QtGui
import random
import sys

from src.model.Node import Node
from src.packages.HierarchyTreeModel import HierarchyTreeModel
from src.packages.HierarchyTreeView import HierarchyTreeView
from src.packages.TextEdit import Window
from src.packages.PreviewPage import PreviewPage
from src.packages.pageView import pageView


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Treeview
        self.rootNode = Node('ROOT')
        self.treeModel = HierarchyTreeModel(self.rootNode)

        self.tree = HierarchyTreeView()
        self.tree.setModel(self.treeModel)
        self.tree.setMaximumWidth(180)



        # Setting up and add to layout
        self.layout = QtWidgets.QHBoxLayout()
        self.layout.addWidget(self.tree)
        #self.layout.addWidget(self.pageView)

        # Menu Bar//////

        self.mainMenu = QtWidgets.QMenuBar()

        # End of menu bar

        # PREVIEWPAGEEE


        self.preview = pageView()



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

        self.actionBold = QtWidgets.QAction("Bold", None)
        self.actionBold.setShortcut("Ctlr+B")
        self.actionBold.triggered.connect(self.boldAction)
        self.actionBold = QtWidgets.QAction(QtGui.QIcon("src/media/b.png"), "Bold", self)

        self.actionItalic = QtWidgets.QAction("Italic", None)
        self.actionItalic.setShortcut("Ctlr+I")
        self.actionItalic.triggered.connect(self.italicAction)
        self.actionItalic = QtWidgets.QAction(QtGui.QIcon("src/media/i.png"), "Italic", self)

        self.actionUnderline = QtWidgets.QAction("Underline", None)
        self.actionUnderline.setShortcut("Ctlr+I")
        self.actionUnderline.triggered.connect(self.underlineAction)
        self.actionUnderline = QtWidgets.QAction(QtGui.QIcon("src/media/u.png"), "Underline", self)

        self.actionFont = QtWidgets.QAction("Font", None)
        self.actionFont.setShortcut("Ctlr+F")
        self.actionFont.triggered.connect(self.fontAction)
        self.actionFont = QtWidgets.QAction(QtGui.QIcon("src/media/f.png"), "Font", self)

        self.actionCopy = QtWidgets.QAction("Copy", None)
        self.actionCopy.setShortcut("Ctlr+C")
        self.actionCopy.triggered.connect(self.copyAction)
        self.actionCopy = QtWidgets.QAction(QtGui.QIcon("src/media/c.png"), "Copy", self)

        self.actionPaste = QtWidgets.QAction("Paste", None)
        self.actionPaste.setShortcut("Ctlr+V")
        self.actionPaste.triggered.connect(self.pasteAction)
        self.actionPaste = QtWidgets.QAction(QtGui.QIcon("src/media/p.png"), "Paste", self)

        self.actionCut = QtWidgets.QAction("Size", None)
        self.actionCut.setShortcut("Ctlr+X")
        self.actionCut.triggered.connect(self.cutAction)
        self.actionCut = QtWidgets.QAction(QtGui.QIcon("src/media/cut.png"), "Cut", self)

        self.actionSize = QtWidgets.QAction("Size", None)
        ##self.actionSize.setShortcut("") ##Nema shortcut
        self.actionSize.triggered.connect(self.sizeAction)
        self.actionSize = QtWidgets.QAction(QtGui.QIcon("src/media/size.png"), "Size", self)

        self.actionColor = QtWidgets.QAction("Color", None)
        # self.actionColor.setShortcut("")##Nema shortcut
        self.actionColor.triggered.connect(self.colorAction)
        self.actionColor = QtWidgets.QAction(QtGui.QIcon("src/media/color.png"), "color", self)

        self.filemenu = self.mainMenu.addMenu("File")
        self.editmenu = self.mainMenu.addMenu("Edit")
        self.helpmenu = self.mainMenu.addMenu("Help")

        self.editmenu.addAction(self.actionBold)
        self.editmenu.addAction(self.actionItalic)
        self.editmenu.addAction(self.actionUnderline)
        self.editmenu.addAction(self.actionFont)
        self.editmenu.addAction(self.actionCopy)
        self.editmenu.addAction(self.actionPaste)
        self.editmenu.addAction(self.actionCut)
        self.editmenu.addAction(self.actionSize)
        self.editmenu.addAction(self.actionColor)

        self.filemenu.addAction(self.actionExit)   # Dodavanje akcija na menubar
        self.filemenu.addAction(self.actionOpen)

        self.helpmenu.addAction(self.actionHelp)
        self.helpmenu.addAction(self.actionAbout)

    def copyAction(self):
        pass

    def pasteAction(self):
        pass

    def fontAction(self):
        pass

    def cutAction(self):
        pass

    def sizeAction(self):
        pass

    def colorAction(self):
        pass

    def boldAction(self):
        pass

    def italicAction(self):
        pass

    def underlineAction(self):
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