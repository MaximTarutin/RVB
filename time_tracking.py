
""" -----  Модуль ведения учета рабочего времени работников бригады РЦС ----- """

import sys
from calendar import monthrange
from datetime import datetime
from PySide6.QtWidgets import (QApplication, QMainWindow, QAbstractItemView, QMessageBox)
from PySide6.QtSql import (QSqlTableModel, QSqlQuery)
from PySide6.QtCore import (Qt)
from delegate import (NoEditorDelegate, NumericDelegate, NumericDelegate_1)
import ui_time_tracking
import passwrd
import otgulwindow

class Time_tracking(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.FLAG_ADMIN = False
        self.FLAF_OTGUL = False                         # False - окно отгулы не открывалось ни разу
        self.Cur_Year = datetime.now().year             # Получаем текущий год
        self.Cur_Month = datetime.now().month           # Получаем текущий месяц
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowCloseButtonHint)     # деактивируем кнопку закрыть окно

        self.ui = ui_time_tracking.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.action_return.setText("&Назад")
        self.passwordWindow = passwrd.PasswordWindow()
        self.query = QSqlQuery()

        self.model = QSqlTableModel(self)               # Создаем модель и связываем таблицу
        self.model.setTable("time_tracking")            # с моделью
        self.ui.tableView.setModel(self.model)
        self.ui.spinBox_year.setValue(self.Cur_Year)                    # Выставляем текущий месяц и год
        self.ui.comboBox_month.setCurrentIndex(self.Cur_Month-1)
        self.calculation()

        self.msg = QMessageBox()
        self.ui.pushButton_save.hide()

#------------------------- Обработка сигналов ---------------------------------------------------------------

        self.ui.pushButton_return.clicked.connect(self.return_of_window)        # Кнопка вернуться назад
        self.ui.action_return.triggered.connect(self.return_of_window)          # Меню вернуться назад
        self.ui.spinBox_year.valueChanged.connect(self.init_table)              # Изменение года обновляем таблицу
        self.ui.comboBox_month.currentTextChanged.connect(self.init_table)      # Изменение месяца обновляем таблицу
        self.model.dataChanged.connect(self.calculation)                        # Расчет времени и сохранение
        self.ui.checkBox_korr.clicked.connect(self.check_checkbox)              # проверка состояния чекбокса
        self.ui.pushButton_Otgul.clicked.connect(self.__show_win_otgul)         # показать окно отгулов
        self.ui.action_otgul.triggered.connect(self.__show_win_otgul)
        self.ui.tableView.doubleClicked.connect(self.__click_to_table)

