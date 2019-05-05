from Qt import QtWidgets
from Qt import QtCore
from Qt.QtGui import QPen, QBrush, QColor

from link import Link


class Knob(QtWidgets.QGraphicsObject):
    """
    """
    itemType = QtWidgets.QGraphicsItem.UserType + 1
    knobState = {
        'normal': QColor(100, 140, 74),
        'hover': QtCore.Qt.yellow,
        'selected': QtCore.Qt.green,
    }
    message = QtCore.Signal(str)

    def __init__(self, name,
                 x=None,
                 y=None,
                 parent=None):
        """

        Args:
            name:
            pos_x:
            pos_y:
            parent:
        """
        super(Knob, self).__init__(parent=parent)
        self._color = self.knobState['normal']
        self._radius = 10
        self._links = []
        self.tempLink = None
        self._name = name
        self.x = x or 0
        self.y = y or 0
        #flags
        self.setFlag(QtWidgets.QGraphicsItem.ItemSendsScenePositionChanges)
        #enable hover mouse events
        self.setAcceptHoverEvents(True)

    def __repr__(self):
        return 'Knob: {} with parent {} at position ' \
               '{} with links:\n{}'.format(self._name,
                                           self.parentItem(),
                                           self.getPos(),
                                           '\n'.join([str(l)
                                                      for l in self._links])
                                           )

    def getPos(self):
        return self.mapToScene(self.rect().center())

    def boundingRect(self):
        return QtCore.QRectF(self.x, self.y, self._radius, self._radius)

    def rect(self):
        return self.boundingRect()

    def paint(self, painter, option, widget):
        """

        Args:
            painter:
            option:
            widget:
        """
        painter.setPen(QPen(QtCore.Qt.white))
        painter.setBrush(QBrush(self._color))
        painter.drawEllipse(self.boundingRect())

    def hoverEnterEvent(self, event):
        """

        Args:
            event:
        """
        self._color = self.knobState['hover']
        self.update()

    def hoverLeaveEvent(self, event):
        """

        Args:
            event:
        """
        self._color = self.knobState['normal']
        self.update()

    def mousePressEvent(self, event):
        """

        Args:
            event:
        """
        self._color = self.knobState['selected']
        if not self.tempLink:
            pointA = self.mapToScene(self.rect().center())
            pointB = self.mapToScene(event.pos())
            self.tempLink = Link(pointA, pointB)
            self.scene().addItem(self.tempLink)
        self.update()

    def mouseMoveEvent(self, event):
        self.tempLink.setDestinationPos(self.mapToScene(event.pos()))
        self.tempLink.updatePath()
        self.update()

    def mouseReleaseEvent(self, event):
        """

        Args:
            event:
        """
        self._color = self.knobState['normal']
        self.scene().removeItem(self.tempLink)
        itemUnderMouse = self.scene().itemAt(self.mapToScene(event.pos()))
        self.message.emit(str(itemUnderMouse) or 'No knob found to connect')
        if isinstance(itemUnderMouse, Knob):
            link = Link(knobA=self, knobB=itemUnderMouse)
            link.updatePath()
            self.appendLink(link)
            itemUnderMouse.appendLink(link)
            self.scene().addItem(link)

        self.tempLink = None
        self.update()

    def itemChange(self, change, value):
        if change == QtWidgets.QGraphicsItem.ItemScenePositionHasChanged:
            for link in self._links:
                link.updatePath()
        return value

    def type(self):
        return self.itemType

    def appendLink(self, link):
        self._links.append(link)


if __name__ == '__main__':
    application = QtGui.QApplication([])
    widget = QtGui.QGraphicsView()
    scene = QtGui.QGraphicsScene()
    scene.setItemIndexMethod(QtGui.QGraphicsScene.NoIndex)
    scene.setSceneRect(0, 0, 400, 400)
    scene.setBackgroundBrush(QBrush(QtCore.Qt.gray, QtCore.Qt.CrossPattern))
    knobItem = Knob('Test1', 10, 10)
    knobItem2 = Knob('Test2', 120, 20)
    knobItem3 = Knob('Test3', 120, 220)
    scene.addItem(knobItem)
    scene.addItem(knobItem2)
    scene.addItem(knobItem3)
    widget.setScene(scene)
    widget.show()
    application.exec_()
