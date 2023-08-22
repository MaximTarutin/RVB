"""
      Окно показывающее количество часов переработки или недоработки
"""

import sys
from PySide6.QtCore import (Qt)
from PySide6.QtWidgets import (QApplication, QWidget, QAbstractItemView)
from PySide6.QtSql import (QSqlTableModel, QSqlQuery)
import ui_otgulwindow

class OtgulWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = ui_otgulwindow.Ui_OtgulWindow()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.ui.setupUi(self)

        self.model = QSqlTableModel(self)
        self.model.setTable("otgul_table")
        self.ui.tableView.setModel(self.model)
        self.ui.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)  # Запрет редактирования таблицы.
        self.model.setHeaderData(0, Qt.Horizontal, "№")
        self.model.setHeaderData(1, Qt.Horizontal, "Сотрудник")
        self.model.setHeaderData(2, Qt.Horizontal, "Часы")
        self.ui.tableView.setColumnWidth(0, 15)  # Устанавливаем ширину столбцов
        self.ui.tableView.setColumnWidth(1, 350)
        self.ui.tableView.setColumnWidth(2, 60)
        self.ui.tableView.verticalHeader().hide()
        self.query = QSqlQuery()
        self.query.exec('''INSERT INTO otgul_table(name, hour) SELECT DISTINCT Name, summa FROM time_tracking''')
        self.model.select()

        self.ui.pushButton.clicked.connect(self.__closeWindow)

#------------------------- Закрываем окно отгулов --------------------------------------------------------------------

    def __closeWindow(self):
        self.query.exec('''DELETE FROM otgul_table''')
        self.close()
        self.deleteLater()

#---------------------------------------------------------------------------------------------------------------------

if __name__=='_main__':
    app = QApplication(sys.argv)
    mywindow = OtgulWindow()
    mywindow.show()
    sys.exit(app.exec())