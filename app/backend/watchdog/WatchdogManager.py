import logging

from ...utils.app_paths import FILEPATH_ERROR_DUMP
from PySide6.QtCore import Signal, QObject, Slot
from PySide6.QtGui import QPixmap
from PySide6.QtQml import QmlElement, QQmlApplicationEngine

from datetime import datetime

QML_IMPORT_NAME = "backend.watchdog"
QML_IMPORT_MAJOR_VERSION = 1

logger = logging.getLogger(__name__)

@QmlElement
class WatchdogManager(QObject):

    displayError = Signal(str, str, str)

    def __init__(self, parent=None):
        super(WatchdogManager, self).__init__(parent)

        self.displayError.connect(self.onDisplayError)

    @Slot(str, Exception, str)
    def onDisplayError(self, error_code: str, error_desc: Exception, traceback_txt: str):
        logger.error(f"{error_code} {error_desc}")
        logger.error(traceback_txt)

    @Slot()
    def takeScreenshot(self):
        view = QQmlApplicationEngine.contextForObject(self).engine().rootObjects()[0]
        QPixmap(view.grabWindow()).save(
            str(FILEPATH_ERROR_DUMP).format(
                date_str=datetime.now().strftime("%Y%m%d_%H%M%S")
            )
        )
