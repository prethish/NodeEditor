from PySide import QtGui, QtCore


class TreeModel(QtCore.QAbstractItemModel):
    """
    """

    def __init__(self):
        """

        """
        super(TreeModel, self).__init__()


class TreeView(QtGui.QTreeView):
    """
    """

    def __init__(self, parent=None):
        """

        Args:
            parent:
        """
        super(TreeView, self).__init__(parent=parent)


class Outliner(QtGui.QDockWidget):
    """
    """

    def __init__(self, parent=None):
        """

        Args:
            parent:
        """
        super(Outliner, self).__init__(parent=parent)
        self.setAllowedAreas(QtCore.Qt.RightDockWidgetArea)
        self.widget = self.dummyTreeWidget()
        self.widget.alternatingRowColors()
        self.layout = QtGui.QVBoxLayout()
        self.widget.setLayout(self.layout)
        self.setWidget(self.widget)

    def dummyTreeWidget(self):
        folderTree = QtGui.QTreeWidget()

        header = QtGui.QTreeWidgetItem(["Virtual folder tree", "Comment"])

        folderTree.setHeaderItem(header)

        root = QtGui.QTreeWidgetItem(folderTree, ["Untagged files"])
        # Data set to column 2, which is not visible
        root.setData(2, QtCore.Qt.EditRole, 'Some hidden data here')

        folder1 = QtGui.QTreeWidgetItem(root, ["Interiors"])
        # Data set to column 2, which is not visible
        folder1.setData(2, QtCore.Qt.EditRole, 'Some hidden data here')

        folder2 = QtGui.QTreeWidgetItem(root, ["Exteriors"])
        # Data set to column 2, which is not visible
        folder2.setData(2, QtCore.Qt.EditRole, 'Some hidden data here')

        folder1_1 = QtGui.QTreeWidgetItem(
            folder1, ["Bathroom", "Seg was here"])
        # Data set to column 2, which is not visible
        folder1_1.setData(2, QtCore.Qt.EditRole, 'Some hidden data here')

        folder1_2 = QtGui.QTreeWidgetItem(
            folder1, ["Living room", "Approved by client"])
        folder1_2.setData(2, QtCore.Qt.EditRole, 'Some hidden data here')
        return folderTree
