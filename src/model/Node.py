from PySide2.QtCore import QObject, Signal


class Node(QObject):
    """
    Čvor u stablu, može se koristiti kao root klasa za dokument, projekat, paket...
    
    Args:
      name (str): Naziv čvora.

    Attributes:
      name (str): naziv čvora
      parent (Node): čvor na višem nivou hijerarhije
      children (list(Node)): lista čvorova na nižem nivou hijerarhije
      
    TODO: uraditi tipizaciju čvorova nasleđivanjem klase Node
    """

    childInserted = Signal(int)

    def __init__(self, name):
        '''
        Konstruktor
        
        Args:
            name(int): naziv čvora
        '''
        self.name = name
        self.parent = None
        self.children = []
    
    def setParent(self, parent):
        """
        Postavlja roditeljski čvor
        
        Args:
            parent(Node): roditeljski čvor
        """
        self.parent = parent
    
    def getParent(self):        
        """
        Vraća roditeljski čvor
        
        Return:
            Roditeljski čvor; None ukoliko je element na vrhu hijerarhije
        """
        return self.parent
    
    def setName(self, name):
        """
        Postavlja naziv čvora
        
        Args:
            name(string): naziv čvora
        """
        self.name = name
    
    def getName(self):
        """
        Vraća naziv čvora
        
        Return:
            Naziv čvora
        """
        return self.name
    
    def addChild(self, child):
        """
        Dodaje child na kraj liste
        
        Args:
            child(Node): čvor koji se dodaje
        """
        self.children.append(child)
        child.setParent(self)
        
    def insertChild(self, position, child):
        """
        Ubacuje child na određenu poziciju
        
        Args:
            position(int): pozicija u listi na koju se ubacuje
            child(Node): čvor koji se ubacuje
            
        Return:
            True ako je uspešno ubacivanje, False za neispravnu poziciju
        """
        if position < 0 or position > len(self.children):
            return False
        
        self.children.insert(position, child)
        child.setParent(self)
        return True
    
    def removeChild(self, position):
        """
        Izbacuje child sa određene pozicije
        
        Args:
            position(int): pozicija u listi sa koje se izbacuje
            
        Return:
            True ako je uspešno izbacivanje, False za neispravnu poziciju
        """
        if position < 0 or position > len(self.children)-1:
            return False
        child = self.children.pop(position)
        child.setParent(None)
        
        return True

    def childCount(self):
        """
        Vraća broj child čvorova
        
        Return:
            Broj child čvorova (int)
        """
        return len(self.children)
    
    def childAt(self, row):
        """
        Vraća child čvor na zadatoj poziciji
        
        Args:
            row(int): pozicija čvora u listi podčvorova
            
        Return:
            Čvor na zadatoj poziciji (Node); None za neispravnu poziciju
        """            
        if row < 0 or row > len(self.children)-1:
            return None
        else:
            return self.children[row]
    
    def getIndex(self):
        """
        Vraća poziciju elementa u listi child-ova roditeljskog elementa
        
        Return:
            pozicija u listi child-ova parent čvora
        """
        if self.parent is not None:
            return self.parent.children.index(self)
