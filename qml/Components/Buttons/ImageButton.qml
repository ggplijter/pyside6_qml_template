import QtQuick 2.0
import backend.mousetools 1.0

Item{
    id: image_button

    property int buttonWidth
    property int buttonHeight
    property string sourceImage
    property bool doMarkButton: false
    property double init_opacity: 0.8


    width: buttonWidth
    height: buttonHeight

    signal clicked()

    Image{
        id: img_001
        anchors.fill: parent
        width: buttonWidth
        height: buttonHeight
        scale: moonArea.pressed ? 1.1 : 1.0
        opacity: moonArea.containsMouse ? 1.0 : init_opacity
        source: sourceImage

    }

    Rectangle{
        id: debug_rect
        visible: doMarkButton
        width: buttonWidth
        height: buttonHeight
        color: "#dbdbdb"
        border.color: "red"
        border.width: 4
        radius: 20
        anchors.centerIn: img_001
        z: -3

    }

    MaskedMouseArea{
        id: moonArea
        anchors.fill: parent
        enabled: true
        maskSource: img_001.source
        alphaThreshold: 0.4
        onClicked:{
            parent.clicked()
        }
        Component.onCompleted:{
            rescaleImage = true
        }
    }

}

