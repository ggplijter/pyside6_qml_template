import logging
import os

from PySide6.QtCore import Slot
from PySide6.QtQml import QmlElement

from .ContentManagerProps import ContentManagerProps

QML_IMPORT_NAME = "frontend.content"
QML_IMPORT_MAJOR_VERSION = 1


logger = logging.getLogger(__name__)


@QmlElement
class ContentManager(ContentManagerProps):

    def __init__(self, parent=None):
        super(ContentManager, self).__init__(parent)

    # @Slot()
    # def check_hotreload(self):
    #     self.debug = os.environ["ENABLE_HOTRELOAD"] == "1"


