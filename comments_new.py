"""---------- Модуль ввода новых замечаний -----------------"""

import sys
from PySide6.QtCore import (Qt, QDate)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMessageBox)
from PySide6.QtSql import (QSqlQuery)
import ui_commentsnew

class New_Comments_Window(QMainWindow):
    def __init__(self, parent = None):
        self.FLAG_ADMIN = False
        self.FLAG_CHECK = False
        super().__init__(parent)
        self.ui = ui_commentsnew.Ui_CommentsNew()
        self.ui.setupUi(self)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowCloseButtonHint)  # деактивируем кнопку закрыть окно

        self.query = QSqlQuery()
        self.initial()

        self.ui.Add_pushButton.clicked.connect(self.add_to_db)

# ------------------- Инициализация ---------------------------------------

    def initial(self):
        self.ui.date_dateEdit.setDate(QDate.currentDate())  # устанавливаем в dateEdit текущую дату
        self.ui.term_dateEdit.setDate(QDate.currentDate())

        self.query.exec("SELECT Name FROM workers")         # Заполняем бокс исполнитель
        list_workers = []
        while self.query.next():
            name = self.query.value("Name")
            list_workers.append(name)
        self.ui.Executor_Box.clear()
        self.ui.Executor_Box.addItem("")
        for i in list_workers:
            self.ui.Executor_Box.addItem(i)
        del list_workers

        self.query.exec("SELECT Name FROM station")         # Заполняем бокс станции и перегоны
        list_stations = []
        while self.query.next():
            name = self.query.value("Name")
            list_stations.append(name)
        self.ui.Stations_Box.clear()
        self.ui.Stations_Box.addItem("")
        for i in list_stations:
            self.ui.Stations_Box.addItem(i)
        del list_stations

        self.programm_Mode()

# ------------------------- Получаем сигнал со значением режима программы (админ или юзер) ---------------------------

    def sig_admin(self, b):
        self.FLAG_ADMIN = b
        self.programm_Mode()

# -------------------------------- Режим программы (admin or user) -------------------------------------------!!!!!!!

    def programm_Mode(self):
        if self.FLAG_ADMIN:
            self.ui.action_user.setEnabled(True)
            self.ui.action_admin.setEnabled(False)
            self.ui.action_stations.setEnabled(True)
            self.ui.action_workers.setEnabled(True)
            self.ui.action_password.setEnabled(True)
            self.ui.Add_pushButton.setEnabled(True)
            self.ui.date_dateEdit.setEnabled(True)
            self.ui.act_lineEdit.setEnabled(True)
            self.ui.auditor_lineedit.setEnabled(True)
            self.ui.Executor_Box.setEnabled(True)
            self.ui.Komiss_Box.setEnabled(True)
            self.ui.term_dateEdit.setEnabled(True)
            self.ui.text_textEdit.setEnabled(True)
        else:
            self.ui.action_user.setEnabled(False)
            self.ui.action_admin.setEnabled(True)
            self.ui.action_stations.setEnabled(False)
            self.ui.action_workers.setEnabled(False)
            self.ui.action_password.setEnabled(False)
            self.ui.Add_pushButton.setEnabled(False)
            self.ui.date_dateEdit.setEnabled(False)
            self.ui.act_lineEdit.setEnabled(False)
            self.ui.auditor_lineedit.setEnabled(False)
            self.ui.Executor_Box.setEnabled(False)
            self.ui.Komiss_Box.setEnabled(False)
            self.ui.term_dateEdit.setEnabled(False)
            self.ui.text_textEdit.setEnabled(False)

#----------------- Добавляем замечание в базу данных --------------------

    def add_to_db(self):
        self.check_comment()
        if self.FLAG_CHECK:
            number = self.ui.act_lineEdit.text()
            station = self.ui.Stations_Box.currentText()
            kommis = self.ui.Komiss_Box.currentText()
            auditor = self.ui.auditor_lineedit.text()
            comments = self.ui.text_textEdit.toPlainText()
            termdata = self.ui.term_dateEdit.text()
            worker = self.ui.Executor_Box.currentText()
            data = self.ui.date_dateEdit.text()
            performance = "Не выполнено"
            what_is = ""
            foto = "нет"
            olddata = ""
            fotodata = ""
            fotobut=" "
            self.query.exec('''INSERT INTO comments_table (number, data, kommis, station, auditor, comment,
                                                           term_data, worker, performance, old_data, what_is, 
                                                           foto, foto_but, foto_data)
                                VALUES ("'''+number+'''","'''+data+'''","'''+kommis+'''","'''+station+'''",
                                        "'''+auditor+'''","'''+comments+'''","'''+termdata+'''","'''+worker+'''",
                                        "'''+performance+'''","'''+olddata+'''","'''+what_is+'''","'''+foto+'''",
                                        "'''+fotobut+'''","'''+fotodata+'''")''')
            self.ui.act_lineEdit.clear()
            self.ui.Stations_Box.setCurrentIndex(0)
            self.ui.Komiss_Box.setCurrentIndex(0)
            self.ui.auditor_lineedit.clear()
            self.ui.text_textEdit.clear()
            self.ui.Executor_Box.setCurrentIndex(0)
            self.ui.auditor_lineedit.clear()
            self.FLAG_CHECK = False
            self.error_window("Данные успешно внесены в базу !!!")


#----------------- Проверяем все ли поля заполнены ----------------------

    def check_comment(self):
        if len(self.ui.act_lineEdit.text()) < 1:
            self.error_window("Не указан номер замечания по акту !!!")
            return
        if self.ui.Komiss_Box.currentIndex() == 0:
            self.error_window("Не выбрана коммиссия !!!")
            return
        if len(self.ui.auditor_lineedit.text()) < 1:
            self.error_window("Не заполнено поле 'Проверяющий !!!'")
            return
        if self.ui.Stations_Box.currentIndex() == 0:
            self.error_window("Не выбрана станция !!!")
            return
        if self.ui.Executor_Box.currentIndex() == 0:
            self.error_window("Не выбран исполнитель !!!")
            return
        if self.ui.date_dateEdit.date() > self.ui.term_dateEdit.date():
            self.error_window("Срок исполнения меньше даты проверки !!!")
            return
        if len(self.ui.text_textEdit.toPlainText()) < 1 or \
               self.ui.text_textEdit.toPlainText().isspace():
            self.error_window("Не внесён текст замечания !!!")
            return
        self.FLAG_CHECK = True
        return

#------------------ Вывод сообщения об ошибке ---------------------------

    def error_window(self, text):
        self.msg = QMessageBox()
        self.msg.setWindowTitle('Внимание!')
        self.msg.setText(text)
        self.msg.exec()

#----------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainwindow = New_Comments_Window()
    mainwindow.show()
    sys.exit(app.exec())