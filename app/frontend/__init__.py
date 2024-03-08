import logging

from .content.ContentManager import ContentManager

logger = logging.getLogger(__name__)


def print_active_frontend_qmlelements():
    logger.info("Following QmlElement(s) are instantiated for frontend:")

    global_scope = globals()
    for k, v in global_scope.items():
        if hasattr(global_scope[k], "staticMetaObject"):
            if global_scope[k].staticMetaObject.className() == k:
                logger.info(f"[*] {k}")
