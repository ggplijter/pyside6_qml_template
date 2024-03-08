import QtQuick
import QtQuick.Window 2.2
import QtQuick.Controls 2.12

import backend.watchdog 1.0

import "./../Components/Buttons/"
import "./../PopupScreens/"

Item{
    id: watchdog

    property alias manager: _watchdogmanager
    property alias popup: _popupScreen


    property string error_code
    property string error_desc
    property string traceback_txt

    WatchdogManager{
        id: _watchdogmanager
        onDisplayError: function(err_code, error_txt, traceback) {

            error_code = err_code
            error_desc = error_txt;
            traceback_txt = traceback;


            _popupScreen.visible = true

        }
    }

    ErrorPopup {
        id: _popupScreen
        width: 1800
        height: 1000
        modal: true
        anchors.centerIn: parent
    }

}

