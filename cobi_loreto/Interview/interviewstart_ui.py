# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interviewstart.ui'
#
# Created: Thu Jun 26 22:25:02 2008
#      by: PyQt4 UI code generator 4.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_InterviewStart(object):
    def setupUi(self, InterviewStart):
        InterviewStart.setObjectName("InterviewStart")
        InterviewStart.resize(QtCore.QSize(QtCore.QRect(0,0,753,561).size()).expandedTo(InterviewStart.minimumSizeHint()))

        self.vboxlayout = QtGui.QVBoxLayout(InterviewStart)
        self.vboxlayout.setObjectName("vboxlayout")

        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")

        self.vboxlayout1 = QtGui.QVBoxLayout()
        self.vboxlayout1.setObjectName("vboxlayout1")

        self.vboxlayout2 = QtGui.QVBoxLayout()
        self.vboxlayout2.setObjectName("vboxlayout2")

        self.interviewee = QtGui.QGroupBox(InterviewStart)

        font = QtGui.QFont()
        font.setPointSize(11)
        self.interviewee.setFont(font)
        self.interviewee.setObjectName("interviewee")

        self.vboxlayout3 = QtGui.QVBoxLayout(self.interviewee)
        self.vboxlayout3.setObjectName("vboxlayout3")

        self.interviewee_first_name = QtGui.QWidget(self.interviewee)
        self.interviewee_first_name.setObjectName("interviewee_first_name")

        self.hboxlayout1 = QtGui.QHBoxLayout(self.interviewee_first_name)
        self.hboxlayout1.setSpacing(4)
        self.hboxlayout1.setMargin(4)
        self.hboxlayout1.setObjectName("hboxlayout1")

        self.interviewee_first_name_text = QtGui.QLabel(self.interviewee_first_name)
        self.interviewee_first_name_text.setMinimumSize(QtCore.QSize(100,0))
        self.interviewee_first_name_text.setMaximumSize(QtCore.QSize(100,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.interviewee_first_name_text.setFont(font)
        self.interviewee_first_name_text.setObjectName("interviewee_first_name_text")
        self.hboxlayout1.addWidget(self.interviewee_first_name_text)

        self.interviewee_first_name_line = QtGui.QLineEdit(self.interviewee_first_name)
        self.interviewee_first_name_line.setEnabled(True)
        self.interviewee_first_name_line.setMinimumSize(QtCore.QSize(200,0))
        self.interviewee_first_name_line.setMaximumSize(QtCore.QSize(200,16777215))
        self.interviewee_first_name_line.setObjectName("interviewee_first_name_line")
        self.hboxlayout1.addWidget(self.interviewee_first_name_line)
        self.vboxlayout3.addWidget(self.interviewee_first_name)

        self.interviewee_last_name = QtGui.QWidget(self.interviewee)
        self.interviewee_last_name.setObjectName("interviewee_last_name")

        self.hboxlayout2 = QtGui.QHBoxLayout(self.interviewee_last_name)
        self.hboxlayout2.setSpacing(4)
        self.hboxlayout2.setMargin(4)
        self.hboxlayout2.setObjectName("hboxlayout2")

        self.interviewee_last_name_text = QtGui.QLabel(self.interviewee_last_name)
        self.interviewee_last_name_text.setMinimumSize(QtCore.QSize(100,0))
        self.interviewee_last_name_text.setMaximumSize(QtCore.QSize(100,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.interviewee_last_name_text.setFont(font)
        self.interviewee_last_name_text.setObjectName("interviewee_last_name_text")
        self.hboxlayout2.addWidget(self.interviewee_last_name_text)

        self.interviewee_last_name_line = QtGui.QLineEdit(self.interviewee_last_name)
        self.interviewee_last_name_line.setEnabled(True)
        self.interviewee_last_name_line.setMinimumSize(QtCore.QSize(200,0))
        self.interviewee_last_name_line.setMaximumSize(QtCore.QSize(200,16777215))
        self.interviewee_last_name_line.setObjectName("interviewee_last_name_line")
        self.hboxlayout2.addWidget(self.interviewee_last_name_line)
        self.vboxlayout3.addWidget(self.interviewee_last_name)

        self.age = QtGui.QWidget(self.interviewee)
        self.age.setObjectName("age")

        self.hboxlayout3 = QtGui.QHBoxLayout(self.age)
        self.hboxlayout3.setSpacing(4)
        self.hboxlayout3.setMargin(4)
        self.hboxlayout3.setObjectName("hboxlayout3")

        self.age_text = QtGui.QLabel(self.age)
        self.age_text.setMinimumSize(QtCore.QSize(100,0))
        self.age_text.setMaximumSize(QtCore.QSize(100,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.age_text.setFont(font)
        self.age_text.setObjectName("age_text")
        self.hboxlayout3.addWidget(self.age_text)

        self.age_line = QtGui.QLineEdit(self.age)
        self.age_line.setEnabled(True)
        self.age_line.setMinimumSize(QtCore.QSize(200,0))
        self.age_line.setMaximumSize(QtCore.QSize(200,16777215))
        self.age_line.setObjectName("age_line")
        self.hboxlayout3.addWidget(self.age_line)
        self.vboxlayout3.addWidget(self.age)

        self.gender = QtGui.QWidget(self.interviewee)
        self.gender.setObjectName("gender")

        self.hboxlayout4 = QtGui.QHBoxLayout(self.gender)
        self.hboxlayout4.setSpacing(4)
        self.hboxlayout4.setMargin(4)
        self.hboxlayout4.setObjectName("hboxlayout4")

        self.gender_text = QtGui.QLabel(self.gender)
        self.gender_text.setMinimumSize(QtCore.QSize(100,0))
        self.gender_text.setMaximumSize(QtCore.QSize(100,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.gender_text.setFont(font)
        self.gender_text.setObjectName("gender_text")
        self.hboxlayout4.addWidget(self.gender_text)

        self.gender_comboBox = QtGui.QComboBox(self.gender)
        self.gender_comboBox.setMaximumSize(QtCore.QSize(200,16777215))
        self.gender_comboBox.setObjectName("gender_comboBox")
        self.hboxlayout4.addWidget(self.gender_comboBox)
        self.vboxlayout3.addWidget(self.gender)

        self.age_2 = QtGui.QWidget(self.interviewee)
        self.age_2.setObjectName("age_2")

        self.hboxlayout5 = QtGui.QHBoxLayout(self.age_2)
        self.hboxlayout5.setSpacing(4)
        self.hboxlayout5.setMargin(4)
        self.hboxlayout5.setObjectName("hboxlayout5")

        self.city_text = QtGui.QLabel(self.age_2)
        self.city_text.setMinimumSize(QtCore.QSize(100,0))
        self.city_text.setMaximumSize(QtCore.QSize(100,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.city_text.setFont(font)
        self.city_text.setObjectName("city_text")
        self.hboxlayout5.addWidget(self.city_text)

        self.city_line = QtGui.QLineEdit(self.age_2)
        self.city_line.setEnabled(True)
        self.city_line.setMinimumSize(QtCore.QSize(200,0))
        self.city_line.setMaximumSize(QtCore.QSize(200,200))
        self.city_line.setObjectName("city_line")
        self.hboxlayout5.addWidget(self.city_line)
        self.vboxlayout3.addWidget(self.age_2)

        self.home_port_6 = QtGui.QWidget(self.interviewee)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.home_port_6.setFont(font)
        self.home_port_6.setObjectName("home_port_6")

        self.hboxlayout6 = QtGui.QHBoxLayout(self.home_port_6)
        self.hboxlayout6.setObjectName("hboxlayout6")

        self.years_text = QtGui.QLabel(self.home_port_6)
        self.years_text.setMinimumSize(QtCore.QSize(150,0))
        self.years_text.setMaximumSize(QtCore.QSize(250,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.years_text.setFont(font)
        self.years_text.setObjectName("years_text")
        self.hboxlayout6.addWidget(self.years_text)

        self.years_spinBox = QtGui.QSpinBox(self.home_port_6)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.years_spinBox.sizePolicy().hasHeightForWidth())
        self.years_spinBox.setSizePolicy(sizePolicy)
        self.years_spinBox.setMinimumSize(QtCore.QSize(15,0))
        self.years_spinBox.setMaximumSize(QtCore.QSize(200,200))
        self.years_spinBox.setObjectName("years_spinBox")
        self.hboxlayout6.addWidget(self.years_spinBox)
        self.vboxlayout3.addWidget(self.home_port_6)
        self.vboxlayout2.addWidget(self.interviewee)

        self.interviewee_2 = QtGui.QGroupBox(InterviewStart)

        font = QtGui.QFont()
        font.setPointSize(11)
        self.interviewee_2.setFont(font)
        self.interviewee_2.setObjectName("interviewee_2")

        self.gridlayout = QtGui.QGridLayout(self.interviewee_2)
        self.gridlayout.setObjectName("gridlayout")

        self.interviewee_first_name_2 = QtGui.QWidget(self.interviewee_2)
        self.interviewee_first_name_2.setObjectName("interviewee_first_name_2")

        self.hboxlayout7 = QtGui.QHBoxLayout(self.interviewee_first_name_2)
        self.hboxlayout7.setSpacing(4)
        self.hboxlayout7.setMargin(4)
        self.hboxlayout7.setObjectName("hboxlayout7")

        self.date_text = QtGui.QLabel(self.interviewee_first_name_2)
        self.date_text.setMinimumSize(QtCore.QSize(180,0))
        self.date_text.setMaximumSize(QtCore.QSize(180,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.date_text.setFont(font)
        self.date_text.setObjectName("date_text")
        self.hboxlayout7.addWidget(self.date_text)

        self.date_line = QtGui.QLineEdit(self.interviewee_first_name_2)
        self.date_line.setEnabled(True)
        self.date_line.setMinimumSize(QtCore.QSize(150,0))
        self.date_line.setMaximumSize(QtCore.QSize(150,16777215))
        self.date_line.setCursorPosition(0)
        self.date_line.setObjectName("date_line")
        self.hboxlayout7.addWidget(self.date_line)
        self.gridlayout.addWidget(self.interviewee_first_name_2,0,0,1,1)

        self.interviewee_first_name_3 = QtGui.QWidget(self.interviewee_2)
        self.interviewee_first_name_3.setObjectName("interviewee_first_name_3")

        self.hboxlayout8 = QtGui.QHBoxLayout(self.interviewee_first_name_3)
        self.hboxlayout8.setSpacing(4)
        self.hboxlayout8.setMargin(4)
        self.hboxlayout8.setObjectName("hboxlayout8")

        self.interviewer_first_name_text = QtGui.QLabel(self.interviewee_first_name_3)
        self.interviewer_first_name_text.setMinimumSize(QtCore.QSize(180,0))
        self.interviewer_first_name_text.setMaximumSize(QtCore.QSize(180,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.interviewer_first_name_text.setFont(font)
        self.interviewer_first_name_text.setObjectName("interviewer_first_name_text")
        self.hboxlayout8.addWidget(self.interviewer_first_name_text)

        self.interviewer_first_name_line = QtGui.QLineEdit(self.interviewee_first_name_3)
        self.interviewer_first_name_line.setEnabled(True)
        self.interviewer_first_name_line.setMinimumSize(QtCore.QSize(150,0))
        self.interviewer_first_name_line.setMaximumSize(QtCore.QSize(150,16777215))
        self.interviewer_first_name_line.setObjectName("interviewer_first_name_line")
        self.hboxlayout8.addWidget(self.interviewer_first_name_line)
        self.gridlayout.addWidget(self.interviewee_first_name_3,1,0,1,1)

        self.interviewee_first_name_4 = QtGui.QWidget(self.interviewee_2)
        self.interviewee_first_name_4.setObjectName("interviewee_first_name_4")

        self.hboxlayout9 = QtGui.QHBoxLayout(self.interviewee_first_name_4)
        self.hboxlayout9.setSpacing(4)
        self.hboxlayout9.setMargin(4)
        self.hboxlayout9.setObjectName("hboxlayout9")

        self.interviewer_last_name_text = QtGui.QLabel(self.interviewee_first_name_4)
        self.interviewer_last_name_text.setMinimumSize(QtCore.QSize(180,0))
        self.interviewer_last_name_text.setMaximumSize(QtCore.QSize(180,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.interviewer_last_name_text.setFont(font)
        self.interviewer_last_name_text.setObjectName("interviewer_last_name_text")
        self.hboxlayout9.addWidget(self.interviewer_last_name_text)

        self.interviewer_last_name_line = QtGui.QLineEdit(self.interviewee_first_name_4)
        self.interviewer_last_name_line.setEnabled(True)
        self.interviewer_last_name_line.setMinimumSize(QtCore.QSize(150,0))
        self.interviewer_last_name_line.setMaximumSize(QtCore.QSize(150,16777215))
        self.interviewer_last_name_line.setObjectName("interviewer_last_name_line")
        self.hboxlayout9.addWidget(self.interviewer_last_name_line)
        self.gridlayout.addWidget(self.interviewee_first_name_4,2,0,1,1)
        self.vboxlayout2.addWidget(self.interviewee_2)
        self.vboxlayout1.addLayout(self.vboxlayout2)
        self.hboxlayout.addLayout(self.vboxlayout1)

        self.user_group_info = QtGui.QGroupBox(InterviewStart)

        font = QtGui.QFont()
        font.setPointSize(11)
        self.user_group_info.setFont(font)
        self.user_group_info.setObjectName("user_group_info")

        self.gridlayout1 = QtGui.QGridLayout(self.user_group_info)
        self.gridlayout1.setObjectName("gridlayout1")

        self.home_port_2 = QtGui.QWidget(self.user_group_info)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.home_port_2.setFont(font)
        self.home_port_2.setObjectName("home_port_2")

        self.gridlayout2 = QtGui.QGridLayout(self.home_port_2)
        self.gridlayout2.setObjectName("gridlayout2")

        self.comm_fish_text = QtGui.QLabel(self.home_port_2)
        self.comm_fish_text.setMinimumSize(QtCore.QSize(150,0))
        self.comm_fish_text.setMaximumSize(QtCore.QSize(150,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.comm_fish_text.setFont(font)
        self.comm_fish_text.setObjectName("comm_fish_text")
        self.gridlayout2.addWidget(self.comm_fish_text,0,0,1,1)

        self.comm_fish_line = QtGui.QLineEdit(self.home_port_2)
        self.comm_fish_line.setEnabled(True)
        self.comm_fish_line.setMinimumSize(QtCore.QSize(100,0))
        self.comm_fish_line.setMaximumSize(QtCore.QSize(200,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.comm_fish_line.setFont(font)
        self.comm_fish_line.setObjectName("comm_fish_line")
        self.gridlayout2.addWidget(self.comm_fish_line,0,1,1,1)
        self.gridlayout1.addWidget(self.home_port_2,1,0,1,1)

        self.home_port_3 = QtGui.QWidget(self.user_group_info)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.home_port_3.setFont(font)
        self.home_port_3.setObjectName("home_port_3")

        self.gridlayout3 = QtGui.QGridLayout(self.home_port_3)
        self.gridlayout3.setObjectName("gridlayout3")

        self.comm_sport_text = QtGui.QLabel(self.home_port_3)
        self.comm_sport_text.setMinimumSize(QtCore.QSize(150,0))
        self.comm_sport_text.setMaximumSize(QtCore.QSize(150,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.comm_sport_text.setFont(font)
        self.comm_sport_text.setObjectName("comm_sport_text")
        self.gridlayout3.addWidget(self.comm_sport_text,0,0,1,1)

        self.comm_sport_line = QtGui.QLineEdit(self.home_port_3)
        self.comm_sport_line.setEnabled(True)
        self.comm_sport_line.setMinimumSize(QtCore.QSize(100,0))
        self.comm_sport_line.setMaximumSize(QtCore.QSize(200,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.comm_sport_line.setFont(font)
        self.comm_sport_line.setObjectName("comm_sport_line")
        self.gridlayout3.addWidget(self.comm_sport_line,0,1,1,1)
        self.gridlayout1.addWidget(self.home_port_3,2,0,1,1)

        self.ves_license = QtGui.QWidget(self.user_group_info)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.ves_license.setFont(font)
        self.ves_license.setObjectName("ves_license")

        self.hboxlayout10 = QtGui.QHBoxLayout(self.ves_license)
        self.hboxlayout10.setObjectName("hboxlayout10")

        self.private_fish_text = QtGui.QLabel(self.ves_license)
        self.private_fish_text.setMinimumSize(QtCore.QSize(150,0))
        self.private_fish_text.setMaximumSize(QtCore.QSize(150,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.private_fish_text.setFont(font)
        self.private_fish_text.setObjectName("private_fish_text")
        self.hboxlayout10.addWidget(self.private_fish_text)

        self.private_fish_line = QtGui.QLineEdit(self.ves_license)
        self.private_fish_line.setEnabled(True)
        self.private_fish_line.setMinimumSize(QtCore.QSize(100,0))
        self.private_fish_line.setMaximumSize(QtCore.QSize(200,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.private_fish_line.setFont(font)
        self.private_fish_line.setObjectName("private_fish_line")
        self.hboxlayout10.addWidget(self.private_fish_line)
        self.gridlayout1.addWidget(self.ves_license,3,0,1,1)

        self.ves_license_2 = QtGui.QWidget(self.user_group_info)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.ves_license_2.setFont(font)
        self.ves_license_2.setObjectName("ves_license_2")

        self.hboxlayout11 = QtGui.QHBoxLayout(self.ves_license_2)
        self.hboxlayout11.setObjectName("hboxlayout11")

        self.ecotourism_text = QtGui.QLabel(self.ves_license_2)
        self.ecotourism_text.setMinimumSize(QtCore.QSize(150,0))
        self.ecotourism_text.setMaximumSize(QtCore.QSize(150,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.ecotourism_text.setFont(font)
        self.ecotourism_text.setObjectName("ecotourism_text")
        self.hboxlayout11.addWidget(self.ecotourism_text)

        self.ecotourism_line = QtGui.QLineEdit(self.ves_license_2)
        self.ecotourism_line.setEnabled(True)
        self.ecotourism_line.setMinimumSize(QtCore.QSize(100,0))
        self.ecotourism_line.setMaximumSize(QtCore.QSize(200,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.ecotourism_line.setFont(font)
        self.ecotourism_line.setObjectName("ecotourism_line")
        self.hboxlayout11.addWidget(self.ecotourism_line)
        self.gridlayout1.addWidget(self.ves_license_2,4,0,1,1)

        self.vessel_length = QtGui.QWidget(self.user_group_info)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.vessel_length.setFont(font)
        self.vessel_length.setObjectName("vessel_length")

        self.hboxlayout12 = QtGui.QHBoxLayout(self.vessel_length)
        self.hboxlayout12.setObjectName("hboxlayout12")

        self.cons_science_text = QtGui.QLabel(self.vessel_length)
        self.cons_science_text.setMinimumSize(QtCore.QSize(150,0))
        self.cons_science_text.setMaximumSize(QtCore.QSize(200,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.cons_science_text.setFont(font)
        self.cons_science_text.setObjectName("cons_science_text")
        self.hboxlayout12.addWidget(self.cons_science_text)

        self.cons_science_line = QtGui.QLineEdit(self.vessel_length)
        self.cons_science_line.setEnabled(True)
        self.cons_science_line.setMinimumSize(QtCore.QSize(100,0))
        self.cons_science_line.setMaximumSize(QtCore.QSize(200,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.cons_science_line.setFont(font)
        self.cons_science_line.setObjectName("cons_science_line")
        self.hboxlayout12.addWidget(self.cons_science_line)
        self.gridlayout1.addWidget(self.vessel_length,5,0,1,1)

        self.vessel_length_2 = QtGui.QWidget(self.user_group_info)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.vessel_length_2.setFont(font)
        self.vessel_length_2.setObjectName("vessel_length_2")

        self.hboxlayout13 = QtGui.QHBoxLayout(self.vessel_length_2)
        self.hboxlayout13.setObjectName("hboxlayout13")

        self.other_text = QtGui.QLabel(self.vessel_length_2)
        self.other_text.setMinimumSize(QtCore.QSize(150,0))
        self.other_text.setMaximumSize(QtCore.QSize(150,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.other_text.setFont(font)
        self.other_text.setObjectName("other_text")
        self.hboxlayout13.addWidget(self.other_text)

        self.other_line = QtGui.QLineEdit(self.vessel_length_2)
        self.other_line.setEnabled(True)
        self.other_line.setMinimumSize(QtCore.QSize(100,0))
        self.other_line.setMaximumSize(QtCore.QSize(200,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.other_line.setFont(font)
        self.other_line.setObjectName("other_line")
        self.hboxlayout13.addWidget(self.other_line)
        self.gridlayout1.addWidget(self.vessel_length_2,6,0,1,1)

        self.vessel_length_3 = QtGui.QWidget(self.user_group_info)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.vessel_length_3.setFont(font)
        self.vessel_length_3.setObjectName("vessel_length_3")

        self.vboxlayout4 = QtGui.QVBoxLayout(self.vessel_length_3)
        self.vboxlayout4.setObjectName("vboxlayout4")

        self.define_other_text = QtGui.QLabel(self.vessel_length_3)
        self.define_other_text.setMinimumSize(QtCore.QSize(150,0))
        self.define_other_text.setMaximumSize(QtCore.QSize(300,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.define_other_text.setFont(font)
        self.define_other_text.setObjectName("define_other_text")
        self.vboxlayout4.addWidget(self.define_other_text)

        self.define_other_line = QtGui.QLineEdit(self.vessel_length_3)
        self.define_other_line.setEnabled(True)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.define_other_line.sizePolicy().hasHeightForWidth())
        self.define_other_line.setSizePolicy(sizePolicy)
        self.define_other_line.setMinimumSize(QtCore.QSize(200,0))
        self.define_other_line.setMaximumSize(QtCore.QSize(800,200))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.define_other_line.setFont(font)
        self.define_other_line.setObjectName("define_other_line")
        self.vboxlayout4.addWidget(self.define_other_line)
        self.gridlayout1.addWidget(self.vessel_length_3,7,0,1,1)
        self.hboxlayout.addWidget(self.user_group_info)
        self.vboxlayout.addLayout(self.hboxlayout)

        self.button_box = QtGui.QWidget(InterviewStart)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred,QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_box.sizePolicy().hasHeightForWidth())
        self.button_box.setSizePolicy(sizePolicy)
        self.button_box.setMinimumSize(QtCore.QSize(0,50))
        self.button_box.setObjectName("button_box")

        self.hboxlayout14 = QtGui.QHBoxLayout(self.button_box)
        self.hboxlayout14.setContentsMargins(12,7,-1,7)
        self.hboxlayout14.setObjectName("hboxlayout14")

        spacerItem = QtGui.QSpacerItem(693,45,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout14.addItem(spacerItem)

        self.pbnCancel = QtGui.QPushButton(self.button_box)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.pbnCancel.setFont(font)
        self.pbnCancel.setObjectName("pbnCancel")
        self.hboxlayout14.addWidget(self.pbnCancel)

        self.pbnNextWindow = QtGui.QPushButton(self.button_box)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.pbnNextWindow.setFont(font)
        self.pbnNextWindow.setCheckable(False)
        self.pbnNextWindow.setDefault(True)
        self.pbnNextWindow.setFlat(False)
        self.pbnNextWindow.setObjectName("pbnNextWindow")
        self.hboxlayout14.addWidget(self.pbnNextWindow)
        self.vboxlayout.addWidget(self.button_box)

        self.retranslateUi(InterviewStart)
        QtCore.QMetaObject.connectSlotsByName(InterviewStart)

    def retranslateUi(self, InterviewStart):
        InterviewStart.setWindowTitle(QtGui.QApplication.translate("InterviewStart", "OpenOceanMap - Interview", None, QtGui.QApplication.UnicodeUTF8))
        self.interviewee.setTitle(QtGui.QApplication.translate("InterviewStart", "Interviewee", None, QtGui.QApplication.UnicodeUTF8))
        self.interviewee_first_name_text.setText(QtGui.QApplication.translate("InterviewStart", "First Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.interviewee_first_name_line.setText(QtGui.QApplication.translate("InterviewStart", "Dane", None, QtGui.QApplication.UnicodeUTF8))
        self.interviewee_last_name_text.setText(QtGui.QApplication.translate("InterviewStart", "Last Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.age_text.setText(QtGui.QApplication.translate("InterviewStart", "Age:", None, QtGui.QApplication.UnicodeUTF8))
        self.gender_text.setText(QtGui.QApplication.translate("InterviewStart", "Gender:", None, QtGui.QApplication.UnicodeUTF8))
        self.gender_comboBox.addItem(QtGui.QApplication.translate("InterviewStart", "Male", None, QtGui.QApplication.UnicodeUTF8))
        self.gender_comboBox.addItem(QtGui.QApplication.translate("InterviewStart", "Female", None, QtGui.QApplication.UnicodeUTF8))
        self.city_text.setText(QtGui.QApplication.translate("InterviewStart", "City of residence:", None, QtGui.QApplication.UnicodeUTF8))
        self.years_text.setText(QtGui.QApplication.translate("InterviewStart", "Years working in the area:", None, QtGui.QApplication.UnicodeUTF8))
        self.interviewee_2.setTitle(QtGui.QApplication.translate("InterviewStart", "Interviewer", None, QtGui.QApplication.UnicodeUTF8))
        self.date_text.setText(QtGui.QApplication.translate("InterviewStart", "Interview Date (mm/dd/yyyy):", None, QtGui.QApplication.UnicodeUTF8))
        self.date_line.setText(QtGui.QApplication.translate("InterviewStart", "/2008", None, QtGui.QApplication.UnicodeUTF8))
        self.interviewer_first_name_text.setText(QtGui.QApplication.translate("InterviewStart", "First Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.interviewer_last_name_text.setText(QtGui.QApplication.translate("InterviewStart", "Last Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.user_group_info.setTitle(QtGui.QApplication.translate("InterviewStart", "What percentage of your income comes from the following?", None, QtGui.QApplication.UnicodeUTF8))
        self.comm_fish_text.setText(QtGui.QApplication.translate("InterviewStart", "Commercial Fishing:", None, QtGui.QApplication.UnicodeUTF8))
        self.comm_fish_line.setText(QtGui.QApplication.translate("InterviewStart", "10", None, QtGui.QApplication.UnicodeUTF8))
        self.comm_sport_text.setText(QtGui.QApplication.translate("InterviewStart", "Commercial Sport Fishing:", None, QtGui.QApplication.UnicodeUTF8))
        self.comm_sport_line.setText(QtGui.QApplication.translate("InterviewStart", "90", None, QtGui.QApplication.UnicodeUTF8))
        self.private_fish_text.setText(QtGui.QApplication.translate("InterviewStart", "Private Sport Fishing:", None, QtGui.QApplication.UnicodeUTF8))
        self.private_fish_line.setText(QtGui.QApplication.translate("InterviewStart", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.ecotourism_text.setText(QtGui.QApplication.translate("InterviewStart", "Ecotourism:", None, QtGui.QApplication.UnicodeUTF8))
        self.ecotourism_line.setText(QtGui.QApplication.translate("InterviewStart", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.cons_science_text.setText(QtGui.QApplication.translate("InterviewStart", "Conservation/Scientific Research:", None, QtGui.QApplication.UnicodeUTF8))
        self.cons_science_line.setText(QtGui.QApplication.translate("InterviewStart", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.other_text.setText(QtGui.QApplication.translate("InterviewStart", "Other:", None, QtGui.QApplication.UnicodeUTF8))
        self.other_line.setText(QtGui.QApplication.translate("InterviewStart", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.define_other_text.setText(QtGui.QApplication.translate("InterviewStart", "Define type of other Income:", None, QtGui.QApplication.UnicodeUTF8))
        self.pbnCancel.setText(QtGui.QApplication.translate("InterviewStart", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.pbnNextWindow.setText(QtGui.QApplication.translate("InterviewStart", "Next Window", None, QtGui.QApplication.UnicodeUTF8))

