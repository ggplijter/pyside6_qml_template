from PySide6.QtCore import Property, QObject, Signal
import os

class ContentManagerProps(QObject):
    doHotreloadChanged = Signal()

    @Property(bool, notify=doHotreloadChanged)
    def do_hotreload(self) -> bool:
        return os.environ["ENABLE_HOTRELOAD"] == "1"

    # @do_hotreload.setter
    # def do_hotreload(self, _debug: bool):
    #     self.m_debug = _debug
    #     self.debugChanged.emit()


