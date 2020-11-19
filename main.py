import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QStyleFactory
from PySide2.QtCore import QFile

# import mainwindow.py as module and it's main class
from mainwindow import Ui_MainWindow



# in PyCharm:
# in Run Configuration, Run Before Launch, add External Tool
# Command: pyside2-uic
# Arguments: mainwindow.ui -o mainwindow.py
# Folder: $ProjectFileDir$




class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # print available styles
        print(QStyleFactory.keys())


        # Signals
        self.ui.my_button.clicked.connect(self.test)



    def test(self):
        print("test!")



if __name__ == "__main__":
    app = QApplication(sys.argv)

    style = QStyleFactory.create('Fusion')
    app.setStyle(style)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
