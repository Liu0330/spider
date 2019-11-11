# -*- coding: utf-8 -*-

# Date:2018-12-12
#
# Created by: DaddyHu_CN
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.NonModal)
        Form.setEnabled(True)
        Form.resize(436, 336)
        Form.setMinimumSize(QtCore.QSize(436, 336))
        Form.setMaximumSize(QtCore.QSize(436, 336))
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 421, 250))
        self.groupBox.setObjectName("groupBox")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.weatherComboBox = QtWidgets.QComboBox(self.groupBox)
        self.weatherComboBox.setObjectName("weatherComboBox")
        self.weatherComboBox.addItem("")
        self.weatherComboBox.addItem("")
        self.weatherComboBox.addItem("")
        self.weatherComboBox.addItem("")
        self.weatherComboBox.addItem("")
        self.weatherComboBox.addItem("")
        self.weatherComboBox.addItem("")
        self.weatherComboBox.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.weatherComboBox)
        self.resultText = QtWidgets.QTextEdit(self.groupBox)
        self.resultText.setEnabled(True)
        self.resultText.setReadOnly(True)
        self.resultText.setObjectName("resultText")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.resultText)
        self.queryBtn = QtWidgets.QPushButton(Form)
        self.queryBtn.setGeometry(QtCore.QRect(70, 280, 101, 31))
        self.queryBtn.setObjectName("queryBtn")
        self.clearBtn = QtWidgets.QPushButton(Form)
        self.clearBtn.setEnabled(True)
        self.clearBtn.setGeometry(QtCore.QRect(260, 280, 101, 31))
        self.clearBtn.setObjectName("clearBtn")
        self.queryBtn.raise_()
        self.groupBox.raise_()
        self.clearBtn.raise_()

        self.retranslateUi(Form)
        self.queryBtn.clicked.connect(Form.queryWeather)
        self.clearBtn.clicked.connect(Form.clearResult)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "天气快速查询"))
        self.groupBox.setTitle(_translate("Form", "查询城市天气"))
        self.label.setText(_translate("Form", "  城市"))
        self.weatherComboBox.setItemText(0, _translate("Form", "北京"))
        self.weatherComboBox.setItemText(1, _translate("Form", "石家庄"))
        self.weatherComboBox.setItemText(2, _translate("Form", "上海"))
        self.weatherComboBox.setItemText(7, _translate("Form", "天津"))
        self.weatherComboBox.setItemText(3, _translate("Form", "重庆"))
        self.weatherComboBox.setItemText(4, _translate("Form", "郑州"))
        self.weatherComboBox.setItemText(5, _translate("Form", "长沙"))
        self.weatherComboBox.setItemText(6, _translate("Form", "乌鲁木齐"))
        self.queryBtn.setText(_translate("Form", "查询"))
        self.clearBtn.setText(_translate("Form", "清空"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())