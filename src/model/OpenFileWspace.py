from PySide2.QtWidgets import QAction, QApplication, QFileDialog

from src.model.Book import Book
from src.packages.HierarchyTreeModel import HierarchyTreeModel

class Open(QAction):

    def __init__(self):

        super(Open, self).__init__("Load")
        self.triggered.connect(self.execute)


    def execute(self):
        global name
        model = QApplication.instance()

        name = QFileDialog.getExistingDirectory(None,"","")
        self.setWorkspace()

    def setWorkspace(self):
        global name
        file = open("workspace.txt","r")
        global delimiter0
        line = file.readline()
        delimiter0 = line.split("|")
        file.close()
        file = open("workspace.txt","w")
        file.write(name+"|"+delimiter0[1])
        file.close()
