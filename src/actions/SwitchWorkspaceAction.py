# Embedded file name: actions\SwitchWorkspaceAction.py
"""
Created on Apr 18, 2016

@author: Petar
"""
from PySide2.QtWidgets import QAction, QApplication
from gui.WorkspaceDialog import WorkspaceDialog
from model.Workspace import Workspace

class SwitchWorkspaceAction(QAction):
    """
    classdocs
    """

    def __init__(self, parent):
        """
        Constructor
        """
        super(SwitchWorkspaceAction, self).__init__('Switch WS', parent)
        self.triggered.connect(self.execute)

    def execute(self):
        dlgWs = WorkspaceDialog(QApplication.instance().profile)
        if dlgWs.exec_():
            result = dlgWs.getResult()
            QApplication.instance().workspace = result['ws']
            QApplication.instance().model.root = Workspace(result['ws'])
            QApplication.instance().main_window.reloadWS()