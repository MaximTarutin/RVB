""" ---------- Модуль просмотра замечаний --------------"""

# ДОРАБАТЫВАЕМ ДЕЛЕГАТ КНОПКИ


import sys
from PySide6.QtCore import (Qt, QDate, QDir)
from PySide6.QtWidgets import (QApplication, QMainWindow, QAbstractItemView, QLabel, QFileDialog)
from PySide6.QtSql import (QSqlQuery, QSqlTableModel)
from datetime import (date, datetime)
from delegate import (ColorDelegate, NoEditorDelegate, Date_delegate, Worker_Name_delegate, Button_delegate,
                      Foto_Color_Delegate)
import xlsxwriter
import ui_commentsview
from file_view import File_View

class Lbl(QLabel):
    def __init__(self, parrent=None):
        super().__init__(parrent)
    def init(self):
        self.resize(600,600)
        self.show()

class Comments_View(QMainWindow):
    def __init__(self, parrent = None):
        self.signal_value = None
        self.FLAG_ADMIN = False
        super().__init__(parrent)
        self.ui = ui_commentsview.Ui_CommentsView()
        self.ui.setupUi(self)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowCloseButtonHint)  # деактивируем кнопку закрыть окно
        self.ui.del_Button.setEnabled(False)
        self.ui.day_dateEdit.setDate(QDate.currentDate())
        self.query = QSqlQuery()

        self.color_delegat = ColorDelegate(self)
        self.no_edit_delegat = NoEditorDelegate(self)
        self.date_delegat = Date_delegate(self)
        self.worker_delegat = Worker_Name_delegate(self)
        self.button_delegat = Button_delegate(self)
        self.foto_color_delegat = Foto_Color_Delegate(self)
        self.fileview = File_View()


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
        self.model.setHeaderData(13, Qt.Horizontal,"*")

        self.ui.tableView.setModel(self.model)

        self.ui.performance_Box.clear()
        self.ui.performance_Box.addItem("")
        self.ui.performance_Box.addItem("Выполнено")
        self.ui.performance_Box.addItem("Не выполнено")
        self.ui.performance_Box.addItem("Подходит срок")
        self.ui.performance_Box.addItem("Выполнить сегодня")
        self.ui.performance_Box.addItem("Просрочено")

        self.ui.tableView.setColumnHidden(0, True)
        self.ui.tableView.setColumnHidden(14, True)
        self.ui.tableView.setItemDelegateForColumn(1, self.no_edit_delegat) # запрещаем редактирование некоторых
        self.ui.tableView.setItemDelegateForColumn(2, self.no_edit_delegat) # столбцов
        self.ui.tableView.setItemDelegateForColumn(3, self.no_edit_delegat)
        self.ui.tableView.setItemDelegateForColumn(4, self.no_edit_delegat)
        self.ui.tableView.setItemDelegateForColumn(5, self.no_edit_delegat)
        self.ui.tableView.setItemDelegateForColumn(6, self.no_edit_delegat)
        self.ui.tableView.setItemDelegateForColumn(7, self.date_delegat)    # Установка даты в ячейке
        self.ui.tableView.setItemDelegateForColumn(8, self.worker_delegat)  # выпадающий список
        self.ui.tableView.setItemDelegateForColumn(9, self.color_delegat)   # Цвет ячейки в зависимости от выполнения
        self.ui.tableView.setItemDelegateForColumn(10, self.date_delegat)   # Установка даты в ячейке
        self.ui.tableView.setItemDelegateForColumn(12, self.foto_color_delegat)
        self.ui.tableView.setItemDelegateForColumn(13, self.button_delegat)

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
        self.ui.tableView.setColumnWidth(13, 20)

        self.initial()

        self.ui.edit_checkBox.stateChanged.connect(self.__check_checkBox)           # разрешено ли редактирование?
        self.ui.edit_checkBox_data.stateChanged.connect(self.__check_checkBox)      # включен ли фильтр по дате?
        self.ui.commis_Box.currentIndexChanged.connect(self.__data_filter)          # применяем фильтр по коммиссии
        self.ui.station_Box.currentIndexChanged.connect(self.__data_filter)         # применяем фильтр по станции
        self.ui.auditor_Box.currentIndexChanged.connect(self.__data_filter)         # применяем фильтр по проверяющему
        self.ui.worker_Box.currentIndexChanged.connect(self.__data_filter)          # применяем фильтр по исполнителю
        self.ui.performance_Box.currentIndexChanged.connect(self.__data_filter)     # применяем фильтр по выполнению
        self.ui.day_dateEdit.dateChanged.connect(self.__data_filter)                # применяем фильтр по дате
        self.model.dataChanged.connect(self.__proverka)                             # если в таблице (модели) меняется
                                                                                    # какая либо дата, то изменяем
                                                                                    # формат из yyyy-MM-dd в dd.MM.yyyy
        self.button_delegat.button_signal.connect(self.sig_delegate)                # принимаем номер строки из делегата
        self.fileview.ui.pushButton_del.clicked.connect(self.__del_file)            # удаляем фото из базы данных
        self.fileview.ui.pushButton_close.clicked.connect(self.__close_file)        # Закрываем просмотр фото
        self.fileview.ui.pushButton_save.clicked.connect(self.__save_file)          # Сохраняем фото
        self.ui.excel_Button.clicked.connect(self.data_to_excel)                    # Конвентируем отчет в Excel
        self.ui.action_Excel.triggered.connect(self.data_to_excel)
        self.ui.del_Button.clicked.connect(self.__del_string)                       # Удаляем выбранные строки

