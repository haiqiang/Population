# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_bufferbypercentage.ui'
#
# Created: Fri Mar 07 01:31:47 2014
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_BufferByPercentage(object):
    def setupUi(self, BufferByPercentage):
        BufferByPercentage.setObjectName(_fromUtf8("xxxxx"))
        BufferByPercentage.resize(545, 590)
        self.verticalLayout = QtGui.QVBoxLayout(BufferByPercentage)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.vboxlayout = QtGui.QVBoxLayout()
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.label_1 = QtGui.QLabel(BufferByPercentage)
        self.label_1.setObjectName(_fromUtf8("label_1"))
        self.vboxlayout.addWidget(self.label_1)
        self.inputLayer = QtGui.QComboBox(BufferByPercentage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inputLayer.sizePolicy().hasHeightForWidth())
        self.inputLayer.setSizePolicy(sizePolicy)
        self.inputLayer.setObjectName(_fromUtf8("inputLayer"))
        self.vboxlayout.addWidget(self.inputLayer)
        self.verticalLayout.addLayout(self.vboxlayout)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout.addLayout(self.horizontalLayout)
        self._4 = QtGui.QHBoxLayout()
        self._4.setObjectName(_fromUtf8("_4"))
        self._5 = QtGui.QHBoxLayout()
        self._5.setObjectName(_fromUtf8("_5"))
        self._4.addLayout(self._5)
        self.verticalLayout.addLayout(self._4)
        self._7 = QtGui.QVBoxLayout()
        self._7.setObjectName(_fromUtf8("_7"))
        self.radioPercentageField = QtGui.QRadioButton(BufferByPercentage)
        self.radioPercentageField.setObjectName(_fromUtf8("radioPercentageField"))
        self._7.addWidget(self.radioPercentageField)
        self.widget = QtGui.QWidget(BufferByPercentage)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_3.setContentsMargins(20, 0, -1, -1)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.dropdownPercentageField = QtGui.QComboBox(self.widget)
        self.dropdownPercentageField.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dropdownPercentageField.sizePolicy().hasHeightForWidth())
        self.dropdownPercentageField.setSizePolicy(sizePolicy)
        self.dropdownPercentageField.setObjectName(_fromUtf8("dropdownPercentageField"))
        self.verticalLayout_3.addWidget(self.dropdownPercentageField)
        self._7.addWidget(self.widget)
        self.verticalLayout.addLayout(self._7)
        spacerItem = QtGui.QSpacerItem(20, 194, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.line = QtGui.QFrame(BufferByPercentage)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        self.radioOutputLayer = QtGui.QRadioButton(BufferByPercentage)
        self.radioOutputLayer.setObjectName(_fromUtf8("radioOutputLayer"))
        self.buttonGroup = QtGui.QButtonGroup(BufferByPercentage)
        self.buttonGroup.setObjectName(_fromUtf8("buttonGroup"))
        self.buttonGroup.addButton(self.radioOutputLayer)
        self.verticalLayout.addWidget(self.radioOutputLayer)
        self.outputLayerWidget = QtGui.QWidget(BufferByPercentage)
        self.outputLayerWidget.setEnabled(False)
        self.outputLayerWidget.setObjectName(_fromUtf8("outputLayerWidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.outputLayerWidget)
        self.verticalLayout_2.setContentsMargins(20, 0, -1, -1)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self._3 = QtGui.QHBoxLayout()
        self._3.setMargin(0)
        self._3.setObjectName(_fromUtf8("_3"))
        self.outputLayer = QtGui.QLineEdit(self.outputLayerWidget)
        self.outputLayer.setReadOnly(True)
        self.outputLayer.setObjectName(_fromUtf8("outputLayer"))
        self._3.addWidget(self.outputLayer)
        self.btnBrowse = QtGui.QPushButton(self.outputLayerWidget)
        self.btnBrowse.setObjectName(_fromUtf8("btnBrowse"))
        self._3.addWidget(self.btnBrowse)
        self.verticalLayout_2.addLayout(self._3)
        self.verticalLayout.addWidget(self.outputLayerWidget)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.buttonBox = QtGui.QDialogButtonBox(BufferByPercentage)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.horizontalLayout_2.addWidget(self.buttonBox)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(BufferByPercentage)
        QtCore.QObject.connect(self.radioPercentageField, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.dropdownPercentageField.setEnabled)
        QtCore.QObject.connect(self.radioOutputLayer, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.outputLayerWidget.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(BufferByPercentage)

    def retranslateUi(self, BufferByPercentage):
        BufferByPercentage.setWindowTitle(_translate("BufferByPercentage", "UI Two", None))
        self.label_1.setText(_translate("BufferByPercentage", "Input vector layer", None))
        self.radioPercentageField.setText(_translate("BufferByPercentage", "Attributes of Input layer", None))
        self.radioOutputLayer.setText(_translate("BufferByPercentage", "Output shapefile", None))
        self.btnBrowse.setText(_translate("BufferByPercentage", "Browse", None))

