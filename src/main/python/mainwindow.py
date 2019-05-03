# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""
# 添加下面这两句
import sys
import os.path

from PyQt5.QtCore import (pyqtSlot, Qt, QLocale, QUrl)
# 添加 `,QApplication`
from PyQt5.QtWidgets import (QMainWindow, QApplication, QFileDialog,
                             QTableWidgetItem, QShortcut, QHeaderView, QMessageBox, QTableWidget)
from PyQt5.QtGui import (QKeySequence, QDesktopServices)
# 去掉 from .Ui_mainwindow 中的点
from Ui_mainwindow import Ui_MainWindow

from serviceFile import ServiceFile

from serviceTranslate import ServiceTranslate


# TODO: 拖放支持,支持文件拖放;
# TODO:  添加对 ssa 等其他格式字幕的支持;
# TODO:  添加字幕转换功能;

class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        """
        Constructor

        @param parent reference to the parent widget
        @type QWidget
        """

        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        # 快捷键
        # 查找文件
        QShortcut(QKeySequence("Ctrl+F"), self,
                  self.on_pushButtonFindFile_clicked)
        # 自动翻译
        QShortcut(QKeySequence("Ctrl+T"), self,
                  self.on_pushButtonTranslate_clicked)
        # 保存翻译后的字幕文件
        QShortcut(QKeySequence("Ctrl+S"), self,
                  self.on_pushButtonSaveFile_clicked)
        # 保存双语字幕
        QShortcut(QKeySequence("Ctrl+Shift+S"), self,
                  self.on_pushButtonSaveFile2_clicked)
        # 打开帮助页面
        QShortcut(QKeySequence("F1"), self, self.showHelp)
        QShortcut(QKeySequence("Ctrl+H"), self, self.showHelp)

        self.sf = ServiceFile()

        # 目标语种初始化
        if QLocale.languageToString(QLocale.system().language()) == "Chinese":
            self.targetLanguage = "zh-CN"
        else:
            self.targetLanguage = "zh-CN"

        self.canBeSave = False
        self.helpURL = "http://coolwp.com/subtitle-translator.html"

    def dragEnterEvent(self, e):
        if e.mimeData().hasFormat('text/plain'):
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        # self.setFile(filePath)
        # self.setText(e.mimeData().text())
        print(e)

    def resizeEvent(self, event):
        # self.resized.emit()
        '''自动处理的窗口缩放事件

        event.size()的示例

        PyQt5.QtCore.QSize(1097, 628)
                print("resized")
                print(event.size().width())
                print(event.size().height())
        '''

        #self.tableWidget.resize(self.width(), self.height())

        return super(MainWindow, self).resizeEvent(event)

    def showHelp(self):

        if not QDesktopServices.openUrl(QUrl(self.helpURL)):
            QMessageBox.warning(self, 'Open Url', 'Could not open url')
#############################################

    def keyPressEvent(self, e):
        '''keyPressEvent
        按键事件处理方法,该方法不用绑定,将会被默认执行。
        窗口的最大/最小以及退出窗口的快捷键处理
        '''
        if e.key() == Qt.Key_Escape:
            self.close()
        if e.key() == Qt.Key_F11:
            if self.isMaximized():
                self.showNormal()
            else:
                self.showMaximized()

    def setSB(self, text, timeDurationInMs=5000):
        self.statusBar().showMessage(text, timeDurationInMs)

    def outputToTableWidget(self):

        parseRtn = self.sf.parseItems()

        if parseRtn == 1:
            self.setSB("返回已解析过的items")
        elif parseRtn == 2:
            self.setSB("文件路径为空?")
        elif parseRtn == 3:
            self.setSB("不被支持的文件扩展名,仅支持srt,ssa类型的字幕文件")
        elif parseRtn == 666:
            self.setSB("尚未支持的字幕格式")
        elif parseRtn == 999:
            self.setSB("未知错误")

        if parseRtn != 0:
            return

        items = self.sf.items
        itemsLen = len(items)
        if itemsLen == 0:
            self.setSB("not found any item?")
        else:

            self.tableWidget.setColumnCount(2)

            header = self.tableWidget.horizontalHeader()
            # QHeaderView.Stretch

            header.setSectionResizeMode(QHeaderView.ResizeToContents)
            header.setSectionResizeMode(0, QHeaderView.Stretch)

            self.tableWidget.setRowCount(itemsLen)
            self.tableWidget.setHorizontalHeaderLabels(
                ['原字符串', '翻译为'])
            i = 0
            if self.sf.fileExt == ".srt":

                for item in items:
                    self.tableWidget.setItem(
                        i, 0, QTableWidgetItem(str(item.text)))
                    self.tableWidget.setItem(i, 1, QTableWidgetItem(""))
                    i += 1

            self.setSB("Loaded {0} text should be translated.".format(i))
        pass
