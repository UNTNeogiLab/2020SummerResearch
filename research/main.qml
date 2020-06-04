import QtQuick 2.13
import QtQuick.Window 2.13

Window {
    title: qsTr("Hello World")
    width: 640
    height: 480
    visible: true

    Flickable {
        id: flickable
        x: 0
        y: 0
        width: 300
        height: 300
    }
}
