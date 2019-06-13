from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtCore
from PySide2.QtCore import Qt

import sys
import time

from PySide2.QtWidgets import *
# from PySide2.QtWidgets.QFontComboBox import QFontComboBox
# from PySide2.QtWidgets.QLabel import QLabel

hideTB = True
hideFB = True
hideSB = True

class Main(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self, None)
        self.top = 600
        self.bottom = 200
        self.width = 700
        self.height = 700

        self.initUI()

    def initUI(self):
        ############################################################################################
        newAction = QAction(QIcon("src/media/new.png"), "New", self)
        newAction.setShortcut("Ctrl+N")
        newAction.setStatusTip("Create a new document.")
        newAction.triggered.connect(self.New)

        openAction = QAction(QIcon("src/media/open.png"), "Open file", self)
        openAction.setStatusTip("Open document")
        openAction.setShortcut("Ctrl+O")
        openAction.triggered.connect(self.Open)

        saveAction = QAction(QIcon("src/media/save.png"), "Save", self)
        saveAction.setStatusTip("Save document")
        saveAction.setShortcut("Ctrl+S")
        saveAction.triggered.connect(self.Save)

        cutAction = QAction(QIcon("src/media/cut.png"), "Cut", self)
        cutAction.setStatusTip("Delete and copy text")
        cutAction.setShortcut("Ctrl+X")
        cutAction.triggered.connect(self.Cut)

        copyAction = QAction(QIcon("src/media/copy.png"), "Copy", self)
        copyAction.setStatusTip("Copy text")
        copyAction.setShortcut("Ctrl+C")
        copyAction.triggered.connect(self.Copy)

        pasteAction = QAction(QIcon("src/media/paste.png"), "Paste", self)
        pasteAction.setStatusTip("Paste text")
        pasteAction.setShortcut("Ctrl+V")
        pasteAction.triggered.connect(self.Paste)

        undoAction = QAction(QIcon("src/media/undo.png"), "Undo", self)
        undoAction.setStatusTip("Undo")
        undoAction.setShortcut("Ctrl+Z")
        undoAction.triggered.connect(self.Undo)

        ############################################################################################
        #konfig toolBara

        self.toolbar = self.addToolBar("Options")
        self.toolbar.addAction(newAction)
        self.toolbar.addAction(openAction)
        self.toolbar.addAction(saveAction)

        self.toolbar.addSeparator()

        self.toolbar.addAction(cutAction)
        self.toolbar.addAction(copyAction)
        self.toolbar.addAction(pasteAction)
        self.toolbar.addAction(undoAction)

        self.addToolBarBreak()

        self.fontFamily = QFontComboBox(self)
        self.fontFamily.currentFontChanged.connect(self.FontFamily)

        fontSize = QComboBox(self)
        fontSize.setEditable(True)
        fontSize.activated.connect(self.FontSize)

        velicina = [6,7,8,9,10,11,12,13,14,15,16,18,20,22,24,26,28,32,36,40,44,48,54,60,66,72,80,88,96]

        for broj in velicina:
            fontSize.addItem(str(broj))

        fontColor = QAction(QIcon("src/media/color.gif"), "Change font color", self)
        fontColor.triggered.connect(self.FontColor)

        boldAction = QAction(QIcon("src/media/bold.png"), "Bold", self)
        boldAction.triggered.connect(self.Bold)

        italicAction = QAction(QIcon("src/media/italic.png"), "Italic", self)
        italicAction.triggered.connect(self.Italic)

        underlAction = QAction(QIcon("src/media/underline.png"), "Underline", self)
        underlAction.triggered.connect(self.Underline)

        alignLeft = QAction(QIcon("src/media/alignLeft.png"), "Align left", self)
        alignLeft.triggered.connect(self.alignLeft)

        alignCenter = QAction(QIcon("src/media/alignCenter.png"), "Align center", self)
        alignCenter.triggered.connect(self.alignCenter)

        alignRight = QAction(QIcon("src/media/alignRight.png"), "Align right", self)
        alignRight.triggered.connect(self.alignRight)

        backColor = QAction(QIcon("src/media/backcolor.png"), "Change background color", self)
        backColor.triggered.connect(self.FontBackColor)

        bulletAction = QAction(QIcon("src/media/tackica.png"), "Dotted List", self)
        bulletAction.triggered.connect(self.BulletList)

        numberedAction = QAction(QIcon("src/media/brojevi.png"), "Numerical List", self)
        numberedAction.triggered.connect(self.NumberedList)

        ############################################################################################

        space1 = QLabel("  ", self)
        space2 = QLabel("  ", self)
        space3 = QLabel("  ", self)

        self.formatbar = self.addToolBar("FormatBar")

        self.formatbar.addAction(boldAction)
        self.formatbar.addAction(italicAction)
        self.formatbar.addAction(underlAction)

        self.formatbar.addSeparator()

        self.formatbar.addAction(alignLeft)
        self.formatbar.addAction(alignCenter)
        self.formatbar.addAction(alignRight)

        self.formatbar.addSeparator()

        self.formatbar.addAction(bulletAction)
        self.formatbar.addAction(numberedAction)

        self.formatbar.addSeparator()

        self.formatbar.addAction(fontColor)
        self.formatbar.addAction(backColor)

        self.formatbar.addSeparator()

        self.formatbar.addWidget(self.fontFamily)
        self.formatbar.addWidget(space1)
        self.formatbar.addWidget(fontSize)
        self.formatbar.addWidget(space2)

        ############################################################################################

        self.text = QTextEdit(self)
        self.setCentralWidget(self.text)

        ############################################################################################

        self.status = self.statusBar()
        self.text.cursorPositionChanged.connect(self.CursorPosition)

        ############################################################################################

        self.setGeometry(self.top,self.bottom,self.width,self.height)
        self.setWindowTitle("MAUS")
        self.setWindowIcon(QIcon("icons/maus.jpg"))
        self.show()

        menubar = self.menuBar()
        file = menubar.addMenu("File")
        # edit = menubar.addMenu("Edit")
        # view = menubar.addMenu("View")
        #
        file.addAction(newAction)
        file.addAction(openAction)
        file.addAction(saveAction)
        #
        # edit.addAction(undoAction)
        # edit.addAction(cutAction)
        # edit.addAction(copyAction)


    def hideToolBar(self):
        global hideTB

        if hideTB == True:
            self.toolbar.hide()
            hideTB = False
        else:
            self.toolbar.show()
            hideTB = True

    def hideFormatBar(self):
        global hideFB

        if hideFB == True:
            self.formatbar.hide()
            hideFB = False
        else:
            self.formatbar.show()
            hideFB = True

    def hideStatusBar(self):
        global hideSB

        if hideSB == True:
            self.status.hide()
            hideSB = False
        else:
            self.status.show()
            hideSB = True

    def New(self):
        self.text.clear()

    def Open(self):
        filename = QFileDialog.getOpenFileName(self, 'Open File')
        f = open(filename, 'r')
        filedata = f.read()
        self.text.setText(filedata)
        f.close()

    def Save(self):
        filename = QFileDialog.getSaveFileName(self, 'Save File')
        f = open(filename, 'w')
        filedata = self.text.toPlainText()
        f.write(filedata)
        f.close()

    def Undo(self):
        self.text.undo()

    def Redo(self):
        self.text.redo()

    def Cut(self):
        self.text.cut()

    def Copy(self):
        self.text.copy()

    def Paste(self):
        self.text.paste()

    def CursorPosition(self):
        line = self.text.textCursor().blockNumber()
        col = self.text.textCursor().columnNumber()
        linecol = ("Line: " + str(line) + " | " + "Column: " + str(col))
        self.status.showMessage(linecol)

    def FontFamily(self, font):
        font = QFont(self.fontFamily.currentFont())
        self.text.setCurrentFont(font)

    def FontSize(self, fsize):
        size = (int(fsize))
        self.text.setFontPointSize(size)

    def FontColor(self):
        c = QColorDialog.getColor()

        self.text.setTextColor(c)

    def FontBackColor(self):
        c = QColorDialog.getColor()

        self.text.setTextBackgroundColor(c)

    def Bold(self):
        w = self.text.fontWeight()
        if w == 50:
            self.text.setFontWeight(QFont.Bold)
        elif w == 75:
            self.text.setFontWeight(QFont.Normal)

    def Italic(self):
        i = self.text.fontItalic()

        if i == False:
            self.text.setFontItalic(True)
        elif i == True:
            self.text.setFontItalic(False)

    def Underline(self):
        ul = self.text.fontUnderline()

        if ul == False:
            self.text.setFontUnderline(True)
        elif ul == True:
            self.text.setFontUnderline(False)

    def alignLeft(self):
        self.text.setAlignment(Qt.AlignLeft)

    def alignRight(self):
        self.text.setAlignment(Qt.AlignRight)

    def alignCenter(self):
        self.text.setAlignment(Qt.AlignCenter)

    def BulletList(self):
        self.text.insertHtml("<ul><li> ...</li></ul>")

    def NumberedList(self):
        self.text.insertHtml("<ol><li> ...</li></ol>")