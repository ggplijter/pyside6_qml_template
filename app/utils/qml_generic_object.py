import sys
from app.utils.qml_tools import convert_qrc
from PySide6.QtCore import QObject, QUrl, Slot
from PySide6.QtQml import QQmlApplicationEngine


class EngineObject(QObject):

    m_engine: QQmlApplicationEngine

    def __init__(self, parent=None):
        super(EngineObject, self).__init__(parent)

    def setEngine(self, engine: QQmlApplicationEngine):
        self.m_engine = engine

    @Slot()
    def reloadQml(self):
        # clean up qml files
        from app.resources.resources_rc import qCleanupResources
        qCleanupResources()

        # important step to really update frontend and backend (DO NOT DELETE!)
        self.m_engine.clearComponentCache()
        root_obj = self.m_engine.rootObjects().pop()
        self.m_engine.setObjectOwnership(root_obj, QQmlApplicationEngine.CppOwnership)
        root_obj.deleteLater()

        # create new qrc with updated qml
        convert_qrc()
        # delete old resources_rc from sys.modules
        if "app.resources.resources_rc" in sys.modules:
            del sys.modules["app.resources.resources_rc"]

        # re-import resources_rc (with updated qml)
        from app.resources.resources_rc import qInitResources
        qInitResources()

        # reload new main.qml
        self.m_engine.load(QUrl("qrc:/qml/main.qml"))