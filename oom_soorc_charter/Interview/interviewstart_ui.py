# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interviewstart.ui'
#
# Created: Wed Jul 23 14:58:22 2008
#      by: PyQt4 UI code generator 4.3.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_InterviewStart(object):
    def setupUi(self, InterviewStart):
        InterviewStart.setObjectName("InterviewStart")
        InterviewStart.resize(QtCore.QSize(QtCore.QRect(0,0,778,489).size()).expandedTo(InterviewStart.minimumSizeHint()))

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
        font.setPointSize(10)
        self.interviewee.setFont(font)
        self.interviewee.setObjectName("interviewee")

        self.vboxlayout3 = QtGui.QVBoxLayout(self.interviewee)
        self.vboxlayout3.setSpacing(0)
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
        self.gender_text.setObjectName("gender_text")
        self.hboxlayout4.addWidget(self.gender_text)

        self.gender_comboBox = QtGui.QComboBox(self.gender)
        self.gender_comboBox.setMaximumSize(QtCore.QSize(200,16777215))
        self.gender_comboBox.setObjectName("gender_comboBox")
        self.gender_comboBox.addItem("")
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
        self.city_text.setObjectName("city_text")
        self.hboxlayout5.addWidget(self.city_text)

        self.city_line = QtGui.QLineEdit(self.age_2)
        self.city_line.setEnabled(True)
        self.city_line.setMinimumSize(QtCore.QSize(200,0))
        self.city_line.setMaximumSize(QtCore.QSize(200,16777215))
        self.city_line.setObjectName("city_line")
        self.hboxlayout5.addWidget(self.city_line)
        self.vboxlayout3.addWidget(self.age_2)
        self.vboxlayout2.addWidget(self.interviewee)

        self.interviewee_2 = QtGui.QGroupBox(InterviewStart)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.interviewee_2.setFont(font)
        self.interviewee_2.setObjectName("interviewee_2")

        self.vboxlayout4 = QtGui.QVBoxLayout(self.interviewee_2)
        self.vboxlayout4.setSpacing(0)
        self.vboxlayout4.setObjectName("vboxlayout4")

        self.interviewee_first_name_2 = QtGui.QWidget(self.interviewee_2)
        self.interviewee_first_name_2.setObjectName("interviewee_first_name_2")

        self.hboxlayout6 = QtGui.QHBoxLayout(self.interviewee_first_name_2)
        self.hboxlayout6.setSpacing(4)
        self.hboxlayout6.setMargin(4)
        self.hboxlayout6.setObjectName("hboxlayout6")

        self.date_text = QtGui.QLabel(self.interviewee_first_name_2)
        self.date_text.setMinimumSize(QtCore.QSize(180,0))
        self.date_text.setMaximumSize(QtCore.QSize(180,16777215))
        self.date_text.setObjectName("date_text")
        self.hboxlayout6.addWidget(self.date_text)

        self.date_line = QtGui.QLineEdit(self.interviewee_first_name_2)
        self.date_line.setEnabled(True)
        self.date_line.setMinimumSize(QtCore.QSize(150,0))
        self.date_line.setMaximumSize(QtCore.QSize(150,16777215))
        self.date_line.setObjectName("date_line")
        self.hboxlayout6.addWidget(self.date_line)
        self.vboxlayout4.addWidget(self.interviewee_first_name_2)

        self.interviewee_first_name_3 = QtGui.QWidget(self.interviewee_2)
        self.interviewee_first_name_3.setObjectName("interviewee_first_name_3")

        self.hboxlayout7 = QtGui.QHBoxLayout(self.interviewee_first_name_3)
        self.hboxlayout7.setSpacing(4)
        self.hboxlayout7.setMargin(4)
        self.hboxlayout7.setObjectName("hboxlayout7")

        self.interviewer1_first_name_text = QtGui.QLabel(self.interviewee_first_name_3)
        self.interviewer1_first_name_text.setMinimumSize(QtCore.QSize(180,0))
        self.interviewer1_first_name_text.setMaximumSize(QtCore.QSize(180,16777215))
        self.interviewer1_first_name_text.setObjectName("interviewer1_first_name_text")
        self.hboxlayout7.addWidget(self.interviewer1_first_name_text)

        self.interviewer1_first_name_line = QtGui.QLineEdit(self.interviewee_first_name_3)
        self.interviewer1_first_name_line.setEnabled(True)
        self.interviewer1_first_name_line.setMinimumSize(QtCore.QSize(150,0))
        self.interviewer1_first_name_line.setMaximumSize(QtCore.QSize(150,16777215))
        self.interviewer1_first_name_line.setObjectName("interviewer1_first_name_line")
        self.hboxlayout7.addWidget(self.interviewer1_first_name_line)
        self.vboxlayout4.addWidget(self.interviewee_first_name_3)

        self.interviewee_first_name_4 = QtGui.QWidget(self.interviewee_2)
        self.interviewee_first_name_4.setObjectName("interviewee_first_name_4")

        self.hboxlayout8 = QtGui.QHBoxLayout(self.interviewee_first_name_4)
        self.hboxlayout8.setSpacing(4)
        self.hboxlayout8.setMargin(4)
        self.hboxlayout8.setObjectName("hboxlayout8")

        self.interviewer1_last_name_text = QtGui.QLabel(self.interviewee_first_name_4)
        self.interviewer1_last_name_text.setMinimumSize(QtCore.QSize(180,0))
        self.interviewer1_last_name_text.setMaximumSize(QtCore.QSize(180,16777215))
        self.interviewer1_last_name_text.setObjectName("interviewer1_last_name_text")
        self.hboxlayout8.addWidget(self.interviewer1_last_name_text)

        self.interviewer1_last_name_line = QtGui.QLineEdit(self.interviewee_first_name_4)
        self.interviewer1_last_name_line.setEnabled(True)
        self.interviewer1_last_name_line.setMinimumSize(QtCore.QSize(150,0))
        self.interviewer1_last_name_line.setMaximumSize(QtCore.QSize(150,16777215))
        self.interviewer1_last_name_line.setObjectName("interviewer1_last_name_line")
        self.hboxlayout8.addWidget(self.interviewer1_last_name_line)
        self.vboxlayout4.addWidget(self.interviewee_first_name_4)

        self.interviewee_first_name_5 = QtGui.QWidget(self.interviewee_2)
        self.interviewee_first_name_5.setObjectName("interviewee_first_name_5")

        self.hboxlayout9 = QtGui.QHBoxLayout(self.interviewee_first_name_5)
        self.hboxlayout9.setSpacing(4)
        self.hboxlayout9.setMargin(4)
        self.hboxlayout9.setObjectName("hboxlayout9")

        self.mood_text = QtGui.QLabel(self.interviewee_first_name_5)
        self.mood_text.setMinimumSize(QtCore.QSize(180,0))
        self.mood_text.setMaximumSize(QtCore.QSize(180,16777215))
        self.mood_text.setObjectName("mood_text")
        self.hboxlayout9.addWidget(self.mood_text)

        self.mood_line = QtGui.QLineEdit(self.interviewee_first_name_5)
        self.mood_line.setEnabled(True)
        self.mood_line.setMinimumSize(QtCore.QSize(150,0))
        self.mood_line.setMaximumSize(QtCore.QSize(150,16777215))
        self.mood_line.setObjectName("mood_line")
        self.hboxlayout9.addWidget(self.mood_line)
        self.vboxlayout4.addWidget(self.interviewee_first_name_5)
        self.vboxlayout2.addWidget(self.interviewee_2)
        self.vboxlayout1.addLayout(self.vboxlayout2)

        spacerItem = QtGui.QSpacerItem(20,40,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.vboxlayout1.addItem(spacerItem)
        self.hboxlayout.addLayout(self.vboxlayout1)

        self.vessel_info = QtGui.QGroupBox(InterviewStart)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.vessel_info.setFont(font)
        self.vessel_info.setObjectName("vessel_info")

        self.vboxlayout5 = QtGui.QVBoxLayout(self.vessel_info)
        self.vboxlayout5.setSpacing(0)
        self.vboxlayout5.setObjectName("vboxlayout5")

        self.home_port_2 = QtGui.QWidget(self.vessel_info)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.home_port_2.setFont(font)
        self.home_port_2.setObjectName("home_port_2")

        self.hboxlayout10 = QtGui.QHBoxLayout(self.home_port_2)
        self.hboxlayout10.setSpacing(4)
        self.hboxlayout10.setMargin(4)
        self.hboxlayout10.setObjectName("hboxlayout10")

        self.perc_income_text = QtGui.QLabel(self.home_port_2)
        self.perc_income_text.setMinimumSize(QtCore.QSize(150,0))
        self.perc_income_text.setMaximumSize(QtCore.QSize(150,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.perc_income_text.setFont(font)
        self.perc_income_text.setObjectName("perc_income_text")
        self.hboxlayout10.addWidget(self.perc_income_text)

        self.cpfv_income_line = QtGui.QLineEdit(self.home_port_2)
        self.cpfv_income_line.setEnabled(True)
        self.cpfv_income_line.setMinimumSize(QtCore.QSize(100,0))
        self.cpfv_income_line.setMaximumSize(QtCore.QSize(200,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.cpfv_income_line.setFont(font)
        self.cpfv_income_line.setObjectName("cpfv_income_line")
        self.hboxlayout10.addWidget(self.cpfv_income_line)
        self.vboxlayout5.addWidget(self.home_port_2)

        spacerItem1 = QtGui.QSpacerItem(20,40,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.vboxlayout5.addItem(spacerItem1)
        self.hboxlayout.addWidget(self.vessel_info)
        self.vboxlayout.addLayout(self.hboxlayout)

        self.button_box = QtGui.QWidget(InterviewStart)
        self.button_box.setObjectName("button_box")

        self.hboxlayout11 = QtGui.QHBoxLayout(self.button_box)
        self.hboxlayout11.setSpacing(2)
        self.hboxlayout11.setMargin(2)
        self.hboxlayout11.setObjectName("hboxlayout11")

        spacerItem2 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout11.addItem(spacerItem2)

        self.pbnCancel = QtGui.QPushButton(self.button_box)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.pbnCancel.setFont(font)
        self.pbnCancel.setObjectName("pbnCancel")
        self.hboxlayout11.addWidget(self.pbnCancel)

        self.pbnSelectFishery = QtGui.QPushButton(self.button_box)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.pbnSelectFishery.setFont(font)
        self.pbnSelectFishery.setObjectName("pbnSelectFishery")
        self.hboxlayout11.addWidget(self.pbnSelectFishery)
        self.vboxlayout.addWidget(self.button_box)

        self.retranslateUi(InterviewStart)
        QtCore.QMetaObject.connectSlotsByName(InterviewStart)

    def retranslateUi(self, InterviewStart):
        InterviewStart.setWindowTitle(QtGui.QApplication.translate("InterviewStart", "OpenOceanMap - Interview", None, QtGui.QApplication.UnicodeUTF8))
        self.interviewee.setTitle(QtGui.QApplication.translate("InterviewStart", "Interviewee", None, QtGui.QApplication.UnicodeUTF8))
        self.interviewee_first_name_text.setText(QtGui.QApplication.translate("InterviewStart", "First Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.interviewee_last_name_text.setText(QtGui.QApplication.translate("InterviewStart", "Last Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.age_text.setText(QtGui.QApplication.translate("InterviewStart", "Age:", None, QtGui.QApplication.UnicodeUTF8))
        self.gender_text.setText(QtGui.QApplication.translate("InterviewStart", "Gender:", None, QtGui.QApplication.UnicodeUTF8))
        self.gender_comboBox.addItem(QtGui.QApplication.translate("InterviewStart", "Male", None, QtGui.QApplication.UnicodeUTF8))
        self.gender_comboBox.addItem(QtGui.QApplication.translate("InterviewStart", "Female", None, QtGui.QApplication.UnicodeUTF8))
        self.city_text.setText(QtGui.QApplication.translate("InterviewStart", "City of residence:", None, QtGui.QApplication.UnicodeUTF8))
        self.interviewee_2.setTitle(QtGui.QApplication.translate("InterviewStart", "Interviewer", None, QtGui.QApplication.UnicodeUTF8))
        self.date_text.setText(QtGui.QApplication.translate("InterviewStart", "Interview Date (mm/dd/yyyy):", None, QtGui.QApplication.UnicodeUTF8))
        self.interviewer1_first_name_text.setText(QtGui.QApplication.translate("InterviewStart", "First Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.interviewer1_last_name_text.setText(QtGui.QApplication.translate("InterviewStart", "Last Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.mood_text.setText(QtGui.QApplication.translate("InterviewStart", "Interviewer Mood:", None, QtGui.QApplication.UnicodeUTF8))
        self.vessel_info.setTitle(QtGui.QApplication.translate("InterviewStart", "Fishing Information:", None, QtGui.QApplication.UnicodeUTF8))
        self.perc_income_text.setText(QtGui.QApplication.translate("InterviewStart", "% income from CPFV:", None, QtGui.QApplication.UnicodeUTF8))
        self.pbnCancel.setText(QtGui.QApplication.translate("InterviewStart", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.pbnSelectFishery.setText(QtGui.QApplication.translate("InterviewStart", "Select Fishery", None, QtGui.QApplication.UnicodeUTF8))

