from PyQt5.QtWidgets import QApplication
from PyQt5.QtQml import QQmlApplicationEngine, qmlRegisterType, QQmlListProperty
from PyQt5.QtCore import QAbstractListModel

import sys

from stock_model import StockModel

if __name__ == "__main__":
    app = QApplication(sys.argv)

    engine = QQmlApplicationEngine()
    ctx = engine.rootContext()
    ctx.setContextProperty("main", engine)

    model = StockModel()
    model.setStocks([{"ticker": "AAPL", "price": 20}, {"ticker": "GOOG", "price": 120}])
    ctx.setContextProperty("stock_model", model)

    engine.addImportPath('./')
    engine.load('main.qml')

    win = engine.rootObjects()[0]
    win.show()

    # app.exec_() runs until the program ends (i.e. someone clicks X on the main window)
    return_code = app.exec_()
    sys.exit(return_code)
