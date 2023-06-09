# Form implementation generated from reading ui file 'EWB Calculator 2.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(476, 500)
        self.lineEdit = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(290, 10, 111, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(290, 40, 111, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(290, 100, 111, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lblFloorArea = QtWidgets.QLabel(parent=Dialog)
        self.lblFloorArea.setGeometry(QtCore.QRect(20, 10, 111, 21))
        self.lblFloorArea.setObjectName("lblFloorArea")
        self.labelWallArea = QtWidgets.QLabel(parent=Dialog)
        self.labelWallArea.setGeometry(QtCore.QRect(20, 40, 111, 16))
        self.labelWallArea.setObjectName("labelWallArea")
        self.labelRoofArea = QtWidgets.QLabel(parent=Dialog)
        self.labelRoofArea.setGeometry(QtCore.QRect(20, 100, 111, 16))
        self.labelRoofArea.setObjectName("labelRoofArea")
        self.lblWindowArea = QtWidgets.QLabel(parent=Dialog)
        self.lblWindowArea.setGeometry(QtCore.QRect(20, 70, 111, 21))
        self.lblWindowArea.setObjectName("lblWindowArea")
        self.lineEdit_4 = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(290, 70, 111, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lblFloorMaterial = QtWidgets.QLabel(parent=Dialog)
        self.lblFloorMaterial.setGeometry(QtCore.QRect(20, 130, 111, 21))
        self.lblFloorMaterial.setObjectName("lblFloorMaterial")
        self.lblWallMaterial = QtWidgets.QLabel(parent=Dialog)
        self.lblWallMaterial.setGeometry(QtCore.QRect(20, 160, 111, 21))
        self.lblWallMaterial.setObjectName("lblWallMaterial")
        self.lbRoofMaterial = QtWidgets.QLabel(parent=Dialog)
        self.lbRoofMaterial.setGeometry(QtCore.QRect(20, 200, 111, 21))
        self.lbRoofMaterial.setObjectName("lbRoofMaterial")
        self.lblFloorThickness = QtWidgets.QLabel(parent=Dialog)
        self.lblFloorThickness.setGeometry(QtCore.QRect(20, 238, 111, 20))
        self.lblFloorThickness.setObjectName("lblFloorThickness")
        self.lblWallThickness = QtWidgets.QLabel(parent=Dialog)
        self.lblWallThickness.setGeometry(QtCore.QRect(20, 270, 111, 21))
        self.lblWallThickness.setObjectName("lblWallThickness")
        self.lblWindowThickness = QtWidgets.QLabel(parent=Dialog)
        self.lblWindowThickness.setGeometry(QtCore.QRect(20, 300, 111, 21))
        self.lblWindowThickness.setObjectName("lblWindowThickness")
        self.lblroofThickness = QtWidgets.QLabel(parent=Dialog)
        self.lblroofThickness.setGeometry(QtCore.QRect(20, 330, 111, 20))
        self.lblroofThickness.setObjectName("lblroofThickness")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(parent=Dialog)
        self.commandLinkButton.setGeometry(QtCore.QRect(10, 360, 251, 31))
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.lblCalculationResult = QtWidgets.QLabel(parent=Dialog)
        self.lblCalculationResult.setGeometry(QtCore.QRect(20, 400, 401, 61))
        self.lblCalculationResult.setObjectName("lblCalculationResult")
        self.lineEdit_9 = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit_9.setGeometry(QtCore.QRect(290, 330, 113, 20))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_10 = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit_10.setGeometry(QtCore.QRect(290, 240, 113, 20))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.comboBox_4 = QtWidgets.QComboBox(parent=Dialog)
        self.comboBox_4.setGeometry(QtCore.QRect(290, 160, 71, 22))
        self.comboBox_4.setObjectName("comboBox_4")
        self.lineEdit_11 = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit_11.setGeometry(QtCore.QRect(290, 300, 113, 20))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.comboBox_5 = QtWidgets.QComboBox(parent=Dialog)
        self.comboBox_5.setGeometry(QtCore.QRect(290, 130, 71, 22))
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_6 = QtWidgets.QComboBox(parent=Dialog)
        self.comboBox_6.setGeometry(QtCore.QRect(290, 200, 71, 22))
        self.comboBox_6.setObjectName("comboBox_6")
        self.lineEdit_12 = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit_12.setGeometry(QtCore.QRect(290, 270, 113, 20))
        self.lineEdit_12.setObjectName("lineEdit_12")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "EWB U-Value Calculator (Mozambique)"))
        self.lineEdit.setText(_translate("Dialog", "Floor Area (m2)"))
        self.lineEdit_2.setText(_translate("Dialog", "Wall Area (m2)"))
        self.lineEdit_3.setText(_translate("Dialog", "Roof Area (m2)"))
        self.lblFloorArea.setText(_translate("Dialog", "Floor Area (m2)"))
        self.labelWallArea.setText(_translate("Dialog", "Wall Area (m2)"))
        self.labelRoofArea.setText(_translate("Dialog", "Roof Area (m2)"))
        self.lblWindowArea.setText(_translate("Dialog", "Window Area (m2)"))
        self.lineEdit_4.setText(_translate("Dialog", "Window Area (m2)"))
        self.lblFloorMaterial.setText(_translate("Dialog", "Floor Material"))
        self.lblWallMaterial.setText(_translate("Dialog", "Wall Material"))
        self.lbRoofMaterial.setText(_translate("Dialog", "Roof Material"))
        self.lblFloorThickness.setText(_translate("Dialog", "Floor Thickness (mm)"))
        self.lblWallThickness.setText(_translate("Dialog", "Wall Thickness (mm)"))
        self.lblWindowThickness.setText(_translate("Dialog", "Window Thickness (mm)"))
        self.lblroofThickness.setText(_translate("Dialog", "Roof Thickness (mm)"))
        self.commandLinkButton.setText(_translate("Dialog", "Calculate Now"))
        self.lblCalculationResult.setText(_translate("Dialog", "Calculation Result"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
