"""Simple textExit widget to display messages from other widgets.
The messages are directed to the printOut slot.
"""
from Qt import QtWidgets
from Qt import QtCore


class Console(QtWidgets.QWidget):
    """Wrapper around the QTextEdit.
    """
    def __init__(self, parent=None):
        """Init

        Keyword Args:
            parent (QtWidget): The parent QtWidget. Defaults to None.
        """
        super(Console, self).__init__(parent=parent)
        self.layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.layout)
        self.outText = QtWidgets.QTextEdit()
        self.layout.addWidget(self.outText)

    @QtCore.Slot(str)
    def printOut(self, text):
        """Slot for appending text to the textEdit.

        Args:
            text (str): The text that needs to be added to the textEdit.
        """
        self.outText.append(text)