#-------------------------- Инициализация таблицы -----------------------------------------------------------
    def init_table(self):
        year = int(self.ui.spinBox_year.text())
        month = self.ui.comboBox_month.currentIndex()+1
        day = int(monthrange(year, month)[1])                   # количество дней в заданном году и месяце

        self.delegate_1 = NoEditorDelegate(self)                # Определяем делегаты для отображения в таблице
        self.delegate_2 = NumericDelegate(self)                 # цифры и определенные буквы валидатор
        self.delegate_3 = NumericDelegate_1(self)               # только цифры валидатор

    # Ячейки - дни месяца вводим цифры и определенные буквы
        for i in range(4,37):
            self.ui.tableView.setItemDelegateForColumn(i, self.delegate_2)

        self.ui.tableView.setItemDelegateForColumn(2, self.delegate_3)      # Столбец норма - вводим только цифры
        self.ui.tableView.setItemDelegateForColumn(1, self.delegate_1)      # Столбец сотрудник - не редактируется
        self.ui.tableView.setItemDelegateForColumn(3, self.delegate_1)      # Столбец факт - не редактируется
        self.ui.tableView.setItemDelegateForColumn(4, self.delegate_1)      # Столбец отгулы - не редактируется
        self.ui.tableView.setItemDelegateForColumn(5, self.delegate_3)

        self.model.setHeaderData(0, Qt.Horizontal, "№")                     # Наименование столбцов
        self.model.setHeaderData(1, Qt.Horizontal, "Сотрудник")
        self.model.setHeaderData(2, Qt.Horizontal, "Норма")
        self.model.setHeaderData(3, Qt.Horizontal, "Факт")
        self.model.setHeaderData(4, Qt.Horizontal, "Отгулы")
        self.model.setHeaderData(5, Qt.Horizontal, "Корр")
        self.ui.tableView.setColumnWidth(0,0)                               # Устанавливаем ширину столбцов
        self.ui.tableView.setColumnWidth(1,250)
        self.ui.tableView.setColumnWidth(2,60)
        self.ui.tableView.setColumnWidth(3,60)
        self.ui.tableView.setColumnWidth(4,60)
        self.ui.tableView.setColumnWidth(5,60)

        for i in range(6,37):
            self.model.setHeaderData(i, Qt.Horizontal, i-5)
            self.ui.tableView.setColumnWidth(i,45)

        if day == 30:                                       # Скрываем столбцы в зависимости от количества дней в месяце
            self.ui.tableView.setColumnHidden(36, True)
            self.ui.tableView.setColumnHidden(35, False)
            self.ui.tableView.setColumnHidden(34, False)
        elif day == 29:
            self.ui.tableView.setColumnHidden(35, True)
            self.ui.tableView.setColumnHidden(36, True)
            self.ui.tableView.setColumnHidden(34, False)
        elif day == 28:
            self.ui.tableView.setColumnHidden(34, True)
            self.ui.tableView.setColumnHidden(35, True)
            self.ui.tableView.setColumnHidden(36, True)
        elif day == 31:
            self.ui.tableView.setColumnHidden(34, False)
            self.ui.tableView.setColumnHidden(35, False)
            self.ui.tableView.setColumnHidden(36, False)

        self.ui.tableView.setColumnHidden(37, True)             # Скрываем столбец month
        self.ui.tableView.setColumnHidden(38, True)             # скрываем столбец year
        self.ui.tableView.setColumnHidden(39, True)             # скрываем столбец summa
        self.check_checkbox()

    # Далее необходимо проверить существуют ли в таблице заданные сотрудник, месяц и год, если нет то внести месяц и год
    # в ячейки month и year и сотрудника в ячейки Name таблицы time_tracking

        name_table_workers = []                             # Создаем список сотрудников
        count = 0

        self.query.exec('SELECT Name FROM workers')         # Заносим сотрудников из workers в список
        while self.query.next():
            name = self.query.value("Name")
            name_table_workers.append(name)

        self.query.exec('SELECT Name FROM time_tracking')   # Проверяем есть ли хоть одна запись в таблице
        while self.query.next():
            count+=1
        if count==0:                                        # Если таблица пуста, то вносим первую запись
            for i in name_table_workers:
                self.query.exec('''INSERT INTO time_tracking (Name,Norm,Otgul,Korr,d01,d02,d03,d04,d05,d06,d07,d08,d09,
                                                              d10,d11,d12,d13,d14,d15,d16,d17,d18,d19,d20,d21,d22,d23,
                                                              d24,d25,d26,d27,d28,d29,d30,d31, month, year, summa)   
                                VALUES ("''' + i + '''","0", "0", "0", "0","0","0","0","0","0","0","0","0","0",
                                        "0","0","0","0","0","0","0","0","0","0","0","0","0","0",
                                        "0","0","0","0","0","0","0", "''' + str(month) + '''", 
                                        "''' + str(year) + '''", "0")''')

        # Вносим данные в таблицу, если совпадений по месяцу и году нет
        count = 0
        self.query.exec(
            'SELECT month, year FROM time_tracking WHERE month="' + str(month) + '"and year="' + str(year) + '"')
        while self.query.next():
            count += 1
        if count == 0:
            for i in name_table_workers:
                self.query.exec('''INSERT INTO time_tracking (Name,Norm,Otgul,Korr,d01,d02,d03,d04,d05,d06,d07,d08,d09,
                                                                d10,d11,d12,d13,d14,d15,d16,d17,d18,d19,d20,d21,d22,d23,
                                                                d24,d25,d26,d27,d28,d29,d30,d31, month, year, summa)   
                                                VALUES ("''' + i + '''", "0", "0", "0", "0","0","0","0","0","0","0","0",
                                                        "0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0",
                                                        "0","0","0","0","0","0","0", "''' + str(month) + '''", 
                                                        "''' + str(year) + '''", "0")''')

        self.model.setFilter("month like '" + str(month) + "' AND year like '" + str(year) + "'")
        self.model.select()
        self.calculation()

