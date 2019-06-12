import os
import pickle

from PyQt5.QtCore import QPoint
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QAction, QApplication, QFileDialog

from src.model.Book import Book
from src.model.Chapter import Chapter
from src.model.Page import Page
from src.model.Slot import Slot
from src.packages.HierarchyTreeModel import HierarchyTreeModel
from src.packages.HierarchyTreeView import HierarchyTreeView
"""
.maus - ekstenzija
"""

class Save(QAction):

    def __init__(self):

        super(Save, self).__init__("Save")
        #self.setIcon(QIcon("../../res/icons/save.png"))
        self.triggered.connect(self.execute)


    def execute(self):
        model = QApplication.instance()
        a =name, filter = QFileDialog.getSaveFileName(None, 'Save graphic file', '.', '*.maus', '', QFileDialog.DontUseNativeDialog)

        if not name:
            pass
        else:
            name = name + '.maus'
            fileObject = open(name,'wb')
            pickle.dump(a,fileObject)
            fileObject.close()

class Open(QAction):

    def __init__(self):

        super(Open, self).__init__("Load")
        #self.setIcon(QIcon("../../res/icons/open.png"))
        self.triggered.connect(self.execute)


    def execute(self):
        # path = str(QFileDialog.getExistingDirectory())
        # if path is None or path is "":
        #     return
        # if (path.split("/")[-1].find(".maus") == -1):
        #     print("Pokusaj otvaranja pogresne vrste fajla. ")
        #     return
        # root = QApplication.instance().selectionModel
        # ime = path.split("/")[-1]
        # doc = Book(ime)
        # for child in root.children:
        #     if (child.name == ime):
        #         print("Dokument sa istim imenom je vec otvoren. ")
        #         return
        # root.addChild(doc)
        # noviPath = path.split("/")
        # noviPath.pop()
        # noviPath = "/".join(noviPath)
        # doc.putanja = noviPath
        # chapteri = [x for x in os.listdir(path) if (os.path.isdir(os.path.join(path, x)))]
        # for i in chapteri:
        #     ch = Chapter(path.split("/")[-1], i)
        #     doc.addChild(ch)
        # for i in range(len(chapteri)):
        #     noviPath = path + "/" + chapteri[i]
        #     stranice = [s for s in os.listdir(noviPath) if (os.path.isdir(os.path.join(noviPath, s)))]
        #     for strana in stranice:
        #         stranica = Page(strana, i + 1)
        #         doc.children[i].addChild(stranica)
        # for i in range(len(chapteri)):
        #     noviPath = path + "/" + chapteri[i]
        #     stranice = [s for s in os.listdir(noviPath) if (os.path.isdir(os.path.join(noviPath, s)))]
        #     for j in range(len(stranice)):
        #         noviPath = path + "/" + chapteri[i] + "/" + stranice[j]
        #         textDocs = [t for t in os.listdir(noviPath) if (os.path.isdir(os.path.join(noviPath, t)))]
        #         print(textDocs)
        #         for t in textDocs:
        #             textDoc = Slot(t, t, i)
        #             imeFajla = t.split(".")
        #             imeFajla[-1] = "html"
        #             imeFajla = ".".join(imeFajla)
        #             tempPath = noviPath + "/" + t + "/" + imeFajla
        #             with open(tempPath, "r") as fajl:
        #                 data = fajl.read()
        #             textDoc.sadrzaj = data
        #             doc.children[i].children[j].addChild(textDoc)


        model = QApplication.instance()


        name, filter = QFileDialog.getOpenFileName(None, 'Load graphic file', '.', '*.maus', '', QFileDialog.DontUseNativeDialog)


        if not name:
            pass
        else:
            input = open(name, 'rb')
           # data = pickle.load(input)
            from src.packages.view import MainWindow

            with input:
                text = input.read()
                self.view = HierarchyTreeModel(Book)
            input.close()
            #model.loadData(data)

    # def actionCalled(self):
    #     '''
    #     Nudi opciju biranja dokumenta i ucitava dokument u workspace ako je validan.
    #
    #     Ukoliko dokument nije validan(nema ekstenziju unimuk) on se nece ucitati i dobicemo poruku da nije validan.
    #
    #     Ukoliko je dokument sa istim imenom vec otvoren u workspace-u, dokument se nece ucitati i dobicemo poruku da dokument sa istim imenom vec postoji.
    #     '''
    #     path = str(QFileDialog.getExistingDirectory())
    #     if path is None or path is "":
    #         return
    #     if (path.split("/")[-1].find(".unimuk") == -1):
    #         print("Pokusaj otvaranja pogresne vrste fajla. ")
    #         return
    #     root = QApplication.instance().selectionModel
    #     ime = path.split("/")[-1]
    #     doc = Document(ime)
    #     for child in root.children:
    #         if(child.name == ime):
    #             print("Dokument sa istim imenom je vec otvoren. ")
    #             return
    #     root.addChild(doc)
    #     noviPath = path.split("/")
    #     noviPath.pop()
    #     noviPath = "/".join(noviPath)
    #     doc.putanja = noviPath
    #     chapteri = [x for x in os.listdir(path) if (os.path.isdir(os.path.join(path, x)))]
    #     for i in chapteri:
    #         ch = Chapter(path.split("/")[-1], i)
    #         doc.addChild(ch)
    #     for i in range(len(chapteri)):
    #         noviPath = path + "/" + chapteri[i]
    #         stranice = [s for s in os.listdir(noviPath) if (os.path.isdir(os.path.join(noviPath, s)))]
    #         for strana in stranice:
    #             stranica = Page(strana, i + 1)
    #             doc.children[i].addChild(stranica)
    #     for i in range(len(chapteri)):
    #         noviPath = path + "/" + chapteri[i]
    #         stranice = [s for s in os.listdir(noviPath) if (os.path.isdir(os.path.join(noviPath, s)))]
    #         for j in range(len(stranice)):
    #             noviPath = path + "/" + chapteri[i] + "/" + stranice[j]
    #             textDocs = [t for t in os.listdir(noviPath) if (os.path.isdir(os.path.join(noviPath, t)))]
    #             print(textDocs)
    #             for t in textDocs:
    #                 textDoc = TextSlot(t, t, i)
    #                 imeFajla = t.split(".")
    #                 imeFajla[-1] = "html"
    #                 imeFajla = ".".join(imeFajla)
    #                 tempPath = noviPath + "/" + t + "/" + imeFajla
    #                 with open(tempPath, "r") as fajl:
    #                     data = fajl.read()
    #                 textDoc.sadrzaj = data
    #                 doc.children[i].children[j].addChild(textDoc)