"""
         Модуль работы с вводом и заменой паролей,
         а также валидности введенного пароля
"""

import sys
from PySide6.QtCore import (Qt, Signal)
from PySide6.QtWidgets import (QApplication, QMainWindow, QLineEdit, QMessageBox)
from PySide6.QtSql import (QSqlQuery)
from copy import copy
import ui_passwordform
import hashlib

class PasswordWindow(QMainWindow):
    admin_signal = Signal(bool)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.FLAG_PASSWORD = False
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.ui = ui_passwordform.Ui_Form()
        self.ui.setupUi(self)
        self.ui.passw_lineEdit.setEchoMode(QLineEdit.Password)
        self.ui.new_passw_lineEdit.setEchoMode(QLineEdit.Password)                      # Заменяем текст точками
        self.ui.new_passw_lineEdit_1.setEchoMode(QLineEdit.Password)

        self.ui.passw_lineEdit.setFocus()

        self.ui.button_Cancel.clicked.connect(self.__return_of_password)                # Кнопка отмена
        self.ui.button_Ok.clicked.connect(self.__check_password)                        # Кнопка Ok


#----------------------------- закрыть окно паролей ------------------------------------

    def __return_of_password(self):
        self.ui.passw_lineEdit.clear()
        self.ui.new_passw_lineEdit_1.clear()
        self.ui.new_passw_lineEdit.clear()
        self.close()

#------------- Проверка правильности ввода пароля и его сохранение --------------------

    def __check_password(self):
        self.query = QSqlQuery()
        self.query.exec("SELECT Password FROM password_table")

#                      ОКНО ВВОДА ПАРОЛЯ

        if self.ui.passw_lineEdit.isEnabled() and \
            self.ui.new_passw_lineEdit.isHidden() and \
            self.ui.new_passw_lineEdit_1.isHidden():
            self.query.next()
            password_db = self.query.value("Password")
            password_this = self.ui.passw_lineEdit.text()

            hash_object = hashlib.md5(password_this.encode())
            password_this = hash_object.hexdigest()
            if password_this != password_db:
                self.ui.passw_lineEdit.clear()
                self.__window_error('Введен неверный пароль !!!')
                return
            else:
                self.admin_signal[bool].emit(True)          # Посылаем сигнал admin True.
                self.ui.passw_lineEdit.clear()
                self.close()
            return

#                       ОКНО СОЗДАНИЯ ПАРОЛЯ

        if self.ui.passw_lineEdit.isHidden() and \
            self.ui.new_passw_lineEdit.isEnabled() and \
            self.ui.new_passw_lineEdit_1.isEnabled():
            self.__Password_valide('create_password')
            if self.FLAG_PASSWORD:
                passw_1 = self.ui.new_passw_lineEdit.text()
                hash_object = hashlib.md5(passw_1.encode())
                passw_1 = hash_object.hexdigest()
                self.query.exec('INSERT INTO password_table (Password) VALUES ("'+passw_1+'")')
                self.ui.new_passw_lineEdit_1.clear()
                self.ui.new_passw_lineEdit.clear()
                self.FLAG_PASSWORD = False
                self.close()
                return
            return

#                       ОКНО СМЕНЫ ПАРОЛЯ

        if self.ui.passw_lineEdit.isEnabled() and \
            self.ui.new_passw_lineEdit.isEnabled() and \
            self.ui.new_passw_lineEdit_1.isEnabled():
            passw_1 = self.ui.new_passw_lineEdit.text()
            self.__Password_valide('edit_password')
            if self.FLAG_PASSWORD:
                hash_object = hashlib.md5(passw_1.encode())
                passw_1 = hash_object.hexdigest()
                self.query.exec('UPDATE password_table SET Password ="'+passw_1+'" WHERE ItemID = 1')
                self.ui.new_passw_lineEdit_1.clear()
                self.ui.new_passw_lineEdit.clear()
                self.ui.passw_lineEdit.clear()
                self.FLAG_PASSWORD = False
                self.close()
                return
            return


#------------------------ Проверка валидности пароля -----------------------------------

    def __Password_valide(self, name_define):
        passw_old = self.ui.passw_lineEdit.text()
        passw_1 = self.ui.new_passw_lineEdit.text()
        passw_2 = self.ui.new_passw_lineEdit_1.text()

        if name_define == 'create_password':                            # валидность для формы создания пароля
            if passw_1 != passw_2:
                self.__window_error('Введенные пароли не совпадают !!!')
                self.FLAG_PASSWORD = False
                return
            elif len(passw_1)<8 or len(passw_2)<8:
                self.__window_error('Пароль должен состоять не менее чем \n из 8 символов')
                self.FLAG_PASSWORD = False
                return

            self.FLAG_PASSWORD = True
            return

        if name_define == 'edit_password':                              # валидность для формы смены пароля
            hash_object = hashlib.md5(passw_old.encode())
            passw_old_1=copy(passw_old)
            passw_old = hash_object.hexdigest()
            self.query.next()
            passw_old_bd = self.query.value("Password")
            if passw_old != passw_old_bd:
                self.__window_error('Введен неверный пароль администратора')
                self.ui.passw_lineEdit.clear()
                self.ui.new_passw_lineEdit_1.clear()
                self.ui.new_passw_lineEdit.clear()
                return
            elif passw_old_1 == passw_1:
                self.__window_error('Пароль не изменился, придумайте новый пароль !!!')
                self.FLAG_PASSWORD = False
                return
            elif passw_1 != passw_2:
                self.__window_error('Введенные пароли не совпадают !!!')
                self.FLAG_PASSWORD = False
                self.ui.passw_lineEdit.clear()
                self.ui.new_passw_lineEdit_1.clear()
                self.ui.new_passw_lineEdit.clear()
                return
            elif len(passw_1)<8 or len(passw_2)<8:
                self.__window_error('Пароль должен состоять не менее чем \n из 8 символов')
                self.FLAG_PASSWORD = False
                self.ui.passw_lineEdit.clear()
                self.ui.new_passw_lineEdit_1.clear()
                self.ui.new_passw_lineEdit.clear()
                return
            self.FLAG_PASSWORD = True
            return



#---------------------------- Сообщение об ошибке ---------------------------------------

    def __window_error(self, text):
        self.msg = QMessageBox()
        self.msg.setWindowTitle('Внимание!')
        self.msg.setText(text)
        self.msg.exec()
        self.ui.passw_lineEdit.clear()
        self.ui.new_passw_lineEdit.clear()
        self.ui.new_passw_lineEdit_1.clear()
        self.ui.passw_lineEdit.setFocus()
        return

#----------------- Обработка нажатия клавиши ENTER --------------------------------

    def keyPressEvent(self, e):
        if e.key() in [Qt.Key_Enter, Qt.Key_Return]:
            self.__check_password()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mywindow = PasswordWindow()
    sys.exit(app.exec())
