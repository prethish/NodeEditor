from PySide import QtGui


class CustomComboBox(QtGui.QWidget):
    """"""

    def __init__(self, text='default', items='Dummmy', parent=None):
        """Constructor for CustomComboBox"""
        super(CustomComboBox, self).__init__(parent=parent)
        self.layout = QtGui.QHBoxLayout()
        self.setLayout(self.layout)
        self.label = QtGui.QLabel(text)
        self.comboBox = QtGui.QComboBox()
        self.populateComboBox(items)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.comboBox)

    def populateComboBox(self, items):
        self.comboBox.clear()
        self.comboBox.addItems(items)


class Parameter(QtGui.QWidget):
    """
    """

    def __init__(self, parent=None):
        """

        Args:
            parent:
        """
        super(Parameter, self).__init__(parent=parent)
        self.layout = QtGui.QVBoxLayout()
        self.setLayout(self.layout)
        self.grpBx = QtGui.QGroupBox('Parameters')
        self.layout.addWidget(self.grpBx)
        self.grpLayout = QtGui.QVBoxLayout()
        self.inAttrs = CustomComboBox('In Attrs')
        self.outAttrs = CustomComboBox('out Attrs')
        self.grpLayout.addWidget(self.inAttrs)
        self.grpLayout.addWidget(self.outAttrs)
        self.grpBx.setLayout(self.grpLayout)

    def updateParameters(self, nodeObj):
        self.grpBx.setTitle(nodeObj.name)
        self.inAttrs.populateComboBox(nodeObj.inAttrs)
        self.outAttrs.populateComboBox(nodeObj.outAttrs)


if __name__ == '__main__':
    application = QtGui.QApplication([])
    widget = Parameter()
    widget.show()
    application.exec_()
