import QtQuick
import QtQuick.Window 2.2
import QtQuick.Controls 2.12

import frontend.content 1.0


Item{
    id: contentManager

    property alias manager: _contentManager

    ContentManager{
        id: _contentManager
    }
}
