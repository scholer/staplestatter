# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'staplestatter.ui'
#
# Created: Tue May 13 23:09:11 2014
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(475, 496)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.processButton = QtGui.QPushButton(self.tab)
        self.processButton.setObjectName("processButton")
        self.verticalLayout_4.addWidget(self.processButton)
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.label_3 = QtGui.QLabel(self.tab)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.browsePlotfileButton = QtGui.QPushButton(self.tab)
        self.browsePlotfileButton.setObjectName("browsePlotfileButton")
        self.horizontalLayout_2.addWidget(self.browsePlotfileButton)
        self.browseStatsfileButton = QtGui.QPushButton(self.tab)
        self.browseStatsfileButton.setObjectName("browseStatsfileButton")
        self.horizontalLayout_2.addWidget(self.browseStatsfileButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.plotsfileLineEdit = QtGui.QLineEdit(self.tab)
        self.plotsfileLineEdit.setObjectName("plotsfileLineEdit")
        self.horizontalLayout_3.addWidget(self.plotsfileLineEdit)
        self.statsfileLineEdit = QtGui.QLineEdit(self.tab)
        self.statsfileLineEdit.setObjectName("statsfileLineEdit")
        self.horizontalLayout_3.addWidget(self.statsfileLineEdit)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.processButton2 = QtGui.QPushButton(self.tab_2)
        self.processButton2.setObjectName("processButton2")
        self.verticalLayout.addWidget(self.processButton2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.newSpecfileButton = QtGui.QPushButton(self.tab_2)
        self.newSpecfileButton.setObjectName("newSpecfileButton")
        self.horizontalLayout.addWidget(self.newSpecfileButton)
        self.loadSpecfileButton = QtGui.QPushButton(self.tab_2)
        self.loadSpecfileButton.setObjectName("loadSpecfileButton")
        self.horizontalLayout.addWidget(self.loadSpecfileButton)
        self.saveSpecfileAsButton = QtGui.QPushButton(self.tab_2)
        self.saveSpecfileAsButton.setObjectName("saveSpecfileAsButton")
        self.horizontalLayout.addWidget(self.saveSpecfileAsButton)
        self.saveSpecfileButton = QtGui.QPushButton(self.tab_2)
        self.saveSpecfileButton.setObjectName("saveSpecfileButton")
        self.horizontalLayout.addWidget(self.saveSpecfileButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label = QtGui.QLabel(self.tab_2)
        self.label.setObjectName("label")
        self.horizontalLayout_10.addWidget(self.label)
        self.specfilepathLineEdit = QtGui.QLineEdit(self.tab_2)
        self.specfilepathLineEdit.setObjectName("specfilepathLineEdit")
        self.horizontalLayout_10.addWidget(self.specfilepathLineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.specfileTextEdit = QtGui.QPlainTextEdit(self.tab_2)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(10)
        self.specfileTextEdit.setFont(font)
        self.specfileTextEdit.setObjectName("specfileTextEdit")
        self.verticalLayout.addWidget(self.specfileTextEdit)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.tab_3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.scrollArea = QtGui.QScrollArea(self.tab_3)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 433, 425))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.usageTextEdit = QtGui.QPlainTextEdit(self.scrollAreaWidgetContents)
        self.usageTextEdit.setUndoRedoEnabled(False)
        self.usageTextEdit.setReadOnly(True)
        self.usageTextEdit.setObjectName("usageTextEdit")
        self.verticalLayout_6.addWidget(self.usageTextEdit)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_5.addWidget(self.scrollArea)
        self.tabWidget.addTab(self.tab_3, "")
        self.verticalLayout_2.addWidget(self.tabWidget)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.processButton.setText(QtGui.QApplication.translate("Dialog", "Process and plot!", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Use the next tab to specify processing methods, then press \'Process\'.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "Save plot or stats/scores to file:", None, QtGui.QApplication.UnicodeUTF8))
        self.browsePlotfileButton.setText(QtGui.QApplication.translate("Dialog", "Save plot to file...", None, QtGui.QApplication.UnicodeUTF8))
        self.browseStatsfileButton.setText(QtGui.QApplication.translate("Dialog", "Save stats to file...", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("Dialog", "Control", None, QtGui.QApplication.UnicodeUTF8))
        self.processButton2.setText(QtGui.QApplication.translate("Dialog", "Process and plot!", None, QtGui.QApplication.UnicodeUTF8))
        self.newSpecfileButton.setText(QtGui.QApplication.translate("Dialog", "New...", None, QtGui.QApplication.UnicodeUTF8))
        self.loadSpecfileButton.setText(QtGui.QApplication.translate("Dialog", "Load...", None, QtGui.QApplication.UnicodeUTF8))
        self.saveSpecfileAsButton.setText(QtGui.QApplication.translate("Dialog", "Save As...", None, QtGui.QApplication.UnicodeUTF8))
        self.saveSpecfileButton.setText(QtGui.QApplication.translate("Dialog", "Save!", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "File: ", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("Dialog", "Specify plots", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QtGui.QApplication.translate("Dialog", "Usage help", None, QtGui.QApplication.UnicodeUTF8))

