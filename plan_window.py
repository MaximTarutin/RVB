import sys
import ui_planwindow
from PySide6.QtWidgets import (QApplication, QMainWindow)
from PySide6.QtCore import (Qt, Signal)
from PySide6.QtSql import (QSqlTableModel, QSqlQuery)
import passwrd
from planeditor import PlanEditor

class Plan_Window(QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.FLAG_ADMIN = False                                 # Флаг режима администратора True - администратор
        self.ui = ui_planwindow.Ui_PlanWindow()
        self.ui.setupUi(self)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowCloseButtonHint)     # деактивируем кнопку закрыть окно

        self.PasswordWindow = passwrd.PasswordWindow()
        self.PlanEditor= PlanEditor()

        self.query = QSqlQuery()
        self.__set_list_workers()
        self.__set_list_stations()

        self.model = QSqlTableModel()
        self.model.setTable("plan_table")
        self.ui.tableView.setModel(self.model)

        self.init()

        self.ui.pushButton_return.clicked.connect(self.return_to_mainwindow)    # вернуться в главное окно
        self.ui.action_return.triggered.connect(self.return_to_mainwindow)
        self.ui.checkBox.stateChanged.connect(self.__checkbox_state)            # состояние checkbox
        self.ui.pushButton_add.clicked.connect(self.__add_plan)                 # Кнопка "Редактор"

# ------------------------- Получаем сигнал со значением режима программы (админ или юзер) ---------------------------

    def sig_admin(self, b):
        self.FLAG_ADMIN = b                 # Не срабатывает True
        self.programm_Mode()

#-------------------------------- Режим программы (admin or user) -------------------------------------------

    def programm_Mode(self):
        if self.FLAG_ADMIN:
            self.ui.action_user.setDisabled(False)
            self.ui.action_admin.setDisabled(True)
            self.ui.pushButton_add.setDisabled(False)
            self.ui.pushButton_delete.setDisabled(False)
            self.ui.action_workers.setDisabled(False)
            self.ui.action_stations.setDisabled(False)
            self.ui.action_admin_edit.setDisabled(False)
            self.ui.action_plan_edit.setDisabled(False)
        else:
            self.ui.action_admin.setDisabled(False)
            self.ui.action_user.setDisabled(True)
            self.ui.pushButton_delete.setDisabled(True)
            self.ui.pushButton_add.setDisabled(True)
            self.ui.action_workers.setDisabled(True)
            self.ui.action_stations.setDisabled(True)
            self.ui.action_admin_edit.setDisabled(True)
            self.ui.action_plan_edit.setDisabled(True)

#------------------------------------------ Состояние чекбокса --------------------------------------------

    def __checkbox_state(self):
        if self.ui.checkBox.isChecked():
            self.ui.ultimate_dateEdit.show()
            self.ui.label_initial.show()
            self.ui.label_initial_2.show()
        else:
            self.ui.ultimate_dateEdit.hide()
            self.ui.label_initial.hide()
            self.ui.label_initial_2.hide()


#------------------------------------------ Закрыть окно ---------------------------------------------------

    def return_to_mainwindow(self):
        self.close()

#------------------------------- Создаем список сотрудников ----------------------------------

    def __set_list_workers(self):
        list_workers = []
        self.query.exec("SELECT Name FROM workers")
        while self.query.next():
            name = self.query.value("Name")
            list_workers.append(name)

        self.ui.comboBox_workers.clear()
        self.ui.comboBox_workers.addItem("")
        for name in list_workers:
            self.ui.comboBox_workers.addItem(name)
        list_workers.clear()

#------------------------------- Создаем список станций ----------------------------------

    def __set_list_stations(self):
        list_stations = []
        self.query.exec("SELECT NAME FROM station")
        while self.query.next():
            name = self.query.value("NAME")
            list_stations.append(name)

        self.ui.comboBox_station.clear()
        self.ui.comboBox_station.addItem("")
        for name in list_stations:
            self.ui.comboBox_station.addItem(name)
        list_stations.clear()

#----------------------------------- Инициализация -------------------------------------------

    def init(self):
        self.model.setHeaderData(0, Qt.Horizontal, "№")
        self.model.setHeaderData(1, Qt.Horizontal, "Дата")
        self.model.setHeaderData(2, Qt.Horizontal, "Сотрудник")
        self.model.setHeaderData(3, Qt.Horizontal, "Станция")
        self.model.setHeaderData(4, Qt.Horizontal, "Работа")
        self.ui.tableView.setColumnWidth(0, 20)
        self.ui.tableView.setColumnWidth(1, 120)
        self.ui.tableView.setColumnWidth(2,220)
        self.ui.tableView.setColumnWidth(3,220)
        self.ui.tableView.horizontalHeader().setStretchLastSection(True)    # последний столбец подгоняется под таблицу

        self.__checkbox_state()
        self.model.select()

#------------------------------- включаем редактор планировщика ----------------------------------------

    def __add_plan(self):
        self.PlanEditor.show()


if __name__ == "main":
    app = QApplication(sys.argv)
    mywindow = Plan_Window()
    sys.exit(app.exec())
