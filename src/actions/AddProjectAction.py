# Embedded file name: actions\AddProjectAction.py
"""
Created on Apr 13, 2016

@author: Profesor
"""
import os
from PySide2.QtWidgets import QAction, QInputDialog, QApplication, QMessageBox, QErrorMessage
from PySide2.QtGui import QIcon
from model.Project import Project
from util.FileHandler import FileHandler
from util.InvalidNodeTypeException import InvalidNodeTypeException

class AddProjectAction(QAction):
    """
    classdocs
    """

    def __init__(self, tree):
        """
        Constructor
        """
        super(AddProjectAction, self).__init__('New Project', None)
        self.setIcon(QIcon('../res/icons/folder.png'))
        self.tree = tree
        self.triggered.connect(self.execute)
        return

    def execute(self):
        result, ok = QInputDialog.getText(None, 'Create project', 'Name')
        fh = FileHandler()
        if ok:
            parent = QApplication.instance().selection
            project = Project(parent.path, result)
            if result in parent.children:
                QMessageBox.critical(None, 'Error', 'Project with same name already exists')
                return
            try:
                QApplication.instance().model.addChild(parent, project)
            except InvalidNodeTypeException:
                QMessageBox.critical(None, 'Error', 'Project can only be added to workspace!')
                return

            if result in fh.getChildList(QApplication.instance().selection.path):
                QApplication.instance().model.removeChild(parent, project.getIndex())
                QMessageBox.critical(None, 'Error', 'Project with same name already exists')
                return 
            fh.createDirectory(QApplication.instance().selection.path, project.name)
        return
    