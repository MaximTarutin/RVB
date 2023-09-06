"""
-------------------------------------------------------------------------------
        Программа предназначена для управления бригадой работников РЦС:
           1) Учет рабочего времени каждого работника по факту и нормативу
           2) Планирование работ каждого работника на станциях и перегонах
           3) Ввод и контроль устранения замечаний ревизий разного уровня
-------------------------------------------------------------------------------
"""

import sys
import rc_res
from PySide6.QtCore import (Signal)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMessageBox)
from PySide6.QtSql import (QSqlDatabase, QSqlQueryModel, QSqlQuery)
import time_tracking
import worker
import ui_mainwindow
import passwrd
import plan_window
import comments_main
import comments_new
import comments_view
import help_window

class MyWindow(QMainWindow, ui_mainwindow.Ui_MainWindow):
    admin_signal = Signal(bool)
    def __init__(self):
        super().__init__()
        self.FLAG_ADMIN = False
        self.setupUi(self)

        self.passwordWindow = passwrd.PasswordWindow()                  # окно ввода пароля
        self.editPasswordWindow = passwrd.PasswordWindow()              # окно смены пароля
        self.newPasswordWindow = passwrd.PasswordWindow()               # окно ввода нового пароля при первом запуске
        self.commentsMain = comments_main.Comments_main()               # модуль работы с замечаниями
        self.commentsNew = comments_new.New_Comments_Window()           # Модуль ввода замечаний
        self.commentsView = comments_view.Comments_View()               # Модуль просмотра и редактирования замечаний
        self.helpWindow = help_window.HelpWindow()                      # Модуль справки

        self.query = QSqlQuery()
        self.model = QSqlQueryModel(self)

        self.db_init()                                                  # Инициализируем базу данных

        self.workerWindow = worker.WorkerWindow()                       # окно редактора сотрудников
        self.stationWindow = worker.StationWindow()                     # окно редактора станций и перегонов
        self.timeTrackingWindow = time_tracking.Time_tracking()         # окно учета рабочего времени сотрудников
        self.planWindow = plan_window.Plan_Window()                     # окно планировщика работ

        self.passwordWindow.ui.passw_label_2.hide()
        self.passwordWindow.ui.passw_label_3.hide()
        self.passwordWindow.ui.new_passw_lineEdit_1.hide()
        self.passwordWindow.ui.new_passw_lineEdit.hide()
        self.passwordWindow.ui.passw_label.move(20, 140)
        self.passwordWindow.ui.passw_lineEdit.move(290, 140)

        self.newPasswordWindow.ui.passw_lineEdit.hide()
        self.newPasswordWindow.ui.passw_label.hide()
        self.newPasswordWindow.ui.passw_label_2.move(20, 100)
        self.newPasswordWindow.ui.new_passw_lineEdit.move(290, 100)
        self.newPasswordWindow.ui.passw_label_3.move(20, 150)
        self.newPasswordWindow.ui.new_passw_lineEdit_1.move(290, 150)
        self.newPasswordWindow.ui.label.setText('Создайте пароль администратора')

        self.resize(800, 600)
        self.setWindowTitle('РВБ')
        self.show()

        self.programm_Mode()                        # Настройка активных пунктов меню в зависимости от режима программы


