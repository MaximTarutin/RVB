""" -------- Главное окно модуля работы с замечаниями ---------------"""

import sys
from PySide6.QtWidgets import (QApplication, QWidget)
from PySide6.QtCore import (Qt)
import ui_commentswindow


class Comments_main(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = ui_commentswindow.Ui_commentsWindow()
        self.ui.setupUi(self)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowCloseButtonHint)  # деактивируем кнопку закрыть окно

        self.ui.return_button.clicked.connect(self.return_to_main)

#---------------- Закрыть модуль замечаний -------------------------

    def return_to_main(self):
        self.close()

#---------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = Comments_main()
    mywindow.show()
    sys.exit(app.exec())