# ------------------------- Инициализация -------------------------------

    def initial(self):
        self.ui.edit_checkBox_data.setEnabled(True)
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

        self.__check_checkBox()
        self.model.select()
        self.__data_filter()
        self.__compare_date()
        self.ui.tableView.resizeRowsToContents()                        # Содержимое вписывается в ячейку


# ------------------------- отображаем данные в таблице по заданному фильтру ----------------------------------------

    def __data_filter(self):
        commis = self.ui.commis_Box.currentText()
        station = self.ui.station_Box.currentText()
        auditor = self.ui.auditor_Box.currentText()
        worker = self.ui.worker_Box.currentText()
        performance = self.ui.performance_Box.currentText()
        data = self.ui.day_dateEdit.date().toString("dd.MM.yyyy")

        if not self.ui.edit_checkBox_data.isChecked():
            self.model.setFilter('''kommis like "%'''+commis+'''%" AND station like "%'''+station+'''%" AND
                                    auditor like "%'''+auditor+'''%" AND worker like "%'''+worker+'''%" AND
                                    performance like "'''+performance+'''%"''')
        else:
            self.model.setFilter('''data like "%'''+data+'''%" AND kommis like "%''' + commis + '''%" AND 
                                    station like "%''' + station + '''%" AND auditor like "%''' + auditor + '''%" AND 
                                    worker like "%''' + worker + '''%" AND
                                    performance like "''' + performance + '''%"''')

# ------------------------------  изменение статуса выполнения -------------------------------------

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
            d0 = datetime.strptime(d0,"%d.%m.%Y").date()
            data_1 = date.today()
            period = (d0-data_1).days
            workers = self.query.value("worker")
            d1 = self.query.value("old_data")
            what_is = self.query.value("what_is")

            # Если поля срок, исполнитель и что сделано заполнены, то ставим в поле выполнение статус "Выполнено",
            # иначе выставляем статус в зависимости от разницы сроки и текущей даты

            if (len(d1) != 0 or d1.isspace()) and (len(workers) != 0 or workers.isspace()) and \
                    (len(what_is) != 0 or what_is.isspace()):
                list_done.append(id_in_table)
            elif period < 0:
                list_overdue.append(id_in_table)
            elif period > 0 and period <= 10:
                list_soon_data.append(id_in_table)
            elif period == 0:
                list_today.append(id_in_table)
            elif period > 10:
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

# ------------------------- Переключение режима работы программы (админ или пользователь) -----------------------------

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

