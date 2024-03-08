import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.VirtualKeyboard 2.4
import QtQuick.Controls 2.15
import QtQuick.Controls.Material 2.15
import QtScxml

import "./Components/Buttons/"
import "./Frontend"
import "./Backend"
import "./Pages"

ApplicationWindow {
    property string mainGradientColorTop: "#21ed91"
    property string gradientColorMid: "#c8e1d5"
    property string mainGradientColorBottom: "#0066ff"

    property string mainTextColor: "#4E4E4E"

    property int screenWidth: 1200
    property int screenHeight: 800

    property int subPageIdx: 0
    property var subPages: [
        "qrc:/qml/Pages/SubPage01.qml",                     // 0
    ]

    id: windowroot
    visible: true
    Material.accent: Material.BlueGrey
    screen: {
        if (Qt.application.screens.length > 1 ){
            return Qt.application.screens[1]
        }
        else{
            return Qt.application.screens[0]
        }
    }
    x: screen.virtualX
    y: screen.virtualY  - 1
    width: screen.width > 1920 ? 1920 : screen.width
    height: screen.height > 1080 ? 1200 : screen.height + 1
    flags: Qt.Window | Qt.FramelessWindowHint
    visibility: "FullScreen"

    Component.onCompleted: {
        // bind close-button of popup to button-close of mainPage
        watchdog.popup.close_btn = mainPage.btn_close

        // set the startPage when hotreloading is anbeld
        if (content.manager.do_hotreload){
            subPageIdx = 0
        }
    }

    ContentFrontend{
        id: content
    }

    WatchdogBackend{
        id: watchdog
        anchors.fill: parent
    }

    DataSimulatorBackend{
        id: simulator
    }

    onSubPageIdxChanged: {
        if (subPageIdx >= subPages.length){
            subPageIdx = subPages.length - 1
        }
        if (subPageIdx < 0){
            subPageIdx = 0
        }
    }

    MainPage{
        id: mainPage
        width: parent.width
        height: parent.height
    }

    InputPanel {
        id: inputPanel
        z: 99
        x: 0
        y: windowroot.height
        width: windowroot.width

        states: State {
            name: "visible"
            when: inputPanel.active
            PropertyChanges {
                target: inputPanel
                y: windowroot.height - inputPanel.height
            }
        }
        transitions: Transition {
            from: ""
            to: "visible"
            reversible: true
            ParallelAnimation {
                NumberAnimation {
                    properties: "y"
                    duration: 1000
                    easing.type: Easing.InOutQuad
                }
            }
        }
    }



}