#############################################

    @pyqtSlot()
    def on_pushButtonSaveFile2_clicked(self):
        """
        保存双语字幕
        """
        if self.canBeSave == False:
            self.setSB("没有翻译任何条目,不需要保存...")
            return
        i = 0
        for item in self.sf.items:
            self.sf.items[i].text += "\n" + self.tableWidget.item(i, 1).text()
            i += 1

        if self.sf.saveToFile(self.sf.items, self.targetLanguage, True):
            self.setSB("已保存...")
        else:

            self.setSB("保存失败...")

    @pyqtSlot()
    def on_pushButtonSaveFile_clicked(self):
        """
        Slot documentation goes here.
        """

        if self.canBeSave == False:
            self.setSB("没有翻译任何条目,不需要保存...")
            return
        i = 0
        for item in self.sf.items:
            self.sf.items[i].text = self.tableWidget.item(i, 1).text()
            i += 1

        if self.sf.saveToFile(self.sf.items, self.targetLanguage, False):
            self.setSB("已保存...")
        else:

            self.setSB("保存失败...")

    @pyqtSlot()
    def on_pushButtonTranslate_clicked(self):
        """
        Slot documentation goes here.
        """
        parseRtn = self.sf.parseItems()
        if parseRtn != 1:
            self.setSB("没有载入字幕文件,无法获取翻译的内容...")
            return

        self.setSB("正在翻译,可能会暂时不响应任何操作...", 15000)
        items = self.sf.items
        itemsLen = len(items)
        if itemsLen == 0:
            self.setSB("not found any item?")
        else:

            self.tableWidget.setRowCount(itemsLen)
            self.tableWidget.setHorizontalHeaderLabels(
                ['原字符串', '翻译为'])
            i = 0
            strListSrc = []
            if self.sf.fileExt == ".srt":

                for item in items:
                    strListSrc.append(self.tableWidget.item(i, 0).text())
                    self.tableWidget.setItem(i, 1, QTableWidgetItem(""))
                    i += 1

                tS = ServiceTranslate()
                strListDest = tS.t(strListSrc, self.targetLanguage)
                if len(strListDest) != 0:
                    i = 0
                    for s in strListDest:
                        self.tableWidget.setItem(
                            i, 1, QTableWidgetItem(s.text))
                        i += 1

            self.setSB("Translated {0} strings...".format(i))
            self.canBeSave = True

    @pyqtSlot()
    def on_pushButtonFindFile_clicked(self):
        """
        Slot documentation goes here.
        """
        filePath, _ = QFileDialog.getOpenFileName(
            self, "Open File", "", "subtitle(*.srt *.ssa)")
        if not os.path.exists(filePath):
            self.setSB("Not Found: {0}".format(filePath))
        else:
            # self.textBrowserShowFileName.setText(filePath)
            self.setFile(filePath)

    def setFile(self, filePath):
        self.sf.setFilePath(filePath)
        self.outputToTableWidget()

    @pyqtSlot(int)
    def on_comboBoxDeSt_currentIndexChanged(self, index):
        """
        选择目标语种

        @param index DESCRIPTION
        @type int
        """
        if index == 0:
            self.targetLanguage = "zh-CN"
        elif index == 2:
            self.targetLanguage = "zh-TW"
        elif index == 3:
            self.targetLanguage = "en"
        elif index == 4:
            self.targetLanguage = "es"
            self.targetLanguage = "en"
        elif index == 5:
            self.targetLanguage = "ru"

        self.sf.items = []
        self.sf.setItems([])


def main():
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
