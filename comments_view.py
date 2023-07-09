""" ---------- Модуль просмотра замечаний --------------"""

import sys
from PySide6.QtCore import (Qt, QRect)
from PySide6.QtWidgets import (QApplication, QMainWindow, QStyledItemDelegate)
from PySide6.QtSql import (QSqlQuery, QSqlTableModel)
from PySide6.QtGui import QBrush, QColor
from delegate import NumericDelegate
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
        self.model = QSqlTableModel()
        #self.model = MyModel()

        self.model.setTable("comments_table")
        self.ui.tableView.setModel(self.model)

        self.ui.performance_Box.clear()
        self.ui.performance_Box.addItem("")
        self.ui.performance_Box.addItem("Выполнено")
        self.ui.performance_Box.addItem("Не выполнено")
        self.initial()

        self.ui.edit_checkBox.stateChanged.connect(self.check_checkBox)
        self.ui.commis_Box.currentIndexChanged.connect(self.__data_filter)
        self.ui.station_Box.currentIndexChanged.connect(self.__data_filter)
        self.ui.auditor_Box.currentIndexChanged.connect(self.__data_filter)
        self.ui.worker_Box.currentIndexChanged.connect(self.__data_filter)
        self.ui.performance_Box.currentIndexChanged.connect(self.__data_filter)

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

        self.query.exec("SELECT auditor FROM comments_table")
        list_auditor = []
        while self.query.next():
            name = self.query.value("auditor")
            list_auditor.append(name)
        new_list_auditor = set(list_auditor)                    # убираем дубликаты проверяющих из списка
        self.ui.auditor_Box.clear()
        self.ui.auditor_Box.addItem("")
        for i in new_list_auditor:
            self.ui.auditor_Box.addItem(i)
        del new_list_auditor
        del list_auditor

        self.query.exec("SELECT kommis FROM comments_table")
        list_kommis = []
        while self.query.next():
            name = self.query.value("kommis")
            list_kommis.append(name)
        new_list_kommis = set(list_kommis)
        self.ui.commis_Box.clear()
        self.ui.commis_Box.addItem("")
        for i in new_list_kommis:
            self.ui.commis_Box.addItem(i)
        del new_list_kommis
        del list_kommis

        self.ui.tableView.verticalHeader().hide()
        #self.ui.tableView.setColumnHidden(0, True)
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
        self.model.select()

        self.ui.tableView.setColumnWidth(1, 20)
        self.ui.tableView.setColumnWidth(2, 100)
        self.ui.tableView.setColumnWidth(3, 160)
        self.ui.tableView.setColumnWidth(4, 160)
        self.ui.tableView.setColumnWidth(5, 160)
        self.ui.tableView.setColumnWidth(6, 400)
        self.ui.tableView.setColumnWidth(7, 100)
        self.ui.tableView.setColumnWidth(8, 160)
        self.ui.tableView.setColumnWidth(9, 160)
        self.ui.tableView.setColumnWidth(10,100)
        self.ui.tableView.setColumnWidth(11,400)
        self.ui.tableView.setColumnWidth(12, 20)

        self.ui.tableView.resizeRowsToContents()                        # Содержимое вписывается в ячейку
        self.__data_filter()


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
        self.__color_row()

#------------------ Закрашиваем ячейку с номером замечания в зависимости от выполнения --------------------------

    def __color_row(self):
        self.query.exec("SELECT performance FROM comments_table")      #0xe3ebf8
        deleg = NumericDelegate()
        self.model.select()
        count = self.ui.tableView.model().rowCount()
        print(count)
        for i in range(0, count):
            #index = self.ui.tableView.model().index(i,9)
            #print(self.ui.tableView.model().data(index))
            #if self.ui.tableView.model().data(index) == "Не выполнено":
            self.ui.tableView.setItemDelegateForRow(i, deleg)



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

#----------------------- Проверка состояния чекбокса --------------------------------------

    def check_checkBox(self):
        if self.ui.edit_checkBox.isChecked():
            self.ui.del_Button.setEnabled(True)
        else:
            self.ui.del_Button.setEnabled(False)

#--------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainwindow = Comments_View()
    mainwindow.show()
    sys.exit(app.exec())
