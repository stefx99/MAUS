# Embedded file name: actions\RenameAction.py
"""
Created on Apr 13, 2016

@author: Profesor
"""
import os
from PySide2.QtWidgets import QAction, QInputDialog, QApplication
from PySide2.QtGui import QIcon
from model.Document import Document
from model.Project import Project
from logging import FileHandler

class RenameAction(QAction):
    """
    classdocs
    """

    def __init__(self, tree):
        """
        Constructor
        """
        super(RenameAction, self).__init__('Rename', None)
        self.tree = tree
        self.triggered.connect(self.execute)
        return

    def execute(self):
        node = QApplication.instance().selection
        if not (isinstance(node, Project) or isinstance(node, Document)):
            return
        else:
            result, ok = QInputDialog.getText(None, 'Rename', 'Name')
            if ok:
                node.setName(result)
            return