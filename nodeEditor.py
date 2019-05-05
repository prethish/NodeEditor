from Qt import QtWidgets
from Qt import QtCore
from Qt.QtGui import QPen, QBrush, QColor

from consoleWidget import Console
from constants import STYLESHEET
from node import Node
from outlinerWidget import Outliner
from parameterWidget import Parameter
from toolbarWidget import ToolBar
import resource


class NodeView(QtWidgets.QGraphicsView):
    """
    """

    def __init__(self, parent=None):
        """

        Args:
            parent:
        """
        super(NodeView, self).__init__(parent=parent)
        scene = QtWidgets.QGraphicsScene(self)
        scene.setItemIndexMethod(QtWidgets.QGraphicsScene.NoIndex)
        scene.setSceneRect(0, 0, 400, 400)
        self.setScene(scene)
        self.setCacheMode(QtWidgets.QGraphicsView.CacheBackground)
        scene.setBackgroundBrush(
            QBrush(QtCore.Qt.black, QtCore.Qt.CrossPattern))

    def contextMenuEvent(self, event):
        popup_menu = QtWidgets.QMenu(self)

        # menu item
        item_clear = QtWidgets.QAction("Clear", self)
        item_clear.triggered.connect(self.clearItems)
        popup_menu.addAction(item_clear)
        popup_menu.exec_(event.globalPos())

    def addItem(self, item):
        """

        """
        self.scene().addItem(item)

    def clearItems(self):
        items = self.scene().items()
        scene = self.scene()
        # TODO : need to implement delete for the node
        for item in items:
            scene.removeItem(item)


class NodeEditor(QtWidgets.QMainWindow):
    """
    """

    def __init__(self, parent=None):
        """

        Args:
            parent:
        """
        super(NodeEditor, self).__init__(parent=parent)
        global STYLESHEET
        with open(STYLESHEET, "r") as fh:
            self.setStyleSheet(fh.read())
        self.nodeView = NodeView()
        self.toolbar = ToolBar()
        self.outliner = Outliner()
        self.console = Console()
        self.paramter = Parameter()
        self.createLayout()
        self.connectSlots()

    def createLayout(self):
        """

        """
        self.centerWidget = QtWidgets.QWidget()
        self.sideLayout = QtWidgets.QVBoxLayout()
        self.sideLayout.addWidget(self.paramter)
        self.sideLayout.addWidget(self.console)
        self.mainLayout = QtWidgets.QHBoxLayout()
        self.mainLayout.addWidget(self.nodeView)
        self.mainLayout.addLayout(self.sideLayout)
        self.centerWidget.setLayout(self.mainLayout)
        self.setCentralWidget(self.centerWidget)
        self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, self.toolbar)
        self.addDockWidget(QtCore.Qt.RightDockWidgetArea, self.outliner)

    def connectSlots(self):
        """

        """
        self.toolbar.button1.clicked.connect(self.addNode)

    def addNode(self):
        newNode = Node('Test', ['InAttr', 'InAttr2'], [
                       'OutAttr', 'OutAttr3', 'OutAttr2'])
        self.nodeView.addItem(newNode)
        self.paramter.updateParameters(newNode)
        newNode.message.connect(self.console.printOut)


if __name__ == '__main__':
    application = QtWidgets.QApplication([])
    widget = NodeEditor()
    widget.show()
    application.exec_()
