# Embedded file name: actions\ImportProjectAction.py
"""
Created on May 29, 2016

@author: Petar
"""
from PySide2.QtWidgets import QAction
from gui.ImportProjectDialog import ImportProjectDialog

class ImportProjectAction(QAction):
    """
    classdocs
    """

    def __init__(self, parent):
        """
        Constructor
        """
        super(ImportProjectAction, self).__init__(parent)
        self.setText('Import Project')
        self.triggered.connect(self.execute)

    def execute(self):
        dlg = ImportProjectDialog()
        dlg.exec_()