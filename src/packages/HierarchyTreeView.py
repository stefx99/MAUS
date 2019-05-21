from PySide2.QtCore import QModelIndex, Qt
from PySide2.QtWidgets import QTreeView, QMenu, QAction, QAbstractItemView, QInputDialog, QMessageBox
import os
from src.model.Node import Node



class HierarchyTreeView(QTreeView):
    """
    Grafički prikaz hijerarhijskog stabla uz implementiran kontekstni meni
    """


    def __init__(self):
        """
        Konstruktor
        
        Uključuje opciju prikazivanja kontekstnog menija. 
        """
        super(HierarchyTreeView, self).__init__()
        
        # ukljucuje kontekstni meni
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.openMenu)
        
    
    def openMenu(self, position):
        """
        Metoda povezana na customContextMenuRequested. Kreira kontekstni meni sa akcijama dodavanja, brisanja i promene naziva elemenata. 
        Kontekstni meni se prikazuje na poziciji na kojoj se nalazio kursor miša.
        Args: 
            position(QPoint): pozicija kursora miša
        """
        self.contextMenu = QMenu()
        newMenu = QMenu("New") 
        self.contextMenu.addMenu(newMenu)
        
        actionNewProj = QAction("NewProject", None)
        actionNewProj.triggered.connect(self.addNode)
        
        actionRename = QAction("Rename", None)
        actionRename.triggered.connect(self.showDialog)
        
        actionRemProj = QAction("Delete", None)
        actionRemProj.triggered.connect(self.removeConfirmDialog)
        
        newMenu.addAction(actionNewProj)
        self.contextMenu.addAction(actionRename)
        self.contextMenu.addAction(actionRemProj)
        
        # prikaz kontekstnog menija
        self.contextMenu.exec_(self.viewport().mapToGlobal(position))
        


    """
        Dodavanje novog Node-a 
        
        //TODO: Dodati proveru za unikatne nazive 
    """
    def addNode(self):
        model = self.model()

        dialog = QInputDialog()
        dialog.setWindowTitle("New package")
        dialog.setLabelText("Type new package name:")
        dialog.open()

        text, ok = dialog.getText(self, "New package", "Type new package name:")

        node = Node(text)
        if not self.currentIndex().isValid():
            model.insertRow(model.rowCount(self.currentIndex()), node)
        else:
            model.insertRow(model.rowCount(self.currentIndex()), node, self.currentIndex())
        self.expand(self.currentIndex())


        ########


    def renameNodeDialog(self):
        self.currentIndex()
    
    def removeNode(self):

        model = self.model()


        model.removeRow(self.currentIndex().internalPointer().getIndex(), self.currentIndex().parent())    
        



    def mousePressEvent(self, event):
        """
        Redefinisanje mouse pressed event-a. 
        Urađeno jer default-na implementacija rukovanja ovim događajem ne podrazumeva deselekciju elementa stabla prilikom klika na praznu površinu.
        """
        if(self.selectionMode() == QAbstractItemView.SingleSelection):
            self.clearSelection()
            self.setCurrentIndex(QModelIndex())
        super(HierarchyTreeView, self).mousePressEvent(event)



    def showDialog(self):

        dialog = QInputDialog()
        dialog.setWindowTitle("Rename node")
        dialog.setLabelText("Type new package name:")
        dialog.open()

        text ,ok = dialog.getText(self, "Rename node", "Type new package name:")

        if ok:
            if text == "":
                return False
            else:
                self.currentIndex().internalPointer().setName(text)
        else:
            return False

    def removeConfirmDialog(self):
        msgBox = QMessageBox()
        msgBox.setText("The package will be deleted.")
        msgBox.setInformativeText("Do you want to delete package?")
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No )
        msgBox.setDefaultButton(QMessageBox.No)


        ret = msgBox.exec_()

        if ret == QMessageBox.Yes:
            self.removeNode()
        elif ret == QMessageBox.No:
            return False

        else:
            return  False

