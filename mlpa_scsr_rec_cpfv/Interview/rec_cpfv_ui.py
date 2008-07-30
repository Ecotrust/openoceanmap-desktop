# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rec_cpfv.ui'
#
# Created: Wed Jul 30 16:28:41 2008
#      by: PyQt4 UI code generator 4.3.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_RecCpfv(object):
    def setupUi(self, RecCpfv):
        RecCpfv.setObjectName("RecCpfv")
        RecCpfv.setWindowModality(QtCore.Qt.WindowModal)
        RecCpfv.resize(QtCore.QSize(QtCore.QRect(0,0,935,629).size()).expandedTo(RecCpfv.minimumSizeHint()))

        self.vboxlayout = QtGui.QVBoxLayout(RecCpfv)
        self.vboxlayout.setObjectName("vboxlayout")

        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")

        self.vboxlayout1 = QtGui.QVBoxLayout()
        self.vboxlayout1.setObjectName("vboxlayout1")

        self.groupBox = QtGui.QGroupBox(RecCpfv)

        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")

        self.vboxlayout2 = QtGui.QVBoxLayout(self.groupBox)
        self.vboxlayout2.setObjectName("vboxlayout2")

        self.ves_license_6 = QtGui.QWidget(self.groupBox)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.ves_license_6.setFont(font)
        self.ves_license_6.setObjectName("ves_license_6")

        self.hboxlayout1 = QtGui.QHBoxLayout(self.ves_license_6)
        self.hboxlayout1.setSpacing(4)
        self.hboxlayout1.setMargin(4)
        self.hboxlayout1.setObjectName("hboxlayout1")

        self.federal_vessel_id_text_5 = QtGui.QLabel(self.ves_license_6)
        self.federal_vessel_id_text_5.setMinimumSize(QtCore.QSize(150,0))
        self.federal_vessel_id_text_5.setMaximumSize(QtCore.QSize(150,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.federal_vessel_id_text_5.setFont(font)
        self.federal_vessel_id_text_5.setWordWrap(True)
        self.federal_vessel_id_text_5.setObjectName("federal_vessel_id_text_5")
        self.hboxlayout1.addWidget(self.federal_vessel_id_text_5)

        spacerItem = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout1.addItem(spacerItem)

        self.cpfv_num_op_line = QtGui.QLineEdit(self.ves_license_6)
        self.cpfv_num_op_line.setEnabled(True)
        self.cpfv_num_op_line.setMinimumSize(QtCore.QSize(50,0))
        self.cpfv_num_op_line.setMaximumSize(QtCore.QSize(50,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.cpfv_num_op_line.setFont(font)
        self.cpfv_num_op_line.setObjectName("cpfv_num_op_line")
        self.hboxlayout1.addWidget(self.cpfv_num_op_line)
        self.vboxlayout2.addWidget(self.ves_license_6)

        self.ves_license_7 = QtGui.QWidget(self.groupBox)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.ves_license_7.setFont(font)
        self.ves_license_7.setObjectName("ves_license_7")

        self.hboxlayout2 = QtGui.QHBoxLayout(self.ves_license_7)
        self.hboxlayout2.setSpacing(4)
        self.hboxlayout2.setMargin(4)
        self.hboxlayout2.setObjectName("hboxlayout2")

        self.federal_vessel_id_text_6 = QtGui.QLabel(self.ves_license_7)
        self.federal_vessel_id_text_6.setMinimumSize(QtCore.QSize(150,0))
        self.federal_vessel_id_text_6.setMaximumSize(QtCore.QSize(150,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.federal_vessel_id_text_6.setFont(font)
        self.federal_vessel_id_text_6.setWordWrap(True)
        self.federal_vessel_id_text_6.setObjectName("federal_vessel_id_text_6")
        self.hboxlayout2.addWidget(self.federal_vessel_id_text_6)

        spacerItem1 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout2.addItem(spacerItem1)

        self.cpfv_yr_op_line = QtGui.QLineEdit(self.ves_license_7)
        self.cpfv_yr_op_line.setEnabled(True)
        self.cpfv_yr_op_line.setMinimumSize(QtCore.QSize(50,0))
        self.cpfv_yr_op_line.setMaximumSize(QtCore.QSize(50,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.cpfv_yr_op_line.setFont(font)
        self.cpfv_yr_op_line.setObjectName("cpfv_yr_op_line")
        self.hboxlayout2.addWidget(self.cpfv_yr_op_line)
        self.vboxlayout2.addWidget(self.ves_license_7)
        self.vboxlayout1.addWidget(self.groupBox)

        self.vessel_info_2 = QtGui.QGroupBox(RecCpfv)

        font = QtGui.QFont()
        font.setPointSize(11)
        self.vessel_info_2.setFont(font)
        self.vessel_info_2.setObjectName("vessel_info_2")

        self.vboxlayout3 = QtGui.QVBoxLayout(self.vessel_info_2)
        self.vboxlayout3.setObjectName("vboxlayout3")

        self.ves_license_4 = QtGui.QWidget(self.vessel_info_2)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.ves_license_4.setFont(font)
        self.ves_license_4.setObjectName("ves_license_4")

        self.hboxlayout3 = QtGui.QHBoxLayout(self.ves_license_4)
        self.hboxlayout3.setSpacing(4)
        self.hboxlayout3.setMargin(4)
        self.hboxlayout3.setObjectName("hboxlayout3")

        self.federal_vessel_id_text_3 = QtGui.QLabel(self.ves_license_4)
        self.federal_vessel_id_text_3.setMinimumSize(QtCore.QSize(150,0))
        self.federal_vessel_id_text_3.setMaximumSize(QtCore.QSize(150,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.federal_vessel_id_text_3.setFont(font)
        self.federal_vessel_id_text_3.setWordWrap(True)
        self.federal_vessel_id_text_3.setObjectName("federal_vessel_id_text_3")
        self.hboxlayout3.addWidget(self.federal_vessel_id_text_3)

        spacerItem2 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout3.addItem(spacerItem2)

        self.cpfv_num_own_line = QtGui.QLineEdit(self.ves_license_4)
        self.cpfv_num_own_line.setEnabled(True)
        self.cpfv_num_own_line.setMinimumSize(QtCore.QSize(50,0))
        self.cpfv_num_own_line.setMaximumSize(QtCore.QSize(50,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.cpfv_num_own_line.setFont(font)
        self.cpfv_num_own_line.setObjectName("cpfv_num_own_line")
        self.hboxlayout3.addWidget(self.cpfv_num_own_line)
        self.vboxlayout3.addWidget(self.ves_license_4)

        self.ves_license_5 = QtGui.QWidget(self.vessel_info_2)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.ves_license_5.setFont(font)
        self.ves_license_5.setObjectName("ves_license_5")

        self.hboxlayout4 = QtGui.QHBoxLayout(self.ves_license_5)
        self.hboxlayout4.setSpacing(4)
        self.hboxlayout4.setMargin(4)
        self.hboxlayout4.setObjectName("hboxlayout4")

        self.federal_vessel_id_text_4 = QtGui.QLabel(self.ves_license_5)
        self.federal_vessel_id_text_4.setMinimumSize(QtCore.QSize(150,0))
        self.federal_vessel_id_text_4.setMaximumSize(QtCore.QSize(150,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.federal_vessel_id_text_4.setFont(font)
        self.federal_vessel_id_text_4.setWordWrap(True)
        self.federal_vessel_id_text_4.setObjectName("federal_vessel_id_text_4")
        self.hboxlayout4.addWidget(self.federal_vessel_id_text_4)

        spacerItem3 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout4.addItem(spacerItem3)

        self.cpfv_yr_own_line = QtGui.QLineEdit(self.ves_license_5)
        self.cpfv_yr_own_line.setEnabled(True)
        self.cpfv_yr_own_line.setMinimumSize(QtCore.QSize(50,0))
        self.cpfv_yr_own_line.setMaximumSize(QtCore.QSize(50,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.cpfv_yr_own_line.setFont(font)
        self.cpfv_yr_own_line.setObjectName("cpfv_yr_own_line")
        self.hboxlayout4.addWidget(self.cpfv_yr_own_line)
        self.vboxlayout3.addWidget(self.ves_license_5)

        self.home_port_23 = QtGui.QWidget(self.vessel_info_2)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.home_port_23.setFont(font)
        self.home_port_23.setObjectName("home_port_23")

        self.hboxlayout5 = QtGui.QHBoxLayout(self.home_port_23)
        self.hboxlayout5.setSpacing(4)
        self.hboxlayout5.setMargin(4)
        self.hboxlayout5.setObjectName("hboxlayout5")

        self.landing_port_text_9 = QtGui.QLabel(self.home_port_23)
        self.landing_port_text_9.setMinimumSize(QtCore.QSize(150,0))
        self.landing_port_text_9.setMaximumSize(QtCore.QSize(150,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.landing_port_text_9.setFont(font)
        self.landing_port_text_9.setWordWrap(True)
        self.landing_port_text_9.setObjectName("landing_port_text_9")
        self.hboxlayout5.addWidget(self.landing_port_text_9)

        spacerItem4 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout5.addItem(spacerItem4)

        self.cpfv_operating_cost_line = QtGui.QLineEdit(self.home_port_23)
        self.cpfv_operating_cost_line.setEnabled(True)
        self.cpfv_operating_cost_line.setMinimumSize(QtCore.QSize(50,0))
        self.cpfv_operating_cost_line.setMaximumSize(QtCore.QSize(50,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.cpfv_operating_cost_line.setFont(font)
        self.cpfv_operating_cost_line.setObjectName("cpfv_operating_cost_line")
        self.hboxlayout5.addWidget(self.cpfv_operating_cost_line)
        self.vboxlayout3.addWidget(self.home_port_23)

        self.home_port_24 = QtGui.QWidget(self.vessel_info_2)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.home_port_24.setFont(font)
        self.home_port_24.setObjectName("home_port_24")

        self.hboxlayout6 = QtGui.QHBoxLayout(self.home_port_24)
        self.hboxlayout6.setSpacing(4)
        self.hboxlayout6.setMargin(4)
        self.hboxlayout6.setObjectName("hboxlayout6")

        self.landing_port_text_10 = QtGui.QLabel(self.home_port_24)
        self.landing_port_text_10.setMinimumSize(QtCore.QSize(150,0))
        self.landing_port_text_10.setMaximumSize(QtCore.QSize(150,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.landing_port_text_10.setFont(font)
        self.landing_port_text_10.setWordWrap(True)
        self.landing_port_text_10.setObjectName("landing_port_text_10")
        self.hboxlayout6.addWidget(self.landing_port_text_10)

        spacerItem5 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout6.addItem(spacerItem5)

        self.cpfv_labor_cost_line = QtGui.QLineEdit(self.home_port_24)
        self.cpfv_labor_cost_line.setEnabled(True)
        self.cpfv_labor_cost_line.setMinimumSize(QtCore.QSize(50,0))
        self.cpfv_labor_cost_line.setMaximumSize(QtCore.QSize(50,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.cpfv_labor_cost_line.setFont(font)
        self.cpfv_labor_cost_line.setObjectName("cpfv_labor_cost_line")
        self.hboxlayout6.addWidget(self.cpfv_labor_cost_line)
        self.vboxlayout3.addWidget(self.home_port_24)

        self.home_port_25 = QtGui.QWidget(self.vessel_info_2)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.home_port_25.setFont(font)
        self.home_port_25.setObjectName("home_port_25")

        self.hboxlayout7 = QtGui.QHBoxLayout(self.home_port_25)
        self.hboxlayout7.setSpacing(4)
        self.hboxlayout7.setMargin(4)
        self.hboxlayout7.setObjectName("hboxlayout7")

        self.landing_port_text_11 = QtGui.QLabel(self.home_port_25)
        self.landing_port_text_11.setMinimumSize(QtCore.QSize(150,0))
        self.landing_port_text_11.setMaximumSize(QtCore.QSize(150,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.landing_port_text_11.setFont(font)
        self.landing_port_text_11.setWordWrap(True)
        self.landing_port_text_11.setObjectName("landing_port_text_11")
        self.hboxlayout7.addWidget(self.landing_port_text_11)

        spacerItem6 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout7.addItem(spacerItem6)

        self.cpfv_fuel_cost_line = QtGui.QLineEdit(self.home_port_25)
        self.cpfv_fuel_cost_line.setEnabled(True)
        self.cpfv_fuel_cost_line.setMinimumSize(QtCore.QSize(50,0))
        self.cpfv_fuel_cost_line.setMaximumSize(QtCore.QSize(50,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.cpfv_fuel_cost_line.setFont(font)
        self.cpfv_fuel_cost_line.setObjectName("cpfv_fuel_cost_line")
        self.hboxlayout7.addWidget(self.cpfv_fuel_cost_line)
        self.vboxlayout3.addWidget(self.home_port_25)

        spacerItem7 = QtGui.QSpacerItem(20,40,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.vboxlayout3.addItem(spacerItem7)
        self.vboxlayout1.addWidget(self.vessel_info_2)
        self.hboxlayout.addLayout(self.vboxlayout1)

        self.vessel_info = QtGui.QGroupBox(RecCpfv)

        font = QtGui.QFont()
        font.setPointSize(11)
        self.vessel_info.setFont(font)
        self.vessel_info.setObjectName("vessel_info")

        self.vboxlayout4 = QtGui.QVBoxLayout(self.vessel_info)
        self.vboxlayout4.setObjectName("vboxlayout4")

        self.home_port_13 = QtGui.QWidget(self.vessel_info)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.home_port_13.setFont(font)
        self.home_port_13.setObjectName("home_port_13")

        self.hboxlayout8 = QtGui.QHBoxLayout(self.home_port_13)
        self.hboxlayout8.setSpacing(4)
        self.hboxlayout8.setMargin(4)
        self.hboxlayout8.setObjectName("hboxlayout8")

        self.type_of_charter_text_5 = QtGui.QLabel(self.home_port_13)
        self.type_of_charter_text_5.setMinimumSize(QtCore.QSize(150,0))
        self.type_of_charter_text_5.setMaximumSize(QtCore.QSize(150,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.type_of_charter_text_5.setFont(font)
        self.type_of_charter_text_5.setWordWrap(True)
        self.type_of_charter_text_5.setObjectName("type_of_charter_text_5")
        self.hboxlayout8.addWidget(self.type_of_charter_text_5)

        spacerItem8 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout8.addItem(spacerItem8)

        self.cpfv_type_combo = QtGui.QComboBox(self.home_port_13)
        self.cpfv_type_combo.setObjectName("cpfv_type_combo")
        self.cpfv_type_combo.addItem("")
        self.hboxlayout8.addWidget(self.cpfv_type_combo)
        self.vboxlayout4.addWidget(self.home_port_13)

        self.ves_license_3 = QtGui.QWidget(self.vessel_info)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.ves_license_3.setFont(font)
        self.ves_license_3.setObjectName("ves_license_3")

        self.hboxlayout9 = QtGui.QHBoxLayout(self.ves_license_3)
        self.hboxlayout9.setSpacing(4)
        self.hboxlayout9.setMargin(4)
        self.hboxlayout9.setObjectName("hboxlayout9")

        self.federal_vessel_id_text_2 = QtGui.QLabel(self.ves_license_3)
        self.federal_vessel_id_text_2.setMinimumSize(QtCore.QSize(150,0))
        self.federal_vessel_id_text_2.setMaximumSize(QtCore.QSize(150,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.federal_vessel_id_text_2.setFont(font)
        self.federal_vessel_id_text_2.setWordWrap(True)
        self.federal_vessel_id_text_2.setObjectName("federal_vessel_id_text_2")
        self.hboxlayout9.addWidget(self.federal_vessel_id_text_2)

        spacerItem9 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout9.addItem(spacerItem9)

        self.cpfv_lic_line = QtGui.QLineEdit(self.ves_license_3)
        self.cpfv_lic_line.setEnabled(True)
        self.cpfv_lic_line.setMinimumSize(QtCore.QSize(100,0))
        self.cpfv_lic_line.setMaximumSize(QtCore.QSize(100,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.cpfv_lic_line.setFont(font)
        self.cpfv_lic_line.setObjectName("cpfv_lic_line")
        self.hboxlayout9.addWidget(self.cpfv_lic_line)
        self.vboxlayout4.addWidget(self.ves_license_3)

        self.vessel_length_5 = QtGui.QWidget(self.vessel_info)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.vessel_length_5.setFont(font)
        self.vessel_length_5.setObjectName("vessel_length_5")

        self.hboxlayout10 = QtGui.QHBoxLayout(self.vessel_length_5)
        self.hboxlayout10.setSpacing(4)
        self.hboxlayout10.setMargin(4)
        self.hboxlayout10.setObjectName("hboxlayout10")

        self.vessel_length_text_3 = QtGui.QLabel(self.vessel_length_5)
        self.vessel_length_text_3.setMinimumSize(QtCore.QSize(150,0))
        self.vessel_length_text_3.setMaximumSize(QtCore.QSize(150,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.vessel_length_text_3.setFont(font)
        self.vessel_length_text_3.setWordWrap(True)
        self.vessel_length_text_3.setObjectName("vessel_length_text_3")
        self.hboxlayout10.addWidget(self.vessel_length_text_3)

        spacerItem10 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout10.addItem(spacerItem10)

        self.cpfv_len_line_2 = QtGui.QLineEdit(self.vessel_length_5)
        self.cpfv_len_line_2.setEnabled(True)
        self.cpfv_len_line_2.setMinimumSize(QtCore.QSize(50,0))
        self.cpfv_len_line_2.setMaximumSize(QtCore.QSize(50,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.cpfv_len_line_2.setFont(font)
        self.cpfv_len_line_2.setObjectName("cpfv_len_line_2")
        self.hboxlayout10.addWidget(self.cpfv_len_line_2)
        self.vboxlayout4.addWidget(self.vessel_length_5)

        self.vessel_length_4 = QtGui.QWidget(self.vessel_info)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.vessel_length_4.setFont(font)
        self.vessel_length_4.setObjectName("vessel_length_4")

        self.hboxlayout11 = QtGui.QHBoxLayout(self.vessel_length_4)
        self.hboxlayout11.setSpacing(4)
        self.hboxlayout11.setMargin(4)
        self.hboxlayout11.setObjectName("hboxlayout11")

        self.vessel_length_text_2 = QtGui.QLabel(self.vessel_length_4)
        self.vessel_length_text_2.setMinimumSize(QtCore.QSize(150,0))
        self.vessel_length_text_2.setMaximumSize(QtCore.QSize(150,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.vessel_length_text_2.setFont(font)
        self.vessel_length_text_2.setWordWrap(True)
        self.vessel_length_text_2.setObjectName("vessel_length_text_2")
        self.hboxlayout11.addWidget(self.vessel_length_text_2)

        spacerItem11 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout11.addItem(spacerItem11)

        self.cpfv_len_line = QtGui.QLineEdit(self.vessel_length_4)
        self.cpfv_len_line.setEnabled(True)
        self.cpfv_len_line.setMinimumSize(QtCore.QSize(50,0))
        self.cpfv_len_line.setMaximumSize(QtCore.QSize(50,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.cpfv_len_line.setFont(font)
        self.cpfv_len_line.setObjectName("cpfv_len_line")
        self.hboxlayout11.addWidget(self.cpfv_len_line)
        self.vboxlayout4.addWidget(self.vessel_length_4)

        self.home_port_17 = QtGui.QWidget(self.vessel_info)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.home_port_17.setFont(font)
        self.home_port_17.setObjectName("home_port_17")

        self.hboxlayout12 = QtGui.QHBoxLayout(self.home_port_17)
        self.hboxlayout12.setSpacing(4)
        self.hboxlayout12.setMargin(4)
        self.hboxlayout12.setObjectName("hboxlayout12")

        self.type_of_charter_text_6 = QtGui.QLabel(self.home_port_17)
        self.type_of_charter_text_6.setMinimumSize(QtCore.QSize(150,0))
        self.type_of_charter_text_6.setMaximumSize(QtCore.QSize(150,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.type_of_charter_text_6.setFont(font)
        self.type_of_charter_text_6.setWordWrap(True)
        self.type_of_charter_text_6.setObjectName("type_of_charter_text_6")
        self.hboxlayout12.addWidget(self.type_of_charter_text_6)

        spacerItem12 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout12.addItem(spacerItem12)

        self.cpfv_trip_length_combo = QtGui.QComboBox(self.home_port_17)
        self.cpfv_trip_length_combo.setMaximumSize(QtCore.QSize(150,16777215))
        self.cpfv_trip_length_combo.setObjectName("cpfv_trip_length_combo")
        self.cpfv_trip_length_combo.addItem("")
        self.hboxlayout12.addWidget(self.cpfv_trip_length_combo)
        self.vboxlayout4.addWidget(self.home_port_17)

        self.home_port_12 = QtGui.QWidget(self.vessel_info)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.home_port_12.setFont(font)
        self.home_port_12.setObjectName("home_port_12")

        self.hboxlayout13 = QtGui.QHBoxLayout(self.home_port_12)
        self.hboxlayout13.setSpacing(4)
        self.hboxlayout13.setMargin(4)
        self.hboxlayout13.setObjectName("hboxlayout13")

        self.home_port_text_2 = QtGui.QLabel(self.home_port_12)
        self.home_port_text_2.setMinimumSize(QtCore.QSize(150,0))
        self.home_port_text_2.setMaximumSize(QtCore.QSize(150,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.home_port_text_2.setFont(font)
        self.home_port_text_2.setWordWrap(True)
        self.home_port_text_2.setObjectName("home_port_text_2")
        self.hboxlayout13.addWidget(self.home_port_text_2)

        spacerItem13 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout13.addItem(spacerItem13)

        self.cpfv_home_port_line = QtGui.QLineEdit(self.home_port_12)
        self.cpfv_home_port_line.setEnabled(True)
        self.cpfv_home_port_line.setMinimumSize(QtCore.QSize(150,0))
        self.cpfv_home_port_line.setMaximumSize(QtCore.QSize(150,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.cpfv_home_port_line.setFont(font)
        self.cpfv_home_port_line.setObjectName("cpfv_home_port_line")
        self.hboxlayout13.addWidget(self.cpfv_home_port_line)
        self.vboxlayout4.addWidget(self.home_port_12)

        self.home_port_11 = QtGui.QWidget(self.vessel_info)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.home_port_11.setFont(font)
        self.home_port_11.setObjectName("home_port_11")

        self.hboxlayout14 = QtGui.QHBoxLayout(self.home_port_11)
        self.hboxlayout14.setSpacing(4)
        self.hboxlayout14.setMargin(4)
        self.hboxlayout14.setObjectName("hboxlayout14")

        self.years_text_4 = QtGui.QLabel(self.home_port_11)
        self.years_text_4.setMinimumSize(QtCore.QSize(200,0))
        self.years_text_4.setMaximumSize(QtCore.QSize(150,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.years_text_4.setFont(font)
        self.years_text_4.setWordWrap(True)
        self.years_text_4.setObjectName("years_text_4")
        self.hboxlayout14.addWidget(self.years_text_4)

        spacerItem14 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout14.addItem(spacerItem14)

        self.cpfv_yr_exp_line = QtGui.QLineEdit(self.home_port_11)
        self.cpfv_yr_exp_line.setEnabled(True)
        self.cpfv_yr_exp_line.setMinimumSize(QtCore.QSize(50,0))
        self.cpfv_yr_exp_line.setMaximumSize(QtCore.QSize(50,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.cpfv_yr_exp_line.setFont(font)
        self.cpfv_yr_exp_line.setObjectName("cpfv_yr_exp_line")
        self.hboxlayout14.addWidget(self.cpfv_yr_exp_line)
        self.vboxlayout4.addWidget(self.home_port_11)

        self.home_port_14 = QtGui.QWidget(self.vessel_info)
        self.home_port_14.setMinimumSize(QtCore.QSize(200,0))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.home_port_14.setFont(font)
        self.home_port_14.setObjectName("home_port_14")

        self.hboxlayout15 = QtGui.QHBoxLayout(self.home_port_14)
        self.hboxlayout15.setSpacing(4)
        self.hboxlayout15.setMargin(4)
        self.hboxlayout15.setObjectName("hboxlayout15")

        self.landing_port_text_6 = QtGui.QLabel(self.home_port_14)
        self.landing_port_text_6.setMinimumSize(QtCore.QSize(200,0))
        self.landing_port_text_6.setMaximumSize(QtCore.QSize(200,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.landing_port_text_6.setFont(font)
        self.landing_port_text_6.setWordWrap(True)
        self.landing_port_text_6.setObjectName("landing_port_text_6")
        self.hboxlayout15.addWidget(self.landing_port_text_6)

        spacerItem15 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout15.addItem(spacerItem15)

        self.cpfv_num_days_line = QtGui.QLineEdit(self.home_port_14)
        self.cpfv_num_days_line.setEnabled(True)
        self.cpfv_num_days_line.setMinimumSize(QtCore.QSize(50,0))
        self.cpfv_num_days_line.setMaximumSize(QtCore.QSize(50,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.cpfv_num_days_line.setFont(font)
        self.cpfv_num_days_line.setObjectName("cpfv_num_days_line")
        self.hboxlayout15.addWidget(self.cpfv_num_days_line)
        self.vboxlayout4.addWidget(self.home_port_14)

        self.home_port_15 = QtGui.QWidget(self.vessel_info)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.home_port_15.setFont(font)
        self.home_port_15.setObjectName("home_port_15")

        self.hboxlayout16 = QtGui.QHBoxLayout(self.home_port_15)
        self.hboxlayout16.setSpacing(4)
        self.hboxlayout16.setMargin(4)
        self.hboxlayout16.setObjectName("hboxlayout16")

        self.landing_port_text_7 = QtGui.QLabel(self.home_port_15)
        self.landing_port_text_7.setMinimumSize(QtCore.QSize(200,0))
        self.landing_port_text_7.setMaximumSize(QtCore.QSize(150,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.landing_port_text_7.setFont(font)
        self.landing_port_text_7.setWordWrap(True)
        self.landing_port_text_7.setObjectName("landing_port_text_7")
        self.hboxlayout16.addWidget(self.landing_port_text_7)

        spacerItem16 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout16.addItem(spacerItem16)

        self.cpfv_num_clients_line = QtGui.QLineEdit(self.home_port_15)
        self.cpfv_num_clients_line.setEnabled(True)
        self.cpfv_num_clients_line.setMinimumSize(QtCore.QSize(50,0))
        self.cpfv_num_clients_line.setMaximumSize(QtCore.QSize(50,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.cpfv_num_clients_line.setFont(font)
        self.cpfv_num_clients_line.setObjectName("cpfv_num_clients_line")
        self.hboxlayout16.addWidget(self.cpfv_num_clients_line)
        self.vboxlayout4.addWidget(self.home_port_15)

        self.home_port_18 = QtGui.QWidget(self.vessel_info)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.home_port_18.setFont(font)
        self.home_port_18.setObjectName("home_port_18")

        self.hboxlayout17 = QtGui.QHBoxLayout(self.home_port_18)
        self.hboxlayout17.setSpacing(4)
        self.hboxlayout17.setMargin(4)
        self.hboxlayout17.setObjectName("hboxlayout17")

        self.landing_port_text_12 = QtGui.QLabel(self.home_port_18)
        self.landing_port_text_12.setMinimumSize(QtCore.QSize(200,0))
        self.landing_port_text_12.setMaximumSize(QtCore.QSize(150,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.landing_port_text_12.setFont(font)
        self.landing_port_text_12.setWordWrap(True)
        self.landing_port_text_12.setObjectName("landing_port_text_12")
        self.hboxlayout17.addWidget(self.landing_port_text_12)

        spacerItem17 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout17.addItem(spacerItem17)

        self.cpfv_num_crew_line_2 = QtGui.QLineEdit(self.home_port_18)
        self.cpfv_num_crew_line_2.setEnabled(True)
        self.cpfv_num_crew_line_2.setMinimumSize(QtCore.QSize(50,0))
        self.cpfv_num_crew_line_2.setMaximumSize(QtCore.QSize(50,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.cpfv_num_crew_line_2.setFont(font)
        self.cpfv_num_crew_line_2.setObjectName("cpfv_num_crew_line_2")
        self.hboxlayout17.addWidget(self.cpfv_num_crew_line_2)
        self.vboxlayout4.addWidget(self.home_port_18)

        self.home_port_16 = QtGui.QWidget(self.vessel_info)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.home_port_16.setFont(font)
        self.home_port_16.setObjectName("home_port_16")

        self.hboxlayout18 = QtGui.QHBoxLayout(self.home_port_16)
        self.hboxlayout18.setSpacing(4)
        self.hboxlayout18.setMargin(4)
        self.hboxlayout18.setObjectName("hboxlayout18")

        self.landing_port_text_8 = QtGui.QLabel(self.home_port_16)
        self.landing_port_text_8.setMinimumSize(QtCore.QSize(200,0))
        self.landing_port_text_8.setMaximumSize(QtCore.QSize(150,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.landing_port_text_8.setFont(font)
        self.landing_port_text_8.setWordWrap(True)
        self.landing_port_text_8.setObjectName("landing_port_text_8")
        self.hboxlayout18.addWidget(self.landing_port_text_8)

        spacerItem18 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout18.addItem(spacerItem18)

        self.cpfv_num_crew_line = QtGui.QLineEdit(self.home_port_16)
        self.cpfv_num_crew_line.setEnabled(True)
        self.cpfv_num_crew_line.setMinimumSize(QtCore.QSize(50,0))
        self.cpfv_num_crew_line.setMaximumSize(QtCore.QSize(50,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.cpfv_num_crew_line.setFont(font)
        self.cpfv_num_crew_line.setObjectName("cpfv_num_crew_line")
        self.hboxlayout18.addWidget(self.cpfv_num_crew_line)
        self.vboxlayout4.addWidget(self.home_port_16)

        spacerItem19 = QtGui.QSpacerItem(20,16,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.vboxlayout4.addItem(spacerItem19)
        self.hboxlayout.addWidget(self.vessel_info)

        self.vboxlayout5 = QtGui.QVBoxLayout()
        self.vboxlayout5.setObjectName("vboxlayout5")

        self.groupBox_2 = QtGui.QGroupBox(RecCpfv)

        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")

        self.vboxlayout6 = QtGui.QVBoxLayout(self.groupBox_2)
        self.vboxlayout6.setObjectName("vboxlayout6")

        self.label = QtGui.QLabel(self.groupBox_2)

        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.vboxlayout6.addWidget(self.label)

        self.hboxlayout19 = QtGui.QHBoxLayout()
        self.hboxlayout19.setObjectName("hboxlayout19")

        spacerItem20 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout19.addItem(spacerItem20)

        self.label_2 = QtGui.QLabel(self.groupBox_2)

        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.hboxlayout19.addWidget(self.label_2)

        self.cpfv_strat_tuna = QtGui.QLineEdit(self.groupBox_2)
        self.cpfv_strat_tuna.setEnabled(True)
        self.cpfv_strat_tuna.setMinimumSize(QtCore.QSize(50,0))
        self.cpfv_strat_tuna.setMaximumSize(QtCore.QSize(50,16777215))

        font = QtGui.QFont()
        font.setPointSize(9)
        self.cpfv_strat_tuna.setFont(font)
        self.cpfv_strat_tuna.setObjectName("cpfv_strat_tuna")
        self.hboxlayout19.addWidget(self.cpfv_strat_tuna)
        self.vboxlayout6.addLayout(self.hboxlayout19)

        self.hboxlayout20 = QtGui.QHBoxLayout()
        self.hboxlayout20.setObjectName("hboxlayout20")

        spacerItem21 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout20.addItem(spacerItem21)

        self.label_3 = QtGui.QLabel(self.groupBox_2)

        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.hboxlayout20.addWidget(self.label_3)

        self.cpfv_strat_coastal = QtGui.QLineEdit(self.groupBox_2)
        self.cpfv_strat_coastal.setEnabled(True)
        self.cpfv_strat_coastal.setMinimumSize(QtCore.QSize(50,0))
        self.cpfv_strat_coastal.setMaximumSize(QtCore.QSize(50,16777215))

        font = QtGui.QFont()
        font.setPointSize(9)
        self.cpfv_strat_coastal.setFont(font)
        self.cpfv_strat_coastal.setObjectName("cpfv_strat_coastal")
        self.hboxlayout20.addWidget(self.cpfv_strat_coastal)
        self.vboxlayout6.addLayout(self.hboxlayout20)

        self.hboxlayout21 = QtGui.QHBoxLayout()
        self.hboxlayout21.setObjectName("hboxlayout21")

        spacerItem22 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout21.addItem(spacerItem22)

        self.label_5 = QtGui.QLabel(self.groupBox_2)

        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.hboxlayout21.addWidget(self.label_5)

        self.cpfv_strat_island = QtGui.QLineEdit(self.groupBox_2)
        self.cpfv_strat_island.setEnabled(True)
        self.cpfv_strat_island.setMinimumSize(QtCore.QSize(50,0))
        self.cpfv_strat_island.setMaximumSize(QtCore.QSize(50,16777215))

        font = QtGui.QFont()
        font.setPointSize(9)
        self.cpfv_strat_island.setFont(font)
        self.cpfv_strat_island.setObjectName("cpfv_strat_island")
        self.hboxlayout21.addWidget(self.cpfv_strat_island)
        self.vboxlayout6.addLayout(self.hboxlayout21)

        self.hboxlayout22 = QtGui.QHBoxLayout()
        self.hboxlayout22.setObjectName("hboxlayout22")

        spacerItem23 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout22.addItem(spacerItem23)

        self.label_4 = QtGui.QLabel(self.groupBox_2)

        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.hboxlayout22.addWidget(self.label_4)

        self.cpfv_strat_rockfish = QtGui.QLineEdit(self.groupBox_2)
        self.cpfv_strat_rockfish.setEnabled(True)
        self.cpfv_strat_rockfish.setMinimumSize(QtCore.QSize(50,0))
        self.cpfv_strat_rockfish.setMaximumSize(QtCore.QSize(50,16777215))

        font = QtGui.QFont()
        font.setPointSize(9)
        self.cpfv_strat_rockfish.setFont(font)
        self.cpfv_strat_rockfish.setObjectName("cpfv_strat_rockfish")
        self.hboxlayout22.addWidget(self.cpfv_strat_rockfish)
        self.vboxlayout6.addLayout(self.hboxlayout22)

        self.hboxlayout23 = QtGui.QHBoxLayout()
        self.hboxlayout23.setObjectName("hboxlayout23")

        spacerItem24 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout23.addItem(spacerItem24)

        self.label_6 = QtGui.QLabel(self.groupBox_2)

        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.hboxlayout23.addWidget(self.label_6)

        self.cpfv_strat_misc = QtGui.QLineEdit(self.groupBox_2)
        self.cpfv_strat_misc.setEnabled(True)
        self.cpfv_strat_misc.setMinimumSize(QtCore.QSize(50,0))
        self.cpfv_strat_misc.setMaximumSize(QtCore.QSize(50,16777215))

        font = QtGui.QFont()
        font.setPointSize(9)
        self.cpfv_strat_misc.setFont(font)
        self.cpfv_strat_misc.setObjectName("cpfv_strat_misc")
        self.hboxlayout23.addWidget(self.cpfv_strat_misc)
        self.vboxlayout6.addLayout(self.hboxlayout23)
        self.vboxlayout5.addWidget(self.groupBox_2)

        self.groupBox_3 = QtGui.QGroupBox(RecCpfv)

        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")

        self.hboxlayout24 = QtGui.QHBoxLayout(self.groupBox_3)
        self.hboxlayout24.setObjectName("hboxlayout24")

        self.vboxlayout7 = QtGui.QVBoxLayout()
        self.vboxlayout7.setObjectName("vboxlayout7")

        self.hboxlayout25 = QtGui.QHBoxLayout()
        self.hboxlayout25.setObjectName("hboxlayout25")

        self.label_7 = QtGui.QLabel(self.groupBox_3)
        self.label_7.setMinimumSize(QtCore.QSize(80,0))
        self.label_7.setMaximumSize(QtCore.QSize(80,16777215))

        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.hboxlayout25.addWidget(self.label_7)

        self.cpfv_target_barracuda = QtGui.QLineEdit(self.groupBox_3)
        self.cpfv_target_barracuda.setEnabled(True)
        self.cpfv_target_barracuda.setMinimumSize(QtCore.QSize(30,0))
        self.cpfv_target_barracuda.setMaximumSize(QtCore.QSize(50,16777215))

        font = QtGui.QFont()
        font.setPointSize(8)
        self.cpfv_target_barracuda.setFont(font)
        self.cpfv_target_barracuda.setObjectName("cpfv_target_barracuda")
        self.hboxlayout25.addWidget(self.cpfv_target_barracuda)
        self.vboxlayout7.addLayout(self.hboxlayout25)

        self.hboxlayout26 = QtGui.QHBoxLayout()
        self.hboxlayout26.setObjectName("hboxlayout26")

        self.label_8 = QtGui.QLabel(self.groupBox_3)
        self.label_8.setMinimumSize(QtCore.QSize(80,0))
        self.label_8.setMaximumSize(QtCore.QSize(80,16777215))

        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.hboxlayout26.addWidget(self.label_8)

        self.cpfv_target_bonito = QtGui.QLineEdit(self.groupBox_3)
        self.cpfv_target_bonito.setEnabled(True)
        self.cpfv_target_bonito.setMinimumSize(QtCore.QSize(30,0))
        self.cpfv_target_bonito.setMaximumSize(QtCore.QSize(50,16777215))

        font = QtGui.QFont()
        font.setPointSize(8)
        self.cpfv_target_bonito.setFont(font)
        self.cpfv_target_bonito.setObjectName("cpfv_target_bonito")
        self.hboxlayout26.addWidget(self.cpfv_target_bonito)
        self.vboxlayout7.addLayout(self.hboxlayout26)

        self.hboxlayout27 = QtGui.QHBoxLayout()
        self.hboxlayout27.setObjectName("hboxlayout27")

        self.label_9 = QtGui.QLabel(self.groupBox_3)
        self.label_9.setMinimumSize(QtCore.QSize(80,0))
        self.label_9.setMaximumSize(QtCore.QSize(80,16777215))

        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.hboxlayout27.addWidget(self.label_9)

        self.cpfv_target_calico = QtGui.QLineEdit(self.groupBox_3)
        self.cpfv_target_calico.setEnabled(True)
        self.cpfv_target_calico.setMinimumSize(QtCore.QSize(30,0))
        self.cpfv_target_calico.setMaximumSize(QtCore.QSize(50,16777215))

        font = QtGui.QFont()
        font.setPointSize(8)
        self.cpfv_target_calico.setFont(font)
        self.cpfv_target_calico.setObjectName("cpfv_target_calico")
        self.hboxlayout27.addWidget(self.cpfv_target_calico)
        self.vboxlayout7.addLayout(self.hboxlayout27)

        self.hboxlayout28 = QtGui.QHBoxLayout()
        self.hboxlayout28.setObjectName("hboxlayout28")

        self.label_10 = QtGui.QLabel(self.groupBox_3)
        self.label_10.setMinimumSize(QtCore.QSize(80,0))
        self.label_10.setMaximumSize(QtCore.QSize(80,16777215))

        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.hboxlayout28.addWidget(self.label_10)

        self.cpfv_target_humboldt = QtGui.QLineEdit(self.groupBox_3)
        self.cpfv_target_humboldt.setEnabled(True)
        self.cpfv_target_humboldt.setMinimumSize(QtCore.QSize(30,0))
        self.cpfv_target_humboldt.setMaximumSize(QtCore.QSize(50,16777215))

        font = QtGui.QFont()
        font.setPointSize(8)
        self.cpfv_target_humboldt.setFont(font)
        self.cpfv_target_humboldt.setObjectName("cpfv_target_humboldt")
        self.hboxlayout28.addWidget(self.cpfv_target_humboldt)
        self.vboxlayout7.addLayout(self.hboxlayout28)

        self.hboxlayout29 = QtGui.QHBoxLayout()
        self.hboxlayout29.setObjectName("hboxlayout29")

        self.label_11 = QtGui.QLabel(self.groupBox_3)
        self.label_11.setMinimumSize(QtCore.QSize(80,0))
        self.label_11.setMaximumSize(QtCore.QSize(80,16777215))

        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.hboxlayout29.addWidget(self.label_11)

        self.cpfv_target_halibut = QtGui.QLineEdit(self.groupBox_3)
        self.cpfv_target_halibut.setEnabled(True)
        self.cpfv_target_halibut.setMinimumSize(QtCore.QSize(30,0))
        self.cpfv_target_halibut.setMaximumSize(QtCore.QSize(50,16777215))

        font = QtGui.QFont()
        font.setPointSize(8)
        self.cpfv_target_halibut.setFont(font)
        self.cpfv_target_halibut.setObjectName("cpfv_target_halibut")
        self.hboxlayout29.addWidget(self.cpfv_target_halibut)
        self.vboxlayout7.addLayout(self.hboxlayout29)

        self.hboxlayout30 = QtGui.QHBoxLayout()
        self.hboxlayout30.setObjectName("hboxlayout30")

        self.label_18 = QtGui.QLabel(self.groupBox_3)
        self.label_18.setMinimumSize(QtCore.QSize(80,0))
        self.label_18.setMaximumSize(QtCore.QSize(80,16777215))

        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.hboxlayout30.addWidget(self.label_18)

        self.cpfv_target_lingcod = QtGui.QLineEdit(self.groupBox_3)
        self.cpfv_target_lingcod.setEnabled(True)
        self.cpfv_target_lingcod.setMinimumSize(QtCore.QSize(30,0))
        self.cpfv_target_lingcod.setMaximumSize(QtCore.QSize(50,16777215))

        font = QtGui.QFont()
        font.setPointSize(8)
        self.cpfv_target_lingcod.setFont(font)
        self.cpfv_target_lingcod.setObjectName("cpfv_target_lingcod")
        self.hboxlayout30.addWidget(self.cpfv_target_lingcod)
        self.vboxlayout7.addLayout(self.hboxlayout30)

        self.hboxlayout31 = QtGui.QHBoxLayout()
        self.hboxlayout31.setObjectName("hboxlayout31")

        self.label_16 = QtGui.QLabel(self.groupBox_3)
        self.label_16.setMinimumSize(QtCore.QSize(80,0))
        self.label_16.setMaximumSize(QtCore.QSize(80,16777215))

        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.hboxlayout31.addWidget(self.label_16)

        self.cpfv_target_dockfish = QtGui.QLineEdit(self.groupBox_3)
        self.cpfv_target_dockfish.setEnabled(True)
        self.cpfv_target_dockfish.setMinimumSize(QtCore.QSize(30,0))
        self.cpfv_target_dockfish.setMaximumSize(QtCore.QSize(50,16777215))

        font = QtGui.QFont()
        font.setPointSize(8)
        self.cpfv_target_dockfish.setFont(font)
        self.cpfv_target_dockfish.setObjectName("cpfv_target_dockfish")
        self.hboxlayout31.addWidget(self.cpfv_target_dockfish)
        self.vboxlayout7.addLayout(self.hboxlayout31)

        self.hboxlayout32 = QtGui.QHBoxLayout()
        self.hboxlayout32.setObjectName("hboxlayout32")

        self.label_17 = QtGui.QLabel(self.groupBox_3)
        self.label_17.setMinimumSize(QtCore.QSize(80,0))
        self.label_17.setMaximumSize(QtCore.QSize(80,16777215))

        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.hboxlayout32.addWidget(self.label_17)

        self.cpfv_target_sand = QtGui.QLineEdit(self.groupBox_3)
        self.cpfv_target_sand.setEnabled(True)
        self.cpfv_target_sand.setMinimumSize(QtCore.QSize(30,0))
        self.cpfv_target_sand.setMaximumSize(QtCore.QSize(50,16777215))

        font = QtGui.QFont()
        font.setPointSize(8)
        self.cpfv_target_sand.setFont(font)
        self.cpfv_target_sand.setObjectName("cpfv_target_sand")
        self.hboxlayout32.addWidget(self.cpfv_target_sand)
        self.vboxlayout7.addLayout(self.hboxlayout32)
        self.hboxlayout24.addLayout(self.vboxlayout7)

        self.vboxlayout8 = QtGui.QVBoxLayout()
        self.vboxlayout8.setObjectName("vboxlayout8")

        self.hboxlayout33 = QtGui.QHBoxLayout()
        self.hboxlayout33.setObjectName("hboxlayout33")

        self.cpfv_strat_sculpin_label = QtGui.QLabel(self.groupBox_3)
        self.cpfv_strat_sculpin_label.setMinimumSize(QtCore.QSize(135,0))
        self.cpfv_strat_sculpin_label.setMaximumSize(QtCore.QSize(135,16777215))

        font = QtGui.QFont()
        font.setPointSize(8)
        self.cpfv_strat_sculpin_label.setFont(font)
        self.cpfv_strat_sculpin_label.setObjectName("cpfv_strat_sculpin_label")
        self.hboxlayout33.addWidget(self.cpfv_strat_sculpin_label)

        self.cpfv_target_sculpin = QtGui.QLineEdit(self.groupBox_3)
        self.cpfv_target_sculpin.setEnabled(True)
        self.cpfv_target_sculpin.setMinimumSize(QtCore.QSize(30,0))
        self.cpfv_target_sculpin.setMaximumSize(QtCore.QSize(50,16777215))

        font = QtGui.QFont()
        font.setPointSize(8)
        self.cpfv_target_sculpin.setFont(font)
        self.cpfv_target_sculpin.setObjectName("cpfv_target_sculpin")
        self.hboxlayout33.addWidget(self.cpfv_target_sculpin)
        self.vboxlayout8.addLayout(self.hboxlayout33)

        self.hboxlayout34 = QtGui.QHBoxLayout()
        self.hboxlayout34.setObjectName("hboxlayout34")

        self.cpfv_strat_white_abel = QtGui.QLabel(self.groupBox_3)
        self.cpfv_strat_white_abel.setMinimumSize(QtCore.QSize(135,0))
        self.cpfv_strat_white_abel.setMaximumSize(QtCore.QSize(135,16777215))

        font = QtGui.QFont()
        font.setPointSize(8)
        self.cpfv_strat_white_abel.setFont(font)
        self.cpfv_strat_white_abel.setObjectName("cpfv_strat_white_abel")
        self.hboxlayout34.addWidget(self.cpfv_strat_white_abel)

        self.cpfv_target_white = QtGui.QLineEdit(self.groupBox_3)
        self.cpfv_target_white.setEnabled(True)
        self.cpfv_target_white.setMinimumSize(QtCore.QSize(30,0))
        self.cpfv_target_white.setMaximumSize(QtCore.QSize(50,16777215))

        font = QtGui.QFont()
        font.setPointSize(8)
        self.cpfv_target_white.setFont(font)
        self.cpfv_target_white.setObjectName("cpfv_target_white")
        self.hboxlayout34.addWidget(self.cpfv_target_white)
        self.vboxlayout8.addLayout(self.hboxlayout34)

        self.hboxlayout35 = QtGui.QHBoxLayout()
        self.hboxlayout35.setObjectName("hboxlayout35")

        self.label_19 = QtGui.QLabel(self.groupBox_3)
        self.label_19.setMinimumSize(QtCore.QSize(135,0))
        self.label_19.setMaximumSize(QtCore.QSize(135,16777215))

        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.hboxlayout35.addWidget(self.label_19)

        self.cpfv_target_yellowtail = QtGui.QLineEdit(self.groupBox_3)
        self.cpfv_target_yellowtail.setEnabled(True)
        self.cpfv_target_yellowtail.setMinimumSize(QtCore.QSize(30,0))
        self.cpfv_target_yellowtail.setMaximumSize(QtCore.QSize(50,16777215))

        font = QtGui.QFont()
        font.setPointSize(8)
        self.cpfv_target_yellowtail.setFont(font)
        self.cpfv_target_yellowtail.setObjectName("cpfv_target_yellowtail")
        self.hboxlayout35.addWidget(self.cpfv_target_yellowtail)
        self.vboxlayout8.addLayout(self.hboxlayout35)

        self.hboxlayout36 = QtGui.QHBoxLayout()
        self.hboxlayout36.setObjectName("hboxlayout36")

        self.label_21 = QtGui.QLabel(self.groupBox_3)
        self.label_21.setMinimumSize(QtCore.QSize(135,0))
        self.label_21.setMaximumSize(QtCore.QSize(135,16777215))

        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.hboxlayout36.addWidget(self.label_21)

        self.cpfv_target_sheephead = QtGui.QLineEdit(self.groupBox_3)
        self.cpfv_target_sheephead.setEnabled(True)
        self.cpfv_target_sheephead.setMinimumSize(QtCore.QSize(30,0))
        self.cpfv_target_sheephead.setMaximumSize(QtCore.QSize(50,16777215))

        font = QtGui.QFont()
        font.setPointSize(8)
        self.cpfv_target_sheephead.setFont(font)
        self.cpfv_target_sheephead.setObjectName("cpfv_target_sheephead")
        self.hboxlayout36.addWidget(self.cpfv_target_sheephead)
        self.vboxlayout8.addLayout(self.hboxlayout36)

        self.hboxlayout37 = QtGui.QHBoxLayout()
        self.hboxlayout37.setObjectName("hboxlayout37")

        self.label_24 = QtGui.QLabel(self.groupBox_3)
        self.label_24.setMinimumSize(QtCore.QSize(135,0))
        self.label_24.setMaximumSize(QtCore.QSize(135,16777215))

        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.hboxlayout37.addWidget(self.label_24)

        self.cpfv_target_shark = QtGui.QLineEdit(self.groupBox_3)
        self.cpfv_target_shark.setEnabled(True)
        self.cpfv_target_shark.setMinimumSize(QtCore.QSize(30,0))
        self.cpfv_target_shark.setMaximumSize(QtCore.QSize(50,16777215))

        font = QtGui.QFont()
        font.setPointSize(8)
        self.cpfv_target_shark.setFont(font)
        self.cpfv_target_shark.setObjectName("cpfv_target_shark")
        self.hboxlayout37.addWidget(self.cpfv_target_shark)
        self.vboxlayout8.addLayout(self.hboxlayout37)

        self.hboxlayout38 = QtGui.QHBoxLayout()
        self.hboxlayout38.setObjectName("hboxlayout38")

        self.label_26 = QtGui.QLabel(self.groupBox_3)
        self.label_26.setMinimumSize(QtCore.QSize(135,0))
        self.label_26.setMaximumSize(QtCore.QSize(135,16777215))

        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.hboxlayout38.addWidget(self.label_26)

        self.cpfv_target_salmon = QtGui.QLineEdit(self.groupBox_3)
        self.cpfv_target_salmon.setEnabled(True)
        self.cpfv_target_salmon.setMinimumSize(QtCore.QSize(30,0))
        self.cpfv_target_salmon.setMaximumSize(QtCore.QSize(50,16777215))

        font = QtGui.QFont()
        font.setPointSize(8)
        self.cpfv_target_salmon.setFont(font)
        self.cpfv_target_salmon.setObjectName("cpfv_target_salmon")
        self.hboxlayout38.addWidget(self.cpfv_target_salmon)
        self.vboxlayout8.addLayout(self.hboxlayout38)

        self.hboxlayout39 = QtGui.QHBoxLayout()
        self.hboxlayout39.setObjectName("hboxlayout39")

        self.label_23 = QtGui.QLabel(self.groupBox_3)
        self.label_23.setMinimumSize(QtCore.QSize(135,0))
        self.label_23.setMaximumSize(QtCore.QSize(135,16777215))

        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.hboxlayout39.addWidget(self.label_23)

        self.cpfv_target_tuna = QtGui.QLineEdit(self.groupBox_3)
        self.cpfv_target_tuna.setEnabled(True)
        self.cpfv_target_tuna.setMinimumSize(QtCore.QSize(30,0))
        self.cpfv_target_tuna.setMaximumSize(QtCore.QSize(50,16777215))

        font = QtGui.QFont()
        font.setPointSize(8)
        self.cpfv_target_tuna.setFont(font)
        self.cpfv_target_tuna.setObjectName("cpfv_target_tuna")
        self.hboxlayout39.addWidget(self.cpfv_target_tuna)
        self.vboxlayout8.addLayout(self.hboxlayout39)

        self.hboxlayout40 = QtGui.QHBoxLayout()
        self.hboxlayout40.setObjectName("hboxlayout40")

        self.label_25 = QtGui.QLabel(self.groupBox_3)
        self.label_25.setMinimumSize(QtCore.QSize(135,0))
        self.label_25.setMaximumSize(QtCore.QSize(135,16777215))

        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.hboxlayout40.addWidget(self.label_25)

        self.cpfv_target_whitefish = QtGui.QLineEdit(self.groupBox_3)
        self.cpfv_target_whitefish.setEnabled(True)
        self.cpfv_target_whitefish.setMinimumSize(QtCore.QSize(30,0))
        self.cpfv_target_whitefish.setMaximumSize(QtCore.QSize(50,16777215))

        font = QtGui.QFont()
        font.setPointSize(8)
        self.cpfv_target_whitefish.setFont(font)
        self.cpfv_target_whitefish.setObjectName("cpfv_target_whitefish")
        self.hboxlayout40.addWidget(self.cpfv_target_whitefish)
        self.vboxlayout8.addLayout(self.hboxlayout40)
        self.hboxlayout24.addLayout(self.vboxlayout8)
        self.vboxlayout5.addWidget(self.groupBox_3)
        self.hboxlayout.addLayout(self.vboxlayout5)
        self.vboxlayout.addLayout(self.hboxlayout)

        self.button_box = QtGui.QWidget(RecCpfv)
        self.button_box.setObjectName("button_box")

        self.hboxlayout41 = QtGui.QHBoxLayout(self.button_box)
        self.hboxlayout41.setSpacing(2)
        self.hboxlayout41.setMargin(2)
        self.hboxlayout41.setObjectName("hboxlayout41")

        spacerItem25 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout41.addItem(spacerItem25)

        self.pbnCancel = QtGui.QPushButton(self.button_box)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.pbnCancel.setFont(font)
        self.pbnCancel.setObjectName("pbnCancel")
        self.hboxlayout41.addWidget(self.pbnCancel)

        self.pbnFinished = QtGui.QPushButton(self.button_box)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.pbnFinished.setFont(font)
        self.pbnFinished.setObjectName("pbnFinished")
        self.hboxlayout41.addWidget(self.pbnFinished)
        self.vboxlayout.addWidget(self.button_box)

        self.retranslateUi(RecCpfv)
        QtCore.QMetaObject.connectSlotsByName(RecCpfv)

    def retranslateUi(self, RecCpfv):
        RecCpfv.setWindowTitle(QtGui.QApplication.translate("RecCpfv", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("RecCpfv", "If a CPFV Operator:", None, QtGui.QApplication.UnicodeUTF8))
        self.federal_vessel_id_text_5.setText(QtGui.QApplication.translate("RecCpfv", "How many CPFVs do you operate?", None, QtGui.QApplication.UnicodeUTF8))
        self.federal_vessel_id_text_6.setText(QtGui.QApplication.translate("RecCpfv", "Years operating CPFVs?", None, QtGui.QApplication.UnicodeUTF8))
        self.vessel_info_2.setTitle(QtGui.QApplication.translate("RecCpfv", "If a CPFV Owner:", None, QtGui.QApplication.UnicodeUTF8))
        self.federal_vessel_id_text_3.setText(QtGui.QApplication.translate("RecCpfv", "How many CPFVs do you own?", None, QtGui.QApplication.UnicodeUTF8))
        self.federal_vessel_id_text_4.setText(QtGui.QApplication.translate("RecCpfv", "Years owning CPFVs?", None, QtGui.QApplication.UnicodeUTF8))
        self.landing_port_text_9.setText(QtGui.QApplication.translate("RecCpfv", "What percentage of your gross revenue from CPFV goes towards overall operating costs?", None, QtGui.QApplication.UnicodeUTF8))
        self.landing_port_text_10.setText(QtGui.QApplication.translate("RecCpfv", "Of your overall operating costs, what percentage goes towards crew share or labor?", None, QtGui.QApplication.UnicodeUTF8))
        self.landing_port_text_11.setText(QtGui.QApplication.translate("RecCpfv", "Of your overall operating costs, what percentage goes towards fuel?", None, QtGui.QApplication.UnicodeUTF8))
        self.vessel_info.setTitle(QtGui.QApplication.translate("RecCpfv", "CFPV Owner or Operator:", None, QtGui.QApplication.UnicodeUTF8))
        self.type_of_charter_text_5.setText(QtGui.QApplication.translate("RecCpfv", "Type of trip:", None, QtGui.QApplication.UnicodeUTF8))
        self.cpfv_type_combo.addItem(QtGui.QApplication.translate("RecCpfv", "Open Party", None, QtGui.QApplication.UnicodeUTF8))
        self.cpfv_type_combo.addItem(QtGui.QApplication.translate("RecCpfv", "Charter", None, QtGui.QApplication.UnicodeUTF8))
        self.federal_vessel_id_text_2.setText(QtGui.QApplication.translate("RecCpfv", "Vessel document number:", None, QtGui.QApplication.UnicodeUTF8))
        self.vessel_length_text_3.setText(QtGui.QApplication.translate("RecCpfv", "Vessel Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.vessel_length_text_2.setText(QtGui.QApplication.translate("RecCpfv", "Vessel Length :", None, QtGui.QApplication.UnicodeUTF8))
        self.type_of_charter_text_6.setText(QtGui.QApplication.translate("RecCpfv", "Trip length:", None, QtGui.QApplication.UnicodeUTF8))
        self.cpfv_trip_length_combo.addItem(QtGui.QApplication.translate("RecCpfv", "1/2 day", None, QtGui.QApplication.UnicodeUTF8))
        self.cpfv_trip_length_combo.addItem(QtGui.QApplication.translate("RecCpfv", "3/4 day", None, QtGui.QApplication.UnicodeUTF8))
        self.cpfv_trip_length_combo.addItem(QtGui.QApplication.translate("RecCpfv", "All Day", None, QtGui.QApplication.UnicodeUTF8))
        self.cpfv_trip_length_combo.addItem(QtGui.QApplication.translate("RecCpfv", "Overnight or multi-day", None, QtGui.QApplication.UnicodeUTF8))
        self.home_port_text_2.setText(QtGui.QApplication.translate("RecCpfv", "Homeport of boat:", None, QtGui.QApplication.UnicodeUTF8))
        self.years_text_4.setText(QtGui.QApplication.translate("RecCpfv", "Years sportfishing (in addition or including years owning/operating):", None, QtGui.QApplication.UnicodeUTF8))
        self.landing_port_text_6.setText(QtGui.QApplication.translate("RecCpfv", "Average # of days CPFV fishing per year:", None, QtGui.QApplication.UnicodeUTF8))
        self.landing_port_text_7.setText(QtGui.QApplication.translate("RecCpfv", "Average number of passengers on boat per trip:", None, QtGui.QApplication.UnicodeUTF8))
        self.landing_port_text_12.setText(QtGui.QApplication.translate("RecCpfv", "Percentage of passengers from out of state:", None, QtGui.QApplication.UnicodeUTF8))
        self.landing_port_text_8.setText(QtGui.QApplication.translate("RecCpfv", "Number of crew, not counting owner/operator:", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("RecCpfv", "Fishing Strategies:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("RecCpfv", "Assuming there are five (5) major fishing strategies, what percentage of your trips are associated with each strategy?", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("RecCpfv", "Offshore Tuna", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("RecCpfv", "Coastal Freelance", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("RecCpfv", "Island Freelance", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("RecCpfv", "Rockfish", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("RecCpfv", "Misc.", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("RecCpfv", "Targeted Species:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("RecCpfv", "Barracuda:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("RecCpfv", "Bonito", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("RecCpfv", "Calico Bass", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("RecCpfv", "Humboldt Squid", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("RecCpfv", "Halibut", None, QtGui.QApplication.UnicodeUTF8))
        self.label_18.setText(QtGui.QApplication.translate("RecCpfv", "Lingcod", None, QtGui.QApplication.UnicodeUTF8))
        self.label_16.setText(QtGui.QApplication.translate("RecCpfv", "Dockfish", None, QtGui.QApplication.UnicodeUTF8))
        self.label_17.setText(QtGui.QApplication.translate("RecCpfv", "Sand Bass", None, QtGui.QApplication.UnicodeUTF8))
        self.cpfv_strat_sculpin_label.setText(QtGui.QApplication.translate("RecCpfv", "Sculpin (Cal. Scorpion Fish)", None, QtGui.QApplication.UnicodeUTF8))
        self.cpfv_strat_white_abel.setText(QtGui.QApplication.translate("RecCpfv", "White Seabass", None, QtGui.QApplication.UnicodeUTF8))
        self.label_19.setText(QtGui.QApplication.translate("RecCpfv", "Yellowtail", None, QtGui.QApplication.UnicodeUTF8))
        self.label_21.setText(QtGui.QApplication.translate("RecCpfv", "Sheephead", None, QtGui.QApplication.UnicodeUTF8))
        self.label_24.setText(QtGui.QApplication.translate("RecCpfv", "Thresher/Mako/Blue Shark", None, QtGui.QApplication.UnicodeUTF8))
        self.label_26.setText(QtGui.QApplication.translate("RecCpfv", "Salmon", None, QtGui.QApplication.UnicodeUTF8))
        self.label_23.setText(QtGui.QApplication.translate("RecCpfv", "Tuna & Dorado", None, QtGui.QApplication.UnicodeUTF8))
        self.label_25.setText(QtGui.QApplication.translate("RecCpfv", "Whitefish", None, QtGui.QApplication.UnicodeUTF8))
        self.pbnCancel.setText(QtGui.QApplication.translate("RecCpfv", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.pbnFinished.setText(QtGui.QApplication.translate("RecCpfv", "Continue", None, QtGui.QApplication.UnicodeUTF8))