#--------------------------- Клик по таблице вызывает информацию о данном рабочем дне -----------------------

    def __click_to_table(self):
        if self.FLAG_ADMIN: return     # если права администратора, то функцию не выполняем

        # ячейки с датами в таблице от 6 до 36
        temp = self.ui.tableView.currentIndex().column()
        if temp >= 6 and temp <= 36:
            cur_row = self.ui.tableView.currentIndex().row()            # получаем выбранную дату в формате yyyy-mm-dd
            cur_column = self.ui.tableView.currentIndex().column()
            select_day = cur_column - 5
            if select_day < 10 : select_day = "0"+str(select_day)
            select_month = self.ui.comboBox_month.currentIndex()+1
            if select_month < 10 : select_month = "0"+str(select_month)
            select_year = self.ui.spinBox_year.text()
            select_data = select_year+'-'+str(select_month)+'-'+str(select_day)
            name_workers = self.ui.tableView.model().index(cur_row, 1).data()   # получаем ФИО сотрудника

            # Находим данные по сотруднику на выбранный день из таблицы plan_table
            plantext=""
            count=0
            self.query.exec('SELECT * FROM plan_table')
            while self.query.next():
                datahide = self.query.value("DataHide")
                data = self.query.value("Data")
                name = self.query.value("Name")
                station = self.query.value("Station")
                plan = self.query.value("Plan")
                if datahide == select_data and name == name_workers :
                    plantext += str(count+1)+") "+station+"\n     "+plan+"\n"
                    count += 1
                    name1 = name
            self.query.next()
            if count == 0:
                plantext = "Данных нет"
                name1 = ""
            self.msg.setWindowTitle("План")
            self.msg.setText(name1+"\n"+plantext)
            self.msg.exec()

#--------------------------- Закрыть окно --------------------------------------------------------------------

    def return_of_window(self):
        self.calculation()
        self.close()

#------------------------- Получаем сигнал со значением режима программы (админ или юзер) ---------------------------

    def sig_admin(self, b):
        self.FLAG_ADMIN = b
        self.programm_Mode()

