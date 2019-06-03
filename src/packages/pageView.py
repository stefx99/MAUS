from PySide2.QtWidgets import QScrollArea, QTabWidget, QBoxLayout, QHBoxLayout, QTextEdit, QWidget, QVBoxLayout



class pageView(QScrollArea):

    def __init__(self, page = None):
        super(pageView, self).__init__()
        self._children = []
        self.panel = QWidget()
        self.pageLayout = QVBoxLayout()

        self.panel.setLayout(self.pageLayout)
        self.setWidgetResizable(True)
        self.setWidget(self.panel)

        #self.page = page


        #
        # self.page.childInsertedSignal.connect(self.add_slot)
        # self.page.childRemovedSignal.connect(self.remove_slot)
        # self.page.nameChangedSignal.connect(self.nameChanged)



