from PySide2.QtCore import QModelIndex, Qt
from PySide2.QtWidgets import QTreeView, QMenu, QAction, QAbstractItemView

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
        actionRename.triggered.connect(self.renameNode)
        
        actionRemProj = QAction("Delete", None)
        actionRemProj.triggered.connect(self.removeNode)
        
        newMenu.addAction(actionNewProj)
        self.contextMenu.addAction(actionRename)
        self.contextMenu.addAction(actionRemProj)
        
        # prikaz kontekstnog menija
        self.contextMenu.exec_(self.viewport().mapToGlobal(position))
        
    def addNode(self):
        """
            Metoda povezana na triggered signal akcije za kreiranje novog čvora.
             
            TODO: implementirati dijalog za unos naziva, mogućnost dodavanje tipiziranih čvorova i rukovanje situacijom postojanja elementa sa istim nazivom.
        """ 
        model = self.model()
        
        node = Node("NoviCvor")
        
        if not self.currentIndex().isValid():
            model.insertRow(model.rowCount(self.currentIndex()), node)
        else:
            model.insertRow(model.rowCount(self.currentIndex()), node, self.currentIndex())
        self.expand(self.currentIndex())
    
    def removeNode(self):
        """
            Povezana na triggered signal akcije za brisanje čvora.
             
            TODO: implementirati dijalog za potvrdu akcije brisanja.
        """
        model = self.model()
        model.removeRow(self.currentIndex().internalPointer().getIndex(), self.currentIndex().parent())    
        
    def renameNode(self):
        """
            Povezana na triggered signal akcije za promenu naziva čvora.
             
            TODO: implementirati dijalog za unos naziva i rukovanje situacijom postojanja elementa sa istim nazivom.
        """
        self.currentIndex().internalPointer().setName("NOVO")

    def mousePressEvent(self, event):
        """
        Redefinisanje mouse pressed event-a. 
        Urađeno jer default-na implementacija rukovanja ovim događajem ne podrazumeva deselekciju elementa stabla prilikom klika na praznu površinu.
        """
        if(self.selectionMode() == QAbstractItemView.SingleSelection):
            self.clearSelection()
            self.setCurrentIndex(QModelIndex())
        super(HierarchyTreeView, self).mousePressEvent(event)
