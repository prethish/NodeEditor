"""Module for defining the scenegraph view or nodes in a
hierarchy
TODO: Implement this.
"""

from _core.Qt import QtWidgets, QtCore


class TreeModel(QtCore.QAbstractItemModel):
    def __init__(self):
        super(TreeModel, self).__init__()


class TreeView(QtWidgets.QTreeView):
    def __init__(self, parent=None):
        super(TreeView, self).__init__(parent=parent)


class Outliner(QtWidgets.QDockWidget):
    def __init__(self, parent=None):
        """
        """
        super(Outliner, self).__init__(parent=parent)
        self.setAllowedAreas(QtCore.Qt.RightDockWidgetArea)
        self.widget = self.dummyTreeWidget()
        self.widget.alternatingRowColors()
        self.layout = QtWidgets.QVBoxLayout()
        self.widget.setLayout(self.layout)
        self.setWidget(self.widget)

    def dummyTreeWidget(self):
        """Sample info.
        """
        folderTree = QtWidgets.QTreeWidget()

        header = QtWidgets.QTreeWidgetItem(["Virtual folder tree", "Comment"])
        folderTree.setHeaderItem(header)
        root = QtWidgets.QTreeWidgetItem(folderTree, ["Untagged files"])
        # Data set to column 2, which is not visible
        root.setData(2, QtCore.Qt.EditRole, 'Some hidden data here')
        folder1 = QtWidgets.QTreeWidgetItem(root, ["Interiors"])
        # Data set to column 2, which is not visible
        folder1.setData(2, QtCore.Qt.EditRole, 'Some hidden data here')
        folder2 = QtWidgets.QTreeWidgetItem(root, ["Exteriors"])
        # Data set to column 2, which is not visible
        folder2.setData(2, QtCore.Qt.EditRole, 'Some hidden data here')
        folder1_1 = QtWidgets.QTreeWidgetItem(
            folder1, ["Bathroom", "Seg was here"])
        # Data set to column 2, which is not visible
        folder1_1.setData(2, QtCore.Qt.EditRole, 'Some hidden data here')
        folder1_2 = QtWidgets.QTreeWidgetItem(
            folder1, ["Living room", "Approved by client"])
        folder1_2.setData(2, QtCore.Qt.EditRole, 'Some hidden data here')
        return folderTree
