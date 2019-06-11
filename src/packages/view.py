from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtWidgets import QMdiArea
import random
import sys
import textwrap
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

        # self.mdi = QMdiArea()
        # self.setMdiWidget(self.mdi)


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

    # def setMdiWidget(self,widget):
    #     print("")
    #     self.show()
    # def addToMdi(self,widget):
    #     self.mdiWidget.addTab(widget,"ime")

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
        subwindow = QtWidgets.QMdiSubWindow()
        subwindow.show()

    def close_application(self):
        sys.exit()

    def editor(self):

        self.textEdit = QtGui.QTextEdit()
        self.setCentralWidget(self.textEdit)

    def helpWindow(self):

        msgBox = QtWidgets.QMessageBox(self)
        msgBox.setWindowTitle(msgBox.tr("Help"))
        h = textwrap.dedent(''' HELP
                1.  Pravljenje Novog Fajla ili Otvaranje Postojećeg Fajla
                File -> New - Otvoriće se prozor koji će vam ponuditi da izaberete direktorijum gde želite novi projekat da napravite.
                Nakon kreiranja otvoriće se workspace koji će biti spreman za rad.
                Druga opcija: Otvaranje postojećeg fajla
                File -> Open - Otvoriće se prozor koji će vam ponuditi da izaberete direktorijum gde se već postojeći fajl nalazi.
                Nakon odabira otvoriće se workspace koji će biti spreman za rad.

                2.  Chapteri (Poglavlja)
                Nakon kreiranja novog radnog mesta ili otvaranja već postojećeg dolazi na red pravljenja novih poglavlja koji će sadržati stranice dokumenata.
                Desnim klikom na stablo (Ako je novi fajl stablo neće biti prikazano nego prazan prostor sa leve strane prozora) iskače meni.
                Na tom meniju uraditi sledeće:
                New -> New Chapter – Otvoriće se prozor koji će da zahteva unos korisnika. Unos koji se traži je novo ime poglavlja.
                Napomena: Ime poglavlja ne može biti prazan unos. Dva poglavlja ne mogu da imaju ista imena!
                Nakon unosa imena uspešno je kreirano novo poglavlje.
                Brisanje: Desni klik na poglavlje -> Delete – Briše poglavlje kao i njegove stranice!
                Promena imena: Desni klik na poglavlje -> Rename – Otvara prozor u kojem se unosi željeno novo ime. Napomena: Ime poglavlja ne može biti prazan unos. Dva poglavlja ne mogu da imaju ista imena!
                Insert Above (Unos iznad) / Insert Bellow (Unos ispod):
                Insert Above: Desni klik na poglavlje -> Insert Above – Pravi novo poglavlje sa željenim imenom i  smešta ga iznad poglavlja na kome je izvršen desni klik. Napomena: Ime poglavlja ne može biti prazan unos. Dva poglavlja ne mogu da imaju ista imena!
                Insert Bellow: Desni klik na poglavlje -> Insert Bellow – Pravi novo poglavlje sa željenim imenom i smešta ga ispod poglavlja na kome je izvršen desni klik. Napomena: Ime poglavlja ne može biti prazan unos. Dva poglavlja ne mogu da imaju ista imena!

                3.  Pageovi (Stranica)
                Nakon kreiranja poglavlja dolazi na red pravljenje novih stranica. Desnim klikom na postojeće poglavlje iskače meni.
                Na tom meniju uraditi sledeće:
                New -> New Page – Otvoriće se prozor koji će da zahteva unos korisnika. Unos koji se traži je novo ime poglavlja. Nakon toga iskaču opcije za slotove (Pogledati poglavlje broj 5.).
                Napomena: Ime poglavlja ne može biti prazan unos. Dva poglavlja ne mogu da imaju ista imena!
                Nakon unosa imena uspešno je kreirano novo poglavlje.
                Brisanje: Desni klik na stranicu -> Delete – Briše stranicu.
                Promena imena: Desni klik na stranicu -> Rename – Otvara prozor u kojem se unosi željeno novo ime. Napomena: Ime poglavlja ne može biti prazan unos. Dva poglavlja ne mogu da imaju ista imena!
                Insert Above (Unos iznad) / Insert Bellow (Unos ispod):
                Insert Above: Desni klik na stranicu -> Insert Above – Pravi novo poglavlje sa željenim imenom i  smešta ga iznad poglavlja na kome je izvršen desni klik. Napomena: Ime poglavlja ne može biti prazan unos. Dva poglavlja ne mogu da imaju ista imena!
                Insert Bellow: Desni klik na stranicu -> Insert Bellow – Pravi novo poglavlje sa željenim imenom i smešta ga ispod poglavlja na kome je izvršen desni klik. Napomena: Ime poglavlja ne može biti prazan unos. Dva poglavlja ne mogu da imaju ista imena!

                4.  Slotovi
                Nakon kreiranja stranice i dodeljivanja imena stranici iskače prozor koji nudi željeni broj slotova na stranici. Nakon odabira slotova u stranici se napravi taj broj slotova.
                Rad sa slotovima:
                Promena imena: Desni klik na slot -> Rename – Otvara prozor u kojem se unosi željeno novo ime.

                Za dodatnu pomoć pogledati dokumentaciju alata - "M A U S.pdf"
                ''')

        msgBox.setText(h)
        msgBox.show()

    def aboutWindow(self):

        msgBox = QtWidgets.QMessageBox(self)
        msgBox.setWindowTitle(msgBox.tr("About"))
        a = textwrap.dedent('''
                MAUS 2019


                Ekipa: Marko Vukotić  Uroš Blagojević  Aleksandar Jovanović  Stefan Manojlović

                Predmet: UUSI #2018-2019

                Profesor: Branko Perišić

                Asistent: Ognjen Francuski        

                '''
                            )
        msgBox.setText(a)
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
