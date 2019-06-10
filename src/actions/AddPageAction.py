# Embedded file name: actions\AddPageAction.py
"""
Created on Apr 13, 2016

@author: Profesor
"""
from PySide2.QtWidgets import QAction, QApplication, QMessageBox
from PySide2.QtGui import QIcon
from model.Page import Page
from util.InvalidNodeTypeException import InvalidNodeTypeException

class AddPageAction(QAction):
    """
    classdocs
    """

    def __init__(self, tree):
        """
        Constructor
        """
        super(AddPageAction, self).__init__('New Page', None)
        self.setIcon(QIcon('../res/icons/page.png'))
        self.tree = tree
        self.triggered.connect(self.execute)
        return

    def execute(self):
        node = Page('NovaStrana')

        try:
            QApplication.instance().model.addChild(parent, node)
        except InvalidNodeTypeException:
            QMessageBox.critical(None, 'Error', 'Page can only be added to Document!')
            return

        return