import os

os.environ["ENABLE_HOTRELOAD"] = os.getenv("ENABLE_HOTRELOAD", default="1")
os.environ["CONVERT_QRC"] = os.getenv("CONVERT_QRC", default="1")

os.environ["QT_IM_MODULE"] = "qtvirtualkeyboard"
os.environ["QT_DECLARATIVE_DEBUG"] = "1"
os.environ["STATECHANGE_DEBUG"] = "1"
os.environ["QSG_RHI_BACKEND"] = "opengl"

import logging
import sys

from PySide6.QtCore import QUrl, qInstallMessageHandler
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtQuickControls2 import QQuickStyle
from PySide6.QtWidgets import QApplication

from app.utils.app_logger import setup_logging
from app.utils.app_paths import ROOT_DIR
from app.utils.qml_generic_object import EngineObject
from app.utils.qml_tools import convert_qrc, qt_message_handler

setup_logging()

logging.basicConfig(level="INFO")

logger = logging.getLogger(__name__)

if os.environ["CONVERT_QRC"] == "1":
    convert_qrc()

def startApp():
    qInstallMessageHandler(qt_message_handler)

    app = QApplication(sys.argv)

    QQuickStyle.setStyle("Material")

    engine = QQmlApplicationEngine()

    engineObject = EngineObject()
    engineObject.setEngine(engine)
    engine.rootContext().setContextProperty("$engine", engineObject)

    engine.setExtraFileSelectors(ROOT_DIR.as_uri())
    engine.load(QUrl("qrc:/qml/main.qml"))

    if not engine.rootObjects():
        logger.error("No root objects found")
        sys.exit(-1)

    sys.exit(app.exec())


if __name__ == "__main__":
    from app.backend import *

    print_active_backend_qmlelements()

    from app.frontend import *
    from app.resources.resources_rc import qInitResources

    qInitResources()
    print_active_frontend_qmlelements()

    startApp()
