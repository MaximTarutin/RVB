"""  ------ Делегаты для QTableView ------
"""

from PySide6.QtWidgets import (QStyledItemDelegate, QComboBox, QLineEdit, QDateEdit, QPushButton,
                               QStyle, QStyleOptionButton, QApplication)
from PySide6.QtCore import (Qt, QRegularExpression, QDate, Signal)
from PySide6.QtGui import (QColor, QRegularExpressionValidator)
from PySide6.QtSql import (QSqlQuery)

# --------------------- Цвет ячейки наличия фото ---------------------------------------------

class Foto_Color_Delegate(QStyledItemDelegate):
    def __init__(self, parent):
        QStyledItemDelegate.__init__(self, parent)

    def createEditor(self, parent, option, index):
        return

    def initStyleOption(self, option, index):
        super().initStyleOption(option, index)
        text = option.text
        option.displayAlignment = Qt.AlignCenter
        color = "#e6e6e6"
        if text=='нет':
            color = "pink"
        if text=='да':
            color = "lightgreen"
        option.backgroundBrush = QColor(color)

#------------- Делегат со списком работников ---------------------------------------------

class Worker_Name_delegate(QStyledItemDelegate):
    def __init__(self, parent):
        QStyledItemDelegate.__init__(self, parent)
        self.query = QSqlQuery()

    def createEditor(self, parent, options, index):
        editor = QComboBox(parent)
        editor.addItem("")
        self.query.exec("SELECT Name FROM workers")  # Заполняем комбобоксы из базы данных
        list_worker = []
        while self.query.next():
            name = self.query.value("Name")
            list_worker.append(name)
        editor.clear()
        editor.addItem("")
        for i in list_worker:
            editor.addItem(i)
        del list_worker
        return editor

#------------- Делегат выбора даты --------------------------------------------------------

class Date_delegate(QStyledItemDelegate):
    def __init__(self, parent):
        QStyledItemDelegate.__init__(self, parent)

    def createEditor(self, parent, options, index):
        editor = QDateEdit(parent)
        editor.setCalendarPopup(True)
        d = QDate.currentDate()
        editor.setDate(d)
        return editor


#------------- Делегат для таблицы в виде выпадающего списка-------------------------------

class Worker_delegate(QStyledItemDelegate):
    def __init__(self, parent):
        QStyledItemDelegate.__init__(self, parent)

    def createEditor(self, parent, options, index):
        editor = QComboBox(parent)
        editor.addItem('Старший электромеханик')
        editor.addItem('Электромеханик')
        editor.addItem('Электромонтер')
        editor.addItem('Начальник участка')
        editor.addItem('Заместитель начальника')
        editor.addItem('Главный инженер')
        editor.addItem('Начальник центра')
        return editor

#------------ Делегат запрещает редактирование ячеек -------------------------------------

class NoEditorDelegate(QStyledItemDelegate):
    def __init__(self, parent):
        QStyledItemDelegate.__init__(self, parent)

    def createEditor(self, parent, option, index):
        return

#----------  Делегат устанавливает текст в ячейке по центру -----------------------------

class AlignDelegate(QStyledItemDelegate):
    def __init__(self, parent):
        QStyledItemDelegate.__init__(self, parent)

    def initStyleOption(self, option, index):
        super(AlignDelegate, self).initStyleOption(option, index)
        option.displayAlignment = Qt.AlignCenter

#--- Валидатор, только числа и определенные символы, один или 2 знака, закрашивает по условию -----------

class NumericDelegate(QStyledItemDelegate):
    def __init__(self, parent):
        QStyledItemDelegate.__init__(self, parent)

    def initStyleOption(self, option, index):
        super().initStyleOption(option, index)
        text = option.text
        option.displayAlignment = Qt.AlignCenter
        color = "#e6e6e6"
        match text:
            case 'о' | 'О':
                color = "yellow"        # Отпуск
            case 'у' | 'У':
                color = "cyan"          # Учеба
            case 'н' | 'Н':
                color = "magenta"       # За свой счет
            case 'б' | 'Б':
                color = "pink"          # Больничный
            case 'в' | 'В':
                color = "lightgreen"    # Выходной
            case 'к' | 'К':
                color = "lightblue"     # Командировка
            case 'п' | 'П':
                color = "red"           # Прогул
            case 'Не выполнено':
                color = "red"
        option.backgroundBrush = QColor(color)

    def createEditor(self, parent, option, index):
        editor = QLineEdit(parent)
        option.displayAlignment = Qt.AlignCenter
        editor.setValidator(QRegularExpressionValidator(QRegularExpression \
                           ("[0-9,о,О,у,У,н,Н,б,Б,в,В,к,К,п,П]{0,1}[0-9.]{0,2}")))
        return editor

#--- Валидатор, только числа и определенные символы, один или 3 знака -----------

class NumericDelegate_1(QStyledItemDelegate):
    def __init__(self, parent):
        QStyledItemDelegate.__init__(self, parent)

    def initStyleOption(self, option, index):
        super().initStyleOption(option, index)
        #text = option.text
        option.displayAlignment = Qt.AlignCenter

    def createEditor(self, parent, option, index):
        editor = QLineEdit(parent)
        option.displayAlignment = Qt.AlignCenter
        editor.setValidator(QRegularExpressionValidator(QRegularExpression \
                           ("^-?[0-9]{0,3}[0-9.]{0,2}$")))
        return editor

#------------------------------------------ Цвет устранения замечаний ------------------------------------------------

class ColorDelegate(QStyledItemDelegate):
    def __init__(self, parent):
        QStyledItemDelegate.__init__(self, parent)

    def initStyleOption(self, option, index):
        super().initStyleOption(option, index)
        text = option.text
        option.displayAlignment = Qt.AlignCenter
        color = "#e6e6e6"
        match text:
            case 'Просрочено':
                color = "red"
            case 'Выполнено':
                color = "lightgreen"
            case 'Подходит срок':
                color = "yellow"
            case 'Выполнить сегодня':
                color = "pink"
            case 'Не выполнено':
                color = 0xe3ebf8
        option.backgroundBrush = QColor(color)

    def createEditor(self, parent, option, index):
        return
