from PySide2 import *
import sys
from src.model.WorkspaceGUI import WorkspaceGUI
from src.packages.view import MainWindow

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = WorkspaceGUI()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec_())