# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget

from scene_window import Ui_Scene
from role_window import Ui_Role
from vits_window import Ui_Vits
from script_window import Ui_Script

class Ui_main_window(object):
    def setupUi(self, main_window):
        main_window.setObjectName("main_window")
        main_window.resize(1920, 1080)
        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setObjectName("centralwidget")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(10, 0, 1901, 1041))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.frame = QtWidgets.QFrame(self.splitter)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.SceneButton = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SceneButton.sizePolicy().hasHeightForWidth())
        self.SceneButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("阿里巴巴普惠体")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.SceneButton.setFont(font)
        self.SceneButton.setObjectName("SceneButton")
        self.verticalLayout_4.addWidget(self.SceneButton)
        self.RoleButton = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RoleButton.sizePolicy().hasHeightForWidth())
        self.RoleButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("阿里巴巴普惠体")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.RoleButton.setFont(font)
        self.RoleButton.setObjectName("RoleButton")
        self.verticalLayout_4.addWidget(self.RoleButton)
        self.VitsButton = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.VitsButton.sizePolicy().hasHeightForWidth())
        self.VitsButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("阿里巴巴普惠体")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.VitsButton.setFont(font)
        self.VitsButton.setObjectName("VitsButton")
        self.verticalLayout_4.addWidget(self.VitsButton)
        self.ScriptButton = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ScriptButton.sizePolicy().hasHeightForWidth())
        self.ScriptButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("阿里巴巴普惠体")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.ScriptButton.setFont(font)
        self.ScriptButton.setObjectName("ScriptButton")
        self.verticalLayout_4.addWidget(self.ScriptButton)
        # self.frame_2 = QtWidgets.QFrame(self.splitter)
        # self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        # self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        # self.frame_2.setObjectName("frame_2")
        # self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_2)
        # self.verticalLayout_5.setObjectName("verticalLayout_5")
        # self.listView = QtWidgets.QListView(self.frame_2)
        # self.listView.setObjectName("listView")
        # self.verticalLayout_5.addWidget(self.listView)
        main_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(main_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 23))
        self.menubar.setObjectName("menubar")
        main_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(main_window)
        self.statusbar.setObjectName("statusbar")
        main_window.setStatusBar(self.statusbar)

        self.retranslateUi(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

        # 初始化4个对象，并把 first对象 加入到 splitter 中
        self.Scene = Scene_Menu()
        self.Role = Role_Menu()
        self.Vits = Vits_Menu()
        self.Script = Script_Menu()
        self.splitter.addWidget(self.Scene)

        # 绑定Button到槽函数
        self.SceneButton.clicked.connect(lambda: self.change(self.SceneButton.objectName()))
        self.RoleButton.clicked.connect(lambda: self.change(self.RoleButton.objectName()))
        self.VitsButton.clicked.connect(lambda: self.change(self.VitsButton.objectName()))
        self.ScriptButton.clicked.connect(lambda: self.change(self.ScriptButton.objectName()))

    def change(self, name):
        if name == "SceneButton":
            self.splitter.widget(1).setParent(None)
            self.splitter.insertWidget(1, self.Scene)

        if name == "RoleButton":
            self.splitter.widget(1).setParent(None)
            self.splitter.insertWidget(1, self.Role)

        if name == "VitsButton":
            self.splitter.widget(1).setParent(None)
            self.splitter.insertWidget(1, self.Vits)

        if name == "ScriptButton":
            self.splitter.widget(1).setParent(None)
            self.splitter.insertWidget(1, self.Script)

    def retranslateUi(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "MainWindow"))
        self.SceneButton.setText(_translate("main_window", "场景生成"))
        self.RoleButton.setText(_translate("main_window", "人物导入"))
        self.VitsButton.setText(_translate("main_window", "语音合成"))
        self.ScriptButton.setText(_translate("main_window", "脚本编辑"))


class Scene_Menu(QWidget, Ui_Scene):
    def __init__(self):
        super(Scene_Menu, self).__init__()
        # 子窗口初始化时实现子窗口布局
        self.setupUi(self)

        # 设置子窗体最小尺寸
        self.setMinimumWidth(30)
        self.setMinimumHeight(30)


class Role_Menu(QWidget, Ui_Role):
    def __init__(self):
        super(Role_Menu, self).__init__()
        self.setupUi(self)
        self.setMinimumWidth(30)
        self.setMinimumHeight(30)

class Vits_Menu(QWidget, Ui_Vits):
    def __init__(self):
        super(Vits_Menu, self).__init__()
        # 子窗口初始化时实现子窗口布局
        self.setupUi(self)

        # 设置子窗体最小尺寸
        self.setMinimumWidth(30)
        self.setMinimumHeight(30)


class Script_Menu(QWidget, Ui_Script):
    def __init__(self):
        super(Script_Menu, self).__init__()
        self.setupUi(self)
        self.setMinimumWidth(30)
        self.setMinimumHeight(30)

if __name__ == '__main__':
  import sys
  app = QtWidgets.QApplication(sys.argv)
  MainWindow = QtWidgets.QMainWindow()
  ui = Ui_main_window()
  ui.setupUi(MainWindow)
  MainWindow.show()
  sys.exit(app.exec_())