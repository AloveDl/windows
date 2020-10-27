# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tip.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow


class TipWidget(QMainWindow):
    def __init__(self, tips):
        super(TipWidget, self).__init__()

        self.setObjectName("MainWindow")
        self.resize(252, 239)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 30, 150, 51))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(70, 120, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 252, 26))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi(tips)
        self.pushButton.clicked.connect(self.tip_close)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, tips):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle("提示")
        self.label.setText(tips)
        self.pushButton.setText(_translate("MainWindow", "确定"))

    def tip_close(self):
        self.close()

if __name__ =="__main__":
    app = QApplication(sys.argv)
    # mainWin = QMainWindow()
    myWin = TipWidget("密码错误")
    # myWin.setupUi(mainWin)
    myWin.show()
    sys.exit(app.exec_())

# if __name__=="__main__":
#     app = QApplication(sys.argv)
#     widget = QMainWindow()
#     ui = TipWidget()
#     ui.setupUi(widget)
#     widget.show()
#     sys.exit(app.exec_())