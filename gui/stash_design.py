# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/stash_design.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(813, 611)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setMaximumSize(QtCore.QSize(801, 571))
        self.tabWidget.setObjectName("tabWidget")
        self.stash_tab = QtWidgets.QWidget()
        self.stash_tab.setObjectName("stash_tab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.stash_tab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.stackedWidget = QtWidgets.QStackedWidget(self.stash_tab)
        self.stackedWidget.setObjectName("stackedWidget")
        self.input_stash_page = QtWidgets.QWidget()
        self.input_stash_page.setObjectName("input_stash_page")
        self.input_poesessid = QtWidgets.QPlainTextEdit(self.input_stash_page)
        self.input_poesessid.setGeometry(QtCore.QRect(70, 15, 692, 41))
        self.input_poesessid.setObjectName("input_poesessid")
        self.GetStashButton = QtWidgets.QPushButton(self.input_stash_page)
        self.GetStashButton.setGeometry(QtCore.QRect(70, 347, 691, 31))
        self.GetStashButton.setObjectName("GetStashButton")
        self.input_poetabs = QtWidgets.QPlainTextEdit(self.input_stash_page)
        self.input_poetabs.setGeometry(QtCore.QRect(70, 74, 692, 31))
        self.input_poetabs.setObjectName("input_poetabs")
        self.label = QtWidgets.QLabel(self.input_stash_page)
        self.label.setGeometry(QtCore.QRect(9, 78, 51, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.input_stash_page)
        self.label_2.setGeometry(QtCore.QRect(9, 15, 55, 41))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.input_stash_page)
        self.label_3.setGeometry(QtCore.QRect(9, 176, 22, 151))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.input_stash_page)
        self.label_4.setGeometry(QtCore.QRect(400, 130, 16, 16))
        self.label_4.setObjectName("label_4")
        self.input_json = QtWidgets.QPlainTextEdit(self.input_stash_page)
        self.input_json.setGeometry(QtCore.QRect(70, 180, 691, 151))
        self.input_json.setObjectName("input_json")
        self.stackedWidget.addWidget(self.input_stash_page)
        self.stash_page = QtWidgets.QWidget()
        self.stash_page.setObjectName("stash_page")
        self.formLayout_3 = QtWidgets.QFormLayout(self.stash_page)
        self.formLayout_3.setObjectName("formLayout_3")
        self.ShowStashItems = QtWidgets.QTreeWidget(self.stash_page)
        self.ShowStashItems.setObjectName("ShowStashItems")
        item_0 = QtWidgets.QTreeWidgetItem(self.ShowStashItems)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.ShowStashItems)
        self.ResetStashButton = QtWidgets.QPushButton(self.stash_page)
        self.ResetStashButton.setObjectName("ResetStashButton")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.ResetStashButton)
        self.ShowStashItemText = QtWidgets.QTextBrowser(self.stash_page)
        self.ShowStashItemText.setObjectName("ShowStashItemText")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.ShowStashItemText)
        self.stackedWidget.addWidget(self.stash_page)
        self.gridLayout_3.addWidget(self.stackedWidget, 0, 0, 1, 1)
        self.tabWidget.addTab(self.stash_tab, "")
        self.filters_tab = QtWidgets.QWidget()
        self.filters_tab.setObjectName("filters_tab")
        self.formLayout_2 = QtWidgets.QFormLayout(self.filters_tab)
        self.formLayout_2.setObjectName("formLayout_2")
        self.ImportFiltersButton = QtWidgets.QPushButton(self.filters_tab)
        self.ImportFiltersButton.setObjectName("ImportFiltersButton")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.ImportFiltersButton)
        self.CreateFiltersButton = QtWidgets.QPushButton(self.filters_tab)
        self.CreateFiltersButton.setObjectName("CreateFiltersButton")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.CreateFiltersButton)
        self.SelectFilterCombo = QtWidgets.QComboBox(self.filters_tab)
        self.SelectFilterCombo.setObjectName("SelectFilterCombo")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.SelectFilterCombo)
        self.ShowFilterStatsText = QtWidgets.QTextBrowser(self.filters_tab)
        self.ShowFilterStatsText.setObjectName("ShowFilterStatsText")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.ShowFilterStatsText)
        self.tabWidget.addTab(self.filters_tab, "")
        self.filtered_items_tab = QtWidgets.QWidget()
        self.filtered_items_tab.setObjectName("filtered_items_tab")
        self.formLayout_4 = QtWidgets.QFormLayout(self.filtered_items_tab)
        self.formLayout_4.setObjectName("formLayout_4")
        self.ShowFilterItems = QtWidgets.QTreeWidget(self.filtered_items_tab)
        self.ShowFilterItems.setObjectName("ShowFilterItems")
        item_0 = QtWidgets.QTreeWidgetItem(self.ShowFilterItems)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_0 = QtWidgets.QTreeWidgetItem(self.ShowFilterItems)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_0 = QtWidgets.QTreeWidgetItem(self.ShowFilterItems)
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.ShowFilterItems)
        self.ShowItemStatsText = QtWidgets.QTextBrowser(self.filtered_items_tab)
        self.ShowItemStatsText.setObjectName("ShowItemStatsText")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.ShowItemStatsText)
        self.ShowFilteredItemsNames = QtWidgets.QTextBrowser(self.filtered_items_tab)
        self.ShowFilteredItemsNames.setObjectName("ShowFilteredItemsNames")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.ShowFilteredItemsNames)
        self.tabWidget.addTab(self.filtered_items_tab, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 813, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.GetStashButton.setText(_translate("MainWindow", "Get Stash"))
        self.input_poetabs.setPlainText(_translate("MainWindow", "q1,q2,q3"))
        self.label.setText(_translate("MainWindow", "Tabs"))
        self.label_2.setText(_translate("MainWindow", "POESESSID"))
        self.label_3.setText(_translate("MainWindow", "Json"))
        self.label_4.setText(_translate("MainWindow", "OR"))
        self.ShowStashItems.headerItem().setText(0, _translate("MainWindow", "1"))
        __sortingEnabled = self.ShowStashItems.isSortingEnabled()
        self.ShowStashItems.setSortingEnabled(False)
        self.ShowStashItems.topLevelItem(0).setText(0, _translate("MainWindow", "Item Class"))
        self.ShowStashItems.topLevelItem(0).child(0).setText(0, _translate("MainWindow", "Boots"))
        self.ShowStashItems.topLevelItem(0).child(0).child(0).setText(0, _translate("MainWindow", "Item 1"))
        self.ShowStashItems.setSortingEnabled(__sortingEnabled)
        self.ResetStashButton.setText(_translate("MainWindow", "Get Stash Again"))
        self.ShowStashItemText.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Item Stats</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.stash_tab), _translate("MainWindow", "Stash"))
        self.ImportFiltersButton.setText(_translate("MainWindow", "Import Filters"))
        self.CreateFiltersButton.setText(_translate("MainWindow", "Create Filter"))
        self.ShowFilterStatsText.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Item Stats</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.filters_tab), _translate("MainWindow", "Filters"))
        self.ShowFilterItems.headerItem().setText(0, _translate("MainWindow", "1"))
        __sortingEnabled = self.ShowFilterItems.isSortingEnabled()
        self.ShowFilterItems.setSortingEnabled(False)
        self.ShowFilterItems.topLevelItem(0).setText(0, _translate("MainWindow", "Filter 1"))
        self.ShowFilterItems.topLevelItem(0).child(0).setText(0, _translate("MainWindow", "Item Class"))
        self.ShowFilterItems.topLevelItem(0).child(0).child(0).setText(0, _translate("MainWindow", "Item 1"))
        self.ShowFilterItems.topLevelItem(1).setText(0, _translate("MainWindow", "Filter 2"))
        self.ShowFilterItems.topLevelItem(1).child(0).setText(0, _translate("MainWindow", "Item Class"))
        self.ShowFilterItems.topLevelItem(1).child(0).child(0).setText(0, _translate("MainWindow", "Item 2"))
        self.ShowFilterItems.setSortingEnabled(__sortingEnabled)
        self.ShowItemStatsText.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Item Stats</p></body></html>"))
        self.ShowFilteredItemsNames.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">All items names</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.filtered_items_tab), _translate("MainWindow", "Filtered Items"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))