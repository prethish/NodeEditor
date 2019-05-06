"""nodeEditor module which contains QtMainWindow App and all the other QWidgets.
"""
import os
from _core.Qt import QtWidgets
from _core.Qt import QtCore
from _core.Qt.QtGui import QPen, QBrush, QColor

from widgets.consoleWidget import Console
from constants import STYLESHEET
from widgets.node import Node
from widgets.outlinerWidget import Outliner
from widgets.parameterWidget import Parameter
from widgets.toolbarWidget import ToolBar
import resource


class NodeView(QtWidgets.QGraphicsView):
    """ 2d Widget(QGraphicsView) for displaying and manupilating nodes.
    TODO : need to implement delete for the selected node
    """
    def __init__(self, parent=None):
        """Init

        Keyword Args:
            parent (QtWidget): The parent QtWidget. Defaults to None.
        """
        super(NodeView, self).__init__(parent=parent)
        scene = QtWidgets.QGraphicsScene(self)
        # set indexing algorithm to NoIndex as its not a static scene
        scene.setItemIndexMethod(QtWidgets.QGraphicsScene.NoIndex)
        scene.setSceneRect(0, 0, 400, 400)
        self.setScene(scene)
        # allocate one pixmap with the full size of the viewport for caching
        self.setCacheMode(QtWidgets.QGraphicsView.CacheBackground)
        # Draw the grid.
        scene.setBackgroundBrush(
            QBrush(QtCore.Qt.black, QtCore.Qt.CrossPattern)
        )

    def contextMenuEvent(self, event):
        """Popup Menu implementation for common graph
        operations.

        Args:
            event (QEvent):
        """
        popup_menu = QtWidgets.QMenu(self)
        # Clear Graph
        item_clear = QtWidgets.QAction("Clear", self)
        item_clear.triggered.connect(self.clearItems)
        popup_menu.addAction(item_clear)
        popup_menu.exec_(event.globalPos())

    def addItem(self, item):
        """Add a node to the node view.

        Args:
            item (QtWidgets.QGraphicsObject): Node
        """
        self.scene().addItem(item)

    def clearItems(self):
        """Clear all the items in QGraphicsScene.
        """
        items = self.scene().items()
        scene = self.scene()

        for item in items:
            scene.removeItem(item)


class NodeEditor(QtWidgets.QMainWindow):
    """The QMainWindow app that contains all the QWidgets.

    List of QWidgtes:
        NodeView: 2d Widget for displaying and manupilating nodes.
        ToolBar: Display buttons for creating and destroying nodes.
        Outliner: Simple Tree view which needs to display the scenegraph(TODO)
        Console: Display messages during node operations for debugging.
        Parameter: Display parameters for a node(TODO)
    """

    def __init__(self, parent=None):
        """Init

        Keyword Args:
            parent (QtWidget): The parent QtWidget. Defaults to None.
        """
        super(NodeEditor, self).__init__(parent=parent)
        stylesheet_path = os.path.join(
            os.path.dirname(__file__),
            STYLESHEET
        )
        with open(stylesheet_path, "r") as fh:
            self.setStyleSheet(fh.read())
        self.nodeView = NodeView()
        self.toolbar = ToolBar()
        self.outliner = Outliner()
        self.console = Console()
        self.paramter = Parameter()
        self.createLayout()
        self.connectSlots()

    def createLayout(self):
        """Create the layout for the MainWindow
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
        """Connect Qt signals and slots of the Widgets.
        """
        # Toolbar node creation connections
        self.toolbar.addNode.clicked.connect(self.addNode)
        self.toolbar.addNode2.clicked.connect(lambda: self.addNode(nodeType=2))

    def addNode(self, nodeType=None):
        """Dummy addNode function to test with the
        parameter widget works as expected.
        """
        if nodeType:
            newNode = Node(
                'Node1',
                ('InAttr', 'InAttr2', 'InAttr3', 'InAttr4'),
                ('OutAttr', 'OutAttr3', 'OutAttr2')
            )
        else:
            newNode = Node(
                'Node2',
                ('InAttr',),
                ('OutAttr',)
            )
        self.nodeView.addItem(newNode)
        self.paramter.updateParameters(newNode)
        newNode.message.connect(self.console.printOut)


if __name__ == '__main__':
    application = QtWidgets.QApplication([])
    widget = NodeEditor()
    widget.show()
    application.exec_()
