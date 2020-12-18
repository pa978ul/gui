from PyQt5.QtCore import QAbstractListModel, QObject, QModelIndex, Qt


class StockModel(QAbstractListModel):

    TickerRole = Qt.UserRole + 1
    PriceRole = Qt.UserRole + 2

    def __init__(self):
        super().__init__(None)
        self._stocks = []


    def setStocks(self, stocks):
        self.beginResetModel()
        self._stocks = stocks
        self.endResetModel()

    def rowCount(self, parent=QModelIndex()):
        return len(self._stocks)


    def data(self, index, role=Qt.DisplayRole):
        row = index.row()
        if role == StockModel.TickerRole:
            return self._stocks[row]['ticker']
        if role == StockModel.PriceRole:
            return self._stocks[row]['price']

    def roleNames(self):
        return {
            StockModel.TickerRole: b'ticker',
            StockModel.PriceRole: b'price'
        }
