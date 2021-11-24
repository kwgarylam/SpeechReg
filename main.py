from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import QTimer
from GUI import Ui_MainWindow
import sys
import threading
import time
from collections import deque
import speech

# Create a list of 3 empty strings
words = deque(["", "", ""])
dataStream = ""


def myjob():
    while True:
        global dataStream

        dataStream = speech.main()


class MainWindow(QtWidgets.QMainWindow):
    global dataStream

    def __init__(self):

        super(MainWindow, self).__init__()
        self.timer_i = 0
        self.counter = 0
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #self.setFixedWidth(1024)
        #self.setFixedHeight(600)
        self.ui.label.setText('Hello World!')

        # Timer
        self.qTimer = QTimer()
        self.qTimer.setInterval(100)  # set interval to 1 s; 1000 ms = 1 s
        self.qTimer.timeout.connect(self.updateMessages)  # connect timeout signal to signal handler
        self.qTimer.start()  # start timer

        # Button
        self.ui.pushButton.clicked.connect(self.PreButtonClicked)
        self.ui.pushButton_2.clicked.connect(self.NextButtonClicked)

    def updateMessages(self):
        global words
        global dataStream

        if speech.myrecording:
            self.ui.label_5.setStyleSheet("background-color: red; color:white")
        else:
            self.ui.label_5.setStyleSheet("background-color: black; color:white")

        # print("Data is: ", dataStream)

        if dataStream is not None:

            if len(dataStream) > 0 and len(dataStream) <= 8:
                words.rotate(-1)
                words[2] = dataStream
                self.ui.label.setStyleSheet("color:white")
                self.ui.label_6.setStyleSheet("color:white")
                self.ui.label_7.setStyleSheet("color:Yellow")



            elif len(dataStream) > 8 and len(dataStream) <= 16:
                words.rotate(-2)
                words[1] = dataStream[:8]
                words[2] = dataStream[8:]
                self.ui.label.setStyleSheet("color:white")
                self.ui.label_6.setStyleSheet("color:Yellow")
                self.ui.label_7.setStyleSheet("color:Yellow")


            elif len(dataStream) > 16:
                words.rotate(-3)
                words[0] = dataStream[:8]
                words[1] = dataStream[8:16]
                words[2] = dataStream[16:24]
                self.ui.label.setStyleSheet("color:Yellow")
                self.ui.label_6.setStyleSheet("color:Yellow")
                self.ui.label_7.setStyleSheet("color:Yellow")

            self.ui.label.setText(f'{words[0]}')
            self.ui.label_6.setText(f'{words[1]}')
            self.ui.label_7.setText(f'{words[2]}')
            dataStream = ""

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
