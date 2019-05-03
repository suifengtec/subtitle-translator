# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Y:\pyqt\0000-subtitleTranslator\src\src\main\python\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1076, 614)
        MainWindow.setMinimumSize(QtCore.QSize(1076, 614))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.centralWidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(618, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButtonFindFile = QtWidgets.QPushButton(self.centralWidget)
        self.pushButtonFindFile.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonFindFile.setObjectName("pushButtonFindFile")
        self.horizontalLayout.addWidget(self.pushButtonFindFile)
        self.comboBoxDeSt = QtWidgets.QComboBox(self.centralWidget)
        self.comboBoxDeSt.setObjectName("comboBoxDeSt")
        self.comboBoxDeSt.addItem("")
        self.comboBoxDeSt.addItem("")
        self.comboBoxDeSt.addItem("")
        self.comboBoxDeSt.addItem("")
        self.comboBoxDeSt.addItem("")
        self.comboBoxDeSt.addItem("")
        self.comboBoxDeSt.addItem("")
        self.horizontalLayout.addWidget(self.comboBoxDeSt)
        self.pushButtonTranslate = QtWidgets.QPushButton(self.centralWidget)
        self.pushButtonTranslate.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonTranslate.setObjectName("pushButtonTranslate")
        self.horizontalLayout.addWidget(self.pushButtonTranslate)
        self.pushButtonSaveFile2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButtonSaveFile2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonSaveFile2.setObjectName("pushButtonSaveFile2")
        self.horizontalLayout.addWidget(self.pushButtonSaveFile2)
        self.pushButtonSaveFile = QtWidgets.QPushButton(self.centralWidget)
        self.pushButtonSaveFile.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonSaveFile.setObjectName("pushButtonSaveFile")
        self.horizontalLayout.addWidget(self.pushButtonSaveFile)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.pushButtonFindFile, self.comboBoxDeSt)
        MainWindow.setTabOrder(self.comboBoxDeSt, self.pushButtonTranslate)
        MainWindow.setTabOrder(self.pushButtonTranslate, self.pushButtonSaveFile)
        MainWindow.setTabOrder(self.pushButtonSaveFile, self.tableWidget)
        MainWindow.setTabOrder(self.tableWidget, self.pushButtonSaveFile2)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "subtitleTranslator"))
        self.pushButtonFindFile.setText(_translate("MainWindow", "Find(Ctrl+F)"))
        self.comboBoxDeSt.setItemText(0, _translate("MainWindow", "Select Target Language"))
        self.comboBoxDeSt.setItemText(1, _translate("MainWindow", "zh-CN"))
        self.comboBoxDeSt.setItemText(2, _translate("MainWindow", "zh-TW"))
        self.comboBoxDeSt.setItemText(3, _translate("MainWindow", "en"))
        self.comboBoxDeSt.setItemText(4, _translate("MainWindow", "es"))
        self.comboBoxDeSt.setItemText(5, _translate("MainWindow", "ru"))
        self.comboBoxDeSt.setItemText(6, _translate("MainWindow", "fr"))
        self.pushButtonTranslate.setText(_translate("MainWindow", "Translate(Ctrl+T)"))
        self.pushButtonSaveFile2.setText(_translate("MainWindow", "Save Bilingual(Ctrl+Shift+S)"))
        self.pushButtonSaveFile.setText(_translate("MainWindow", "Save(Ctrl+S)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

