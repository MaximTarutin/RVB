""" Редактор планировщика """
import sys
from PySide6.QtWidgets import (QMainWindow, QApplication)
import ui_planeditor


class PlanEditor(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = ui_planeditor.Ui_planEditor()
        self.ui.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mywindow = PlanEditor()
    mywindow.show()
    sys.exit(app.exec())
