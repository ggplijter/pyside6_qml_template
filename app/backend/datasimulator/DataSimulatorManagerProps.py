from PySide6.QtCore import Property, QObject, Signal

class DataSimulatorManagerProps(QObject):
    displayError = Signal(int, Exception, str)

