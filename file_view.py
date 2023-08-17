""" -------- Окно модуля просмотра фотографий ---------------"""

import sys
from PySide6.QtWidgets import (QApplication, QWidget, QFileDialog, QMessageBox)
from PySide6.QtCore import (Qt, QByteArray)
from PySide6.QtSql import (QSqlQuery)
from PySide6.QtGui import (QPixmap)
import ui_file_view

class File_View(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = ui_file_view.Ui_File_View()
        self.ui.setupUi(self)
        self.query = QSqlQuery()

# ----------------------------------- Загружаем фото в базу данных ---------------------------------------------

    def load_file_to_db(self, row):
        arr = QFileDialog().getOpenFileName(self, caption="Загрузить фото", filter="Фото (*.jpg)")
        if len(arr) != 0 or arr.isspace():
            fob = open(arr[0], 'rb')
            blob_d = fob.read()
            blob_d = QByteArray(blob_d)
            self.query.prepare('''UPDATE comments_table SET foto=:foto, foto_data=:foto_data 
                                          WHERE IthemID=''' + str(row))
            self.query.bindValue(":foto", "да")
            self.query.bindValue(":foto_data", blob_d)
            self.query.exec_()
        else:
            return

# ------------------------------------ Просмотр фото из базы данных ---------------------------------------------

    def open_file_from_db(self, row):
        self.query.exec("SELECT foto_data  FROM comments_table WHERE IthemID = " + str(row))
        while self.query.next():
            foo = self.query.value("foto_data")
        pix = QPixmap()
        pix.loadFromData(foo)
        self.ui.label_foto.setPixmap(pix)
        self.ui.label_foto.setPixmap(pix.scaled(800, 600, Qt.KeepAspectRatio))
        self.show()

# ------------------------------------ Удаление фотографии из базы ----------------------------------------------

    def del_file_from_db(self, row):
        dlg = QMessageBox(self)
        dlg.setWindowTitle("Внимание !!!")
        dlg.setText("Удалить фото из базы данных?")
        dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        dlg.setIcon(QMessageBox.Question)
        button = dlg.exec()

        if button == QMessageBox.Yes:
            self.query.prepare('''UPDATE comments_table SET foto=:foto, foto_data=:foto_data
                                                  WHERE IthemID=''' + str(row))
            self.query.bindValue(":foto", "нет")
            self.query.bindValue(":foto_data", "")
            self.query.exec_()

# ------------------------------------ Сохранить фото -----------------------------------------------------------

    def save_file(self, row):
        dlg = QMessageBox(self)
        dlg.setWindowTitle("Внимание !!!")
        dlg.setText("Сохранить фото в базу данных?")
        dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        dlg.setIcon(QMessageBox.Question)
        button = dlg.exec()
        if button == QMessageBox.Yes:
            self.query.exec("SELECT foto_data  FROM comments_table WHERE IthemID = " + str(row))
            while self.query.next():
                foo = self.query.value("foto_data")
            with open('filename.jpg', 'wb') as f:
                f.write(bytes(foo))


# ------------------------------------ Закрыть окно просмотра ---------------------------------------------------

    def close_file_view(self):
        self.close()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    mywindow = File_View()
    mywindow.show()
    sys.exit(app.exec())
