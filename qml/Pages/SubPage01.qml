import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Controls 2.15
import QtCharts 2.5
import backend.mousetools 1.0

import "./../Components/Buttons"

Item {
    id: rectStartScreen
    visible: true

    Component.onCompleted:{
        btnNext.visible = false
        btnPrev.visible = false
        btnCloseApp.visible = true
    }


    Timer{
        id: timer
        interval: 1000
        repeat: false

        onTriggered: {
            btnNext.clicked()
        }
    }

    ImageButton{
        id: btnStartEdo
        anchors.verticalCenter: parent.verticalCenter
        anchors.verticalCenterOffset: 50
        anchors.horizontalCenter: parent.horizontalCenter
        buttonHeight: 276
        buttonWidth: buttonHeight
        sourceImage: "qrc:/qml/Media/Images/on_off_button.png"

        Image{
            id: img_accent_circular
            anchors.fill: parent
            source: "qrc:/qml/Media/Images/accent_circular.png"
            fillMode: Image.PreserveAspectFit
            z: -5
            SequentialAnimation
            {
                id: sequentialAnim
                property double scaleFactor: 1.3
                running: true
                loops: Animation.Infinite
                ParallelAnimation {
                    NumberAnimation {
                        properties: "scale"
                        duration: 500
                        target: img_accent_circular
                        from: 1.0
                        to: sequentialAnim.scaleFactor
                    }
                    NumberAnimation {
                        properties: "opacity"
                        duration: 500
                        target: img_accent_circular
                        from: 1.0
                        to: 0.8
                    }
                }
                ParallelAnimation {
                    NumberAnimation {
                        properties: "scale"
                        duration: 500
                        target: img_accent_circular
                        from: sequentialAnim.scaleFactor
                        to: 1.0
                    }
                    NumberAnimation {
                        properties: "opacity"
                        duration: 500
                        target: img_accent_circular
                        from: 0.8
                        to: 1.0
                    }
                }
            }
        }

        onClicked: {             
            simulator.manager.start_simulator()
        }
    }
}