#------------------------- Настраиваем программы в зависимости от режима admin или user --------------------------

    def programm_Mode(self):
        if not self.FLAG_ADMIN:
            self.ui.action_user.setDisabled(True)
            self.ui.action_admin.setEnabled(True)
            self.ui.action_stations.setDisabled(True)
            self.ui.action_workers.setDisabled(True)
            self.ui.action_password.setDisabled(True)
            self.ui.checkBox_korr.setDisabled(True)
            self.ui.checkBox_korr.setChecked(False)
            self.ui.tableView.setColumnHidden(5, True)
            self.ui.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)     # Запрет редактирования таблицы.
            self.setWindowTitle("Учет рабочего времени")
        else:
            self.ui.action_admin.setDisabled(True)
            self.ui.action_user.setEnabled(True)
            self.ui.action_workers.setEnabled(True)
            self.ui.action_stations.setEnabled(True)
            self.ui.action_password.setEnabled(True)
            self.ui.checkBox_korr.setEnabled(True)
            self.ui.tableView.setEditTriggers(QAbstractItemView.AllEditTriggers)    # Разрешить редактировать таблицу
            self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
            self.setWindowTitle("Учет рабочего времени (режим администратора)")


    # Сделать проверку относительно текущего месяца и года, если удаляем сотрудника,
    # то удаляем все упоминания о нем после текущего месяца, если добавляем сотрудника,
    # то добавляем его начиная с текущего месяца и года, но не добавляем в таблицу ранее
    # текущего месяца)
    # В редакторе сотрудников предусмотреть кнопки "Полное удаление" и "удаление с текущего месяца"

    def compare_lists(self):
        name_table_workers = []
        name_table_time = []
        self.query.exec('SELECT Name FROM workers')  # Сначала читаем таблицу workers и
                                                     # создаем список сотрудников work_table_name
        while self.query.next():
            name = self.query.value("Name")
            name_table_workers.append(name)
        self.query.next()

        self.query.exec('SELECT Name FROM time_tracking')   # Далее читаем таблицу time_tracking
        while self.query.next():                            # и создаем список сотрудников time_tracking_name
            name = self.query.value("Name")
            name_table_time.append(name)
        self.query.next()

        for i in name_table_workers[:]:                     # сравниваем списки work_table_name и список
            if i in name_table_time:                        # time_table_name и удаляем одинаковые элементы
                name_table_workers.remove(i)                # В этом списке остаются сотрудники которых надо
                                                            # добавлять в таблицу time_tracking c текущего месяца
                name_table_time.remove(i)                   # В этом списке остаются сотрудники которых не следует
                                                            # отображать в таблице time_tracking с текущего месяца

        # убираем всех удаленных сотрудников начиная со следующего месяца
        for name in name_table_time:
            self.query.exec('''DELETE FROM time_tracking WHERE Name="'''+name+'''" AND 
                               month > '''+str(self.Cur_Month)+''' AND year >= '''+str(self.Cur_Year))

        # Добавляем новых сотрудников начиная с текущего месяца
        # создадим списки имеющихся в таблице time_tracking месяцев и годов

        month_list = []
        year_list = []

        self.query.exec('SELECT month, year FROM time_tracking')
        while self.query.next():
            month_list.append(self.query.value("month"))
            year_list.append(self.query.value("year"))
        self.query.next()

        # Удаляем повторяющиеся элементы в обоих списках, для этого преобразуем списки во множество,
        # а затем множество обратно в списки

        s = set(month_list)
        s1 = set(year_list)
        month_list = list(s)
        year_list = list(s1)

        # добавляем сотрудников из name_table_workers в том случае если элемент из списка year_list больше или равен
        # текущему году И (AND) элемент из списка month_list больше или равен текущему месяцу

        for name in name_table_workers:
            for y_l in year_list:
                for m_l in month_list:
                    if m_l >= self.Cur_Month and y_l >= self.Cur_Year:
                        self.query.exec('''INSERT INTO time_tracking (Name,Norm,Otgul,Korr,d01,d02,d03,d04,d05,d06,d07,
                                                                      d08,d09,d10,d11,d12,d13,d14,d15,d16,d17,d18,d19,
                                                                      d20,d21,d22,d23,d24,d25,d26,d27,d28,d29,d30,d31, 
                                                                      month,year,summa)   
                                            VALUES ("''' + name + '''", "0", "0", "0", "0","0","0","0","0","0","0","0",
                                                    "0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0",
                                                    "0","0","0","0","0","0","0", "''' + str(m_l) + '''", 
                                                    "''' + str(y_l) + '''", "0")''')
        self.model.select()


#---------------------- Расчет отработанного времени --------------------------------------------------------------

    def calculation(self):
        self.query.exec('''UPDATE time_tracking SET Fakt=d01+d02+d03+d04+d05+d06+d07+d08+d09+d10+d11+d12
                           +d13+d14+d15+d16+d17+d18+d19+d20+d21+d22+d23+d24+d25+d26+d27+d28+d29+d30+d31;''')
        self.query.exec('''UPDATE time_tracking SET Otgul=Fakt-Norm+Korr''')

        name_table=[]

        self.query.exec('''SELECT Name FROM time_tracking''')
        while self.query.next():
            name_table.append(self.query.value("Name"))
        self.query.next()
        for name in name_table:
            self.query.exec('''UPDATE time_tracking SET summa=(SELECT SUM(Otgul) FROM time_tracking 
            WHERE Name="'''+name+'''") WHERE Name="'''+name+'''"''')
        self.query.next()
        self.model.submitAll()
        self.model.select()



#------------------------- Проверяем состояние чекбокса корректировки времени -------------------------------------

    def check_checkbox(self):
        if self.ui.checkBox_korr.isChecked() == True:
            self.ui.tableView.setColumnHidden(5, False)
        else:
            self.ui.tableView.setColumnHidden(5, True)

    # ------------------------------- Показать окно отгулы ----------------------------------------------

    def __show_win_otgul(self):
        self.OtgulWindow = otgulwindow.OtgulWindow()
        self.OtgulWindow.show()

#----------------- Обработка нажатия клавиши ENTER --------------------------------

    def keyPressEvent(self, e):
        if e.key() in [Qt.Key_Enter, Qt.Key_Return]:
            self.calculation()


#-------------------------------------------------------------------------------------------------------------------
if __name__=='__main__':
    app = QApplication(sys.argv)
    mywindow = Time_tracking()
    mywindow.show()
    sys.exit(app.exec())