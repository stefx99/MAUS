from PyQt5.QtWidgets import QApplication,QLabel,QDialog,QCheckBox,QTextEdit,QPushButton,QFileDialog,QAction
import sys
from PyQt5 import QtWidgets,QtCore
from src.packages.view import MainWindow
from src.model.OpenFileWspace import Open
import pickle

class WorkspaceGUI(QDialog):
    def __init__(self):
        super().__init__()

        self.title = "Workspace Dialog"
        self.x = 500
        self.y = 350
        self.height = 300
        self.width = 800

        self.initUI()

    def initUI(self):
        global checkBox
        global pathText
        self.setWindowTitle(self.title)
        self.setGeometry(self.x,self.y,self.width,self.height)

        workspaceLabel = QLabel("Workspace:",self)
        workspaceLabel.move(70,80)

        pathText = QTextEdit(self)
        pathText.setGeometry(140,78,420,25)

        defaultWorkspaceLabel = QLabel("Set as default workspace",self)
        defaultWorkspaceLabel.move(160,130)

        browseButton = QPushButton("Browse",self)
        browseButton.setGeometry(570,77,105,27)
        browseButton.clicked.connect(self.openDialog)

        launchButton = QPushButton("Launch",self)
        launchButton.setGeometry(510,200,105,27)
        launchButton.clicked.connect(self.buttonClicked)

        checkBox = QCheckBox(self)
        checkBox.move(140,130)

        self.show()

    def openDialog(self):
        self.open = Open()
        self.open.execute()
        file = open("workspace.txt", "r")
        line = file.readline()
        dmtr = line.split("|")
        pathText.append(dmtr[0])
        file.close()

    def buttonClicked(self):
        global pathText
        global checkBox
        if checkBox.isChecked():
            self.setWorkspace()
        self.hide()


    def setWorkspace(self):
        file = open("workspace.txt","r")
        global delimiter
        line = file.readline()
        delimiter = line.split("|")
        file.close()
        file = open("workspace.txt","w")
        delimiter[1] = "True"
        file.write(delimiter[0]+"|"+delimiter[1])
        file.close()

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = WorkspaceGUI()
    sys.exit(App.exec_())
