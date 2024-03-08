import QtQuick
import QtQuick.Window 2.2
import QtQuick.Controls 2.12

import backend.simulator 1.0

Item{
    id: simulator

    property alias manager: _datasimulatormanager

    DataSimulatorManager{
        id: _datasimulatormanager
    }


}
