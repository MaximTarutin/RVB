"""  Редактор планировщика. """

import sys
from PySide6.QtWidgets import (QMainWindow, QApplication, QMessageBox, QAbstractItemView)
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
        self.ui.dateEdit.setDate(QDate.currentDate())
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowCloseButtonHint)  # деактивируем кнопку закрыть окно

        self.init_plan_window()
        self.ui.tableView.resizeRowsToContents()

        self.ui.pushButton_add.clicked.connect(self.__add_to_database)          # Заносим данные в базу данных
        self.ui.pushButton_del.clicked.connect(self.__del_string)               # Удаляем выделенные строки
        self.ui.dateEdit.dateChanged.connect(self.__data_filter)                # применяем фильтр
        self.ui.comboBox.currentIndexChanged.connect(self.__data_filter)


#------------------------- Инициализация планировщика ---------------------------------------

    def init_plan_window(self):
        self.model.setTable("plan_table")
        self.ui.tableView.setModel(self.model)

        self.model.setHeaderData(2, Qt.Horizontal, "Дата")                      # Оформляем таблицу
        self.model.setHeaderData(3, Qt.Horizontal, "Сотрудник")
        self.model.setHeaderData(4, Qt.Horizontal, "Станция")
        self.model.setHeaderData(5, Qt.Horizontal, "Работа")

        self.ui.tableView.hideColumn(0)
        self.ui.tableView.hideColumn(1)
        self.ui.tableView.setColumnWidth(2, 100)
        self.ui.tableView.setColumnWidth(3, 250)
        self.ui.tableView.setColumnWidth(4, 200)

        self.ui.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)  # Запрет редактирования таблицы.
        self.ui.tableView.horizontalHeader().setStretchLastSection(True)    # последний столбец подгоняется под таблицу

        self.model.select()

        self.__data_filter()

        self.query.exec("SELECT Name FROM workers")         # Заполняем комбобокс сотрудники
        list_workers = []
        while self.query.next():
            name = self.query.value("Name")
            list_workers.append(name)
        self.ui.comboBox.clear()
        self.ui.comboBox.addItem("")

        for name in list_workers:
            self.ui.comboBox.addItem(name)
        del list_workers

        self.query.exec("SELECT Name FROM station")
        list_station = []
        while self.query.next():
            name = self.query.value("NAME")
            list_station.append(name)
        self.ui.comboBox_2.clear()
        self.ui.comboBox_2.addItem("")
        for name in list_station:
            self.ui.comboBox_2.addItem(name)
        del list_station

#-------------------------- заполняем tableView при выборе даты ---------------------------

    def __data_filter(self):
        DateSelect = str(self.ui.dateEdit.date().toString('yyyy-MM-dd'))
        Worker = self.ui.comboBox.currentText()
        self.model.setFilter('''DataHide like "%''' + DateSelect + '''%"
                                AND Name like "%''' + Worker + '''%"''')
        self.ui.tableView.resizeRowsToContents()  # Содержимое вписывается в ячейку

#------------------------ Закрываем окно редактора -----------------------------------------

    def closeWindow(self):
        self.ui.comboBox.setCurrentIndex(0)
        self.ui.comboBox_2.setCurrentIndex(0)
        self.ui.textEdit_plan.clear()
        self.ui.dateEdit.setDate(QDate.currentDate())
        self.close()


#------------------------ Вносим данные в базу данных -------------------------------------

    def __add_to_database(self):
        if not self.__check_to_data():                  # проверка все ли поля заполнены
            return
        if not self.__checking_for_availability():      # проверка нет ли такой записи уже в базе данных
            print("Такая запись есть")
            return

        print("Такой записи нет")
        DataHide = str(self.ui.dateEdit.date().toString('yyyy-MM-dd'))
        DataThis = self.ui.dateEdit.text()
        NameThis = self.ui.comboBox.currentText()
        StationThis = self.ui.comboBox_2.currentText()
        PlanThis = self.ui.textEdit_plan.toPlainText()

        self.query.exec('''INSERT INTO plan_table (DataHide, Data, Name, Station, Plan)
                           VALUES ("'''+DataHide+'''","'''+DataThis+'''","'''+NameThis+'''","'''+StationThis+
                                    '''","'''+PlanThis+'''")''')

        self.ui.comboBox.setCurrentIndex(0)             # Сбрасываем все поля в начальное состояние
        self.ui.comboBox_2.setCurrentIndex(0)
        self.ui.textEdit_plan.clear()
        self.model.select()
        self.ui.tableView.resizeRowsToContents()

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
        self.query.exec('SELECT DataHide, Name, Station FROM plan_table')
        DataThis = str(self.ui.dateEdit.date().toString('yyyy-MM-dd'))
        NameThis = self.ui.comboBox.currentText()
        StationThis = self.ui.comboBox_2.currentText()

        while self.query.next():
            DataTable = self.query.value('DataHide')
            NameTable = self.query.value('Name')
            StationTable = self.query.value('Station')
            if DataThis==DataTable and NameThis==NameTable and StationThis==StationTable:
                self.__error_message("\n\nРаботы на данного сотрудника в указанную дату"
                                     " на данной станциии уже запланированы\t\t\n\n")
                return False                    # Запись не вносится
        return True                             # Запись вносится

# ---------------------------------- Удаление выбранных строк --------------------------------------

    def __del_string(self):
        if self.ui.tableView.selectionModel().hasSelection():
            for index in self.ui.tableView.selectedIndexes() or []:
                self.ui.tableView.model().removeRow(index.row())
        self.model.select()


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
