"""
      Модуль для работы с редакторами:
        1) Редактор сотрудников бригады РЦС
        2) Редактор станций и перегонов
"""

import sys
from PySide6.QtCore import (Qt)
from PySide6.QtWidgets import (QApplication, QMainWindow, QAbstractItemView)
from PySide6.QtSql import (QSqlTableModel, QSqlQuery)
import ui_workerwindow
from delegate import (Worker_delegate)

#-------------------------------------------------------------------------------------------------------------#
#--------------------------------- Окно редактирования сотрудников -------------------------------------------#
#-------------------------------------------------------------------------------------------------------------#

class WorkerWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = ui_workerwindow.Ui_workerWindow()
        self.ui.setupUi(self)

        self.query = QSqlQuery()
        self.model = QSqlTableModel(self)                                       # Создаем модель и связываем таблицу
        self.model.setTable("workers")                                          # с моделью
        self.model.select()
        self.ui.tableView.setModel(self.model)

        self.setWindowFlags(self.windowFlags() & ~Qt.WindowCloseButtonHint)     # деактивируем кнопку закрыть окно

        self.ui.action_user.setVisible(False)
        self.ui.action_admin.setVisible(False)

        self.init_table()

#--------------------------------- Обработка событий -----------------------------------------------------------------

        self.ui.button_add.clicked.connect(self.__add_data_db)         # Добавить новую строку в таблицу
        self.ui.button_del.clicked.connect(self.__del_string)          # Удаляем выбранную строку с текущего месяца


#---------------------------- Добавление новой строки в таблицу --------------------------------------

    def __add_data_db(self):
        self.query.exec('''SELECT * FROM workers''')
        while self.query.next():
            name = self.query.value("Name")
            post = self.query.value("Post")
            number = self.query.value("Number")
            if len(name)==0 or name.isspace() or \
                    len(post)==0 or post.isspace() \
                    or len(number)==0 or number.isspace():  #Если попадается пустое значение выходим из функции
                return
        self.query.exec_("INSERT INTO workers (Name, Post, Number) values('','','')")
        self.query.next()
        self.model.select()

#---------------------------------- Удаление выбранной строки --------------------------------------

    def __del_string(self):
        if self.ui.tableView.selectionModel().hasSelection():
            for index in self.ui.tableView.selectedIndexes() or []:
                self.ui.tableView.model().removeRow(index.row())
        self.model.select()

#--------------------------------- Инициализация таблицы -------------------------------------------

    def init_table(self):
        self.deleg = Worker_delegate(self)
        self.ui.tableView.setItemDelegateForColumn(2,self.deleg)                # Во 2 столбце задействуем делегат

        self.model.setHeaderData(0, Qt.Horizontal, "")
        self.model.setHeaderData(1, Qt.Horizontal, "Сотрудник")                 # заголовки столбцов
        self.model.setHeaderData(2, Qt.Horizontal, "Должность")
        self.model.setHeaderData(3, Qt.Horizontal, "Таб №")

        self.ui.tableView.setColumnWidth(0,0)
        self.ui.tableView.setColumnWidth(1,280)                                 # Устанавливаем ширину столбцов
        self.ui.tableView.setColumnWidth(2,180)
        self.ui.tableView.setColumnWidth(3,70)

        self.ui.tableView.verticalHeader().hide()                               # Скрываем нумерацию строк

        self.ui.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers |    # Разрешаем редактирование таблицы
                             QAbstractItemView.DoubleClicked)                   # по двойному клику мышки
        self.ui.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)    # Разрешаем выделение строк

#---------------------------------------------------------------------------------------------------------------------#
#---------------------------------- Окно редактирования станций и перегонов ------------------------------------------#
#---------------------------------------------------------------------------------------------------------------------#

class StationWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = ui_workerwindow.Ui_workerWindow()
        self.ui.setupUi(self)
        self.ui.label.setText('Редактор станций и перегонов')
        self.setWindowTitle('Станции и перегоны')
        self.setWindowFlags(self.windowFlags() | Qt.CustomizeWindowHint)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowCloseButtonHint)     # деактивируем кнопку закрыть окно.

        self.ui.button_add.setText("Добавить станцию")
        self.ui.button_del.setText("Удалить станцию")

        self.query = QSqlQuery()
        self.model = QSqlTableModel(self)                               # Создаем модель и связываем таблицу с моделью
        self.model.setTable("station")
        self.model.select()
        self.ui.tableView.setModel(self.model)

        self.__init_table()

        self.ui.action_user.setVisible(False)
        self.ui.action_admin.setVisible(False)

#--------------------------------- Инициализация таблицы -------------------------------------------

    def __init_table(self):
        self.model.setHeaderData(0, Qt.Horizontal, "")
        self.model.setHeaderData(1, Qt.Horizontal, "Станция или перегон")                 # заголовки столбцов

        self.ui.tableView.setColumnWidth(0,0)
        self.ui.tableView.setColumnWidth(1,530)                                 # Устанавливаем ширину столбцов
        self.ui.tableView.verticalHeader().hide()                               # Скрываем нумерацию строк
        self.ui.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers |    # Разрешаем редактирование таблицы
                             QAbstractItemView.DoubleClicked)                   # по двойному клику мышки
        self.ui.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)    # Разрешаем выделение строк

        self.model.select()


    #--------------------------------- Обработка событий -------------------------------------------------

        self.ui.button_add.clicked.connect(self.__add_data_db)            # Добавить новую строку в таблицу
        self.ui.button_del.clicked.connect(self.__del_string)             # Удаляем выбранную строку из таблицы и базы


#---------------------------- Добавление новой строки в таблицу --------------------------------------

    def __add_data_db(self):
        self.query.exec('''SELECT * FROM station''')
        while self.query.next():
            name = self.query.value("Name")
            if len(name)==0 or name.isspace():                      # Если попадается пустое значение выходим из функции
                return
        self.query.exec_("INSERT INTO station (Name) values('')")
        self.query.next()
        self.model.select()

#---------------------------------- Удаление выбранной строки --------------------------------------

    def __del_string(self):
        if self.ui.tableView.selectionModel().hasSelection():
            for index in self.ui.tableView.selectedIndexes() or []:
                self.ui.tableView.model().removeRow(index.row())
        self.model.select()



#----------------------------------------------------------------------------------------------------------------------

if __name__=='__main__':
    app = QApplication(sys.argv)
    mywindow = WorkerWindow()
    sys.exit(app.exec())