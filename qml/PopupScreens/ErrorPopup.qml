import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Controls 2.15
import QtQuick.Shapes 1.3


import "./../Components/Buttons"


Popup {
    id: popup_error
    width: 1800
    height: 1000
    modal: true
    anchors.centerIn: parent

    property QtObject close_btn

    visible: false
    background: Rectangle {
        color: "#FF8F49"
        border.color: mainTextColor
        border.width: 5
        radius: 30
    }

    closePolicy: Popup.NoAutoClose

    Rectangle{
        id: popup_page
        anchors.fill: parent
        color: "transparent"

        Text {
            id: txt_err_code
            anchors.left: parent.left
            anchors.leftMargin: 20
            width: 150
            height: 100
            font.pixelSize: 40
            font.bold: true

            color: mainTextColor
            text: error_code
            verticalAlignment: Text.AlignVCenter
            //            wrapMode: Text.WordWrap
        }

        Text {
            id: txt_err_desc


            anchors.top: txt_err_code.top
            anchors.left: txt_err_code.right
            anchors.leftMargin: 40
            width: 1540
            height: txt_err_code.height
            font.pixelSize: 30
            font.bold: true
            font.italic: true
            color: mainTextColor
            text: error_desc
            verticalAlignment: Text.AlignVCenter
            wrapMode: Text.WordWrap
        }

        Text {
            id: name_1
            anchors.left: txt_err_code.left
            anchors.top: txt_err_code.bottom
            anchors.topMargin: 20
            width: 1730
            height: 700
            text: traceback_txt
            font.pixelSize: 14
            color: "red"
            wrapMode: Text.WordWrap
        }

        Text {
            id: instruction_close
            anchors.verticalCenter: btnClosePopup.verticalCenter
            anchors.right: btnClosePopup.left
            anchors.rightMargin:30

            text: "Check " + error_code + " in manual for more information click here to close the app 👉"
            font.pixelSize: 30
            font.bold: true
        }

        ImageButton{
            id: btnClosePopup
            anchors.bottom: parent.bottom
            anchors.bottomMargin: 70
            anchors.right: parent.right
            anchors.rightMargin: 70
            buttonHeight: 68
            buttonWidth: 74
            sourceImage: "qrc:/qml/Media/Images/window_close.png"

            onClicked: {
                manager.takeScreenshot();
                close_btn.clicked()
            }
        }
    }
}
