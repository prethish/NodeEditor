from Qt import QtWidgets
from Qt import QtCore
from Qt import QtGui


class ToolBar(QtWidgets.QDockWidget):
    """
    """

    def __init__(self, parent=None):
        """

        Args:
            parent:
        """
        super(ToolBar, self).__init__(parent=parent)
        self.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea)
        widget = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout()
        widget.setLayout(layout)
        self.button1 = QtWidgets.QPushButton()
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(":images/Add_List.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off
        )
        self.button1.setIcon(icon)
        layout.addWidget(self.button1)
        self.button2 = QtWidgets.QPushButton()
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(":images/Delete_File.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off
        )
        self.button2.setIcon(icon)
        layout.addWidget(self.button2)
        self.setWidget(widget)
