from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys


class Ui(QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('ui/window.ui', self)

        self.open_btn = self.findChild(QPushButton, 'open_btn')
        self.open_btn.clicked.connect(self.openFile)

        self.file_path = self.findChild(QLabel, 'file_path')
        self.file_path.setText("No file selected")

        self.show()

    def openFile(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\desktop',"xml file (*.fcpxml)")
        #print(fname)
        self.file_path.setText(fname[0])






app = QApplication(sys.argv)
window = Ui()
app.exec_()