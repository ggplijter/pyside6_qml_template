import logging
import subprocess

from PySide6.QtCore import QtMsgType
from PySide6.QtQml import QQmlApplicationEngine
# from app.backend.watchdog.WatchdogManager import WatchdogManager
from app.utils.app_paths import RESOURCES_DIR, RCC_EXE, ROOT_DIR
from app.utils.error_codes import ERROR_UNKNOWN

logger = logging.getLogger(__name__)

def qt_message_handler(mode, context, message):
    if mode == QtMsgType.QtInfoMsg:
        mode = "Info"
    elif mode == QtMsgType.QtWarningMsg:
        mode = "Warning"
    elif mode == QtMsgType.QtCriticalMsg:
        mode = "critical"
    elif mode == QtMsgType.QtFatalMsg:
        mode = "fatal"
    else:
        mode = "Debug"

    logger.info("%s: %s (%s:%d, %s)" % (mode, message, context.file, context.line, context.file))


# def generateQmlError(object, error_txt, traceback_txt):
#     win = QQmlApplicationEngine.contextForObject(object).engine().rootObjects()[0]
#     watchdogManager = win.findChildren(WatchdogManager)[0]
#     watchdogManager.displayError.emit(str(error_txt), traceback_txt)

def generateQmlError(object, error, traceback_txt, error_code=ERROR_UNKNOWN):
    from app.backend.watchdog.WatchdogManager import WatchdogManager

    error_code_str = f"[E-{error_code:04X}]"
    error_desc_str =  f"{error.__class__} {error}"
    win = QQmlApplicationEngine.contextForObject(object).engine().rootObjects()[0]
    watchdogManager = win.findChildren(WatchdogManager)[0]
    watchdogManager.displayError.emit(error_code_str, error_desc_str, traceback_txt)


def convert_qrc(res_name="resources_rc.py"):
    logger.info("Converting resources.qrc")

    resources_qrc = ROOT_DIR / "resources.qrc"
    py_out_name = RESOURCES_DIR / f"./{res_name}"

    subprocess.call(
        [
            str(RCC_EXE),
            "-g",
            "python",
            str(resources_qrc),
            "-o",
            str(py_out_name),
        ]
    )

    with open(py_out_name, "r+", encoding="utf-8") as file:
        lines = file.readlines()
        lines = lines[:-2]

    with open(py_out_name, "w+", encoding="utf-8") as file:
        file.writelines(lines)

    logger.info("Converting resources.qrc finished")
