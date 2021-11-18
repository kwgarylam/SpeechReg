from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import QTimer
from GUI import Ui_MainWindow
import sys
import threading
import time

counter = 0

def myjob():
    while True:
        global counter
        counter += 1
        print(counter)
        time.sleep(1)

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):

        global counter

        super(MainWindow, self).__init__()
        self.timer_i = 0
        self.counter = 0
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.label.setText('Hello World!')

        # Timer
        self.qTimer = QTimer()
        self.qTimer.setInterval(1000)  # set interval to 1 s; 1000 ms = 1 s
        self.qTimer.timeout.connect(self.updateMessages) # connect timeout signal to signal handler
        self.qTimer.start() # start timer

        # Button
        self.ui.pushButton.clicked.connect(self.PreButtonClicked)
        self.ui.pushButton_2.clicked.connect(self.NextButtonClicked)

    def updateMessages(self):
        self.ui.label.setText('%d. Value in the thread' % counter)

    def PreButtonClicked(self):
        if self.counter == 1:
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_0)
            self.counter = 0
        elif self.counter == 2:
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_1)
            self.counter = 1
        elif self.counter == 3:
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_2)
            self.counter = 2

    def NextButtonClicked(self):
        if self.counter == 0:
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_1)
            self.counter = 1
        elif self.counter == 1:
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_2)
            self.counter = 2
        elif self.counter == 2:
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_3)
            self.counter = 3


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()

    # Thread
    t = threading.Thread(target=myjob)
    t.start()

    sys.exit(app.exec_())
    print("Program terminated ...")
    exit()
