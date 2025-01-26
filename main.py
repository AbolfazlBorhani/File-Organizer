from PyQt6.QtWidgets import QMainWindow, QApplication
import sys
import os

includePath = os.path.abspath(os.getcwd() + '/lib')
sys.path.append(includePath)

from fileorganizer import FileOrganizer

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FileOrganizer()
    window.show()
    app.exec()
