from Qt import QtWidgets
from Qt import QtCore
from Qt.QtGui import QPen, QBrush, QColor

from knob import Knob


class Node(QtWidgets.QGraphicsObject):
    """
    """
    message = QtCore.Signal(str)

    def __init__(self, name, inAttrs, outAttrs):
        """

        Args:
            name:
            inAttrs:
            outAttrs:
        """
        super(Node, self).__init__()
        self._name = name
        flags = QtWidgets.QGraphicsItem.ItemIsSelectable | \
            QtWidgets.QGraphicsItem.ItemIsMovable
        self.setFlags(flags)
        self._inKnobs = []
        self._outKnobs = []
        self.brush = QBrush(QColor(150, 177, 188))
        self.pen = QPen(QtCore.Qt.darkGray)
        self.pen.setWidth(1)
        self.shapeGrp = None
        self.w = 50
        self.h = 80
        self.xPos = 0
        self.yPos = 0
        self._inAttrs = inAttrs
        self._outAttrs = outAttrs
        self.updateShape()

    @property
    def name(self):
        return self._name

    @property
    def inAttrs(self):
        return self._inAttrs

    @property
    def outAttrs(self):
        return self._outAttrs

    @QtCore.Slot(str)
    def getMessages(self, text):
        self.message.emit(text)

    def updateShape(self):
        """

        """
        if not self.shapeGrp:

            body = QtCore.QRectF(self.xPos,
                                 self.yPos,
                                 self.w,
                                 self.h
                                 )
            self.shapeGrp = body
            text = QtWidgets.QGraphicsSimpleTextItem(self._name)
            text.setBrush(QBrush(QtCore.Qt.white))
            text.setParentItem(self)
            text.setX(self.xPos+self.boundingRect().center().x()/2)
            n = len(self._inAttrs)
            for index, attr in enumerate(self._inAttrs):
                k = Knob(attr, self.xPos-10, self.yPos + 12 * index)
                k.setParentItem(self)
                k.message.connect(self.getMessages)

            n = len(self._outAttrs)
            for index, attr in enumerate(self._outAttrs):
                k = Knob(attr, self.xPos + self.w, self.yPos + 12 * index)
                k.setParentItem(self)
                k.message.connect(self.getMessages)
        else:
            # provision to add new attrs
            pass
        self.update()

    def boundingRect(self):
        return QtCore.QRectF(self.xPos,
                             self.yPos,
                             self.w,
                             self.h)

    def getParameters(self):
        return (self._inAttrs, self._outAttrs)

    def paint(self, painter, option, widget):
        """

        Args:
            painter:
            option:
            widget:
        """

        painter.setPen(self.pen)
        painter.setBrush(self.brush)
        painter.drawRect(self.shapeGrp)
# TODO implement destructor


if __name__ == '__main__':
    application = QtWidgets.QApplication([])
    widget = QtWidgets.QGraphicsView()
    scene = QtWidgets.QGraphicsScene()
    scene.setItemIndexMethod(QtWidgets.QGraphicsScene.NoIndex)
    scene.setSceneRect(0, 0, 400, 400)
    scene.setBackgroundBrush(QBrush(QtCore.Qt.gray, QtCore.Qt.CrossPattern))
    nodeItem = Node('Test', ['InAttr', 'InAttr2'], [
                    'OutAttr', 'OutAttr3', 'OutAttr2'])
    scene.addItem(nodeItem)
    widget.setScene(scene)
    widget.show()
    application.exec_()
