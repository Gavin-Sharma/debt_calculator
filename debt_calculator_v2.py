# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\debt_calculator.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1071, 788)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(380, 0, 301, 81))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setUnderline(True)
        self.label1.setFont(font)
        self.label1.setObjectName("label1")
        self.avalancherRadioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.avalancherRadioButton.setGeometry(QtCore.QRect(410, 170, 95, 20))
        self.avalancherRadioButton.setObjectName("avalancherRadioButton")
        self.snowballRadioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.snowballRadioButton.setGeometry(QtCore.QRect(550, 170, 95, 20))
        self.snowballRadioButton.setObjectName("snowballRadioButton")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(260, 220, 551, 211))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.addPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.addPushButton.setGeometry(QtCore.QRect(820, 400, 93, 28))
        self.addPushButton.setObjectName("addPushButton")
        self.calculatePushButton = QtWidgets.QPushButton(self.centralwidget)
        self.calculatePushButton.setGeometry(QtCore.QRect(490, 510, 93, 28))
        self.calculatePushButton.setObjectName("calculatePushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1071, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # connect the add button to the add_row function
        self.addPushButton.clicked.connect(self.add_row)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label1.setText(_translate("MainWindow", "Debt Calculator"))
        self.avalancherRadioButton.setText(_translate("MainWindow", "Avalanche"))
        self.snowballRadioButton.setText(_translate("MainWindow", "Snowball"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Debt Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Debt Amount"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Intrest Rate"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Min Payment"))
        self.addPushButton.setText(_translate("MainWindow", "+"))
        self.calculatePushButton.setText(_translate("MainWindow", "Calculate"))

    def add_row(self):
        """when the add button is pressed, add a row to the table"""
        rowPosition = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowPosition)
        print("added row")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())