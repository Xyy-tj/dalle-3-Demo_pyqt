# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\GitHub\pluginbase\dalle\dalle.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(929, 746)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_2.addWidget(self.progressBar, 7, 0, 1, 3)
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 2, 1, 3, 2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.comboBox_imgsize = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_imgsize.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_imgsize.sizePolicy().hasHeightForWidth())
        self.comboBox_imgsize.setSizePolicy(sizePolicy)
        self.comboBox_imgsize.setObjectName("comboBox_imgsize")
        self.comboBox_imgsize.addItem("")
        self.comboBox_imgsize.addItem("")
        self.comboBox_imgsize.addItem("")
        self.gridLayout.addWidget(self.comboBox_imgsize, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.comboBox_style = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_style.sizePolicy().hasHeightForWidth())
        self.comboBox_style.setSizePolicy(sizePolicy)
        self.comboBox_style.setObjectName("comboBox_style")
        self.comboBox_style.addItem("")
        self.comboBox_style.addItem("")
        self.comboBox_style.addItem("")
        self.comboBox_style.addItem("")
        self.comboBox_style.addItem("")
        self.gridLayout.addWidget(self.comboBox_style, 4, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.gridLayout.addLayout(self.horizontalLayout_2, 4, 0, 1, 1)
        self.comboBox_model = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_model.sizePolicy().hasHeightForWidth())
        self.comboBox_model.setSizePolicy(sizePolicy)
        self.comboBox_model.setObjectName("comboBox_model")
        self.comboBox_model.addItem("")
        self.comboBox_model.addItem("")
        self.gridLayout.addWidget(self.comboBox_model, 3, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 8, 0, 1, 2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit_baseurl = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_baseurl.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_baseurl.sizePolicy().hasHeightForWidth())
        self.lineEdit_baseurl.setSizePolicy(sizePolicy)
        self.lineEdit_baseurl.setObjectName("lineEdit_baseurl")
        self.verticalLayout.addWidget(self.lineEdit_baseurl)
        self.lineEdit_apikey = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_apikey.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_apikey.sizePolicy().hasHeightForWidth())
        self.lineEdit_apikey.setSizePolicy(sizePolicy)
        self.lineEdit_apikey.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_apikey.setObjectName("lineEdit_apikey")
        self.verticalLayout.addWidget(self.lineEdit_apikey)
        self.gridLayout_2.addLayout(self.verticalLayout, 8, 2, 1, 1)
        self.sub_system_info = QtWidgets.QTextBrowser(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sub_system_info.sizePolicy().hasHeightForWidth())
        self.sub_system_info.setSizePolicy(sizePolicy)
        self.sub_system_info.setObjectName("sub_system_info")
        self.gridLayout_2.addWidget(self.sub_system_info, 4, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("方正姚体")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("font: 22pt \"方正姚体\";")
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 3)
        self.pushButton_gen = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_gen.sizePolicy().hasHeightForWidth())
        self.pushButton_gen.setSizePolicy(sizePolicy)
        self.pushButton_gen.setObjectName("pushButton_gen")
        self.gridLayout_2.addWidget(self.pushButton_gen, 3, 0, 1, 1)
        self.pushButton_theme = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_theme.setObjectName("pushButton_theme")
        self.gridLayout_2.addWidget(self.pushButton_theme, 6, 2, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_2.addWidget(self.textEdit, 2, 0, 1, 1)
        self.pushButton_figdir = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_figdir.setObjectName("pushButton_figdir")
        self.gridLayout_2.addWidget(self.pushButton_figdir, 6, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 929, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.label_4.setBuddy(self.comboBox_imgsize)
        self.label_3.setBuddy(self.comboBox_model)
        self.label_5.setBuddy(self.comboBox_style)

        self.retranslateUi(MainWindow)
        self.comboBox_model.currentIndexChanged['int'].connect(self.comboBox_imgsize.setCurrentIndex) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboBox_imgsize.setItemText(0, _translate("MainWindow", "1024x1024"))
        self.comboBox_imgsize.setItemText(1, _translate("MainWindow", "512x512"))
        self.comboBox_imgsize.setItemText(2, _translate("MainWindow", "256x256"))
        self.label_4.setText(_translate("MainWindow", "模型选择："))
        self.comboBox_style.setItemText(0, _translate("MainWindow", "默认"))
        self.comboBox_style.setItemText(1, _translate("MainWindow", "科研"))
        self.comboBox_style.setItemText(2, _translate("MainWindow", "素材"))
        self.comboBox_style.setItemText(3, _translate("MainWindow", "图表"))
        self.comboBox_style.setItemText(4, _translate("MainWindow", "动漫"))
        self.label_3.setText(_translate("MainWindow", "当前选择："))
        self.label_5.setText(_translate("MainWindow", "绘图风格："))
        self.comboBox_model.setItemText(0, _translate("MainWindow", "dall-e-3"))
        self.comboBox_model.setItemText(1, _translate("MainWindow", "dall-e-2"))
        self.lineEdit_baseurl.setPlaceholderText(_translate("MainWindow", "请输入您的base_url（可选）"))
        self.lineEdit_apikey.setPlaceholderText(_translate("MainWindow", "请输入您的授权apikey(sk-xxxxxxxxx)"))
        self.label_2.setText(_translate("MainWindow", "猫猫AI绘图工具（Cat-Plus）"))
        self.pushButton_gen.setText(_translate("MainWindow", "AI图像生成"))
        self.pushButton_theme.setText(_translate("MainWindow", "切换主题"))
        self.textEdit.setPlaceholderText(_translate("MainWindow", "请输入生成主题"))
        self.pushButton_figdir.setText(_translate("MainWindow", "生成图像文件夹"))
