from _core.Qt import QtWidgets
from _core.Qt import QtCore
from _core.Qt import QtGui


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
        self.addNode = QtWidgets.QPushButton()
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(":images/Add_List.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off
        )
        self.addNode.setIcon(icon)
        layout.addWidget(self.addNode)
        self.addNode2 = QtWidgets.QPushButton()
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(":images/Delete_File.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off
        )
        self.addNode2.setIcon(icon)
        layout.addWidget(self.addNode2)
        self.setWidget(widget)
