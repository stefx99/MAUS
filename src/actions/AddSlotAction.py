# Embedded file name: actions\AddSlotAction.py
"""
Created on Apr 13, 2016

@author: Profesor
"""
from PySide2.QtWidgets import QAction, QInputDialog, QApplication, QMessageBox
from PySide2.QtGui import QIcon
from model.GraphicSlot import GraphicSlot
from model.Slot import Slot
from model.TextSlot import TextSlot
from util.InvalidNodeTypeException import InvalidNodeTypeException

class AddSlotAction(QAction):
    """
    classdocs
    """

    def __init__(self, tree):
        """
        Constructor
        """
        super(AddSlotAction, self).__init__('New Slot', None)
        self.setIcon(QIcon('../res/icons/slot.png'))
        self.tree = tree
        self.triggered.connect(self.execute)
        return

    def execute(self):
        slotType, ok = QInputDialog.getItem(self.tree, 'Tip slota', 'Odaberite tip slota', ['', 'text', 'graphic'], 0, False)
        if not ok:
            return
        else:
            if slotType == 'text':
                node = TextSlot('NoviSlot')
            if slotType == 'graphic':
                node = GraphicSlot('NoviSlot')
            parent = QApplication.instance().selection
            try:
                QApplication.instance().model.addChild(parent, node)
            except InvalidNodeTypeException:
                QMessageBox.critical(None, 'Error', 'Slot can only be added to Page!')
                return

            return