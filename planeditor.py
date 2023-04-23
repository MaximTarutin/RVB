""" Редактор планировщика """
import sys
from PySide6.QtWidgets import (QMainWindow, QApplication)
from PySide6.QtCore import (QDate, Qt)
from PySide6.QtSql import (QSqlTableModel, QSqlQuery)
import ui_planeditor


class PlanEditor(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = ui_planeditor.Ui_planEditor()
        self.ui.setupUi(self)

        self.model = QSqlTableModel()
        self.query = QSqlQuery()
        self.ui.dateEdit.setMinimumDate(QDate(2023,1,1))
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowCloseButtonHint)  # деактивируем кнопку закрыть окно

        self.init_plan_window()

        self.ui.pushButton_return.clicked.connect(self.__closeWindow)        # Закрываем это окно

#------------------------ Инициализация планировщика ---------------------------------------

    def init_plan_window(self):
        self.model.setTable("plan_table")
        self.ui.tableView.setModel(self.model)

        self.model.setHeaderData(0, Qt.Horizontal, "№")                 # Оформляем таблицу
        self.model.setHeaderData(1, Qt.Horizontal, "Дата")
        self.model.setHeaderData(2, Qt.Horizontal, "Сотрудник")
        self.model.setHeaderData(3, Qt.Horizontal, "Станция")
        self.model.setHeaderData(4, Qt.Horizontal, "Работа")
        self.ui.tableView.setColumnWidth(0, 30)
        self.ui.tableView.setColumnWidth(1, 100)
        self.ui.tableView.setColumnWidth(2, 250)
        self.ui.tableView.setColumnWidth(3, 200)
        self.ui.tableView.horizontalHeader().setStretchLastSection(True)    # последний столбец подгоняется под таблицу

        self.query.exec("SELECT Name FROM workers")         # Заполняем комбобокс сотрудники
        list_workers = []
        while self.query.next():
            name = self.query.value("Name")
            list_workers.append(name)
        self.ui.comboBox.addItem("")
        for name in list_workers:
            self.ui.comboBox.addItem(name)
        del list_workers

        self.query.exec("SELECT NAME FROM station")
        list_station = []
        while self.query.next():
            name = self.query.value("NAME")
            list_station.append(name)
        self.ui.comboBox_2.addItem("")
        for name in list_station:
            self.ui.comboBox_2.addItem(name)
        del list_station


        self.model.select()

#------------------------ Закрываем окно редактора -----------------------------------------

    def __closeWindow(self):
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mywindow = PlanEditor()
    mywindow.show()
    sys.exit(app.exec())
