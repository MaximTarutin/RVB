""" ---------- Модуль просмотра замечаний --------------"""

import sys
from PySide6.QtCore import (Qt)
from PySide6.QtWidgets import (QApplication, QMainWindow, QAbstractItemView)
from PySide6.QtSql import (QSqlQuery, QSqlTableModel)
from datetime import date, datetime
from delegate import ColorDelegate, NoEditorDelegate, Date_delegate
import ui_commentsview

class Comments_View(QMainWindow):
    def __init__(self, parrent = None):
        self.FLAG_ADMIN = False
        super().__init__(parrent)
        self.ui = ui_commentsview.Ui_CommentsView()
        self.ui.setupUi(self)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowCloseButtonHint)  # деактивируем кнопку закрыть окно
        self.ui.del_Button.setEnabled(False)
        self.ui.ZaprosButton.deleteLater()

        self.query = QSqlQuery()

        self.deleg = ColorDelegate(self)
        self.delegat = NoEditorDelegate(self)
        self.date_delegat = Date_delegate(self)

        self.model = QSqlTableModel(self)
        self.model.setTable("comments_table")
        self.model.setHeaderData(1, Qt.Horizontal, "№")
        self.model.setHeaderData(2, Qt.Horizontal, "Дата")
        self.model.setHeaderData(3, Qt.Horizontal, "Комиссия")
        self.model.setHeaderData(4, Qt.Horizontal, "Станция")
        self.model.setHeaderData(5, Qt.Horizontal, "Проверяющий")
        self.model.setHeaderData(6, Qt.Horizontal, "Выявленные замечания")
        self.model.setHeaderData(7, Qt.Horizontal, "Срок")
        self.model.setHeaderData(8, Qt.Horizontal, "Исполнитель")
        self.model.setHeaderData(9, Qt.Horizontal, "Выполнение")
        self.model.setHeaderData(10, Qt.Horizontal, "Дата")
        self.model.setHeaderData(11, Qt.Horizontal, "Отметка о выполнении")
        self.model.setHeaderData(12, Qt.Horizontal, "Фото")
        #self.model.select()

        self.ui.tableView.setModel(self.model)

        self.ui.performance_Box.clear()
        self.ui.performance_Box.addItem("")
        self.ui.performance_Box.addItem("Выполнено")
        self.ui.performance_Box.addItem("Не выполнено")
        self.ui.performance_Box.addItem("Подходит срок")
        self.ui.performance_Box.addItem("Выполнить сегодня")
        self.ui.performance_Box.addItem("Просрочено")

        self.ui.tableView.setColumnHidden(0, True)
        self.ui.tableView.setItemDelegateForColumn(1, self.delegat)  # запрещаем редактирование некоторых столбцов
        self.ui.tableView.setItemDelegateForColumn(2, self.delegat)
        self.ui.tableView.setItemDelegateForColumn(3, self.delegat)
        self.ui.tableView.setItemDelegateForColumn(4, self.delegat)
        self.ui.tableView.setItemDelegateForColumn(5, self.delegat)
        self.ui.tableView.setItemDelegateForColumn(6, self.delegat)
        self.ui.tableView.setItemDelegateForColumn(9, self.deleg)

        self.ui.tableView.setColumnWidth(1, 20)
        self.ui.tableView.setColumnWidth(2, 100)
        self.ui.tableView.setColumnWidth(3, 160)
        self.ui.tableView.setColumnWidth(4, 160)
        self.ui.tableView.setColumnWidth(5, 160)
        self.ui.tableView.setColumnWidth(6, 400)
        self.ui.tableView.setColumnWidth(7, 100)
        self.ui.tableView.setColumnWidth(8, 160)
        self.ui.tableView.setColumnWidth(9, 160)
        self.ui.tableView.setColumnWidth(10, 100)
        self.ui.tableView.setColumnWidth(11, 400)
        self.ui.tableView.setColumnWidth(12, 20)
        self.ui.tableView.resizeRowsToContents()  # Содержимое вписывается в ячейку

        self.initial()

        self.ui.edit_checkBox.stateChanged.connect(self.check_checkBox)
        self.ui.commis_Box.currentIndexChanged.connect(self.__data_filter)
        self.ui.station_Box.currentIndexChanged.connect(self.__data_filter)
        self.ui.auditor_Box.currentIndexChanged.connect(self.__data_filter)
        self.ui.worker_Box.currentIndexChanged.connect(self.__data_filter)
        self.ui.performance_Box.currentIndexChanged.connect(self.__data_filter)
        self.model.dataChanged.connect(self.__proverka)

#------------------------- Инициализация -------------------------------

    def initial(self):
        self.programm_Mode()
        self.query.exec("SELECT Name FROM workers")         # Заполняем комбобоксы из базы данных
        list_worker = []
        while self.query.next():
            name = self.query.value("Name")
            list_worker.append(name)
        self.ui.worker_Box.clear()
        self.ui.worker_Box.addItem("")
        for i in list_worker:
            self.ui.worker_Box.addItem(i)
        del list_worker

        self.query.exec("SELECT Name FROM station")
        list_station  = []
        while self.query.next():
            name = self.query.value("Name")
            list_station.append(name)
        self.ui.station_Box.clear()
        self.ui.station_Box.addItem("")
        for i in list_station:
            self.ui.station_Box.addItem(i)
        del list_station

        self.query.exec("SELECT * FROM comments_table")
        list_auditor = []
        list_kommis = []
        while self.query.next():
            name_kommis = self.query.value("kommis")
            name_auditor = self.query.value("auditor")
            list_kommis.append(name_kommis)
            list_auditor.append(name_auditor)
        new_list_kommis = set(list_kommis)
        new_list_auditor = set(list_auditor)                    # убираем дубликаты из списков
        self.ui.commis_Box.clear()
        self.ui.commis_Box.addItem("")
        for i in new_list_kommis:
            self.ui.commis_Box.addItem(i)
        self.ui.auditor_Box.clear()
        self.ui.auditor_Box.addItem("")
        for i in new_list_auditor:
            self.ui.auditor_Box.addItem(i)

        del new_list_kommis
        del list_kommis
        del new_list_auditor
        del list_auditor

        self.model.select()
        self.__data_filter()
        self.__compare_date()


