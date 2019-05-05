"""Node class represents the node shape and also
defines how the knobs(input and output ports) are parented to main shape.
"""
from Qt import QtWidgets
from Qt import QtCore
from Qt.QtGui import QPen, QBrush, QColor

from knob import Knob


class Node(QtWidgets.QGraphicsObject):
    """ Node class represents the node shape also
    defines how the knobs(input and output ports) are
    parented to main shape.
    It emits a message signal which gives details about
    the current node.
    """
    message = QtCore.Signal(str)

    def __init__(self, name, inAttrs, outAttrs):
        """Init

        Args:
            name (str): The node name.
            inAttrs (list): List of input ports.
            outAttrs (list): List of output ports.
        """
        super(Node, self).__init__()
        self._name = name
        flags = QtWidgets.QGraphicsItem.ItemIsSelectable | \
            QtWidgets.QGraphicsItem.ItemIsMovable
        self.setFlags(flags)
        # The main shape + the knobs.
        self.shapeGrp = None
        # knobs
        self._inKnobs = []
        self._outKnobs = []
        #Style
        self.brush = QBrush(QColor(150, 177, 188))
        self.pen = QPen(QtCore.Qt.darkGray)
        self.pen.setWidth(1)
        self.shapeGrp = None
        #init position
        self.w = 50
        self.h = 80
        self.xPos = 0
        self.yPos = 0
        self._inAttrs = inAttrs
        self._outAttrs = outAttrs
        #Create the shape.
        self.createShape()

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
        """Function that forwards messages to the console.
        Wrote this so that the messages from the knobs get
        routed to the console without having each knob connect
        to the console.

        Args:
            text (str):
        """
        self.message.emit(text)

    def createShape(self):
        """Default Shape of the node.
        """
        # the main rectangle.
        self.shapeGrp = QtCore.QRectF(
            self.xPos,
            self.yPos,
            self.w,
            self.h
        )
        # Display the node name.
        text = QtWidgets.QGraphicsSimpleTextItem(self._name)
        text.setBrush(QBrush(QtCore.Qt.white))
        text.setParentItem(self)
        # Set the position for the top of the node.
        text.setX(self.xPos+self.boundingRect().center().x()/2)
        # generate knobs and space them out.
        for index, attr in enumerate(self._inAttrs):
            k = Knob(attr, self.xPos-10, self.yPos + 12 * index)
            k.setParentItem(self)
            k.message.connect(self.getMessages)

        for index, attr in enumerate(self._outAttrs):
            k = Knob(attr, self.xPos + self.w, self.yPos + 12 * index)
            k.setParentItem(self)
            k.message.connect(self.getMessages)
        self.update()

    def boundingRect(self):
        """Overriding the default boundingRect.


        Returns:
            QRectF. The bouding box of the node
        """
        return QtCore.QRectF(
            self.xPos,
            self.yPos,
            self.w,
            self.h
        )

    def getParameters(self):
        """Public function that returns the
        attributes on a node.

        Returns:
            tuple: 0: The Input attributes, 1: The Output attributes.
        """
        return (self._inAttrs, self._outAttrs)

    def paint(self, painter, option, widget):
        """Overriding the default paint.
        Paints the contents of an item in local coordinates.

        Args:
            painter (QPainter):
            option (QStyleOptionGraphicsItem):
            widget (QWidget):
        """
        # Override the default painter
        painter.setPen(self.pen)
        painter.setBrush(self.brush)
        painter.drawRect(self.shapeGrp)