# ----------------------- Проверка состояния чекбоксов --------------------------------------

    def __check_checkBox(self):
        if self.ui.edit_checkBox.isChecked():
            self.ui.del_Button.setEnabled(True)
            self.ui.tableView.setEditTriggers(QAbstractItemView.AllEditTriggers)  # Разрешаем редактировать таблицу.
            self.ui.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers |  # Разрешаем редактирование таблицы
                                              QAbstractItemView.DoubleClicked)    # по двойному клику мышки
        else:
            self.ui.del_Button.setEnabled(False)
            self.ui.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)   # Запрет редактирования таблицы.
        if self.ui.edit_checkBox_data.isChecked():
            self.ui.day_dateEdit.setEnabled(True)
            self.__data_filter()
        else:
            self.ui.day_dateEdit.setDisabled(True)
            self.__data_filter()

# ------------- Меняем формат даты из делегата (yyyy-MM-dd) в формат dd.MM.yyyy и производим изменения -----------------
# -------------------- в базе данных, также производим сравнение даты выполнения и текущей даты ------------------------

    def __format_date(self):
        temp = {}
        temp1 = {}
        self.query.exec("SELECT IthemID, term_data, old_data FROM comments_table")
        while self.query.next():
            t_d = self.query.value("term_data")
            o_d = self.query.value("old_data")
            t_it_id = self.query.value("IthemID")
            o_it_id = self.query.value("IthemID")
            new_t_d = QDate.fromString(t_d, "yyyy-MM-dd")
            new_t_d = new_t_d.toString("dd.MM.yyyy")
            new_o_d = QDate.fromString(o_d, "yyyy-MM-dd")
            if new_o_d > QDate.currentDate():               # Дата выполнения не может быть больше текущей даты
                new_o_d = QDate.currentDate()
            new_o_d = new_o_d.toString("dd.MM.yyyy")
            if len(new_t_d) > 0:
                temp[t_it_id] = new_t_d
            if len(new_o_d) > 0:
                temp1[o_it_id] = new_o_d
        for i in list(temp):
            tmp = temp[i]
            self.query.exec('''UPDATE comments_table SET term_data="''' + str(tmp) + '''" WHERE IthemID=''' + str(i))
        for i in list(temp1):
            tmp1 = temp1[i]
            self.query.exec('''UPDATE comments_table SET old_data="''' + str(tmp1) + '''" WHERE IthemID=''' + str(i))
        temp.clear()
        temp1.clear()

# ----------- Проверка статуса замечаний (выполнено, не выполнено, просрочено и т.д.) --------------------------------

    def __proverka(self):
        self.__format_date()
        self.__compare_date()
        self.model.submitAll()
        self.model.select()
        self.initial()

# ------------------- Получаем номер строки в которой нажат делегат кнопка ----------------------------------

    def sig_delegate(self, b):
        self.signal_value = b
        self.check_button()

#  ------------------------- проверяем есть ли фото в базе данных ----------------------------------------

    def check_button(self):
        self.query.exec("SELECT foto FROM comments_table WHERE IthemID = " + str(self.signal_value))
        self.query.next()
        foto = self.query.value("foto")
        if foto == 'нет':
            self.__add_foto()
        elif foto == 'да':
            self.__view_foto()
        self.model.select()
        self.initial()

# ------------------------------------- Добавляем фото в базу -----------------------------------------

    def __add_foto(self):
        self.fileview.setParent(self)
        self.fileview.load_file_to_db(self.signal_value)

# ------------------------------------ Просматриваем фото --------------------------------------------

    def __view_foto(self):
        self.fileview.setParent(None)
        self.fileview.open_file_from_db(self.signal_value)

# ----------------------------------- Удаляем фото ---------------------------------------------------

    def __del_file(self):
        self.fileview.del_file_from_db(self.signal_value)
        self.model.select()

# ----------------------------------- Сохраняем фото -------------------------------------------------

    def __save_file(self):
        self.fileview.save_file(self.signal_value)

# ------------------------------------ Закрываем просмотр фото ----------------------------------------

    def __close_file(self):
        self.fileview.close_file_view()
        self.model.select()

