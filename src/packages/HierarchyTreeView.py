from PySide2.QtCore import QModelIndex, Qt
from PySide2.QtWidgets import QTreeView, QMenu, QAction, QWidget, QAbstractItemView, QInputDialog, QMessageBox, QApplication
from PySide2 import QtWidgets
from PySide2.QtWidgets import QMdiArea
import os
from src.model.Chapter import Chapter
from src.model.Node import Node
from src.model.Page import Page
from src.model.Slot import Slot

class HierarchyTreeView(QTreeView):
    """
    Grafički prikaz hijerarhijskog stabla uz implementiran kontekstni meni
    """

    def __init__(self):
        """
        Konstruktor

        Uključuje opciju prikazivanja kontekstnog menija.
        """
        super(HierarchyTreeView, self).__init__()

        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.openMenu)
        self.chapterListName = []


    def openMenu(self, position):
        """
        Metoda povezana na customContextMenuRequested. Kreira kontekstni meni sa akcijama dodavanja, brisanja i promene naziva elemenata.
        Kontekstni meni se prikazuje na poziciji na kojoj se nalazio kursor miša.
        Args:
            position(QPoint): pozicija kursora miša
        """
        self.contextMenu = QMenu()
        newMenu = QMenu("New")
        self.contextMenu.addMenu(newMenu)

        insertMenu = QMenu("Insert")
        self.contextMenu.addMenu(insertMenu)

        actionInsertAboveChapter = QAction("Insert Chapter Above",None)
        actionInsertAboveChapter.triggered.connect(self.insertChapterAbove)

        actionInsertBellowChapter = QAction("Insert Chapter Bellow",None)
        actionInsertBellowChapter.triggered.connect(self.insertChapterBellow)

        actionInsertAbovePage = QAction("Insert Page Above",None)
        actionInsertAbovePage.triggered.connect(self.insertPageAbove)

        actionInsertBellowPage = QAction("Insert Page Bellow",None)
        actionInsertBellowPage.triggered.connect(self.insertPageBellow)

        actionInsertPage = QAction("Insert Page",None)
        actionInsertPage.triggered.connect(self.addPage)

        actionShowDialog = QAction("Rename", None)
        actionShowDialog.triggered.connect(self.showDialog)

        actionNewChapter = QAction("New Chapter",None)
        actionNewChapter.triggered.connect(self.addChapter)

        actionNewProj = QAction("New Page", None)
        actionNewProj.triggered.connect(self.addPage)

        actionRemProj = QAction("Delete", None)
        actionRemProj.triggered.connect(self.removeConfirmDialog)

        if not self.currentIndex().isValid():
            newMenu.addAction(actionNewChapter)
            insertMenu.menuAction().setVisible(False)

        else:
            if isinstance(self.currentIndex().internalPointer(),Page):
                newMenu.menuAction().setVisible(False)
                self.contextMenu.hideTearOffMenu()
                insertMenu.addAction(actionInsertAbovePage)
                insertMenu.addAction(actionInsertBellowPage)
                # self.contextMenu.addAction(actionShowDialog)
                self.contextMenu.addAction(actionRemProj)
            elif isinstance(self.currentIndex().internalPointer(),Slot):
                insertMenu.menuAction().setVisible(False)
                newMenu.menuAction().setVisible(False)
                self.contextMenu.addAction(actionShowDialog)
            else:
                newMenu.addAction(actionNewProj)
                insertMenu.addAction(actionInsertAboveChapter)
                insertMenu.addAction(actionInsertBellowChapter)
                self.contextMenu.addAction(actionShowDialog)
                self.contextMenu.addAction(actionRemProj)


        self.contextMenu.exec_(self.viewport().mapToGlobal(position))

    def insertPageAbove(self):
        model = self.model()

        text, ok = QInputDialog.getText(self, "New page", "Type new page name:")

        layoutGrid, okk = QInputDialog.getItem(self, "Setting up page layout", "Choose layout",
                                               ["2x2", "2x3", "2x4", "3x2", "4x2"], 0, False)

        if ok and okk:
            if text == "":
                msgBox = QtWidgets.QMessageBox(self)
                msgBox.setWindowTitle(msgBox.tr("Error"))
                msgBox.setText('Page must have a name.')
                msgBox.show();
                return False
            else:
                node = Page(text)

                lay = layoutGrid.split('x')

                self.addSlots(node, int(lay[0]), int(lay[1]))

                if not self.currentIndex().isValid():
                    try:
                        model.insertRow(model.rowCount(self.currentIndex()), node)
                    except Exception:
                        msgBox = QtWidgets.QMessageBox(self)
                        msgBox.setWindowTitle(msgBox.tr("Error"))
                        msgBox.setText('Unavailable name.')
                        msgBox.show();
                        return False
                else:
                    try:
                        model.insertRow(self.currentIndex().row(), node, self.currentIndex().parent())
                    except Exception:
                        msgBox = QtWidgets.QMessageBox(self)
                        msgBox.setWindowTitle(msgBox.tr("Error"))
                        msgBox.setText('Unavailable name.')
                        msgBox.show();
                        return False
        else:
            return False

        self.expand(self.currentIndex())

    def insertPageBellow(self):
        model = self.model()

        text, ok = QInputDialog.getText(self, "New page", "Type new page name:")

        layoutGrid, okk = QInputDialog.getItem(self, "Setting up page layout", "Choose layout",
                                               ["2x2", "2x3", "2x4", "3x2", "4x2"], 0, False)

        if ok and okk:
            if text == "":
                msgBox = QtWidgets.QMessageBox(self)
                msgBox.setWindowTitle(msgBox.tr("Error"))
                msgBox.setText('Page must have a name.')
                msgBox.show();
                return False
            else:
                node = Page(text)

                lay = layoutGrid.split('x')

                self.addSlots(node, int(lay[0]), int(lay[1]))

                if not self.currentIndex().isValid():
                    try:
                        model.insertRow(model.rowCount(self.currentIndex()), node)
                    except Exception:
                        msgBox = QtWidgets.QMessageBox(self)
                        msgBox.setWindowTitle(msgBox.tr("Error"))
                        msgBox.setText('Unavailable name.')
                        msgBox.show();
                        return False
                else:
                    try:
                        model.insertRow(self.currentIndex().row()+1, node, self.currentIndex().parent())
                    except Exception:
                        msgBox = QtWidgets.QMessageBox(self)
                        msgBox.setWindowTitle(msgBox.tr("Error"))
                        msgBox.setText('Unavailable name.')
                        msgBox.show();
                        return False
        else:
            return False

        self.expand(self.currentIndex())

    def insertChapterAbove(self):
        model = self.model()

        dialog = QInputDialog()
        dialog.setWindowTitle("New Chapter")
        dialog.setLabelText("Type new chapter name:")
        dialog.open()

        text, ok = dialog.getText(self, "New Chapter", "Type new chapter name:")

        if ok:
            if text == "":
                msgBox = QtWidgets.QMessageBox(self)
                msgBox.setWindowTitle(msgBox.tr("Error"))
                msgBox.setText('File must have a name.')
                msgBox.show();
                return False
            else:
                node = Chapter(text)
                if not self.currentIndex().isValid():
                    try:
                        model.insertRow(model.rowCount(self.currentIndex()), node)
                        self.chapterListName.append(text)
                    except Exception:
                        msgBox = QtWidgets.QMessageBox(self)
                        msgBox.setWindowTitle(msgBox.tr("Error"))
                        msgBox.setText('Unavailable name.')
                        msgBox.show();
                        return False
                else:
                    try:
                        model.insertRow(self.currentIndex().row(), node, self.currentIndex().parent())
                        self.chapterListName.append(text)
                    except Exception:
                        msgBox = QtWidgets.QMessageBox(self)
                        msgBox.setWindowTitle(msgBox.tr("Error"))
                        msgBox.setText('Unavailable name.')
                        msgBox.show();
                        return False
        else:
            return False

        self.expand(self.currentIndex())

    def insertChapterBellow(self):
        model = self.model()

        dialog = QInputDialog()
        dialog.setWindowTitle("New Chapter")
        dialog.setLabelText("Type new chapter name:")
        dialog.open()

        text, ok = dialog.getText(self, "New Chapter", "Type new chapter name:")

        if ok:
            if text == "":
                msgBox = QtWidgets.QMessageBox(self)
                msgBox.setWindowTitle(msgBox.tr("Error"))
                msgBox.setText('File must have a name.')
                msgBox.show();
                return False
            else:
                node = Chapter(text)
                if not self.currentIndex().isValid():
                    try:
                        model.insertRow(model.rowCount(self.currentIndex()), node)
                        self.chapterListName.append(text)
                    except Exception:
                        msgBox = QtWidgets.QMessageBox(self)
                        msgBox.setWindowTitle(msgBox.tr("Error"))
                        msgBox.setText('Unavailable name.')
                        msgBox.show();
                        return False
                else:
                    try:
                        model.insertRow(self.currentIndex().row()+1, node, self.currentIndex().parent())
                        self.chapterListName.append(text)
                    except Exception:
                        msgBox = QtWidgets.QMessageBox(self)
                        msgBox.setWindowTitle(msgBox.tr("Error"))
                        msgBox.setText('Unavailable name.')
                        msgBox.show();
                        return False
        else:
            return False

        self.expand(self.currentIndex())

    def renameChapter(self):
        model = self.model()

        dialog = QInputDialog()
        dialog.setWindowTitle("New Chapter")
        dialog.setLabelText("Type new chapter name:")
        dialog.open()

        text, ok = dialog.getText(self, "New Chapter", "Type new chapter name:")

        if ok:
            if text == "":
                msgBox = QtWidgets.QMessageBox(self)
                msgBox.setWindowTitle(msgBox.tr("Error"))
                msgBox.setText('File must have a name.')
                msgBox.show()
                return False
            else:
                if model.checkName(text,self.currentIndex().internalPointer().getParent()):
                    msgBox = QtWidgets.QMessageBox(self)
                    msgBox.setWindowTitle(msgBox.tr("Error"))
                    msgBox.setText('Unavailable name.')
                    msgBox.show()
                    return False

                else:
                    try:
                        self.currentIndex().internalPointer().setName(text)
                    except Exception:
                        msgBox = QtWidgets.QMessageBox(self)
                        msgBox.setWindowTitle(msgBox.tr("Error"))
                        msgBox.setText('Unavailable name.')
                        msgBox.show();
                        return False
        else:
            return False

        self.expand(self.currentIndex())

    def addChapter(self):
        model = self.model()

        dialog = QInputDialog()
        dialog.setWindowTitle("New Chapter")
        dialog.setLabelText("Type new chapter name:")
        dialog.open()

        text, ok = dialog.getText(self,"New Chapter","Type new chapter name:")

        if ok:
            if text == "":
                msgBox = QtWidgets.QMessageBox(self)
                msgBox.setWindowTitle(msgBox.tr("Error"))
                msgBox.setText('File must have a name.')
                msgBox.show()
                return False
            else:
                node = Chapter(text)
                if not self.currentIndex().isValid():
                    try:
                        model.insertRow(model.rowCount(self.currentIndex()), node)
                        self.chapterListName.append(text)
                    except Exception:
                        msgBox = QtWidgets.QMessageBox(self)
                        msgBox.setWindowTitle(msgBox.tr("Error"))
                        msgBox.setText('Unavailable name.')
                        msgBox.show();
                        return False
                else:
                    try:
                        model.insertRow(model.rowCount(self.currentIndex()), node, self.currentIndex())
                        self.chapterListName.append(text)
                    except Exception:
                        msgBox = QtWidgets.QMessageBox(self)
                        msgBox.setWindowTitle(msgBox.tr("Error"))
                        msgBox.setText('Unavailable name.')
                        msgBox.show();
                        return False
        else:
            return False

        self.expand(self.currentIndex())


    def addPage(self):
        model = self.model()

        text, ok = QInputDialog.getText(self, "New page", "Type new page name:")

        layoutGrid, okk = QInputDialog.getItem(self, "Setting up page layout", "Choose layout",["2x2","2x3","2x4","3x2","4x2"], 0, False)

        if ok and okk:
            if text == "":
                msgBox = QtWidgets.QMessageBox(self)
                msgBox.setWindowTitle(msgBox.tr("Error"))
                msgBox.setText('Page must have a name.')
                msgBox.show();
                return False
            else:
                node = Page(text)

                lay = layoutGrid.split('x')

                self.addSlots(node, int(lay[0]), int(lay[1]))

                if not self.currentIndex().isValid():
                    try:
                        model.insertRow(model.rowCount(self.currentIndex()), node)
                    except Exception:
                        msgBox = QtWidgets.QMessageBox(self)
                        msgBox.setWindowTitle(msgBox.tr("Error"))
                        msgBox.setText('Unavailable name.')
                        msgBox.show();
                        return False
                else:
                    try:
                        model.insertRow(model.rowCount(self.currentIndex()), node, self.currentIndex())
                    except Exception:
                        msgBox = QtWidgets.QMessageBox(self)
                        msgBox.setWindowTitle(msgBox.tr("Error"))
                        msgBox.setText('Unavailable name.')
                        msgBox.show();
                        return False
        else:
            return False

        self.expand(self.currentIndex())

    def renameNodeDialog(self):
        self.currentIndex()

    def removeNode(self):

        model = self.model()


        model.removeRow(self.currentIndex().internalPointer().getIndex(), self.currentIndex().parent())

    def mousePressEvent(self, event):
        """
        Redefinisanje mouse pressed event-a.
        Urađeno jer default-na implementacija rukovanja ovim događajem ne podrazumeva deselekciju elementa stabla prilikom klika na praznu površinu.
        """
        if(self.selectionMode() == QAbstractItemView.SingleSelection):
            self.clearSelection()
            self.setCurrentIndex(QModelIndex())
        super(HierarchyTreeView, self).mousePressEvent(event)

    def showDialog(self):

        dialog = QInputDialog()
        dialog.setWindowTitle("Rename node")
        dialog.setLabelText("Type new package name:")
        dialog.open()

        text ,ok = dialog.getText(self, "Rename node", "Type new package name:")

        if ok:
            if text == "":
                msgBox = QtWidgets.QMessageBox(self)
                msgBox.setWindowTitle(msgBox.tr("Error"))
                msgBox.setText('Invalid name.')
                msgBox.show()
                return False
            elif text in self.chapterListName:
                msgBox = QtWidgets.QMessageBox(self)
                msgBox.setWindowTitle(msgBox.tr("Error"))
                msgBox.setText('Invalid name.')
                msgBox.show()
                return False
            else:
                model = self.model()
                if model.checkName(text,self.currentIndex().internalPointer().getParent()):
                    msgBox = QtWidgets.QMessageBox(self)
                    msgBox.setWindowTitle(msgBox.tr("Error"))
                    msgBox.setText('Unavailable name.')
                    msgBox.show()
                    #NE RADI
                else:
                    self.currentIndex().internalPointer().setName(text)

        else:
            return False

    def removeConfirmDialog(self):
        msgBox = QMessageBox()
        msgBox.setText("The package will be deleted.")
        msgBox.setInformativeText("Do you want to delete package?")
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No )
        msgBox.setDefaultButton(QMessageBox.No)

        ret = msgBox.exec_()

        if ret == QMessageBox.Yes:
            self.removeNode()
        elif ret == QMessageBox.No:
            return False

        else:
            return  False

    def addSlots(self,parent, width, height):

        for i in range(width*height):
            node = Slot("Slot"+ str(i))
            parent.addChild(node)
