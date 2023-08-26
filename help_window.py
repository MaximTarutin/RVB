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

    def __init(self):
        self.show()
        self.resize(600, 600)
        self.setMaximumSize(QSize(600, 600))
        self.textBrowser.resize(600, 560)
        self.button_ok.resize(80, 30)
        self.button_ok.setText("ОК")
        x1 = self.width() / 2 - self.button_ok.width() / 2
        y1 = self.height() - self.button_ok.height() - 5
        self.button_ok.move(x1, y1)
        self.textBrowser.show()
        self.button_ok.show()

# ----------------------------------- О программе --------------------------------------------

    def about(self):
        self.__init()
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
        self.__init()
        self.setWindowTitle("Главный модуль")


    def __close_help(self):
        self.textBrowser.clear()
        self.close()

if __name__=="__main__":
    app = QApplication(sys.argv)
    mywindow = HelpWindow()
    mywindow.show()
    sys.exit(app.exec()) 
