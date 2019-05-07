"""Knobs defines the QGraphicsItem that serves as the point
of connection between nodes using links(QGraphics line)
"""
from _core.Qt import QtWidgets
from _core.Qt import QtCore
from _core.Qt.QtGui import QPen, QBrush, QColor

from widgets.link import Link


class Knob(QtWidgets.QGraphicsObject):
    """"Knobs defines the QGraphicsItem that serves as the point
    of connection between nodes using links(QGraphics line).
    """
    # type information is used by qgraphicsitem_cast() to distinguish between types.
    itemType = QtWidgets.QGraphicsItem.UserType + 1
    # defines the colors for the knob.
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
        """Init

        Args:
            name (str): name of the knob

        Keyword Args:
            x (int): X position in QGraphicsView.
            y (int): Y position in QGraphicsView.
            parent (QGraphicsItem): The parent QGraphicsItem
        """
        super(Knob, self).__init__(parent=parent)
        self._color = self.knobState['normal']
        self._radius = 10
        # Store all the links so that moving the knob will
        # cause the link to be updated.
        self._links = []
        # We create a link from a knob to the position of the mouse
        # when the mousePressevent happens. When the mouse is released
        # we check to see if there is knob there, else destroy the link.
        self.newLink = None
        self._name = name
        self.x = x or 0
        self.y = y or 0
        # flags
        self.setFlag(QtWidgets.QGraphicsItem.ItemSendsScenePositionChanges)
        # enable hover mouse events
        self.setAcceptHoverEvents(True)

    def __str__(self):
        """String representation for the knob.

        Returns:
            str: The knob details.
        """
        return 'Knob: {} with parent {} at position ' \
               '{} with links:\n{}'.format(
                   self._name,
                   self.parentItem(),
                   self.getPos(),
                   '\n'.join([str(l)
                              for l in self._links])
               )

    def getPos(self):
        """Returns the current position of the knob.

        Returns:
            QPointF: The x,y pos of the knob.
        """

        return self.mapToScene(self.rect().center())

    def boundingRect(self):
        """Overriding the default boundingRect based on the
        radius

        Returns:
            QRectF. The bouding box of the node
        """
        return QtCore.QRectF(self.x, self.y, self._radius, self._radius)

    def rect(self):
        return self.boundingRect()

    def paint(self, painter, option, widget):
        """Overriding the default paint.
        Paints the contents of an item in local coordinates.

        Args:
            painter (QPainter):
            option (QStyleOptionGraphicsItem):
            widget (QWidget):
        """
        painter.setPen(QPen(QtCore.Qt.white))
        painter.setBrush(QBrush(self._color))
        painter.drawEllipse(self.boundingRect())

    def hoverEnterEvent(self, event):
        """Overriding the default hover.

        Args:
            event(QGraphicsSceneHoverEvent):
        """
        self._color = self.knobState['hover']
        self.update()

    def hoverLeaveEvent(self, event):
        """Overriding the default hover.

        Args:
            event(QGraphicsSceneHoverEvent):
        """
        self._color = self.knobState['normal']
        self.update()

    def mousePressEvent(self, event):
        """Overriding the default mousePress.
        Create a new link from the knob to the mouse position.

        Args:
            event(QGraphicsSceneMouseEvent):
        """
        self._color = self.knobState['selected']
        if not self.newLink:
            pointA = self.mapToScene(self.rect().center())
            pointB = self.mapToScene(event.pos())
            self.newLink = Link(pointA, pointB)
            self.scene().addItem(self.newLink)
        self.update()

    def mouseMoveEvent(self, event):
        """Overriding the default mousePress.
        Update the link with the mouse position.

        Args:
            event(QGraphicsSceneMouseEvent):
        """
        self.newLink.setDestinationPos(self.mapToScene(event.pos()))
        self.newLink.updatePath()
        self.update()

    def mouseReleaseEvent(self, event):
        """Overriding the default mousePress.
        Check if the link needs to be connected to another knob
        or destroyed.

        Args:
            event(QGraphicsSceneMouseEvent):
        """
        self._color = self.knobState['normal']
        self.scene().removeItem(self.newLink)
        itemUnderMouse = self.scene().itemAt(self.mapToScene(event.pos()))
        self.message.emit(str(itemUnderMouse) or 'No knob found to connect')
        if isinstance(itemUnderMouse, Knob):
            link = Link(knobA=self, knobB=itemUnderMouse)
            link.updatePath()
            self.appendLink(link)
            itemUnderMouse.appendLink(link)
            self.scene().addItem(link)

        self.newLink = None
        self.update()

    def itemChange(self, change, value):
        """Overriding the default itemChange.
        Update the links if the knob moves.

        Args:
            change (GraphicsItemChange):
            value (object):

        Returns:
            object:
        """
        if change == QtWidgets.QGraphicsItem.ItemScenePositionHasChanged:
            for link in self._links:
                link.updatePath()
        return value

    def type(self):
        """Defines the custom userType.

        Returns:
            int:  type of an item as an int.
        """
        return self.itemType

    def appendLink(self, link):
        """Add the newLink to the knob so that we
        can update it when the knob moves.

        Args:
            link (link.Link): Custom link object.
        """
        self._links.append(link)