#------------------------ Обработчики событий --------------------------------------------------------------------

        # ************* События модуля main.py **************

        self.action_exit.triggered.connect(self.exitofprogramm)                         # меню выход из программы
        self.action_worker.triggered.connect(self.open_workerWindow)                    # меню редактор сотрудников
        self.action_time.triggered.connect(self.open_time_tracking)                     # меню учет рабочего времени
        self.action_station.triggered.connect(self.open_stationWindow)                  # меню редактор станций
        self.action_plan.triggered.connect(self.open_planwindow)                        # меню планирование работ
        self.action_remark.triggered.connect(self.open_comments_main)                   # меню модуль замечаний
        self.action_admin.triggered.connect(self.open_passwordWindow)                   # меню режим администратора
        self.action_user.triggered.connect(self.user_Mode)                              # меню режим пользователя
        self.action_user.triggered.connect(self.sig_admin)
        self.action__new_password.triggered.connect(self.edit_passwordWindow)           # меню изменить пароль
        self.Button_exit.clicked.connect(self.exitofprogramm)                           # кнопка выход из программы
        self.button_1.clicked.connect(self.open_time_tracking)                          # кнопка учет времени сотрудник
        self.button_3.clicked.connect(self.open_planwindow)                             # кнопка планировщик работ
        self.button_2.clicked.connect(self.open_comments_main)                          # кнопка модуль замечаний
        self.action_about.triggered.connect(self.help_about)                            # меню о программе
        self.action_module.triggered.connect(self.help_main_window)                     # меню модули

        # ************* События модуля time_tracking.py **************

        self.timeTrackingWindow.ui.action_workers.triggered. \
            connect(self.open_workerWindow)                                             # меню редактор сотрудников
        self.timeTrackingWindow.ui.action_stations.triggered. \
            connect(self.open_stationWindow)                                            # меню редактор станций
        self.timeTrackingWindow.ui.action_admin.triggered.connect \
            (self.open_passwordWindow)                                                  # меню режим администратора
        self.timeTrackingWindow.ui.action_user.triggered.connect \
            (self.user_Mode)                                                            # меню режим пользователя
        self.timeTrackingWindow.ui.action_password.triggered. \
            connect(self.edit_passwordWindow)                                           # меню изменить пароль
        self.timeTrackingWindow.ui.action_return.triggered. \
            connect(self.close_time_tracking)                                           # меню вернуться
        self.timeTrackingWindow.ui.pushButton_return.clicked. \
            connect(self.close_time_tracking)                                           # Кнопка вернуться
        self.timeTrackingWindow.ui.action_about.triggered. \
            connect(self.help_about)                                                    # меню о программе

        # ************* События модуля worker.py **************

        self.workerWindow.ui.button_return.clicked.connect(self.close_workerWindow)     # Закрыть редактор сотрудников
        self.workerWindow.ui.action_return.triggered.connect(self.close_workerWindow)   # Закрыть редактор сотрудников
        self.stationWindow.ui.button_return.clicked.connect(self.close_stationWindow)   # Закрыть редактор станций
        self.stationWindow.ui.action_return.triggered.connect(self.close_stationWindow) # Закрыть редактор станций
        self.workerWindow.ui.action_about.triggered.connect(self.help_about)            # меню о программе
        self.stationWindow.ui.action_about.triggered.connect(self.help_about)

        # ************ События модуля password.py **************

        self.passwordWindow.admin_signal[bool].connect(self.sig_admin)                      # принимаем сигнал режима
        self.passwordWindow.admin_signal[bool].connect(self.timeTrackingWindow.sig_admin)   # программы (админ или юзер)
        self.passwordWindow.admin_signal[bool].connect(self.planWindow.sig_admin)
        self.passwordWindow.admin_signal[bool].connect(self.commentsNew.sig_admin)
        self.passwordWindow.admin_signal[bool].connect(self.commentsView.sig_admin)
        self.newPasswordWindow.ui.button_Cancel.clicked.connect(self.close)                 # если пароль не создан
                                                                                            # то программа не запустится
        # ************ События модуля plan_window.py ******************

        self.planWindow.ui.action_admin.triggered.connect \
            (self.open_passwordWindow)                                                  # меню режим администратора
        self.planWindow.ui.action_user.triggered.connect(self.user_Mode)                # меню режим пользователя
        self.planWindow.ui.action_workers.triggered.connect(self.open_workerWindow)     # меню редактор сотрудников
        self.planWindow.ui.action_stations.triggered.connect(self.open_stationWindow)   # меню редактор станций
        self.planWindow.ui.action_plan_edit.triggered.connect \
            (self.planWindow.add_plan)                                                  # меню редактор планировщика
        self.planWindow.ui.action_admin_edit.triggered.connect \
            (self.edit_passwordWindow)                                                  # изменить пароль администратора
        self.planWindow.ui.action_return.triggered.connect(self.close_planwindow)       # меню вернуться назад
        self.planWindow.ui.pushButton_return.clicked.connect(self.close_planwindow)     # кнопка вернуться назад
        self.planWindow.ui.action_about.triggered.connect(self.help_about)              # меню о программе

        # ************** события модуля comments_main.py ****************

        self.commentsMain.ui.newcommit_button.clicked.connect(self.openCommentsNew)     # открыть модуль ввода замечаний
        self.commentsMain.ui.return_button.clicked.connect(self.close_comments_main)    # закрыть окно
        self.commentsMain.ui.viewcommit_button.clicked.connect(self.openCommentView)    # открыть модуль просмотра замеч

        #************** события модуля comments_new.py *****************

        self.commentsNew.ui.Return_pushButton.clicked.connect(self.closeCommentsNew)    # закрыть модуль ввода замечаний
        self.commentsNew.ui.action_return.triggered.connect(self.closeCommentsNew)
        self.commentsNew.ui.action_admin.triggered.connect(self.open_passwordWindow)    # перейти в режим администратора
        self.commentsNew.ui.action_user.triggered.connect(self.user_Mode)               # перейти в режим пользователя
        self.commentsNew.ui.action_workers.triggered.connect(self.open_workerWindow)    # меню редактор сотрудников
        self.commentsNew.ui.action_stations.triggered.connect(self.open_stationWindow)  # меню редактор станций
        self.commentsNew.ui.action_password.triggered.connect(self.edit_passwordWindow) # изменить пароль администратора
        self.commentsNew.ui.action_about.triggered.connect(self.help_about)             # меню о программе

        # *************** события модуля comments_view.py **********************

        self.commentsView.ui.action_Return.triggered.connect(self.closeCommentView)     # закрыть модуль просмотра
        self.commentsView.ui.return_pushButton.clicked.connect(self.closeCommentView)   # и редактирования замечаний
        self.commentsView.ui.action_User.triggered.connect(self.user_Mode)              # перейти в режим пользователя
        self.commentsView.ui.action_Admin.triggered.connect(self.open_passwordWindow)   # перейти в режим администратора
        self.commentsView.ui.action_Worker.triggered.connect(self.open_workerWindow)    # меню редактор сотрудников
        self.commentsView.ui.action_Station.triggered.connect(self.open_stationWindow)  # меню редактор станций
        self.commentsView.ui.action_Password.triggered.connect \
            (self.edit_passwordWindow)                                                  # изменить пароль администратора
        self.commentsView.ui.action_About.triggered.connect(self.help_about)            # меню о программе

