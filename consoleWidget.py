from Qt import QtWidgets
from Qt import QtCore


class Console(QtWidgets.QWidget):
    """
    """

    def __init__(self, parent=None):
        """

        Args:
            parent:
        """
        super(Console, self).__init__(parent=parent)
        self.layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.layout)
        self.outText = QtWidgets.QTextEdit()
        self.layout.addWidget(self.outText)

    @QtCore.Slot(str)
    def printOut(self, text):
        self.outText.append(text)
