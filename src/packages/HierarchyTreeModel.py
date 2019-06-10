from PySide2.QtCore import QAbstractItemModel, QModelIndex, Qt
from PySide2.QtGui import QIcon
from PySide2 import QtWidgets



class HierarchyTreeModel(QAbstractItemModel):
    '''
    Model hijerarhijskog stabla
    
    Args:
      root (Node): korenski čvor

    Attributes:
      root (Node): korenski čvor
    
    '''


    def __init__(self, root):
        '''
        Konstruktor
        
        Args:
            root(Node): korenski čvor stabla
        '''
        super(HierarchyTreeModel, self).__init__()
        self.root = root
        
    def rowCount(self, parent):
        """
        Vraća broj redova (podelemenata) elementa stabla
        
        Args:
            parent(QModelIndex): indeks elementa čiji se broj podelemenata traži
            
        Return: 
            Broj elemenata
        """
        if not parent.isValid():
            parentNode = self.root
        else:
            parentNode = parent.internalPointer()
        
        return parentNode.childCount()
    
    def columnCount(self, parent):
        """
        Vraća broj kolona elementa stabla
        
        Args:
            parent(QModelIndex): indeks elementa čiji se broj kolona
            
        Return: 
            Za model namenjen kreiranju stabla uvek vraća 1
        """
        return 1
    
    def data(self, index, role):
        """
        Vraća podatke iz modela za prikaz u viewer-u
        
        Args:
            index(QModelIndex): indeks elementa čiji se podaci traže
            role(QtCore.Qt.ItemDataRole): vrsta podataka koji se traže
            
        Return: 
            Naziv čvora za DisplayRole, ikonica za DecorationRole, None za ostalo
            
        TODO: omogućiti da se ikonica koja će biti prikazana dobije iz odgovarajuće klase modela (klase naslednice Node klase) 
        """
        if not index.isValid():
            return None
        
        node = index.internalPointer()
        
        if role == Qt.DisplayRole:
            return node.getName()
        
        if role == Qt.DecorationRole:
            return node.getIcon()
    
    def headerData(self, section, orientation, role):
        """
        Vraća podatke za zaglavlje viewer-a
        
        Args:
            section(int): redni broj reda/kolone zaglavlja
            orientation(QtCore.Qt.Orientation): da li je podatak namenjen prikazu u zaglavlju reda ili kolone
            role(QtCore.Qt.ItemDataRole): vrsta podataka koji se traže
            
        Return: 
            Tekst "PackageExplorer" za DisplayRole, None za ostalo
        """
        if role == Qt.DisplayRole:
            return "Package Explorer" 
    
    def flags(self, index):
        """
        Podešava dozvoljene načine pristupa elementu stabla
        
        Args:
            index(QModelIndex): indeks elementa čije se ponašanje definiše
            
        Return: 
            Dozvoljeni načini pristupa (Qt.ItemFlag) povezani logičkim operatorom "ILI"
        """
        return Qt.ItemIsEnabled | Qt.ItemIsSelectable
    
    def index(self, row, column, parent):
        """
        Kreira QModelIndex 
        
        Args:
            row(int): broj reda elementa
            column(int): broj kolone elementa
            parent(QModelIndex): element u kojem se nalazi element za koji se indeks kreira
            
        Return: 
            QModelIndex sa instancom klase Node kao vrednošću internalPointer-a; Prazan (nevalidan) QModelIndex za nepostojeći child element na toj poziciji 
        """
        if not parent.isValid():
            parentNode = self.root
        else:
            parentNode = parent.internalPointer()
            
        childItem = parentNode.childAt(row)
        if (childItem):
            return self.createIndex(row, 0, childItem)
        else:
            return QModelIndex()
    
    def parent(self, index):
        """
        Vraća indeks roditeljskog elementa
        
        Args:
            index(QModelIndex): indeks elementa čiji se parent traži
            
        Return: 
            QModelIndex sa parent Node-om kao vrednošću internalPointer-a; prazan (nevalidan) QModelIndex ako je index==root 
        """
        node = index.internalPointer()
        parentNode = node.getParent()
        
        if (parentNode == self.root):
            return QModelIndex()
         
        return self.createIndex(parentNode.getIndex(), 0, parentNode)
    
    def insertRow(self, position, row, parent = QModelIndex()):
        """
        Dodavanje novog elementa u stablo
        
        Args:
            position(int): pozicija u listi podelemenata na koju se vrši dodavanje
            row(Node): element koji se dodaje
            parent(QModelIndex): indeks elementa u koji se dodaje
                    
        Return: 
            True za uspešno dodavanje, False za neuspešno 
        """
        if parent.isValid():
            parentNode = parent.internalPointer()
        else:
            parentNode = self.root


        if parentNode.validDepth():

            self.beginInsertRows(parent, position, position)

            success = parentNode.insertChild(position, row)

            self.endInsertRows()

            if self.checkName(row.getName(), parentNode):
                self.removeRow(position, parent)
                raise Exception("Vec postoji")
                # QtWidgets.QDialog().show()
            return success
            # # else:
            #     msgBox = QtWidgets.QMessageBox(self)
            #     msgBox.setWindowTitle(msgBox.tr("Error"))
            #     msgBox.setText('Unavailable name.')
            #     msgBox.show();
            #     return False

        return False
    
    def removeRow(self, position, parent = QModelIndex()):
        """
        Uklanjanje elementa iz stabla
        
        Args:
            position(int): pozicija u listi podelemenata sa koje se uklanja element
            parent(QModelIndex): indeks elementa iz čije liste podelemenata se uklanja element
                    
        Return: 
            True za uspešno uklanjanje, False za neuspešno 
        """
        if parent.isValid():
            parentNode = parent.internalPointer()
        else:
            parentNode = self.root
        
        self.beginRemoveRows(parent, position, position)
        
        success = parentNode.removeChild(position)
        
        self.endRemoveRows()
        
        return success


    def checkName(self, name, parent):
        c = 0
        for child in parent.getChild():
            if child.getName() == name:
                c += 1


        if c > 1:
            return True
        else:
            return False