# -------------------------- Сигналы --------------------------------------------

        self.admin_signal[bool].connect(self.sig_admin)                                 # принимаем сигнал во всех окнах
        self.admin_signal[bool].connect(self.timeTrackingWindow.sig_admin)
        self.admin_signal[bool].connect(self.planWindow.sig_admin)
        self.admin_signal[bool].connect(self.commentsNew.sig_admin)
        self.admin_signal[bool].connect(self.commentsView.sig_admin)

        self.user_Mode()  # Включаем режим пользователя

# ----------------------------- О программе --------------------------------------------------

    def help_about(self):
        self.helpWindow.about()

# ---------------------------- Справка модули -----------------------------------------------

    def help_main_window(self):
        self.helpWindow.help_main_window()

# --------------------------- Выход из программы ------------------------------------------

    def exitofprogramm(self):
        self.close()

# ------------- Переключение в режим пользователя----------------------------------------------

    def user_Mode(self):
        self.admin_signal[bool].emit(False)

# -------------- Показать модуль просмотра и редактирования замечаний (comments_view.py) -----------------------

    def openCommentView(self):
        self.commentsView.showMaximized()
        self.commentsMain.hide()
        self.commentsView.initial()

# -------------- Закрыть модуль просмотра и редактирования замечаний (comments_view.py) ------------------------

    def closeCommentView(self):
        self.commentsMain.show()
        self.commentsView.close()

# -------------- Показать модуль ввода новых замечаний (comments_new.py) ----------------------------------------

    def openCommentsNew(self):
        self.commentsNew.show()
        self.commentsMain.hide()
        self.commentsNew.initial()

# --------------- Закрыть модуль ввода новых замечаний (comments_new.py) ----------------------------------------

    def closeCommentsNew(self):
        self.commentsMain.show()
        self.commentsNew.close()
        self.commentsMain.statistic()           # подсчитываем количество неустраненных замечаний
        self.commentsView.initial()

