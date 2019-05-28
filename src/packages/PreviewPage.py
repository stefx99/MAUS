import random

from PySide2 import QtWidgets


class PreviewPage(QtWidgets.QWidget):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super().__init__()
        self.initCentralPanel()


    def initCentralPanel(self):
        panel = QtWidgets.QWidget()

        panel.setLayout(QtWidgets.QVBoxLayout())

        self.scroll = QtWidgets.QScrollArea()
        self.scroll.setWidget(panel)
        self.scroll.setWidgetResizable(True)

        for x in range(1, 10):
            panel.layout().addWidget(self.newWidget())



    def newWidget(self):
        new = QtWidgets.QWidget()
        new.setAutoFillBackground(True)
        p = new.palette()
        p.setColor(new.backgroundRole(), self.randomColor())
        new.setPalette(p)
        new.setMinimumHeight(600)
        new.setMinimumWidth(800)

        return new

    def randomColor(self):
        r = lambda: random.randint(0, 255)
        g = lambda: random.randint(0, 255)
        b = lambda: random.randint(0, 255)
        return ('#%02X%02X%02X' % (r(), g(), b()))