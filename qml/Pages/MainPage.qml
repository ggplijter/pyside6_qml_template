import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.VirtualKeyboard 2.15
import QtQuick.Controls 2.15

import "./../Components/Buttons/"


Page {
    id: root_page

    property alias btn_close: btnCloseApp

    width: windowroot.width
    height: windowroot.height

    background: Rectangle{
        gradient: Gradient {
            GradientStop {
                position: 0
                color: mainGradientColorTop
            }
            GradientStop {
                position: 0.5
                color: gradientColorMid
            }
            GradientStop {
                position: 1
                color: mainGradientColorBottom
            }
            orientation: Gradient.Vertical
        }
    }

    ImageButton{
        id: btnNext
        sourceImage: "qrc:/qml/Media/Images/button_right.png"
        buttonHeight: 525
        buttonWidth: 165
        anchors.verticalCenter: parent.verticalCenter
        anchors.right: parent.right

        onClicked: {
            windowroot.subPageIdx += 1;
            pageLoader.source = windowroot.subPages[windowroot.subPageIdx]
        }
    }

    ImageButton{
        id: btnPrev
        sourceImage: "qrc:/qml/Media/Images/button_left.png"
        buttonHeight: 525
        buttonWidth: 165
        anchors.verticalCenter: parent.verticalCenter
        anchors.left: parent.left

        onClicked: {
            windowroot.subPageIdx -= 1;
            pageLoader.source = windowroot.subPages[windowroot.subPageIdx]

        }
    }

    ImageButton{
        id: btnCloseApp
        buttonHeight: 100
        buttonWidth: 100
        anchors.right: parent.right
        anchors.rightMargin: 80
        anchors.top: parent.top
        anchors.topMargin: 80
        sourceImage: "qrc:/qml/Media/Images/window_close.png"

        onClicked: {
            if (content.manager.simulate){
                canopen.manager.stop_simulation()
            }
            windowroot.close()

        }
    }

    ImageButton{
        id: btnReloadApp

        Item{
            width: 1000
            height: parent.height
            anchors.right: parent.left
            anchors.verticalCenter: parent.verticalCenter
            Text{
                anchors.fill: parent
                color: "red"
                text: "👉 click for hot reload 🔥 qml! 👉"
                font.pointSize: 40
                verticalAlignment: Text.AlignVCenter
                horizontalAlignment: Text.AlignRight

            }
        }

        buttonHeight: 100
        buttonWidth: 100
        anchors.right: btnCloseApp.left
        anchors.rightMargin: 30
        anchors.verticalCenter: btnCloseApp.verticalCenter
        sourceImage: "qrc:/qml/Media/Images/hotreload.png"
        visible: content.manager.do_hotreload
        doMarkButton: content.manager.do_hotreload ? true : false

        onClicked: {
            btnCloseApp.clicked();
            $engine.reloadQml();
        }
    }

    Rectangle {
        id: pageroot
        width: screenWidth
        height: screenHeight
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.verticalCenter: parent.verticalCenter
        color: "transparent"
        radius: 50

        Loader {
            id: pageLoader
            anchors.fill: parent
            source: subPages[subPageIdx]
        }
    }
}


/*##^##
Designer {
    D{i:0;formeditorZoom:0.33}
}
##^##*/
