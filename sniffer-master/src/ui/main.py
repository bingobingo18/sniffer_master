# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QTextEdit, QTreeWidget, QTreeWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(944, 616)
        font = QFont()
        font.setPointSize(14)
        MainWindow.setFont(font)
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionExit.setFont(font)
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionAbout.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(9, 9, 85, 25))
        self.label.setAlignment(Qt.AlignCenter)
        self.interfaceBox = QComboBox(self.centralwidget)
        self.interfaceBox.setObjectName(u"interfaceBox")
        self.interfaceBox.setGeometry(QRect(100, 10, 751, 30))
        self.startButton = QPushButton(self.centralwidget)
        self.startButton.setObjectName(u"startButton")
        self.startButton.setGeometry(QRect(860, 9, 75, 33))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(9, 48, 51, 25))
        self.label_2.setAlignment(Qt.AlignCenter)
        self.filterEdit = QLineEdit(self.centralwidget)
        self.filterEdit.setObjectName(u"filterEdit")
        self.filterEdit.setGeometry(QRect(100, 48, 751, 29))
        self.filterEdit.setFont(font)
        self.treeWidget = QTreeWidget(self.centralwidget)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.treeWidget.setHeaderItem(__qtreewidgetitem)
        self.treeWidget.setObjectName(u"treeWidget")
        self.treeWidget.setGeometry(QRect(10, 240, 361, 321))
        self.treeWidget.setAnimated(True)
        self.treeWidget.header().setVisible(False)
        self.contentEdit = QTextEdit(self.centralwidget)
        self.contentEdit.setObjectName(u"contentEdit")
        self.contentEdit.setGeometry(QRect(370, 240, 561, 321))
        font1 = QFont()
        font1.setFamilies([u"Fira Code"])
        font1.setPointSize(14)
        self.contentEdit.setFont(font1)
        self.contentEdit.setReadOnly(True)
        self.packetTable = QTableWidget(self.centralwidget)
        if (self.packetTable.columnCount() < 7):
            self.packetTable.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.packetTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.packetTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.packetTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.packetTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.packetTable.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.packetTable.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.packetTable.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.packetTable.setObjectName(u"packetTable")
        self.packetTable.setGeometry(QRect(9, 83, 926, 156))
        font2 = QFont()
        font2.setFamilies([u"Fira Code"])
        font2.setPointSize(12)
        self.packetTable.setFont(font2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 944, 31))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)
        self.actionExit.triggered.connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Sniffer", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Interface:", None))
        self.startButton.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Filter:", None))
        self.filterEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Input BPF expression to filter packet", None))
        ___qtablewidgetitem = self.packetTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"No.", None));
        ___qtablewidgetitem1 = self.packetTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Time", None));
        ___qtablewidgetitem2 = self.packetTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Source", None));
        ___qtablewidgetitem3 = self.packetTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Destination", None));
        ___qtablewidgetitem4 = self.packetTable.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Protocol", None));
        ___qtablewidgetitem5 = self.packetTable.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Length", None));
        ___qtablewidgetitem6 = self.packetTable.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Info", None));
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

