""" Редактор планировщика """
# ДОДЕЛАТЬ ФУНКЦИЮ СОХРАНЕНИЯ В БАЗУ ДАННЫХ:
#  1) Сделать проверку есть ли хоть одна запись в таблице
#  2) Если поля заполнены корректно, то внести запись в базу данных

import sys
from PySide6.QtWidgets import (QMainWindow, QApplication, QMessageBox)
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
        self.ui.pushButton_add.clicked.connect(self.__add_to_database)          # Заносим данные в базу данных

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
        self.model.select()

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

#------------------------ Закрываем окно редактора -----------------------------------------

    def __closeWindow(self):
        self.ui.comboBox.setCurrentIndex(0)
        self.ui.comboBox_2.setCurrentIndex(0)
        self.ui.textEdit_plan.clear()
        self.ui.dateEdit.setDate(QDate.currentDate())
        self.close()

#------------------------ Вносим данные в базу данных -------------------------------------

    def __add_to_database(self):
        if not self.__check_to_data():
            return
        if not self.__checking_for_availability():
            return
        pass                    # Здесь код добавления записи в базу данных

#------------------------ Проверка все ли поля заполнены перед внесением в базу ------------
#-------------------------- если ошибок нет - возвращает истину, иначе - ложь --------------

    def __check_to_data(self):
        if self.ui.comboBox.currentIndex() == 0:
            self.__error_message("\n\n\tНе выбран сотрудник !!!\t\t\n\n")
            return False
        if self.ui.comboBox_2.currentIndex() == 0:
            self.__error_message("\n\n\tНе выбрана станция или перегон !!!\t\t\n\n")
            return False
        if len(self.ui.textEdit_plan.toPlainText()) < 1 or \
               self.ui.textEdit_plan.toPlainText().isspace():
            self.__error_message("\n\n\tНе заполнено поле работы !!!\t\t\n\n")
            return False
        else: return True

#---------------- Проверка не дублируется ли записи придобавлении в базу ------------------------
#----------- для этого проверяем на совпадение поля дата, станция и сотрудник --------------

    def __checking_for_availability(self):
        count = 0
        self.query.exec('SELECT Data, Name, Station FROM plan_table')

        while self.query.next():                    # проверяем есть ли хоть одна запись в таблице,
            count+=1                                # если нет, то выходим из функции и добавляем первую запись
        if count==0: return True

        DataThis = str(self.ui.dateEdit.date().toString('yyyy-MM-dd'))
        NameThis = self.ui.comboBox.currentText()
        StationThis = self.ui.comboBox_2.currentText()

        while self.query.next():
            DataTable = self.query.value('Data')
            NameTable = self.query.value('Name')
            StationTable = self.query.value('Station')
            if DataThis==DataTable and NameThis==NameTable and StationThis==StationTable:
                print('Работы на данного сотрудника в указанную дату на данной станциии уже запланированы')
                return False                    # Запись не вносится
        return True                             # Запись вносится


#------------------------ Окно сообщения об ошибке ------------------------------------------

    def __error_message(self, message):
        self.msg = QMessageBox()
        self.msg.setWindowTitle('Внимание!')
        self.msg.setStyleSheet("background-color: pink; font: 700 italic 16pt 'Times New Roman'")
        self.msg.setText(message)
        self.msg.exec()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mywindow = PlanEditor()
    mywindow.show()
    sys.exit(app.exec())
