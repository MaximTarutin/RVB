import sys
from PySide6.QtWidgets import (QApplication, QMessageBox, QTextBrowser, QWidget, QPushButton)
from PySide6.QtCore import (Qt, QSize)

class HelpWindow(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setWindowModality(Qt.ApplicationModal)
        self.textBrowser = QTextBrowser(self)
        self.button_ok = QPushButton(self)
        self.button_ok.clicked.connect(self.__close_help)

# ----------------------------------- Инициализация ------------------------------------------

    def __init(self,w,h):
        self.show()
        self.resize(w, h)
        self.setMaximumSize(QSize(w, h))
        self.setMinimumSize(QSize(w, h))
        self.textBrowser.resize(w, h-40)
        self.button_ok.resize(80, 30)
        self.button_ok.setText("ОК")
        x1 = w/2-40
        y1 = h-35
        self.button_ok.move(x1, y1)
        self.textBrowser.show()
        self.button_ok.show()

# ----------------------------------- О программе --------------------------------------------

    def about(self):
        self.__init(600,600)
        self.setWindowTitle("О программе")
        self.textBrowser.append('''<center><b><font color="blue" size="7">Программа РВБ</font></b></center></div>
                                   <font color="green" size="5"><div><br>Версия программы: 1.2
                                   <br>Язык разработки: Python 3.11<br>Фреймворк: Qt 6.4.3<br>Библиотека: PySide6
                                   <br><br></font><font color="black" size="5">Программа представляет собой рабочее
                                   место старшего электромеханика Регионального центра связи РЖД. Состоит из трёх 
                                   модулей:<br>1) Учет рабочего времени<br>2) Устранение замечаний<br>3) Планирование 
                                   работ</font><br><br><font size="5" color="red">Программирование: старший 
                                   элетромеханик Сосногорского регионального центра связи Ярославской дирекции связи - 
                                   Тарутин Максим Александрович</font><br><br><br><font size="5" color="blue">
                                   <center><b>Воркута 2023 год</b></center></font>''')

# ------------------------------- справко о главном модуле ------------------------------------------

    def help_main_window(self):
        self.__init(600,400)
        self.setWindowTitle("Главный модуль")
        self.textBrowser.append('''<font color="black" size="4">1.   Для начала работы с 
        программой необходимо придумать пароль администратора, который необходимо запомнить. В случае утери пароля 
        восстановить можно только направив файл database.db на электронный адрес mtarut@mail.ru для разблокировки.
        Позднее изменить пароль возможно в меню "Редакторы -> Изменить пароль администратора".
        <br><br>2. При первом запуске необходимо заполнить базу данных сотрудниками бригады, а также заполнить станции и
        перегоны на которых будут планироваться и производится работы. Для этого необходимо войти в режим 
        администратора: "Сервис -> Режим администратора". Ввести пароль. Затем зайти в меню "Редакторы -> Сотрудники"
        или "Редакторы -> Станции и перегоны" соответственно, для заполнения данных
        <br><br>3. Программа состоит из трех модулей : "Учет рабочего времени", "Устранение замечаний" и "Планирование 
        работ" доступ к которым осуществляется нажатием соответствующей кнопки на главном экране, либо через меню 
        "Сервис" и выбора соответствующего подменю</font>''')

# ---------------------------------- Справка модуля учет рабочего времени ---------------------------------

    def help_timetracking(self):
        self.__init(600,600)
        self.setWindowTitle("Модуль учета рабочего времени")

# --------------------------------- Закрыть модуль --------------------------------------------------------

    def __close_help(self):
        self.textBrowser.clear()
        self.close()

if __name__=="__main__":
    app = QApplication(sys.argv)
    mywindow = HelpWindow()
    mywindow.show()
    sys.exit(app.exec()) 
