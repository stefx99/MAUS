from PySide2.QtCore import Signal
from PySide2.QtWidgets import QWidget
from PySide2.QtGui import QIcon
from src.model.Node import Node
from src.model.InvalidNodeTypeException import InvalidNodeTypeException

class Slot(Node):
    """
    classdocs
    """
    documentChangedSignal = Signal()

    def __init__(self, name):
        """
        Constructor
        """
        super(Slot, self).__init__(name)
        self.viewClass = QWidget

    def getIcon(self):
        return QIcon('src/media/plus.png')

    def addChild(self, child):
        raise InvalidNodeTypeException('Cannot insert nodes of this type')

    def insertChild(self, position, child):
        raise InvalidNodeTypeException('Cannot insert nodes of this type')