# Embedded file name: actions\RemoveNodeAction.py
"""
Created on Apr 13, 2016

@author: Profesor
"""
from PySide2.QtWidgets import QAction, QInputDialog, QApplication
from PySide2.QtGui import QIcon
from model.Document import Document
from model.Project import Project
from gui.RemoveProjectDialog import RemoveProjectDialog

class RemoveNodeAction(QAction):
    """
    classdocs
    """

    def __init__(self, tree):
        """
        Constructor
        """
        super(RemoveNodeAction, self).__init__('Remove Node', None)
        self.setIcon(QIcon('../res/icons/delete.png'))
        self.tree = tree
        self.triggered.connect(self.execute)
        return

    def execute(self):
        child = QApplication.instance().selection
        if isinstance(child, Project):
            RemoveProjectDialog(child).exec_()
        else:
            QApplication.instance().model.removeChild(child.getParent(), child.getIndex())