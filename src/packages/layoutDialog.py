from PySide2.QtWidgets import QInputDialog, QComboBox, QVBoxLayout, QPushButton


class layoutDialog(QInputDialog):


    def __init__(self):
        super(layoutDialog, self).__init__()
        self.setWindowTitle("Layout")

        button = QPushButton("Enter")
        dropdown = selectMenu()

        layout = QVBoxLayout()
        layout.addWidget(dropdown)
        layout.addWidget(button)
        self.setLayout(layout)





class selectMenu(QComboBox):

    def __init__(self):
        super(selectMenu, self).__init__()

        self.addItem("Width: 2 column; Height: 4 column", "2x4")
        self.addItem("Width: 1 column; Height: 4 column", "1x4")
        self.addItem("Width: 3 column; Height: 4 column", "3x4")
        self.addItem("Width: 2 column; Height: 2 column", "2x2")
        self.addItem("Width: 1 column; Height: 2 column", "1x2")



