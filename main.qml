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


    Component {
        id: stock_delegate
        Row {
            spacing: 10
            Text { text: ticker }
            Text { text: '$' + price }
        }
    }

    ListView {
        anchors.fill: parent
        model: stock_model
        delegate: stock_delegate
    }
}













//     ColumnLayout{
// 	   spacing: 10
 

// 	    Rectangle {
// 	    	height: 20
// 	    	RowLayout {
// 	    		spacing: 5

// 	    		Label {
// 		    		text: "AAPL"
// 		    		font.pixelSize: 22
// 		    	}
// 		    	Label {
// 		    		text: "$100"
// 		    	}
// 	    	}
// 	    }
// 	}	
// }
