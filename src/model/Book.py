from PySide2.QtCore import Signal
from src.model.Node import Node
from PySide2.QtGui import QIcon

class Book(Node):
    documentChangedSignal = Signal()

    def __init__(self, name):
        super(Book, self).__init__(name)
        self.layout = None
        self._name = None
        self.elements = {}

    def getIcon(self):
        return QIcon('src/media/book.png')

    def change(self):
        self.documentChangedSignal.emit()