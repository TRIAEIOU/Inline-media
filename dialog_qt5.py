# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dialog(object):
    def setupUi(self, dialog):
        dialog.setObjectName("dialog")
        dialog.resize(317, 258)
        dialog.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.auto_front = QtWidgets.QCheckBox(dialog)
        self.auto_front.setObjectName("auto_front")
        self.verticalLayout.addWidget(self.auto_front)
        self.auto_back = QtWidgets.QCheckBox(dialog)
        self.auto_back.setObjectName("auto_back")
        self.verticalLayout.addWidget(self.auto_back)
        self.loop = QtWidgets.QCheckBox(dialog)
        self.loop.setObjectName("loop")
        self.verticalLayout.addWidget(self.loop)
        self.mute = QtWidgets.QCheckBox(dialog)
        self.mute.setObjectName("mute")
        self.verticalLayout.addWidget(self.mute)
        self.dimension_grid = QtWidgets.QGridLayout()
        self.dimension_grid.setContentsMargins(-1, 0, -1, -1)
        self.dimension_grid.setObjectName("dimension_grid")
        self.height_lbl = QtWidgets.QLabel(dialog)
        self.height_lbl.setObjectName("height_lbl")
        self.dimension_grid.addWidget(self.height_lbl, 0, 1, 1, 1)
        self.height = QtWidgets.QSpinBox(dialog)
        self.height.setMinimum(-1)
        self.height.setMaximum(4000)
        self.height.setObjectName("height")
        self.dimension_grid.addWidget(self.height, 0, 0, 1, 1)
        self.width = QtWidgets.QSpinBox(dialog)
        self.width.setMinimum(-1)
        self.width.setMaximum(4000)
        self.width.setObjectName("width")
        self.dimension_grid.addWidget(self.width, 1, 0, 1, 1)
        self.width_lbl = QtWidgets.QLabel(dialog)
        self.width_lbl.setObjectName("width_lbl")
        self.dimension_grid.addWidget(self.width_lbl, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.dimension_grid)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_del = QtWidgets.QPushButton(dialog)
        self.btn_del.setAutoDefault(False)
        self.btn_del.setObjectName("btn_del")
        self.horizontalLayout.addWidget(self.btn_del)
        self.btn_ok = QtWidgets.QPushButton(dialog)
        self.btn_ok.setDefault(True)
        self.btn_ok.setObjectName("btn_ok")
        self.horizontalLayout.addWidget(self.btn_ok)
        self.btn_cancel = QtWidgets.QPushButton(dialog)
        self.btn_cancel.setAutoDefault(True)
        self.btn_cancel.setObjectName("btn_cancel")
        self.horizontalLayout.addWidget(self.btn_cancel)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(dialog)
        self.btn_ok.clicked.connect(dialog.accept)
        self.btn_cancel.clicked.connect(dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslateUi(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("dialog", "Media properties"))
        self.auto_front.setText(_translate("dialog", "Autostart on front"))
        self.auto_back.setText(_translate("dialog", "Autostart on back"))
        self.loop.setText(_translate("dialog", "Loop playback"))
        self.mute.setText(_translate("dialog", "Mute audio"))
        self.height_lbl.setText(_translate("dialog", "Height (px, -1 for auto)"))
        self.width_lbl.setText(_translate("dialog", "Width (px, -1 for auto)"))
        self.btn_del.setText(_translate("dialog", "Delete"))
        self.btn_ok.setText(_translate("dialog", "Ok"))
        self.btn_cancel.setText(_translate("dialog", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()
    ui = Ui_dialog()
    ui.setupUi(dialog)
    dialog.show()
    sys.exit(app.exec_())