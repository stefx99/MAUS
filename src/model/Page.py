from PySide2.QtCore import Signal
from src.model.Node import Node
from PySide2.QtGui import QIcon



class Page(Node):


    documentChangedSignal = Signal()

    def __init__(self, name):
        super(Page, self).__init__(name)
        self.layout = None
        self.elements = {}

    def getIcon(self):
        return QIcon('src/media/page.png')


    def change(self):
        self.documentChangedSignal.emit()