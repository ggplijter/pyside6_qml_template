
import logging

from .mousetools.MaskedMouseArea import MaskedMouseArea
from .watchdog.WatchdogManager import WatchdogManager
from .datasimulator.DataSimulatorManager import DataSimulatorManager

logger = logging.getLogger(__name__)

def print_active_backend_qmlelements():
    logger.info("Following QmlElement(s) are instantiated for backend:")
    global_scope = globals()
    for k, v in global_scope.items():
        if hasattr(global_scope[k], "staticMetaObject"):
            if global_scope[k].staticMetaObject.className() == k:
                logger.info(f"[*] {k}")