"""Links defines the line drawn between 2 knobs.
"""
from Qt import QtWidgets
from Qt import QtCore
from Qt import QtGui
from Qt.QtGui import QPen, QBrush


class Link(QtWidgets.QGraphicsPathItem):
    """Links defines the line drawn between 2 knobs.
    """
    def __init__(self,
                 pointA=None,
                 pointB=None,
                 knobA=None,
                 knobB=None):
        """Init. Connect between 2 knobs/2 points.
        We always draw a line between 2 points, in case
        of a knob, the position is used the point.

        Keyword Args:
            pointA (QPointF): The first point.
            pointB (QPointF): The second point.
            knobA (knob.Knob): The first knob.
            knobB (knob.Knob): The second knob.
        """
        super(Link, self).__init__()
        self.pointA = pointA or QtCore.QPointF(0, 0)
        self.pointB = pointB or QtCore.QPointF(0, 0)
        self.setSourceKnob(knobA)
        self.setDestinationKnob(knobB)
        # Style
        self.brush = QBrush(QtCore.Qt.NoBrush)
        self.pen = QPen(QtCore.Qt.yellow)
        self.pen.setWidth(2)
        self.linkPath = None
        self.updatePath()

    def __str__(self):
        """String representation for the link.

        Returns:
            str: The link details.
        """
        return 'Link from {} to {}'.format(self.pointA, self.pointB)

    def setSourcePos(self, value):
        """Setter for the first point.

        Args:
            value (QPointF):
        """
        self.pointA = value

    def setDestinationPos(self, value):
        """Setter for the second point.

        Args:
            value (QPointF):
        """
        self.pointB = value

    def setSourceKnob(self, value):
        """Setter for the first knob.

        Args:
            value (knob.Knob):
        """
        self._knobA = value

    def setDestinationKnob(self, value):
        """Setter for the second knob.

        Args:
            value (knob.Knob):
        """
        self._knobB = value

    def updatePath(self):
        """Draw the path between the points.
        """
        # if knobs, get the position.
        if self._knobA:
            self.pointA = self._knobA.getPos()

        if self._knobB:
            self.pointB = self._knobB.getPos()

        self.linkPath = QtGui.QPainterPath(self.pointA)
        self.linkPath.lineTo(self.pointB)
        self.update()

    def paint(self, painter, option, widget):
        """Overriding the default paint.
        Paints the contents of an item in local coordinates.

        Args:
            painter (QPainter):
            option (QStyleOptionGraphicsItem):
            widget (QWidget):
        """
        painter.setPen(self.pen)
        painter.setBrush(self.brush)
        self.setPath(self.linkPath)
        painter.drawPath(self.path())
