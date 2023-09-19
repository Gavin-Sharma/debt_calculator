from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QTableWidget, QTableWidgetItem


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1071, 788)
        MainWindow.setStyleSheet("background-color: rgb(45, 78, 108);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.main_label = QtWidgets.QLabel(self.centralwidget)
        self.main_label.setGeometry(QtCore.QRect(60, 0, 301, 81))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setUnderline(True)
        self.main_label.setFont(font)
        self.main_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.main_label.setObjectName("main_label")
        self.avalancherRadioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.avalancherRadioButton.setGeometry(QtCore.QRect(230, 190, 95, 20))
        self.avalancherRadioButton.setStyleSheet("color: rgb(255, 255, 255);")
        self.avalancherRadioButton.setObjectName("avalancherRadioButton")
        self.snowballRadioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.snowballRadioButton.setGeometry(QtCore.QRect(130, 190, 95, 20))
        self.snowballRadioButton.setStyleSheet("color: rgb(255, 255, 255);")
        self.snowballRadioButton.setObjectName("snowballRadioButton")
        self.debt_table = QtWidgets.QTableWidget(self.centralwidget)
        self.debt_table.setGeometry(QtCore.QRect(40, 240, 541, 491))
        self.debt_table.setStyleSheet(
            "border-color: rgb(255, 255, 255);\n"
            "background-color: rgb(255, 255, 255);"
        )
        self.debt_table.setObjectName("debt_table")
        self.debt_table.setColumnCount(4)
        self.debt_table.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.debt_table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.debt_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.debt_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.debt_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.debt_table.setHorizontalHeaderItem(3, item)
        self.addPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.addPushButton.setGeometry(QtCore.QRect(600, 340, 93, 28))
        self.addPushButton.setStyleSheet("color: rgb(255, 255, 255);")
        self.addPushButton.setObjectName("addPushButton")
        self.calculatePushButton = QtWidgets.QPushButton(self.centralwidget)
        self.calculatePushButton.setGeometry(QtCore.QRect(600, 700, 93, 28))
        self.calculatePushButton.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(0, 85, 0);"
        )
        self.calculatePushButton.setObjectName("calculatePushButton")
        self.clearPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.clearPushButton.setGeometry(QtCore.QRect(600, 300, 93, 28))
        self.clearPushButton.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "background-color: rgb(170, 0, 0);"
        )
        self.clearPushButton.setObjectName("clearPushButton")
        self.avalanche_label = QtWidgets.QLabel(self.centralwidget)
        self.avalanche_label.setGeometry(QtCore.QRect(130, 150, 481, 31))
        self.avalanche_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.avalanche_label.setObjectName("avalanche_label")
        self.snowball_label = QtWidgets.QLabel(self.centralwidget)
        self.snowball_label.setGeometry(QtCore.QRect(130, 130, 481, 16))
        self.snowball_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.snowball_label.setObjectName("snowball_label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 90, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 200, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(730, 90, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.extra_money = QtWidgets.QLineEdit(self.centralwidget)
        self.extra_money.setGeometry(QtCore.QRect(810, 140, 113, 22))
        self.extra_money.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.extra_money.setObjectName("extra_money")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(730, 200, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.clearPushButton.clicked.connect(self.debt_table.clearContents)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # _________________________________________________________________________
        # CONNECT BUTTONS TO FUNCTIONS

        # connect the add button to the add_row function
        self.addPushButton.clicked.connect(self.add_row)

        # connect the calculate button to the get_calculate_input function
        self.calculatePushButton.clicked.connect(self.calculate)

        # _________________________________________________________________________

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.main_label.setText(_translate("MainWindow", "Debt Calculator"))
        self.avalancherRadioButton.setText(_translate("MainWindow", "Avalanche"))
        self.snowballRadioButton.setText(_translate("MainWindow", "Snowball"))
        item = self.debt_table.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.debt_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Debt Name"))
        item = self.debt_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Debt Amount"))
        item = self.debt_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Intrest Rate"))
        item = self.debt_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Min Payment"))
        self.addPushButton.setText(_translate("MainWindow", "Add Row"))
        self.calculatePushButton.setText(_translate("MainWindow", "Calculate"))
        self.clearPushButton.setText(_translate("MainWindow", "Clear"))
        self.avalanche_label.setText(
            _translate(
                "MainWindow",
                "2) Avalanche Debt Repayment (saves more money): Prioritizes high-interest debts.",
            )
        )
        self.snowball_label.setText(
            _translate(
                "MainWindow",
                "1) Snowball Debt Repayment: Focuses on paying off smallest debts for motivation.",
            )
        )
        self.label_2.setText(_translate("MainWindow", "Payoff methods:"))
        self.label_3.setText(_translate("MainWindow", "Debts"))
        self.label_4.setText(_translate("MainWindow", "Extra contribution money"))

    def add_row(self):
        """
        When the add button is pressed, add a row to the table.
        """
        rowPosition = self.debt_table.rowCount()
        self.debt_table.insertRow(rowPosition)
        print("added row")

    def calculate_payoff(self, debts, extra_money, payoff_method):
        """
        Calculate the payoff of the debts. Based on if its snowball or avalanche, the debts will be paid off differently.
            - snowball: pay off the smallest debt first
            - avalanche: pay off the highest interest rate first
        """
        # *** SNOWBALL METHOD ***

        if payoff_method == "snowball":
            # sort debts smallest to largest
            debts.sort(key=lambda x: x[1])

            if extra_money != 0 or extra_money != "":
                for position, debt in enumerate(debts):
                    # the first debt in the list is the smallest and gets 80% of the extra money
                    if position == 0:
                        # store 80% of the extra money in a variable
                        snowball_payment = extra_money * 0.8

                        if debt[3] + snowball_payment <= debt[1]:
                            # add the snowball payment to the debt minimum
                            debt[3] += snowball_payment

                            # update extra money
                            extra_money -= snowball_payment
                        else:
                            # if the snowball payment is greater than the debt, then the debt is paid off
                            above_debt_money = (debt[3] + snowball_payment) - debt[1]

                            # add the new minimum debt amount
                            debt[3] += snowball_payment - above_debt_money

                            # update extra money
                            extra_money += above_debt_money

                    else:
                        # distribute 20% of the remaining money to all the debts
                        distribution_money_amount = extra_money / (len(debts) - 1)

                        if debt[3] + distribution_money_amount <= debt[1]:
                            # add the distribution money to the debt minimum
                            debt[3] += distribution_money_amount
                            # update extra money
                            extra_money -= distribution_money_amount
                        else:
                            # if the distribution money is greater than the debt, then the debt is paid off
                            above_debt_money = (
                                debt[3] + distribution_money_amount
                            ) - debt[1]

                            # add the new minimum debt amount
                            debt[3] += distribution_money_amount - above_debt_money

                            # update extra money
                            extra_money += above_debt_money

                # *** AVLANCHE METHOD ***

        if payoff_method == "avalanche":
            # sort the debts by the highest interest rate
            debts.sort(key=lambda x: x[2])

            if extra_money != 0 or extra_money != "":
                for position, debt in enumerate(debts):
                    # the first debt in the list is the smallest and gets 80% of the extra money
                    if position == 0:
                        # store 80% of the extra money in a variable
                        snowball_payment = extra_money * 0.8

                        if debt[3] + snowball_payment <= debt[1]:
                            # add the snowball payment to the debt minimum
                            debt[3] += snowball_payment

                            # update extra money
                            extra_money -= snowball_payment
                        else:
                            # if the snowball payment is greater than the debt, then the debt is paid off
                            above_debt_money = (debt[3] + snowball_payment) - debt[1]

                            # add the new minimum debt amount
                            debt[3] += snowball_payment - above_debt_money

                            # update extra money
                            extra_money += above_debt_money

                    else:
                        # distribute 20% of the remaining money to all the debts
                        distribution_money_amount = extra_money / (len(debts) - 1)

                        if debt[3] + distribution_money_amount <= debt[1]:
                            # add the distribution money to the debt minimum
                            debt[3] += distribution_money_amount
                            # update extra money
                            extra_money -= distribution_money_amount
                        else:
                            # if the distribution money is greater than the debt, then the debt is paid off
                            above_debt_money = (
                                debt[3] + distribution_money_amount
                            ) - debt[1]

                            # add the new minimum debt amount
                            debt[3] += distribution_money_amount - above_debt_money

                            # update extra money
                            extra_money += above_debt_money

        return debts

    def calculate(self):
        """when the calculate button is pressed, calculate the payoff"""
        # get the number of rows in the table
        row_count = self.debt_table.rowCount()

        # get the number of columns in the table
        column_count = self.debt_table.columnCount()

        # create a list to hold the debts
        debts = []

        # loop through the table and add the debts to the list the debt needs to be a float
        for row in range(row_count):
            debt = []
            for column in range(column_count):
                item = self.debt_table.item(row, column)
                if item is not None:
                    debt.append(item.text())
            debts.append(debt)

        # turn the debts into float values
        for debt in debts:
            debt[1] = float(debt[1])
            debt[2] = float(debt[2])
            debt[3] = float(debt[3])

        # get the extra money from the line edit
        extra_money = float(self.extra_money.text())

        # get the payoff method
        if self.snowballRadioButton.isChecked():
            payoff_method = "snowball"
        elif self.avalancherRadioButton.isChecked():
            payoff_method = "avalanche"
        else:
            payoff_method = "snowball"

        # print the debts
        print(debts)

        # print the extra money
        print(extra_money)

        # print the payoff method
        print(payoff_method)

        # calculate the payoff
        payoff = self.calculate_payoff(debts, extra_money, payoff_method)

        # print the payoff
        print(payoff)

        # Prepare data for the results table
        results_data = []
        for i, debt in enumerate(payoff, 1):
            results_data.append(
                {
                    "Debt Name": debt[0],
                    "Debt Amount": str(debt[1]),
                    "New Min Payment": str(debt[3]),
                }
            )

        # Display the results in the new window
        self.show_results_window(results_data)

    def show_results_window(self, results_text):
        self.results_window = ResultsWindow(results_text)
        self.results_window.exec_()


class ResultsWindow(QDialog):
    def __init__(self, results_data):
        super().__init__()

        self.setWindowTitle("Debt Calculator - Results")
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout()

        self.results_table = QTableWidget()
        self.results_table.setRowCount(len(results_data))
        self.results_table.setColumnCount(
            3
        )  # Columns for Debt Name, Debt Amount, and New Min Payment

        # Set column headers
        self.results_table.setHorizontalHeaderLabels(
            ["Debt Name", "Debt Amount", "New Min Payment"]
        )

        for row, data in enumerate(results_data):
            self.results_table.setItem(row, 0, QTableWidgetItem(data["Debt Name"]))
            self.results_table.setItem(row, 1, QTableWidgetItem(data["Debt Amount"]))
            self.results_table.setItem(
                row, 2, QTableWidgetItem(data["New Min Payment"])
            )

        # Customize the table's appearance
        self.results_table.setStyleSheet(
            "QTableWidget { background-color: rgb(45, 78, 108); color: white; }"  # Set background color and text color
            "QHeaderView::section { background-color: rgb(0, 85, 0); color: white; }"  # Set header background color and text color
            "QTableWidget::item { padding: 5px; }"  # Add padding to table items
        )

        layout.addWidget(self.results_table)

        self.setLayout(layout)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