# ------------- Показать главное окно модуля замечаний (comments_main.py) ----------------------------------------

    def open_comments_main(self):
        self.commentsMain.statistic()
        self.commentsMain.show()
        self.hide()

# ---------------- Закрыть главное окно модуля замечаний (comments_main.py) --------------------------------------

    def close_comments_main(self):
        self.show()
        self.commentsMain.close()

# ------------- Показать окно редактора сотрудников (worker.py) --------------------------------------------

    def open_workerWindow(self):
        self.workerWindow.init_table()
        self.workerWindow.show()
        self.hide()

# ----------------- Закрыть окно редактора сотрудников (worker.py) ----------------------------------------

    def close_workerWindow(self):
        self.del_empty_string()
        self.workerWindow.close()
        self.timeTrackingWindow.compare_lists()
        self.timeTrackingWindow.init_table()
        self.planWindow.init()
        self.commentsNew.initial()
        self.commentsView.initial()
        self.show()

# ------------- Показать окно редактора станций (worker.py) ------------------------------------------------

    def open_stationWindow(self):
        self.stationWindow.show()
        self.hide()

#--------------- Закрыть окно станций (worker.py) ------------------------------------------------------------

    def close_stationWindow(self):
        self.del_empty_string()
        self.stationWindow.close()
        self.planWindow.init()
        self.commentsNew.initial()
        self.commentsView.initial()
        self.show()

# ------------- Показать окно смены пароля (passwrd.py) -------------------------------------------------

    def edit_passwordWindow(self):
        self.editPasswordWindow.ui.passw_lineEdit.setFocus()
        self.editPasswordWindow.show()

# ------------- Показать окно ввода пароля (passwrd.py) -------------------------------------------------

    def open_passwordWindow(self):
        self.passwordWindow.ui.passw_lineEdit.setFocus()
        self.passwordWindow.show()

# ------------- Показать окно созания пароля (passwrd.py) -------------------------------------------------

    def open_new_passwordWindow(self):
        self.newPasswordWindow.show()

# ------------- Показать окно учета времени сотрудников (time_tracking.py) --------------------------------

    def open_time_tracking(self):
        self.timeTrackingWindow.init_table()
        self.timeTrackingWindow.show()
        self.hide()

# ------------- Закрыть окно учета времени сотрудников (time_tracking.py) --------------------------------

    def close_time_tracking(self):
        self.timeTrackingWindow.calculation()
        self.show()
        self.timeTrackingWindow.hide()

# ------------------ Показать окно планировщика работ (plan_window.py)----------------------------------------------

    def open_planwindow(self):
        self.planWindow.show()
        self.hide()
        self.planWindow.init()

# -------------------- Закрыть окно планировщика работ (plan_window.py) ---------------------------------------------

    def close_planwindow(self):
        self.show()
        self.planWindow.hide()


# ----------- Удаление пустых строк в таблице сотрудников и станций при закрытии окон редакторов --------------

    def del_empty_string(self):

        self.msg = QMessageBox()
        self.msg.setWindowTitle('Внимание!')
        self.msg.setText('При закрытии редактора будут удалены \n все строки с пустыми ячейками...')
        self.msg.exec()
        self.query.exec('''SELECT * FROM workers''')
        while self.query.next():
            self.name = self.query.value("Name")
            self.post = self.query.value("Post")
            self.number = self.query.value("Number")
            if len(self.name) == 0 or self.name.isspace() or \
                    len(self.post) == 0 or self.post.isspace() \
                    or len(self.number) == 0 or self.number.isspace():
                self.query.exec("DELETE FROM workers WHERE Name='"+self.name+"' or Post='"+self.post+"'or "
                                                           "Number='"+self.number+"'")

                self.workerWindow.model.select()
        self.query.exec('''SELECT * FROM station''')
        while self.query.next():
            self.name = self.query.value("Name")
            if len(self.name) == 0 or self.name.isspace():
                self.query.exec("DELETE FROM station WHERE Name='" + self.name + "'")
                self.stationWindow.model.select()


