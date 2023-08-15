""" -------- Главное окно модуля работы с замечаниями ---------------"""

import sys
from PySide6.QtWidgets import (QApplication, QWidget)
from PySide6.QtCore import (Qt)
from PySide6.QtSql import (QSqlQuery)
import ui_commentswindow

class Comments_main(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = ui_commentswindow.Ui_commentsWindow()
        self.ui.setupUi(self)
        self.query = QSqlQuery()
        self.statistic()
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowCloseButtonHint)  # деактивируем кнопку закрыть окно

# ---------------------- Выводим статистику по количеству неустраненных замечаний -------------------------------------

    def statistic(self):
        count = 0               # Общее количество неустраненных замечаний
        head_railway = 0        # неустраненные замечания начальника дороги
        deputy_head = 0         # неустраненные замечания заместителя начальника дороги
        auditors = 0            # неустраненные замечания ревизорского аппарата
        safetyday = 0           # неустраненные замечания в дни безопасности
        inspektor = 0           # неустраненные замечания общественных инспекторов
        ksot = 0                # неустраненные замечания охраны труда
        foreman = 0             # неустраненные замечания старшего электромеханика
        other = 0               # прочие неустраненные замечания

        self.query.exec('''SELECT kommis, performance FROM comments_table WHERE performance = "Не выполнено" OR
                           performance = "Подходит срок" OR performance = "Просрочено" OR 
                           performance = "Выполнить сегодня"''')
        self.query.first()
        while self.query.next():
            commission = self.query.value("kommis")
            count+=1
            if commission == "Начальник дороги": head_railway+=1
            if commission == "Зам. по региону": deputy_head+=1
            if commission == "Ревизорский аппарат": auditors+=1
            if commission == "Дни безопасности": safetyday+=1
            if commission == "Общественный инспектор": inspektor+=1
            if commission == "Охрана труда": ksot+=1
            if commission == "Старший электромеханик": foreman+=1
            if commission == "Другое": other+=1
        self.ui.boss_label.setText(str(head_railway))
        self.ui.deputy_label.setText(str(deputy_head))
        self.ui.auditor_label.setText(str(auditors))
        self.ui.safetyday_label.setText(str(safetyday))
        self.ui.inspektor_label_2.setText(str(inspektor))
        self.ui.ksot_label.setText(str(ksot))
        self.ui.foreman_label.setText(str(foreman))
        self.ui.other_2.setText(str(other))
        self.ui.total_label.setText(str(count))

# ---------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = Comments_main()
    mywindow.show()
    sys.exit(app.exec())