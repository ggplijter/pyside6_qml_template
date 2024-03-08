import logging
import threading
import traceback

from PySide6.QtCore import Slot
from PySide6.QtQml import QmlElement

from app.utils.error_codes import ERROR_COULD_NOT_START_SIMULATOR
from app.utils.qml_tools import generateQmlError
from .DataSimulatorManagerProps import DataSimulatorManagerProps

logger = logging.getLogger(__name__)

QML_IMPORT_NAME = "backend.simulator"
QML_IMPORT_MAJOR_VERSION = 1


@QmlElement
class DataSimulatorManager(DataSimulatorManagerProps):

    def __init__(self):
        super(DataSimulatorManager, self).__init__()

        self.displayError.connect(
            lambda error_code, error_desc, traceback_txt: generateQmlError(
                object=self,
                error=error_desc,
                traceback_txt=traceback_txt,
                error_code=error_code,
            )
        )

    @Slot()
    def start_simulator(self):
        def start_simulator_thread():

            try:
                logger.info("Starting simulator thread")
                a = 1 / 0.0
                logger.info(f"{a=}")
            except ZeroDivisionError as e:
                self.displayError.emit(
                    ERROR_COULD_NOT_START_SIMULATOR, e, traceback.format_exc()
                )

        t = threading.Thread(target=start_simulator_thread)
        t.start()
