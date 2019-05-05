"""Paramter widget to display the parameters.
TODO: display the values of the parameters.
"""
from Qt import QtWidgets


class CustomComboBox(QtWidgets.QWidget):
    """Combobox with the text.
    """

    def __init__(self, text='default',
                 items='Dummmy', parent=None):
        """Constructor for CustomComboBox"""
        super(CustomComboBox, self).__init__(parent=parent)
        self.layout = QtWidgets.QHBoxLayout()
        self.setLayout(self.layout)
        self.label = QtWidgets.QLabel(text)
        self.comboBox = QtWidgets.QComboBox()
        self.populateComboBox(items)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.comboBox)

    def populateComboBox(self, items):
        self.comboBox.clear()
        self.comboBox.addItems(items)


class Parameter(QtWidgets.QWidget):
    """ Parameter Widget.
    """

    def __init__(self, parent=None):
        """
        """
        super(Parameter, self).__init__(parent=parent)
        self.layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.layout)
        self.grpBx = QtWidgets.QGroupBox('Parameters')
        self.layout.addWidget(self.grpBx)
        self.grpLayout = QtWidgets.QVBoxLayout()
        self.inAttrs = CustomComboBox('In Attrs')
        self.outAttrs = CustomComboBox('out Attrs')
        self.grpLayout.addWidget(self.inAttrs)
        self.grpLayout.addWidget(self.outAttrs)
        self.grpBx.setLayout(self.grpLayout)

    def updateParameters(self, nodeObj):
        self.grpBx.setTitle(nodeObj.name)
        self.inAttrs.populateComboBox(nodeObj.inAttrs)
        self.outAttrs.populateComboBox(nodeObj.outAttrs)