#------------------------ Инициализация базы данных ------------------------------------------

    def db_init(self):
        self.model.setQuery('''CREATE TABLE workers(IthemID INTEGER PRIMARY KEY NOT NULL,
                                                    Name     TEXT,
                                                    Post     TEXT,
                                                    Number   TEXT)''')
        self.model.setQuery('''CREATE TABLE station(ItemID INTEGER PRIMARY KEY NOT NULL,
                                                    NAME    TEXT)''')
        self.model.setQuery('''CREATE TABLE password_table(IthemID INTEGER PRIMARY KEY NOT NULL,
                                                           Password  TEXT)''')
        self.model.setQuery('''CREATE TABLE plan_table (IthemID INTEGER PRIMARY KEY NOT NULL,
                                                           DataHide TEXT,    Data     TEXT,
                                                           Name     TEXT,    Station  TEXT,
                                                           Plan    TEXT)''')
        self.model.setQuery('''CREATE TABLE time_tracking(IthemID INTEGER PRIMARY KEY NOT NULL,
                                                           Name     TEXT,    Norm    REAL,
                                                           Fakt     REAL,    Otgul   REAL,      Korr    REAL,
                                                           d01      REAL,    d02     REAL,
                                                           d03      REAL,    d04     REAL,
                                                           d05      REAL,    d06     REAL,
                                                           d07      REAL,    d08     REAL,
                                                           d09      REAL,    d10     REAL,
                                                           d11      REAL,    d12     REAL,
                                                           d13      REAL,    d14     REAL,
                                                           d15      REAL,    d16     REAL,
                                                           d17      REAL,    d18     REAL,
                                                           d19      REAL,    d20     REAL,
                                                           d21      REAL,    d22     REAL,
                                                           d23      REAL,    d24     REAL,
                                                           d25      REAL,    d26     REAL,
                                                           d27      REAL,    d28     REAL,
                                                           d29      REAL,    d30     REAL,
                                                           d31      REAL,    month   INTEGER,
                                                           year     INTEGER, summa   REAL)''')
        self.model.setQuery('''CREATE TABLE otgul_table(IthemID INTEGER PRIMARY KEY NOT NULL,
                                                           name    TEXT,    hour    REAL)''')
        self.model.setQuery('''CREATE TABLE comments_table(IthemID INTEGER PRIMARY KEY NOT NULL,
                                                            number      TEXT,    data        TEXT,
                                                            kommis      TEXT,    station     TEXT,    
                                                            auditor     TEXT,    comment     TEXT,    
                                                            term_data   TEXT,    worker      TEXT,    
                                                            performance TEXT,    old_data    TEXT,    
                                                            what_is     TEXT,    foto        TEXT,
                                                            foto_but    TEXT,    foto_data   BLOB)''')

        self.query.exec('SELECT Password FROM password_table')
        count = 0
        while self.query.next():
            self.passw = self.query.value("Password")
            count=count+1
            if len(self.passw)==0 or self.passw.isspace() or count==0:
                self.open_new_passwordWindow()
        if count==0:
            self.open_new_passwordWindow()

#------------------------- Получаем сигнал со значением режима программы (админ или юзер) ---------------------------

    def sig_admin(self, b):
        self.FLAG_ADMIN = b
        self.programm_Mode()


#------------------------ Настройка активных пунктов меню в зависимости от режима программы ------------------------

    def programm_Mode(self):
        if self.FLAG_ADMIN:
            self.action_user.setDisabled(False)
            self.action_admin.setDisabled(True)
            self.action_worker.setDisabled(False)
            self.action_station.setDisabled(False)
            self.action__new_password.setDisabled(False)
            self.setWindowTitle("Моя бригада (режим администратора)")
            self.statusbar.showMessage("Режим администратора")
        else:
            self.action_user.setDisabled(True)
            self.action_admin.setDisabled(False)
            self.action_worker.setDisabled(True)
            self.action_station.setDisabled(True)
            self.action__new_password.setDisabled(True)
            self.statusbar.showMessage("Режим пользователя")
            self.setWindowTitle("Моя бригада")


#------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    db = QSqlDatabase.addDatabase("QSQLITE")  # Открываем базу данных
    db.setDatabaseName("database.db")
    if not db.isOpen():
        db.open()
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    sys.exit(app.exec())


