from PySide6.QtCore import QPoint, QPointF, Qt, Signal
from PySide6.QtGui import QGuiApplication, QImage, QMouseEvent
from PySide6.QtQml import ListProperty, QmlElement

from .MaskedMouseAreaProps import MaskedMouseAreaProps

QML_IMPORT_NAME = "backend.mousetools"
QML_IMPORT_MAJOR_VERSION = 1


def qBound(low, high, value):
    return max(low, min(high, value))


@QmlElement
class MaskedMouseArea(MaskedMouseAreaProps):
    ispressed = Signal()
    released = Signal()
    clicked = Signal()
    canceled = Signal()

    def __init__(self, parent=None):
        super(MaskedMouseArea, self).__init__(parent)

        self.setAcceptedMouseButtons(Qt.LeftButton)
        self.setAcceptHoverEvents(True)

    def contains(self, point: QPointF) -> bool:
        if not super().contains(point) or self.m_maskImage == self.m_maskImage.isNull():
            return False

        p = point.toPoint()

        if (
            p.x() < 0
            or p.x() >= self.m_maskImage.width()
            or p.y() < 0
            or p.y() >= self.m_maskImage.height()
        ):
            return False

        r = int(qBound(0, 255, self.m_alphaThreshold * 255))
        return self.m_maskImage.pixelColor(p).alpha() > r

    def mousePressEvent(self, event: QMouseEvent) -> None:
        self.setPressed(True)
        self.m_pressPoint = event.pos()
        self.ispressed.emit()

    def touchEvent(self, event):
        self.setPressed(True)
        self.m_pressPoint = event.pos()
        self.ispressed.emit()

    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        self.setPressed(False)
        self.released.emit()

        threshold = QGuiApplication.instance().styleHints().startDragDistance()
        isClick = (threshold >= abs((event.pos().x() - self.m_pressPoint.x()))) and (
            threshold >= abs((event.pos().y() - self.m_pressPoint.y()))
        )

        if isClick:
            self.clicked.emit()

    def mouseUngrabEvent(self) -> None:
        self.setPressed(False)
        self.canceled.emit()

    def touchUngrabEvent(self):
        self.setPressed(False)
        self.canceled.emit()

    def hoverEnterEvent(self, event) -> None:
        self.setContainsMouse(True)

    def hoverLeaveEvent(self, event) -> None:
        self.setContainsMouse(False)
