from Qt import QtWidgets
from Qt import QtCore
from Qt import QtGui
from Qt.QtGui import QPen, QBrush


class Link(QtWidgets.QGraphicsPathItem):
    """
    """

    def __init__(self,
                 pointA=None,
                 pointB=None,
                 knobA=None,
                 knobB=None):
        """

        Args:
            pointA:
            pointB:
        """
        super(Link, self).__init__()
        self.pointA = pointA or QtCore.QPointF(0, 0)
        self.pointB = pointB or QtCore.QPointF(0, 0)
        self.setSourceKnob(knobA)
        self.setDestinationKnob(knobB)
        self.brush = QBrush(QtCore.Qt.NoBrush)
        self.pen = QPen(QtCore.Qt.yellow)
        self.pen.setWidth(2)
        self.linkPath = None

        self.updatePath()

    def __repr__(self):
        return 'Link from {} to {}'.format(self.pointA, self.pointB)

    def setSourcePos(self, value):
        self.pointA = value

    def setDestinationPos(self, value):
        self.pointB = value

    def setSourceKnob(self, value):
        self._knobA = value

    def setDestinationKnob(self, value):
        self._knobB = value

    def updatePath(self):
        """

        """
        if self._knobA:
            self.pointA = self._knobA.getPos()

        if self._knobB:
            self.pointB = self._knobB.getPos()

        # if self._knobB and self._knobA:
        #     self._knobA.appendLink(self)
        #     self._knobB.appendLink(self)

        self.linkPath = QtGui.QPainterPath(self.pointA)

        self.linkPath.lineTo(self.pointB)
        self.update()

    def paint(self, painter, option, widget):
        """

        Args:
            painter:
            option:
            widget:
        """
        painter.setPen(self.pen)
        painter.setBrush(self.brush)
        self.setPath(self.linkPath)
        painter.drawPath(self.path())



if __name__ == '__main__':
    application = QtGui.QApplication([])
    widget = QtGui.QGraphicsView()
    scene = QtGui.QGraphicsScene()
    scene.setItemIndexMethod(QtGui.QGraphicsScene.NoIndex)
    scene.setSceneRect(0, 0, 400, 400)
    scene.setBackgroundBrush(QBrush(QtCore.Qt.gray, QtCore.Qt.CrossPattern))
    linkItem = Link(QtCore.QPointF(0, 0), QtCore.QPointF(100, 100))
    linkItem.setDestinationPos(QtCore.QPointF(200, 150))
    linkItem.updatePath()
    scene.addItem(linkItem)
    widget.setScene(scene)
    widget.show()
    application.exec_()