#------------------------- отображаем данные в таблице по заданному фильтру ----------------------------------------

    def __data_filter(self):
        commis = self.ui.commis_Box.currentText()
        station = self.ui.station_Box.currentText()
        auditor = self.ui.auditor_Box.currentText()
        worker = self.ui.worker_Box.currentText()
        performance = self.ui.performance_Box.currentText()

        self.model.setFilter('''kommis like "%'''+commis+'''%" AND station like "%'''+station+'''%" AND 
                                auditor like "%'''+auditor+'''%" AND worker like "%'''+worker+'''%" AND 
                                performance like "'''+performance+'''%"''')

#------------------------------  изменение статуса выполнения -------------------------------------

    def __compare_date(self):
        list_overdue = []                                       # список просроченных замечаний
        list_soon_data = []                                     # список замечаний у которых подходит срок (10 дней)
        list_today = []                                         # список замечаний которые нужно выполнить сегодня
        list_not_done = []                                      # список невыполненных замечаний
        list_done = []                                          # список выполненных замечаний
        self.query.exec("SELECT * FROM comments_table")
        while self.query.next():
            id_in_table = self.query.value("IthemID")
            d0 = self.query.value("term_data")
            performance = self.query.value("performance")
            d0 = datetime.strptime(d0,"%d.%m.%Y").date()
            data_1 = date.today()
            period = (d0-data_1).days
            workers = self.query.value("worker")
            d1 = self.query.value("old_data")
            what_is = self.query.value("what_is")

            if (len(d1)!=0 or d1.isspace()) and (len(workers)!=0 or workers.isspace()) and \
               (len(what_is)!=0 or what_is.isspace()):
                list_done.append(id_in_table)
            if period < 0 and performance != "Выполнено":
                list_overdue.append(id_in_table)
            if period > 0 and period <=10 and performance != "Выполнено":
                list_soon_data.append(id_in_table)
            if period == 0 and performance != "Выполнено":
                list_today.append(id_in_table)
            if period > 10 and performance != "Выполнено":
                list_not_done.append(id_in_table)

        for i in list_overdue:
            self.query.exec('''UPDATE comments_table SET performance = "Просрочено"
                               WHERE IthemID = '''+str(i))
        for i in list_soon_data:
            self.query.exec('''UPDATE comments_table SET performance = "Подходит срок"
                               WHERE IthemID = '''+str(i))
        for i in list_today:
            self.query.exec('''UPDATE comments_table SET performance = "Выполнить сегодня"
                               WHERE IthemID = '''+str(i))
        for i in list_not_done:
            self.query.exec('''UPDATE comments_table SET performance = "Не выполнено"
                               WHERE IthemID = '''+str(i))
        for i in list_done:
            self.query.exec('''UPDATE comments_table SET performance = "Выполнено"
                               WHERE IthemID = '''+str(i))

        list_not_done.clear()
        list_today.clear()
        list_overdue.clear()
        list_soon_data.clear()
        list_done.clear()

# ------------------------- Получаем сигнал со значением режима программы (админ или юзер) ---------------------------

    def sig_admin(self, b):
        self.FLAG_ADMIN = b
        self.programm_Mode()

#------------------------- Переключение режима работы программы (админ или пользователь) -----------------------------

    def programm_Mode(self):
        if self.FLAG_ADMIN:
            self.ui.action_Admin.setEnabled(False)
            self.ui.action_User.setEnabled(True)
            self.ui.action_Worker.setEnabled(True)
            self.ui.action_Station.setEnabled(True)
            self.ui.action_Password.setEnabled(True)
            self.ui.edit_checkBox.setEnabled(True)
        else:
            self.ui.action_Admin.setEnabled(True)
            self.ui.action_User.setEnabled(False)
            self.ui.action_Worker.setEnabled(False)
            self.ui.action_Station.setEnabled(False)
            self.ui.action_Password.setEnabled(False)
            self.ui.edit_checkBox.setEnabled(False)
            self.ui.edit_checkBox.setChecked(False)
            self.ui.del_Button.setEnabled(False)
            self.ui.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)  # Запрет редактирования таблицы.

#----------------------- Проверка состояния чекбокса --------------------------------------

    def check_checkBox(self):
        if self.ui.edit_checkBox.isChecked():
            self.ui.del_Button.setEnabled(True)
            self.ui.tableView.setEditTriggers(QAbstractItemView.AllEditTriggers)  # Разрешаем редактировать таблицу.
            self.ui.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers |  # Разрешаем редактирование таблицы
                                              QAbstractItemView.DoubleClicked)    # по двойному клику мышки
        else:
            self.ui.del_Button.setEnabled(False)
            self.ui.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)   # Запрет редактирования таблицы.

    # ------------------------------------------------------------------

    def __proverka(self):
        self.__compare_date()
        self.model.submitAll()
        self.model.select()

#--------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainwindow = Comments_View()
    mainwindow.show()
    sys.exit(app.exec())
