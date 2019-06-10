# Embedded file name: actions\AddDocumentAction.py
"""
Created on Apr 13, 2016

@author: Profesor
"""
from PySide2.QtWidgets import QAction, QInputDialog, QApplication, QMessageBox
from PySide2.QtGui import QIcon
from model.Document import Document
from util.InvalidNodeTypeException import InvalidNodeTypeException

class AddDocumentAction(QAction):
    """
    classdocs
    """

    def __init__(self, tree):
        """
        Constructor
        """
        super(AddDocumentAction, self).__init__('New Document', None)
        self.setIcon(QIcon('../res/icons/document.png'))
        self.tree = tree
        self.triggered.connect(self.execute)
        return

    def execute(self):
        result, ok = QInputDialog.getText(None, 'Create document', 'Name')
        if ok:
            node = Document(result)
            parent = QApplication.instance().selection
            try:
                QApplication.instance().model.addChild(parent, node)
            except InvalidNodeTypeException:
                QMessageBox.critical(None, 'Error', 'Document can only be added to Project!')
                return

        return