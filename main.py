from PyQt5.QtWidgets import QApplication,QLabel,QDialog,QCheckBox,QTextEdit,QPushButton,QFileDialog,QAction
import sys
from PyQt5 import QtWidgets
from src.model.WorkspaceGUI import WorkspaceGUI
from src.packages.view import MainWindow

def proveraWorkspace():
    file = open("src/model/workspace.txt","r")
    line = file.readline()
    delimiter = line.split("|")
    if delimiter[1] == "False":
        app = QApplication(sys.argv)
        window = WorkspaceGUI()
        sys.exit(app.exec_())
    else:
        pass

if __name__ == "__main__":
    proveraWorkspace()
    app = QtWidgets.QApplication([])

    widget = MainWindow()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec_())