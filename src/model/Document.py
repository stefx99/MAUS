import os
from PySide2.QtCore import Signal
from PySide2.QtGui import QIcon
from src.model.Node import Node
from src.model.Page import Page
from src.packages.FileHandler import FileHandler
from src.model.InvalidNodeTypeException import InvalidNodeTypeException

class Document(Node):
    """
    classdocs
    """
    childAddedSignal = Signal(object)
    documentChangedSignal = Signal()

    def __init__(self, name):
        """
        Constructor
        """
        super(Document, self).__init__(name)
        self.saved = True

    def addChild(self, child):
        if isinstance(child, Page):
            super(Document, self).addChild(child)
            child.documentChangedSignal.connect(self.changed)
            self.childAddedSignal.emit(child)
            child.setParent(self)
            self.saved = False
            self.documentChangedSignal.emit()
        else:
            raise InvalidNodeTypeException('Cannot insert nodes of this type')
        self.renumerate()

    def insertChild(self, position, child):
        if isinstance(child, Page):
            super(Document, self).insertChild(position, child)
            child.documentChangedSignal.connect(self.changed)
            self.childAddedSignal.emit(child)
            self.saved = False
            self.documentChangedSignal.emit()
        else:
            raise InvalidNodeTypeException('Cannot insert nodes of this type')
        self.renumerate()

    def removeChild(self, position):
        super(Document, self).removeChild(position)
        self.saved = False
        self.documentChangedSignal.emit()
        self.renumerate()

    def getIcon(self):
        return QIcon('../res/icons/document.png')

    def serializableContent(self):
        content = {}
        pages = []
        for page in self.children:
            pages.append(page.serializableContent())

        content['pages'] = pages
        return content

    def deserialize(self, data):
        for item in data['pages']:
            page = Page('1')
            page.deserialize(item)
            self.addChild(page)

        self.renumerate()

    def setName(self, name):
        oldName = self.name
        super(Document, self).setName(name)
        fh = FileHandler()
        fh.rename(os.path.join(self.getParent().path, self.getParent().name), oldName + '.gmd', name + '.gmd')

    def renumerate(self):
        for idx, item in enumerate(self.children):
            item.setName('Page ' + str(idx + 1))

    def isSaved(self):
        return self.saved

    def changed(self):
        self.saved = False
        self.documentChangedSignal.emit()