# ------------------------------------- Запись в Excel ------------------------------------------------

    def data_to_excel(self):
        f = QFileDialog.getSaveFileName(self, caption='Сохранить как...', filter="Excel *.xlsx (*.xlsx)")
        if f[0]!="":
            kommis = self.ui.commis_Box.currentText()
            station = self.ui.station_Box.currentText()
            auditor = self.ui.auditor_Box.currentText()
            worker = self.ui.worker_Box.currentText()
            performance = self.ui.performance_Box.currentText()
            data = self.ui.day_dateEdit.text()
            index = 4

            workbook = xlsxwriter.Workbook(f[0])
            worksheet = workbook.add_worksheet()
            worksheet.set_landscape()
            worksheet.set_page_view()
            worksheet.set_paper(9)
            merge_format = workbook.add_format({
                'bold': True,                       # Полужирный шрифт
                'align': 'center',
                'valign': 'vcenter',
                'font_size': 14,
            })
            worksheet.merge_range('A1:G2', 'ОТЧЕТ \n по замечаниям выявленым в ходе проверки _____ ', merge_format)
            merge_format1 = workbook.add_format({
                'text_wrap': True,                  #   Текст переносить по словам
                'border': 1,                        #   Установить границы ячейки
                'font_size': 12,                    #   Размер шрифта
                'align': 'center',                  #   Форматирование по центру
                'valign': 'vcenter'
            })
            merge_format2 = workbook.add_format({
                'text_wrap': True,  # Текст переносить по словам
                'border': 1,  # Установить границы ячейки
                'font_size': 12,  # Размер шрифта
                'align': 'fill',  # Форматирование по центру
                'valign': 'vcenter'
            })
            worksheet.set_column('A:A',4)
            worksheet.set_column('B:B',15)
            worksheet.set_column('C:C',37)
            worksheet.set_column('D:D',10)                  # Устанавливаем ширину столбцов
            worksheet.set_column('E:E',15)
            worksheet.set_column('F:F',10)
            worksheet.set_column('G:G',35)
            worksheet.write(3,0,'№', merge_format1)
            worksheet.write(3,1,'Станция', merge_format1)
            worksheet.write(3,2,'Выявленные замечания', merge_format1)
            worksheet.write(3,3,'Срок исполнения', merge_format1)                   # Запись данных в ячейки
            worksheet.write(3,4,'Исполнитель', merge_format1)
            worksheet.write(3,5,'Дата', merge_format1)
            worksheet.write(3,6,'Отметка о выполнении', merge_format1)

            if self.ui.edit_checkBox_data.isChecked() == False:
                self.query.exec('''SELECT * FROM comments_table WHERE kommis LIKE "%''' + str(kommis) + '''%" AND
                               station LIKE "%'''+str(station)+'''%" AND auditor LIKE "%'''+str(auditor)+'''%" AND 
                               worker LIKE "%'''+str(worker)+'''%" AND performance LIKE "%'''+str(performance)+'''%"''')
            else:
                self.query.exec('''SELECT * FROM comments_table WHERE kommis LIKE "%''' + str(kommis) + '''%" AND
                               station LIKE "%'''+str(station)+'''%" AND auditor LIKE "%'''+str(auditor)+'''%" AND 
                               worker LIKE "%'''+str(worker)+'''%" AND performance LIKE "%'''+str(performance)+'''%" AND
                               data LIKE "%'''+str(data)+'''%"''')
            while self.query.next():
                number_db = self.query.value("number")
                station_db = self.query.value("station")
                comment_db = self.query.value("comment")
                term_data_db = self.query.value("term_data")
                worker_db = self.query.value("worker")
                old_data_db = self.query.value("old_data")
                what_is_db = self.query.value("what_is")
                worksheet.write(index, 0, number_db, merge_format1)
                worksheet.write(index, 1, station_db, merge_format1)
                worksheet.write(index, 2, comment_db, merge_format2)
                worksheet.write(index, 3, term_data_db, merge_format1)
                worksheet.write(index, 4, worker_db, merge_format1)
                worksheet.write(index, 5, old_data_db, merge_format1)
                worksheet.write(index, 6, what_is_db, merge_format2)
                index+=1

            worksheet.write(index+2, 2, 'РЦСНС - _________/_______________________/', merge_format)
            workbook.close()

# ---------------------------------- Удаление выбранной строки --------------------------------------

    def __del_string(self):
        if self.ui.tableView.selectionModel().hasSelection():
            for index in self.ui.tableView.selectedIndexes() or []:
                self.ui.tableView.model().removeRow(index.row())
        self.model.select()

#--------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainwindow = Comments_View()
    mainwindow.show()
    sys.exit(app.exec())
