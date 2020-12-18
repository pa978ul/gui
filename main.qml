import QtQuick 2.7
import QtQuick.Window 2.1
import QtQuick.Controls 1.2
import QtQuick.Dialogs 1.1
import QtQuick.Layouts 1.2
// import components 1.0


ApplicationWindow {
    title: "Arm Control"

    width: 200
    height: 200


     CheckBox {
        text: "connected"
        checked: true
        id: mybutton
    }

}