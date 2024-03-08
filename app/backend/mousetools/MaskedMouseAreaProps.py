from PySide6.QtCore import Property, QObject, QPoint, QPointF, Signal
from PySide6.QtGui import QImage
from PySide6.QtQml import QQmlFile
from PySide6.QtQuick import QQuickItem

# https://stackoverflow.com/questions/63071403/how-can-i-use-a-mousearea-on-a-shapepath-in-qml

def qBound(low, high, value):
    return max(low, min(high, value))

class MaskedMouseAreaProps(QQuickItem):
    # ispressed               = Signal()
    # released                = Signal()
    # clicked                 = Signal()
    # canceled                = Signal()
    pressedChanged          = Signal()
    maskSourceChanged       = Signal()
    containsMouseChanged    = Signal()
    alphaThresholdChanged   = Signal()

    m_pressed               = False
    m_maskSource            = ""
    m_maskImage             = QImage()
    m_pressPoint            = QPointF(0, 0)
    m_alphaThreshold        = 0.0
    m_containsMouse         = False

    def getPressed(self):
        return self.m_pressed

    def setPressed(self, pressed: bool):
        if self.m_pressed != pressed:
            self.m_pressed = pressed
            self.pressedChanged.emit()

    def getContainsMouse(self):
        return self.m_containsMouse

    def setContainsMouse(self, containsMouse: bool):
        if self.m_containsMouse != containsMouse:
            self.m_containsMouse = containsMouse
            self.containsMouseChanged.emit()

    def getMaskSource(self) -> str:
        return self.m_maskSource

    def setMaskSource(self, source: str):
        if self.m_maskSource != source:
            self.m_maskSource = source
            self.m_maskImage = QImage(QQmlFile.urlToLocalFileOrQrc(source))
            self.maskSourceChanged.emit()

    def getAlphaThreshold(self):
        return self.m_alphaThreshold

    def setAlphaThreshold(self, treshold: float):
        if self.m_alphaThreshold != treshold:
            self.m_alphaThreshold = treshold
            self.alphaThresholdChanged.emit()

    def setScaledImage(self, doScale: bool) -> None:
        if doScale and not self.m_maskImage.isNull():
            self.m_maskImage = self.m_maskImage.scaledToHeight(self.parent().height())
            self.maskSourceChanged.emit()

    pressed         = Property(bool, getPressed, notify=pressedChanged)
    containsMouse   = Property(bool, getContainsMouse, notify=containsMouseChanged)
    maskSource      = Property(str, getMaskSource, setMaskSource, notify=maskSourceChanged)
    alphaThreshold  = Property(float, getAlphaThreshold, setAlphaThreshold, notify=alphaThresholdChanged)
    rescaleImage    = Property(bool, fset=setScaledImage, notify=maskSourceChanged)



