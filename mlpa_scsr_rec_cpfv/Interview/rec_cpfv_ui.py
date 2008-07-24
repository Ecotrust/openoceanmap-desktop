# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rec_cpfv.ui'
#
# Created: Wed Jul 23 15:03:53 2008
#      by: PyQt4 UI code generator 4.3.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_RecCpfv(object):
    def setupUi(self, RecCpfv):
        RecCpfv.setObjectName("RecCpfv")
        RecCpfv.setWindowModality(QtCore.Qt.WindowModal)
        RecCpfv.resize(QtCore.QSize(QtCore.QRect(0,0,805,570).size()).expandedTo(RecCpfv.minimumSizeHint()))

        self.vboxlayout = QtGui.QVBoxLayout(RecCpfv)
        self.vboxlayout.setObjectName("vboxlayout")

        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")

        self.vessel_info = QtGui.QGroupBox(RecCpfv)

        font = QtGui.QFont()
        font.setPointSize(11)
        self.vessel_info.setFont(font)
        self.vessel_info.setObjectName("vessel_info")

        self.vboxlayout1 = QtGui.QVBoxLayout(self.vessel_info)
        self.vboxlayout1.setObjectName("vboxlayout1")

        self.home_port_13 = QtGui.QWidget(self.vessel_info)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.home_port_13.setFont(font)
        self.home_port_13.setObjectName("home_port_13")

        self.hboxlayout1 = QtGui.QHBoxLayout(self.home_port_13)
        self.hboxlayout1.setSpacing(4)
        self.hboxlayout1.setMargin(4)
        self.hboxlayout1.setObjectName("hboxlayout1")

        self.type_of_charter_text_5 = QtGui.QLabel(self.home_port_13)
        self.type_of_charter_text_5.setMinimumSize(QtCore.QSize(200,0))
        self.type_of_charter_text_5.setMaximumSize(QtCore.QSize(200,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.type_of_charter_text_5.setFont(font)
        self.type_of_charter_text_5.setWordWrap(True)
        self.type_of_charter_text_5.setObjectName("type_of_charter_text_5")
        self.hboxlayout1.addWidget(self.type_of_charter_text_5)

        spacerItem = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout1.addItem(spacerItem)

        self.cpfv_type_combo = QtGui.QComboBox(self.home_port_13)
        self.cpfv_type_combo.setObjectName("cpfv_type_combo")
        self.cpfv_type_combo.addItem("")
        self.hboxlayout1.addWidget(self.cpfv_type_combo)
        self.vboxlayout1.addWidget(self.home_port_13)

        self.ves_license_3 = QtGui.QWidget(self.vessel_info)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.ves_license_3.setFont(font)
        self.ves_license_3.setObjectName("ves_license_3")

        self.hboxlayout2 = QtGui.QHBoxLayout(self.ves_license_3)
        self.hboxlayout2.setSpacing(4)
        self.hboxlayout2.setMargin(4)
        self.hboxlayout2.setObjectName("hboxlayout2")

        self.federal_vessel_id_text_2 = QtGui.QLabel(self.ves_license_3)
        self.federal_vessel_id_text_2.setMinimumSize(QtCore.QSize(200,0))
        self.federal_vessel_id_text_2.setMaximumSize(QtCore.QSize(200,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.federal_vessel_id_text_2.setFont(font)
        self.federal_vessel_id_text_2.setWordWrap(True)
        self.federal_vessel_id_text_2.setObjectName("federal_vessel_id_text_2")
        self.hboxlayout2.addWidget(self.federal_vessel_id_text_2)

        spacerItem1 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout2.addItem(spacerItem1)

        self.cpfv_lic_line = QtGui.QLineEdit(self.ves_license_3)
        self.cpfv_lic_line.setEnabled(True)
        self.cpfv_lic_line.setMinimumSize(QtCore.QSize(100,0))
        self.cpfv_lic_line.setMaximumSize(QtCore.QSize(100,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.cpfv_lic_line.setFont(font)
        self.cpfv_lic_line.setObjectName("cpfv_lic_line")
        self.hboxlayout2.addWidget(self.cpfv_lic_line)
        self.vboxlayout1.addWidget(self.ves_license_3)

        self.home_port_6 = QtGui.QWidget(self.vessel_info)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.home_port_6.setFont(font)
        self.home_port_6.setObjectName("home_port_6")

        self.hboxlayout3 = QtGui.QHBoxLayout(self.home_port_6)
        self.hboxlayout3.setSpacing(4)
        self.hboxlayout3.setMargin(4)
        self.hboxlayout3.setObjectName("hboxlayout3")

        self.years_text_2 = QtGui.QLabel(self.home_port_6)
        self.years_text_2.setMinimumSize(QtCore.QSize(200,0))
        self.years_text_2.setMaximumSize(QtCore.QSize(200,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.years_text_2.setFont(font)
        self.years_text_2.setWordWrap(True)
        self.years_text_2.setObjectName("years_text_2")
        self.hboxlayout3.addWidget(self.years_text_2)

        spacerItem2 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout3.addItem(spacerItem2)

        self.cpfv_yr_op_line = QtGui.QLineEdit(self.home_port_6)
        self.cpfv_yr_op_line.setEnabled(True)
        self.cpfv_yr_op_line.setMinimumSize(QtCore.QSize(50,0))
        self.cpfv_yr_op_line.setMaximumSize(QtCore.QSize(50,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.cpfv_yr_op_line.setFont(font)
        self.cpfv_yr_op_line.setObjectName("cpfv_yr_op_line")
        self.hboxlayout3.addWidget(self.cpfv_yr_op_line)
        self.vboxlayout1.addWidget(self.home_port_6)

        self.home_port_10 = QtGui.QWidget(self.vessel_info)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.home_port_10.setFont(font)
        self.home_port_10.setObjectName("home_port_10")

        self.hboxlayout4 = QtGui.QHBoxLayout(self.home_port_10)
        self.hboxlayout4.setSpacing(4)
        self.hboxlayout4.setMargin(4)
        self.hboxlayout4.setObjectName("hboxlayout4")

        self.years_text_3 = QtGui.QLabel(self.home_port_10)
        self.years_text_3.setMinimumSize(QtCore.QSize(200,0))
        self.years_text_3.setMaximumSize(QtCore.QSize(200,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.years_text_3.setFont(font)
        self.years_text_3.setWordWrap(True)
        self.years_text_3.setObjectName("years_text_3")
        self.hboxlayout4.addWidget(self.years_text_3)

        spacerItem3 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout4.addItem(spacerItem3)

        self.cpfv_yr_own_line = QtGui.QLineEdit(self.home_port_10)
        self.cpfv_yr_own_line.setEnabled(True)
        self.cpfv_yr_own_line.setMinimumSize(QtCore.QSize(50,0))
        self.cpfv_yr_own_line.setMaximumSize(QtCore.QSize(50,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.cpfv_yr_own_line.setFont(font)
        self.cpfv_yr_own_line.setObjectName("cpfv_yr_own_line")
        self.hboxlayout4.addWidget(self.cpfv_yr_own_line)
        self.vboxlayout1.addWidget(self.home_port_10)

        self.vessel_length_4 = QtGui.QWidget(self.vessel_info)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.vessel_length_4.setFont(font)
        self.vessel_length_4.setObjectName("vessel_length_4")

        self.hboxlayout5 = QtGui.QHBoxLayout(self.vessel_length_4)
        self.hboxlayout5.setSpacing(4)
        self.hboxlayout5.setMargin(4)
        self.hboxlayout5.setObjectName("hboxlayout5")

        self.vessel_length_text_2 = QtGui.QLabel(self.vessel_length_4)
        self.vessel_length_text_2.setMinimumSize(QtCore.QSize(200,0))
        self.vessel_length_text_2.setMaximumSize(QtCore.QSize(200,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.vessel_length_text_2.setFont(font)
        self.vessel_length_text_2.setWordWrap(True)
        self.vessel_length_text_2.setObjectName("vessel_length_text_2")
        self.hboxlayout5.addWidget(self.vessel_length_text_2)

        spacerItem4 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout5.addItem(spacerItem4)

        self.cpfv_len_line = QtGui.QLineEdit(self.vessel_length_4)
        self.cpfv_len_line.setEnabled(True)
        self.cpfv_len_line.setMinimumSize(QtCore.QSize(50,0))
        self.cpfv_len_line.setMaximumSize(QtCore.QSize(50,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.cpfv_len_line.setFont(font)
        self.cpfv_len_line.setObjectName("cpfv_len_line")
        self.hboxlayout5.addWidget(self.cpfv_len_line)
        self.vboxlayout1.addWidget(self.vessel_length_4)

        self.home_port_17 = QtGui.QWidget(self.vessel_info)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.home_port_17.setFont(font)
        self.home_port_17.setObjectName("home_port_17")

        self.hboxlayout6 = QtGui.QHBoxLayout(self.home_port_17)
        self.hboxlayout6.setSpacing(4)
        self.hboxlayout6.setMargin(4)
        self.hboxlayout6.setObjectName("hboxlayout6")

        self.type_of_charter_text_6 = QtGui.QLabel(self.home_port_17)
        self.type_of_charter_text_6.setMinimumSize(QtCore.QSize(200,0))
        self.type_of_charter_text_6.setMaximumSize(QtCore.QSize(200,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.type_of_charter_text_6.setFont(font)
        self.type_of_charter_text_6.setWordWrap(True)
        self.type_of_charter_text_6.setObjectName("type_of_charter_text_6")
        self.hboxlayout6.addWidget(self.type_of_charter_text_6)

        self.cpfv_trip_length_combo = QtGui.QComboBox(self.home_port_17)
        self.cpfv_trip_length_combo.setObjectName("cpfv_trip_length_combo")
        self.cpfv_trip_length_combo.addItem("")
        self.hboxlayout6.addWidget(self.cpfv_trip_length_combo)
        self.vboxlayout1.addWidget(self.home_port_17)

        self.home_port_12 = QtGui.QWidget(self.vessel_info)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.home_port_12.setFont(font)
        self.home_port_12.setObjectName("home_port_12")

        self.hboxlayout7 = QtGui.QHBoxLayout(self.home_port_12)
        self.hboxlayout7.setSpacing(4)
        self.hboxlayout7.setMargin(4)
        self.hboxlayout7.setObjectName("hboxlayout7")

        self.home_port_text_2 = QtGui.QLabel(self.home_port_12)
        self.home_port_text_2.setMinimumSize(QtCore.QSize(200,0))
        self.home_port_text_2.setMaximumSize(QtCore.QSize(200,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.home_port_text_2.setFont(font)
        self.home_port_text_2.setWordWrap(True)
        self.home_port_text_2.setObjectName("home_port_text_2")
        self.hboxlayout7.addWidget(self.home_port_text_2)

        self.cpfv_home_port_line = QtGui.QLineEdit(self.home_port_12)
        self.cpfv_home_port_line.setEnabled(True)
        self.cpfv_home_port_line.setMinimumSize(QtCore.QSize(200,0))
        self.cpfv_home_port_line.setMaximumSize(QtCore.QSize(220,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.cpfv_home_port_line.setFont(font)
        self.cpfv_home_port_line.setObjectName("cpfv_home_port_line")
        self.hboxlayout7.addWidget(self.cpfv_home_port_line)
        self.vboxlayout1.addWidget(self.home_port_12)

        self.home_port_11 = QtGui.QWidget(self.vessel_info)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.home_port_11.setFont(font)
        self.home_port_11.setObjectName("home_port_11")

        self.hboxlayout8 = QtGui.QHBoxLayout(self.home_port_11)
        self.hboxlayout8.setSpacing(4)
        self.hboxlayout8.setMargin(4)
        self.hboxlayout8.setObjectName("hboxlayout8")

        self.years_text_4 = QtGui.QLabel(self.home_port_11)
        self.years_text_4.setMinimumSize(QtCore.QSize(200,0))
        self.years_text_4.setMaximumSize(QtCore.QSize(200,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.years_text_4.setFont(font)
        self.years_text_4.setWordWrap(True)
        self.years_text_4.setObjectName("years_text_4")
        self.hboxlayout8.addWidget(self.years_text_4)

        spacerItem5 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout8.addItem(spacerItem5)

        self.cpfv_yr_exp_line = QtGui.QLineEdit(self.home_port_11)
        self.cpfv_yr_exp_line.setEnabled(True)
        self.cpfv_yr_exp_line.setMinimumSize(QtCore.QSize(50,0))
        self.cpfv_yr_exp_line.setMaximumSize(QtCore.QSize(50,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.cpfv_yr_exp_line.setFont(font)
        self.cpfv_yr_exp_line.setObjectName("cpfv_yr_exp_line")
        self.hboxlayout8.addWidget(self.cpfv_yr_exp_line)
        self.vboxlayout1.addWidget(self.home_port_11)

        self.home_port_14 = QtGui.QWidget(self.vessel_info)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.home_port_14.setFont(font)
        self.home_port_14.setObjectName("home_port_14")

        self.hboxlayout9 = QtGui.QHBoxLayout(self.home_port_14)
        self.hboxlayout9.setSpacing(4)
        self.hboxlayout9.setMargin(4)
        self.hboxlayout9.setObjectName("hboxlayout9")

        self.landing_port_text_6 = QtGui.QLabel(self.home_port_14)
        self.landing_port_text_6.setMinimumSize(QtCore.QSize(200,0))
        self.landing_port_text_6.setMaximumSize(QtCore.QSize(200,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.landing_port_text_6.setFont(font)
        self.landing_port_text_6.setWordWrap(True)
        self.landing_port_text_6.setObjectName("landing_port_text_6")
        self.hboxlayout9.addWidget(self.landing_port_text_6)

        spacerItem6 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout9.addItem(spacerItem6)

        self.cpfv_num_days_line = QtGui.QLineEdit(self.home_port_14)
        self.cpfv_num_days_line.setEnabled(True)
        self.cpfv_num_days_line.setMinimumSize(QtCore.QSize(50,0))
        self.cpfv_num_days_line.setMaximumSize(QtCore.QSize(50,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.cpfv_num_days_line.setFont(font)
        self.cpfv_num_days_line.setObjectName("cpfv_num_days_line")
        self.hboxlayout9.addWidget(self.cpfv_num_days_line)
        self.vboxlayout1.addWidget(self.home_port_14)

        self.home_port_15 = QtGui.QWidget(self.vessel_info)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.home_port_15.setFont(font)
        self.home_port_15.setObjectName("home_port_15")

        self.hboxlayout10 = QtGui.QHBoxLayout(self.home_port_15)
        self.hboxlayout10.setSpacing(4)
        self.hboxlayout10.setMargin(4)
        self.hboxlayout10.setObjectName("hboxlayout10")

        self.landing_port_text_7 = QtGui.QLabel(self.home_port_15)
        self.landing_port_text_7.setMinimumSize(QtCore.QSize(200,0))
        self.landing_port_text_7.setMaximumSize(QtCore.QSize(200,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.landing_port_text_7.setFont(font)
        self.landing_port_text_7.setWordWrap(True)
        self.landing_port_text_7.setObjectName("landing_port_text_7")
        self.hboxlayout10.addWidget(self.landing_port_text_7)

        spacerItem7 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout10.addItem(spacerItem7)

        self.cpfv_num_clients_line = QtGui.QLineEdit(self.home_port_15)
        self.cpfv_num_clients_line.setEnabled(True)
        self.cpfv_num_clients_line.setMinimumSize(QtCore.QSize(50,0))
        self.cpfv_num_clients_line.setMaximumSize(QtCore.QSize(50,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.cpfv_num_clients_line.setFont(font)
        self.cpfv_num_clients_line.setObjectName("cpfv_num_clients_line")
        self.hboxlayout10.addWidget(self.cpfv_num_clients_line)
        self.vboxlayout1.addWidget(self.home_port_15)

        self.home_port_16 = QtGui.QWidget(self.vessel_info)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.home_port_16.setFont(font)
        self.home_port_16.setObjectName("home_port_16")

        self.hboxlayout11 = QtGui.QHBoxLayout(self.home_port_16)
        self.hboxlayout11.setSpacing(4)
        self.hboxlayout11.setMargin(4)
        self.hboxlayout11.setObjectName("hboxlayout11")

        self.landing_port_text_8 = QtGui.QLabel(self.home_port_16)
        self.landing_port_text_8.setMinimumSize(QtCore.QSize(200,0))
        self.landing_port_text_8.setMaximumSize(QtCore.QSize(200,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.landing_port_text_8.setFont(font)
        self.landing_port_text_8.setWordWrap(True)
        self.landing_port_text_8.setObjectName("landing_port_text_8")
        self.hboxlayout11.addWidget(self.landing_port_text_8)

        spacerItem8 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout11.addItem(spacerItem8)

        self.cpfv_num_crew_line = QtGui.QLineEdit(self.home_port_16)
        self.cpfv_num_crew_line.setEnabled(True)
        self.cpfv_num_crew_line.setMinimumSize(QtCore.QSize(50,0))
        self.cpfv_num_crew_line.setMaximumSize(QtCore.QSize(50,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.cpfv_num_crew_line.setFont(font)
        self.cpfv_num_crew_line.setObjectName("cpfv_num_crew_line")
        self.hboxlayout11.addWidget(self.cpfv_num_crew_line)
        self.vboxlayout1.addWidget(self.home_port_16)
        self.hboxlayout.addWidget(self.vessel_info)

        self.vessel_info_2 = QtGui.QGroupBox(RecCpfv)

        font = QtGui.QFont()
        font.setPointSize(11)
        self.vessel_info_2.setFont(font)
        self.vessel_info_2.setObjectName("vessel_info_2")

        self.vboxlayout2 = QtGui.QVBoxLayout(self.vessel_info_2)
        self.vboxlayout2.setObjectName("vboxlayout2")

        self.home_port_23 = QtGui.QWidget(self.vessel_info_2)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.home_port_23.setFont(font)
        self.home_port_23.setObjectName("home_port_23")

        self.hboxlayout12 = QtGui.QHBoxLayout(self.home_port_23)
        self.hboxlayout12.setSpacing(4)
        self.hboxlayout12.setMargin(4)
        self.hboxlayout12.setObjectName("hboxlayout12")

        self.landing_port_text_9 = QtGui.QLabel(self.home_port_23)
        self.landing_port_text_9.setMinimumSize(QtCore.QSize(200,0))
        self.landing_port_text_9.setMaximumSize(QtCore.QSize(200,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.landing_port_text_9.setFont(font)
        self.landing_port_text_9.setWordWrap(True)
        self.landing_port_text_9.setObjectName("landing_port_text_9")
        self.hboxlayout12.addWidget(self.landing_port_text_9)

        self.cpfv_operating_cost_line = QtGui.QLineEdit(self.home_port_23)
        self.cpfv_operating_cost_line.setEnabled(True)
        self.cpfv_operating_cost_line.setMinimumSize(QtCore.QSize(50,0))
        self.cpfv_operating_cost_line.setMaximumSize(QtCore.QSize(50,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.cpfv_operating_cost_line.setFont(font)
        self.cpfv_operating_cost_line.setObjectName("cpfv_operating_cost_line")
        self.hboxlayout12.addWidget(self.cpfv_operating_cost_line)
        self.vboxlayout2.addWidget(self.home_port_23)

        self.home_port_24 = QtGui.QWidget(self.vessel_info_2)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.home_port_24.setFont(font)
        self.home_port_24.setObjectName("home_port_24")

        self.hboxlayout13 = QtGui.QHBoxLayout(self.home_port_24)
        self.hboxlayout13.setSpacing(4)
        self.hboxlayout13.setMargin(4)
        self.hboxlayout13.setObjectName("hboxlayout13")

        self.landing_port_text_10 = QtGui.QLabel(self.home_port_24)
        self.landing_port_text_10.setMinimumSize(QtCore.QSize(200,0))
        self.landing_port_text_10.setMaximumSize(QtCore.QSize(200,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.landing_port_text_10.setFont(font)
        self.landing_port_text_10.setWordWrap(True)
        self.landing_port_text_10.setObjectName("landing_port_text_10")
        self.hboxlayout13.addWidget(self.landing_port_text_10)

        self.cpfv_labor_cost_line = QtGui.QLineEdit(self.home_port_24)
        self.cpfv_labor_cost_line.setEnabled(True)
        self.cpfv_labor_cost_line.setMinimumSize(QtCore.QSize(50,0))
        self.cpfv_labor_cost_line.setMaximumSize(QtCore.QSize(50,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.cpfv_labor_cost_line.setFont(font)
        self.cpfv_labor_cost_line.setObjectName("cpfv_labor_cost_line")
        self.hboxlayout13.addWidget(self.cpfv_labor_cost_line)
        self.vboxlayout2.addWidget(self.home_port_24)

        self.home_port_25 = QtGui.QWidget(self.vessel_info_2)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.home_port_25.setFont(font)
        self.home_port_25.setObjectName("home_port_25")

        self.hboxlayout14 = QtGui.QHBoxLayout(self.home_port_25)
        self.hboxlayout14.setSpacing(4)
        self.hboxlayout14.setMargin(4)
        self.hboxlayout14.setObjectName("hboxlayout14")

        self.landing_port_text_11 = QtGui.QLabel(self.home_port_25)
        self.landing_port_text_11.setMinimumSize(QtCore.QSize(200,0))
        self.landing_port_text_11.setMaximumSize(QtCore.QSize(200,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.landing_port_text_11.setFont(font)
        self.landing_port_text_11.setWordWrap(True)
        self.landing_port_text_11.setObjectName("landing_port_text_11")
        self.hboxlayout14.addWidget(self.landing_port_text_11)

        self.cpfv_fuel_cost_line = QtGui.QLineEdit(self.home_port_25)
        self.cpfv_fuel_cost_line.setEnabled(True)
        self.cpfv_fuel_cost_line.setMinimumSize(QtCore.QSize(50,0))
        self.cpfv_fuel_cost_line.setMaximumSize(QtCore.QSize(50,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.cpfv_fuel_cost_line.setFont(font)
        self.cpfv_fuel_cost_line.setObjectName("cpfv_fuel_cost_line")
        self.hboxlayout14.addWidget(self.cpfv_fuel_cost_line)
        self.vboxlayout2.addWidget(self.home_port_25)

        spacerItem9 = QtGui.QSpacerItem(20,40,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.vboxlayout2.addItem(spacerItem9)
        self.hboxlayout.addWidget(self.vessel_info_2)
        self.vboxlayout.addLayout(self.hboxlayout)

        self.button_box = QtGui.QWidget(RecCpfv)
        self.button_box.setObjectName("button_box")

        self.hboxlayout15 = QtGui.QHBoxLayout(self.button_box)
        self.hboxlayout15.setSpacing(2)
        self.hboxlayout15.setMargin(2)
        self.hboxlayout15.setObjectName("hboxlayout15")

        spacerItem10 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout15.addItem(spacerItem10)

        self.pbnCancel = QtGui.QPushButton(self.button_box)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.pbnCancel.setFont(font)
        self.pbnCancel.setObjectName("pbnCancel")
        self.hboxlayout15.addWidget(self.pbnCancel)

        self.pbnFinished = QtGui.QPushButton(self.button_box)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.pbnFinished.setFont(font)
        self.pbnFinished.setObjectName("pbnFinished")
        self.hboxlayout15.addWidget(self.pbnFinished)
        self.vboxlayout.addWidget(self.button_box)

        self.retranslateUi(RecCpfv)
        QtCore.QMetaObject.connectSlotsByName(RecCpfv)

    def retranslateUi(self, RecCpfv):
        RecCpfv.setWindowTitle(QtGui.QApplication.translate("RecCpfv", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.vessel_info.setTitle(QtGui.QApplication.translate("RecCpfv", "CPFV Information:", None, QtGui.QApplication.UnicodeUTF8))
        self.type_of_charter_text_5.setText(QtGui.QApplication.translate("RecCpfv", "Type of Charter:", None, QtGui.QApplication.UnicodeUTF8))
        self.cpfv_type_combo.addItem(QtGui.QApplication.translate("RecCpfv", "Open", None, QtGui.QApplication.UnicodeUTF8))
        self.cpfv_type_combo.addItem(QtGui.QApplication.translate("RecCpfv", "Private", None, QtGui.QApplication.UnicodeUTF8))
        self.federal_vessel_id_text_2.setText(QtGui.QApplication.translate("RecCpfv", "Vessel license:", None, QtGui.QApplication.UnicodeUTF8))
        self.years_text_2.setText(QtGui.QApplication.translate("RecCpfv", "Years operating a CPFV boat:", None, QtGui.QApplication.UnicodeUTF8))
        self.years_text_3.setText(QtGui.QApplication.translate("RecCpfv", "Years of ownership of a CPFV boat:", None, QtGui.QApplication.UnicodeUTF8))
        self.vessel_length_text_2.setText(QtGui.QApplication.translate("RecCpfv", "CPFV Vessel length :", None, QtGui.QApplication.UnicodeUTF8))
        self.type_of_charter_text_6.setText(QtGui.QApplication.translate("RecCpfv", "Trip length:", None, QtGui.QApplication.UnicodeUTF8))
        self.cpfv_trip_length_combo.addItem(QtGui.QApplication.translate("RecCpfv", "1/2 day", None, QtGui.QApplication.UnicodeUTF8))
        self.cpfv_trip_length_combo.addItem(QtGui.QApplication.translate("RecCpfv", "3/4 day", None, QtGui.QApplication.UnicodeUTF8))
        self.cpfv_trip_length_combo.addItem(QtGui.QApplication.translate("RecCpfv", "Overnight or longer (2-day/Mexico)", None, QtGui.QApplication.UnicodeUTF8))
        self.home_port_text_2.setText(QtGui.QApplication.translate("RecCpfv", "Home Port:", None, QtGui.QApplication.UnicodeUTF8))
        self.years_text_4.setText(QtGui.QApplication.translate("RecCpfv", "Years experience CPFV fishing:", None, QtGui.QApplication.UnicodeUTF8))
        self.landing_port_text_6.setText(QtGui.QApplication.translate("RecCpfv", "Average # of days CPFV fishing per year:", None, QtGui.QApplication.UnicodeUTF8))
        self.landing_port_text_7.setText(QtGui.QApplication.translate("RecCpfv", "Average number of clients on vessel per trip:", None, QtGui.QApplication.UnicodeUTF8))
        self.landing_port_text_8.setText(QtGui.QApplication.translate("RecCpfv", "# of crew, not including yourself:", None, QtGui.QApplication.UnicodeUTF8))
        self.vessel_info_2.setTitle(QtGui.QApplication.translate("RecCpfv", "CPFV Revenue Information:", None, QtGui.QApplication.UnicodeUTF8))
        self.landing_port_text_9.setText(QtGui.QApplication.translate("RecCpfv", "What percentage of your gross revenue from CPFV goes towards overall operating costs?", None, QtGui.QApplication.UnicodeUTF8))
        self.landing_port_text_10.setText(QtGui.QApplication.translate("RecCpfv", "Of your overall operating costs, what percentage goes towards crew share or labor?", None, QtGui.QApplication.UnicodeUTF8))
        self.landing_port_text_11.setText(QtGui.QApplication.translate("RecCpfv", "Of your overall operating costs, what percentage goes towards fuel?", None, QtGui.QApplication.UnicodeUTF8))
        self.pbnCancel.setText(QtGui.QApplication.translate("RecCpfv", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.pbnFinished.setText(QtGui.QApplication.translate("RecCpfv", "Continue", None, QtGui.QApplication.UnicodeUTF8))

