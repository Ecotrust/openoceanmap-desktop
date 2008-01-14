# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interviewstart.ui'
#
# Created: Thu Nov 29 19:21:34 2007
#      by: PyQt4 UI code generator 4.3.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_InterviewStart(object):
    def setupUi(self, InterviewStart):
        InterviewStart.setObjectName("InterviewStart")
        InterviewStart.resize(QtCore.QSize(QtCore.QRect(0,0,864,625).size()).expandedTo(InterviewStart.minimumSizeHint()))

        self.gridlayout = QtGui.QGridLayout(InterviewStart)
        self.gridlayout.setMargin(9)
        self.gridlayout.setSpacing(6)
        self.gridlayout.setObjectName("gridlayout")

        self.trip_info = QtGui.QGroupBox(InterviewStart)
        self.trip_info.setObjectName("trip_info")

        self.vboxlayout = QtGui.QVBoxLayout(self.trip_info)
        self.vboxlayout.setMargin(9)
        self.vboxlayout.setSpacing(6)
        self.vboxlayout.setObjectName("vboxlayout")

        self.region = QtGui.QWidget(self.trip_info)
        self.region.setObjectName("region")

        self.hboxlayout = QtGui.QHBoxLayout(self.region)
        self.hboxlayout.setMargin(4)
        self.hboxlayout.setSpacing(4)
        self.hboxlayout.setObjectName("hboxlayout")

        self.region_text = QtGui.QLabel(self.region)
        self.region_text.setObjectName("region_text")
        self.hboxlayout.addWidget(self.region_text)

        self.region_comboBox = QtGui.QComboBox(self.region)
        self.region_comboBox.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContentsOnFirstShow)
        self.region_comboBox.setObjectName("region_comboBox")
        self.hboxlayout.addWidget(self.region_comboBox)
        self.vboxlayout.addWidget(self.region)

        self.ind_per_trip = QtGui.QWidget(self.trip_info)
        self.ind_per_trip.setObjectName("ind_per_trip")

        self.hboxlayout1 = QtGui.QHBoxLayout(self.ind_per_trip)
        self.hboxlayout1.setMargin(4)
        self.hboxlayout1.setSpacing(4)
        self.hboxlayout1.setObjectName("hboxlayout1")

        self.ind_per_trip_text = QtGui.QLabel(self.ind_per_trip)
        self.ind_per_trip_text.setObjectName("ind_per_trip_text")
        self.hboxlayout1.addWidget(self.ind_per_trip_text)

        self.ind_per_trip_line = QtGui.QLineEdit(self.ind_per_trip)
        self.ind_per_trip_line.setEnabled(True)
        self.ind_per_trip_line.setMinimumSize(QtCore.QSize(200,0))
        self.ind_per_trip_line.setObjectName("ind_per_trip_line")
        self.hboxlayout1.addWidget(self.ind_per_trip_line)
        self.vboxlayout.addWidget(self.ind_per_trip)

        self.days_per_year = QtGui.QWidget(self.trip_info)
        self.days_per_year.setObjectName("days_per_year")

        self.hboxlayout2 = QtGui.QHBoxLayout(self.days_per_year)
        self.hboxlayout2.setMargin(4)
        self.hboxlayout2.setSpacing(4)
        self.hboxlayout2.setObjectName("hboxlayout2")

        self.days_per_year_text = QtGui.QLabel(self.days_per_year)
        self.days_per_year_text.setObjectName("days_per_year_text")
        self.hboxlayout2.addWidget(self.days_per_year_text)

        self.days_per_year_line = QtGui.QLineEdit(self.days_per_year)
        self.days_per_year_line.setEnabled(True)
        self.days_per_year_line.setMinimumSize(QtCore.QSize(200,0))
        self.days_per_year_line.setObjectName("days_per_year_line")
        self.hboxlayout2.addWidget(self.days_per_year_line)
        self.vboxlayout.addWidget(self.days_per_year)

        self.travel_time = QtGui.QWidget(self.trip_info)
        self.travel_time.setObjectName("travel_time")

        self.hboxlayout3 = QtGui.QHBoxLayout(self.travel_time)
        self.hboxlayout3.setMargin(4)
        self.hboxlayout3.setSpacing(4)
        self.hboxlayout3.setObjectName("hboxlayout3")

        self.travel_time_text = QtGui.QLabel(self.travel_time)
        self.travel_time_text.setObjectName("travel_time_text")
        self.hboxlayout3.addWidget(self.travel_time_text)

        self.travel_time_line = QtGui.QLineEdit(self.travel_time)
        self.travel_time_line.setEnabled(True)
        self.travel_time_line.setMinimumSize(QtCore.QSize(200,0))
        self.travel_time_line.setObjectName("travel_time_line")
        self.hboxlayout3.addWidget(self.travel_time_line)
        self.vboxlayout.addWidget(self.travel_time)

        self.travel_distance = QtGui.QWidget(self.trip_info)
        self.travel_distance.setObjectName("travel_distance")

        self.hboxlayout4 = QtGui.QHBoxLayout(self.travel_distance)
        self.hboxlayout4.setMargin(4)
        self.hboxlayout4.setSpacing(4)
        self.hboxlayout4.setObjectName("hboxlayout4")

        self.travel_distance_text = QtGui.QLabel(self.travel_distance)
        self.travel_distance_text.setObjectName("travel_distance_text")
        self.hboxlayout4.addWidget(self.travel_distance_text)

        self.travel_distance_line = QtGui.QLineEdit(self.travel_distance)
        self.travel_distance_line.setEnabled(True)
        self.travel_distance_line.setMinimumSize(QtCore.QSize(200,0))
        self.travel_distance_line.setObjectName("travel_distance_line")
        self.hboxlayout4.addWidget(self.travel_distance_line)
        self.vboxlayout.addWidget(self.travel_distance)
        self.gridlayout.addWidget(self.trip_info,1,1,1,1)

        self.vessel_info = QtGui.QGroupBox(InterviewStart)
        self.vessel_info.setObjectName("vessel_info")

        self.vboxlayout1 = QtGui.QVBoxLayout(self.vessel_info)
        self.vboxlayout1.setMargin(9)
        self.vboxlayout1.setSpacing(6)
        self.vboxlayout1.setObjectName("vboxlayout1")

        self.ves_license = QtGui.QWidget(self.vessel_info)
        self.ves_license.setObjectName("ves_license")

        self.hboxlayout5 = QtGui.QHBoxLayout(self.ves_license)
        self.hboxlayout5.setMargin(4)
        self.hboxlayout5.setSpacing(4)
        self.hboxlayout5.setObjectName("hboxlayout5")

        self.ves_license_text = QtGui.QLabel(self.ves_license)
        self.ves_license_text.setObjectName("ves_license_text")
        self.hboxlayout5.addWidget(self.ves_license_text)

        self.ves_license_line = QtGui.QLineEdit(self.ves_license)
        self.ves_license_line.setEnabled(True)
        self.ves_license_line.setMinimumSize(QtCore.QSize(200,0))
        self.ves_license_line.setObjectName("ves_license_line")
        self.hboxlayout5.addWidget(self.ves_license_line)
        self.vboxlayout1.addWidget(self.ves_license)

        self.years_op = QtGui.QWidget(self.vessel_info)
        self.years_op.setObjectName("years_op")

        self.hboxlayout6 = QtGui.QHBoxLayout(self.years_op)
        self.hboxlayout6.setMargin(4)
        self.hboxlayout6.setSpacing(4)
        self.hboxlayout6.setObjectName("hboxlayout6")

        self.years_op_text = QtGui.QLabel(self.years_op)
        self.years_op_text.setObjectName("years_op_text")
        self.hboxlayout6.addWidget(self.years_op_text)

        self.years_op_line = QtGui.QLineEdit(self.years_op)
        self.years_op_line.setEnabled(True)
        self.years_op_line.setMinimumSize(QtCore.QSize(200,0))
        self.years_op_line.setObjectName("years_op_line")
        self.hboxlayout6.addWidget(self.years_op_line)
        self.vboxlayout1.addWidget(self.years_op)

        self.years_own = QtGui.QWidget(self.vessel_info)
        self.years_own.setObjectName("years_own")

        self.hboxlayout7 = QtGui.QHBoxLayout(self.years_own)
        self.hboxlayout7.setMargin(4)
        self.hboxlayout7.setSpacing(4)
        self.hboxlayout7.setObjectName("hboxlayout7")

        self.years_own_text = QtGui.QLabel(self.years_own)
        self.years_own_text.setObjectName("years_own_text")
        self.hboxlayout7.addWidget(self.years_own_text)

        self.years_own_line = QtGui.QLineEdit(self.years_own)
        self.years_own_line.setEnabled(True)
        self.years_own_line.setMinimumSize(QtCore.QSize(200,0))
        self.years_own_line.setObjectName("years_own_line")
        self.hboxlayout7.addWidget(self.years_own_line)
        self.vboxlayout1.addWidget(self.years_own)

        self.vessel_length = QtGui.QWidget(self.vessel_info)
        self.vessel_length.setObjectName("vessel_length")

        self.hboxlayout8 = QtGui.QHBoxLayout(self.vessel_length)
        self.hboxlayout8.setMargin(4)
        self.hboxlayout8.setSpacing(4)
        self.hboxlayout8.setObjectName("hboxlayout8")

        self.vessel_length_text = QtGui.QLabel(self.vessel_length)
        self.vessel_length_text.setObjectName("vessel_length_text")
        self.hboxlayout8.addWidget(self.vessel_length_text)

        self.vessel_length_line = QtGui.QLineEdit(self.vessel_length)
        self.vessel_length_line.setEnabled(True)
        self.vessel_length_line.setMinimumSize(QtCore.QSize(200,0))
        self.vessel_length_line.setObjectName("vessel_length_line")
        self.hboxlayout8.addWidget(self.vessel_length_line)
        self.vboxlayout1.addWidget(self.vessel_length)

        self.home_port = QtGui.QWidget(self.vessel_info)
        self.home_port.setObjectName("home_port")

        self.hboxlayout9 = QtGui.QHBoxLayout(self.home_port)
        self.hboxlayout9.setMargin(4)
        self.hboxlayout9.setSpacing(4)
        self.hboxlayout9.setObjectName("hboxlayout9")

        self.home_port_text = QtGui.QLabel(self.home_port)
        self.home_port_text.setObjectName("home_port_text")
        self.hboxlayout9.addWidget(self.home_port_text)

        self.home_port_line = QtGui.QLineEdit(self.home_port)
        self.home_port_line.setEnabled(True)
        self.home_port_line.setMinimumSize(QtCore.QSize(200,0))
        self.home_port_line.setObjectName("home_port_line")
        self.hboxlayout9.addWidget(self.home_port_line)
        self.vboxlayout1.addWidget(self.home_port)
        self.gridlayout.addWidget(self.vessel_info,0,1,1,1)

        self.interviewee = QtGui.QGroupBox(InterviewStart)
        self.interviewee.setObjectName("interviewee")

        self.vboxlayout2 = QtGui.QVBoxLayout(self.interviewee)
        self.vboxlayout2.setMargin(9)
        self.vboxlayout2.setSpacing(6)
        self.vboxlayout2.setObjectName("vboxlayout2")

        self.interviewee_first_name = QtGui.QWidget(self.interviewee)
        self.interviewee_first_name.setObjectName("interviewee_first_name")

        self.hboxlayout10 = QtGui.QHBoxLayout(self.interviewee_first_name)
        self.hboxlayout10.setMargin(4)
        self.hboxlayout10.setSpacing(4)
        self.hboxlayout10.setObjectName("hboxlayout10")

        self.interviewee_first_name_text = QtGui.QLabel(self.interviewee_first_name)
        self.interviewee_first_name_text.setObjectName("interviewee_first_name_text")
        self.hboxlayout10.addWidget(self.interviewee_first_name_text)

        self.interviewee_first_name_line = QtGui.QLineEdit(self.interviewee_first_name)
        self.interviewee_first_name_line.setEnabled(True)
        self.interviewee_first_name_line.setMinimumSize(QtCore.QSize(200,0))
        self.interviewee_first_name_line.setObjectName("interviewee_first_name_line")
        self.hboxlayout10.addWidget(self.interviewee_first_name_line)
        self.vboxlayout2.addWidget(self.interviewee_first_name)

        self.interviewee_last_name = QtGui.QWidget(self.interviewee)
        self.interviewee_last_name.setObjectName("interviewee_last_name")

        self.hboxlayout11 = QtGui.QHBoxLayout(self.interviewee_last_name)
        self.hboxlayout11.setMargin(4)
        self.hboxlayout11.setSpacing(4)
        self.hboxlayout11.setObjectName("hboxlayout11")

        self.interviewee_last_name_text = QtGui.QLabel(self.interviewee_last_name)
        self.interviewee_last_name_text.setObjectName("interviewee_last_name_text")
        self.hboxlayout11.addWidget(self.interviewee_last_name_text)

        self.interviewee_last_name_line = QtGui.QLineEdit(self.interviewee_last_name)
        self.interviewee_last_name_line.setEnabled(True)
        self.interviewee_last_name_line.setMinimumSize(QtCore.QSize(200,0))
        self.interviewee_last_name_line.setObjectName("interviewee_last_name_line")
        self.hboxlayout11.addWidget(self.interviewee_last_name_line)
        self.vboxlayout2.addWidget(self.interviewee_last_name)

        self.age = QtGui.QWidget(self.interviewee)
        self.age.setObjectName("age")

        self.hboxlayout12 = QtGui.QHBoxLayout(self.age)
        self.hboxlayout12.setMargin(4)
        self.hboxlayout12.setSpacing(4)
        self.hboxlayout12.setObjectName("hboxlayout12")

        self.age_text = QtGui.QLabel(self.age)
        self.age_text.setObjectName("age_text")
        self.hboxlayout12.addWidget(self.age_text)

        self.age_line = QtGui.QLineEdit(self.age)
        self.age_line.setEnabled(True)
        self.age_line.setMinimumSize(QtCore.QSize(200,0))
        self.age_line.setObjectName("age_line")
        self.hboxlayout12.addWidget(self.age_line)
        self.vboxlayout2.addWidget(self.age)

        self.gender = QtGui.QWidget(self.interviewee)
        self.gender.setObjectName("gender")

        self.hboxlayout13 = QtGui.QHBoxLayout(self.gender)
        self.hboxlayout13.setMargin(4)
        self.hboxlayout13.setSpacing(4)
        self.hboxlayout13.setObjectName("hboxlayout13")

        self.gender_text = QtGui.QLabel(self.gender)
        self.gender_text.setObjectName("gender_text")
        self.hboxlayout13.addWidget(self.gender_text)

        self.gender_comboBox = QtGui.QComboBox(self.gender)
        self.gender_comboBox.setObjectName("gender_comboBox")
        self.hboxlayout13.addWidget(self.gender_comboBox)
        self.vboxlayout2.addWidget(self.gender)

        self.years = QtGui.QWidget(self.interviewee)
        self.years.setObjectName("years")

        self.hboxlayout14 = QtGui.QHBoxLayout(self.years)
        self.hboxlayout14.setMargin(4)
        self.hboxlayout14.setSpacing(4)
        self.hboxlayout14.setObjectName("hboxlayout14")

        self.years_text = QtGui.QLabel(self.years)
        self.years_text.setObjectName("years_text")
        self.hboxlayout14.addWidget(self.years_text)

        self.years_line = QtGui.QLineEdit(self.years)
        self.years_line.setEnabled(True)
        self.years_line.setMinimumSize(QtCore.QSize(200,0))
        self.years_line.setObjectName("years_line")
        self.hboxlayout14.addWidget(self.years_line)
        self.vboxlayout2.addWidget(self.years)

        self.license = QtGui.QWidget(self.interviewee)
        self.license.setObjectName("license")

        self.hboxlayout15 = QtGui.QHBoxLayout(self.license)
        self.hboxlayout15.setMargin(4)
        self.hboxlayout15.setSpacing(4)
        self.hboxlayout15.setObjectName("hboxlayout15")

        self.license_text = QtGui.QLabel(self.license)
        self.license_text.setObjectName("license_text")
        self.hboxlayout15.addWidget(self.license_text)

        self.license_line = QtGui.QLineEdit(self.license)
        self.license_line.setEnabled(True)
        self.license_line.setMinimumSize(QtCore.QSize(200,0))
        self.license_line.setObjectName("license_line")
        self.hboxlayout15.addWidget(self.license_line)
        self.vboxlayout2.addWidget(self.license)

        self.city = QtGui.QWidget(self.interviewee)
        self.city.setObjectName("city")

        self.hboxlayout16 = QtGui.QHBoxLayout(self.city)
        self.hboxlayout16.setMargin(4)
        self.hboxlayout16.setSpacing(4)
        self.hboxlayout16.setObjectName("hboxlayout16")

        self.city_text = QtGui.QLabel(self.city)
        self.city_text.setObjectName("city_text")
        self.hboxlayout16.addWidget(self.city_text)

        self.city_line = QtGui.QLineEdit(self.city)
        self.city_line.setEnabled(True)
        self.city_line.setMinimumSize(QtCore.QSize(200,0))
        self.city_line.setObjectName("city_line")
        self.hboxlayout16.addWidget(self.city_line)
        self.vboxlayout2.addWidget(self.city)

        self.user_group = QtGui.QWidget(self.interviewee)
        self.user_group.setObjectName("user_group")

        self.hboxlayout17 = QtGui.QHBoxLayout(self.user_group)
        self.hboxlayout17.setMargin(4)
        self.hboxlayout17.setSpacing(4)
        self.hboxlayout17.setObjectName("hboxlayout17")

        self.user_group_text = QtGui.QLabel(self.user_group)
        self.user_group_text.setObjectName("user_group_text")
        self.hboxlayout17.addWidget(self.user_group_text)

        self.user_group_comboBox = QtGui.QComboBox(self.user_group)
        self.user_group_comboBox.setObjectName("user_group_comboBox")
        self.hboxlayout17.addWidget(self.user_group_comboBox)
        self.vboxlayout2.addWidget(self.user_group)
        self.gridlayout.addWidget(self.interviewee,0,0,2,1)

        self.interviewer = QtGui.QGroupBox(InterviewStart)
        self.interviewer.setObjectName("interviewer")

        self.vboxlayout3 = QtGui.QVBoxLayout(self.interviewer)
        self.vboxlayout3.setMargin(9)
        self.vboxlayout3.setSpacing(6)
        self.vboxlayout3.setObjectName("vboxlayout3")

        self.date = QtGui.QWidget(self.interviewer)
        self.date.setObjectName("date")

        self.hboxlayout18 = QtGui.QHBoxLayout(self.date)
        self.hboxlayout18.setMargin(4)
        self.hboxlayout18.setSpacing(4)
        self.hboxlayout18.setObjectName("hboxlayout18")

        self.date_text = QtGui.QLabel(self.date)
        self.date_text.setObjectName("date_text")
        self.hboxlayout18.addWidget(self.date_text)

        self.date_line = QtGui.QLineEdit(self.date)
        self.date_line.setEnabled(True)
        self.date_line.setMinimumSize(QtCore.QSize(200,0))
        self.date_line.setObjectName("date_line")
        self.hboxlayout18.addWidget(self.date_line)

        spacerItem = QtGui.QSpacerItem(441,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout18.addItem(spacerItem)
        self.vboxlayout3.addWidget(self.date)

        self.widget = QtGui.QWidget(self.interviewer)
        self.widget.setObjectName("widget")

        self.hboxlayout19 = QtGui.QHBoxLayout(self.widget)
        self.hboxlayout19.setMargin(4)
        self.hboxlayout19.setSpacing(4)
        self.hboxlayout19.setObjectName("hboxlayout19")

        self.interviewer_1 = QtGui.QGroupBox(self.widget)
        self.interviewer_1.setObjectName("interviewer_1")

        self.vboxlayout4 = QtGui.QVBoxLayout(self.interviewer_1)
        self.vboxlayout4.setMargin(4)
        self.vboxlayout4.setSpacing(2)
        self.vboxlayout4.setObjectName("vboxlayout4")

        self.interviewer1_first_name = QtGui.QWidget(self.interviewer_1)
        self.interviewer1_first_name.setObjectName("interviewer1_first_name")

        self.hboxlayout20 = QtGui.QHBoxLayout(self.interviewer1_first_name)
        self.hboxlayout20.setMargin(4)
        self.hboxlayout20.setSpacing(4)
        self.hboxlayout20.setObjectName("hboxlayout20")

        self.interviewer1_first_name_text = QtGui.QLabel(self.interviewer1_first_name)
        self.interviewer1_first_name_text.setObjectName("interviewer1_first_name_text")
        self.hboxlayout20.addWidget(self.interviewer1_first_name_text)

        self.interviewer1_first_name_line = QtGui.QLineEdit(self.interviewer1_first_name)
        self.interviewer1_first_name_line.setEnabled(True)
        self.interviewer1_first_name_line.setMinimumSize(QtCore.QSize(200,0))
        self.interviewer1_first_name_line.setObjectName("interviewer1_first_name_line")
        self.hboxlayout20.addWidget(self.interviewer1_first_name_line)
        self.vboxlayout4.addWidget(self.interviewer1_first_name)

        self.interviewer1_last_name = QtGui.QWidget(self.interviewer_1)
        self.interviewer1_last_name.setObjectName("interviewer1_last_name")

        self.hboxlayout21 = QtGui.QHBoxLayout(self.interviewer1_last_name)
        self.hboxlayout21.setMargin(4)
        self.hboxlayout21.setSpacing(4)
        self.hboxlayout21.setObjectName("hboxlayout21")

        self.interviewer1_last_name_text = QtGui.QLabel(self.interviewer1_last_name)
        self.interviewer1_last_name_text.setObjectName("interviewer1_last_name_text")
        self.hboxlayout21.addWidget(self.interviewer1_last_name_text)

        self.interviewer1_last_name_line = QtGui.QLineEdit(self.interviewer1_last_name)
        self.interviewer1_last_name_line.setEnabled(True)
        self.interviewer1_last_name_line.setMinimumSize(QtCore.QSize(200,0))
        self.interviewer1_last_name_line.setObjectName("interviewer1_last_name_line")
        self.hboxlayout21.addWidget(self.interviewer1_last_name_line)
        self.vboxlayout4.addWidget(self.interviewer1_last_name)
        self.hboxlayout19.addWidget(self.interviewer_1)

        self.interviewer_2 = QtGui.QGroupBox(self.widget)
        self.interviewer_2.setObjectName("interviewer_2")

        self.vboxlayout5 = QtGui.QVBoxLayout(self.interviewer_2)
        self.vboxlayout5.setMargin(4)
        self.vboxlayout5.setSpacing(2)
        self.vboxlayout5.setObjectName("vboxlayout5")

        self.interviewer2_first_name = QtGui.QWidget(self.interviewer_2)
        self.interviewer2_first_name.setObjectName("interviewer2_first_name")

        self.hboxlayout22 = QtGui.QHBoxLayout(self.interviewer2_first_name)
        self.hboxlayout22.setMargin(4)
        self.hboxlayout22.setSpacing(4)
        self.hboxlayout22.setObjectName("hboxlayout22")

        self.interviewer2_first_name_text = QtGui.QLabel(self.interviewer2_first_name)
        self.interviewer2_first_name_text.setObjectName("interviewer2_first_name_text")
        self.hboxlayout22.addWidget(self.interviewer2_first_name_text)

        self.interviewer2_first_name_line = QtGui.QLineEdit(self.interviewer2_first_name)
        self.interviewer2_first_name_line.setEnabled(True)
        self.interviewer2_first_name_line.setMinimumSize(QtCore.QSize(200,0))
        self.interviewer2_first_name_line.setObjectName("interviewer2_first_name_line")
        self.hboxlayout22.addWidget(self.interviewer2_first_name_line)
        self.vboxlayout5.addWidget(self.interviewer2_first_name)

        self.interviewer2_last_name = QtGui.QWidget(self.interviewer_2)
        self.interviewer2_last_name.setObjectName("interviewer2_last_name")

        self.hboxlayout23 = QtGui.QHBoxLayout(self.interviewer2_last_name)
        self.hboxlayout23.setMargin(4)
        self.hboxlayout23.setSpacing(4)
        self.hboxlayout23.setObjectName("hboxlayout23")

        self.interviewer2_last_name_text = QtGui.QLabel(self.interviewer2_last_name)
        self.interviewer2_last_name_text.setObjectName("interviewer2_last_name_text")
        self.hboxlayout23.addWidget(self.interviewer2_last_name_text)

        self.interviewer2_last_name_line = QtGui.QLineEdit(self.interviewer2_last_name)
        self.interviewer2_last_name_line.setEnabled(True)
        self.interviewer2_last_name_line.setMinimumSize(QtCore.QSize(200,0))
        self.interviewer2_last_name_line.setObjectName("interviewer2_last_name_line")
        self.hboxlayout23.addWidget(self.interviewer2_last_name_line)
        self.vboxlayout5.addWidget(self.interviewer2_last_name)
        self.hboxlayout19.addWidget(self.interviewer_2)
        self.vboxlayout3.addWidget(self.widget)
        self.gridlayout.addWidget(self.interviewer,2,0,1,2)

        self.button_box = QtGui.QWidget(InterviewStart)
        self.button_box.setObjectName("button_box")

        self.hboxlayout24 = QtGui.QHBoxLayout(self.button_box)
        self.hboxlayout24.setMargin(2)
        self.hboxlayout24.setSpacing(2)
        self.hboxlayout24.setObjectName("hboxlayout24")

        spacerItem1 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout24.addItem(spacerItem1)

        self.pbnCancel = QtGui.QPushButton(self.button_box)
        self.pbnCancel.setObjectName("pbnCancel")
        self.hboxlayout24.addWidget(self.pbnCancel)

        self.pbnSelectFishery = QtGui.QPushButton(self.button_box)
        self.pbnSelectFishery.setObjectName("pbnSelectFishery")
        self.hboxlayout24.addWidget(self.pbnSelectFishery)
        self.gridlayout.addWidget(self.button_box,3,0,1,2)

        self.retranslateUi(InterviewStart)
        QtCore.QMetaObject.connectSlotsByName(InterviewStart)

    def retranslateUi(self, InterviewStart):
        InterviewStart.setWindowTitle(QtGui.QApplication.translate("InterviewStart", "OpenOceanMap - Interview", None, QtGui.QApplication.UnicodeUTF8))
        self.trip_info.setTitle(QtGui.QApplication.translate("InterviewStart", "Trip Information", None, QtGui.QApplication.UnicodeUTF8))
        self.region_text.setText(QtGui.QApplication.translate("InterviewStart", "Region :", None, QtGui.QApplication.UnicodeUTF8))
        self.region_comboBox.addItem(QtGui.QApplication.translate("InterviewStart", "San Francisco County and south, including Pillar Point", None, QtGui.QApplication.UnicodeUTF8))
        self.region_comboBox.addItem(QtGui.QApplication.translate("InterviewStart", "San Francisco Bay access points to Point Reyes", None, QtGui.QApplication.UnicodeUTF8))
        self.region_comboBox.addItem(QtGui.QApplication.translate("InterviewStart", "Point Reyes north to Alder Creek, including Bodega Bay", None, QtGui.QApplication.UnicodeUTF8))
        self.ind_per_trip_text.setText(QtGui.QApplication.translate("InterviewStart", "Individuals per trip :", None, QtGui.QApplication.UnicodeUTF8))
        self.days_per_year_text.setText(QtGui.QApplication.translate("InterviewStart", "Average days fishing per year :", None, QtGui.QApplication.UnicodeUTF8))
        self.travel_time_text.setText(QtGui.QApplication.translate("InterviewStart", "Travel time from home to fishing location :", None, QtGui.QApplication.UnicodeUTF8))
        self.travel_distance_text.setText(QtGui.QApplication.translate("InterviewStart", "Travel distance from home to fishing location :", None, QtGui.QApplication.UnicodeUTF8))
        self.vessel_info.setTitle(QtGui.QApplication.translate("InterviewStart", "Vessel Information", None, QtGui.QApplication.UnicodeUTF8))
        self.ves_license_text.setText(QtGui.QApplication.translate("InterviewStart", "Vessel license :", None, QtGui.QApplication.UnicodeUTF8))
        self.years_op_text.setText(QtGui.QApplication.translate("InterviewStart", "Years operating a boat :", None, QtGui.QApplication.UnicodeUTF8))
        self.years_own_text.setText(QtGui.QApplication.translate("InterviewStart", "Years of ownership :", None, QtGui.QApplication.UnicodeUTF8))
        self.vessel_length_text.setText(QtGui.QApplication.translate("InterviewStart", "Vessel length :", None, QtGui.QApplication.UnicodeUTF8))
        self.home_port_text.setText(QtGui.QApplication.translate("InterviewStart", "Home Port :", None, QtGui.QApplication.UnicodeUTF8))
        self.interviewee.setTitle(QtGui.QApplication.translate("InterviewStart", "Interviewee", None, QtGui.QApplication.UnicodeUTF8))
        self.interviewee_first_name_text.setText(QtGui.QApplication.translate("InterviewStart", "First Name :", None, QtGui.QApplication.UnicodeUTF8))
        self.interviewee_last_name_text.setText(QtGui.QApplication.translate("InterviewStart", "Last Name :", None, QtGui.QApplication.UnicodeUTF8))
        self.age_text.setText(QtGui.QApplication.translate("InterviewStart", "Age :", None, QtGui.QApplication.UnicodeUTF8))
        self.gender_text.setText(QtGui.QApplication.translate("InterviewStart", "Gender :", None, QtGui.QApplication.UnicodeUTF8))
        self.gender_comboBox.addItem(QtGui.QApplication.translate("InterviewStart", "Male", None, QtGui.QApplication.UnicodeUTF8))
        self.gender_comboBox.addItem(QtGui.QApplication.translate("InterviewStart", "Female", None, QtGui.QApplication.UnicodeUTF8))
        self.years_text.setText(QtGui.QApplication.translate("InterviewStart", "Years of experience :", None, QtGui.QApplication.UnicodeUTF8))
        self.license_text.setText(QtGui.QApplication.translate("InterviewStart", "License number :", None, QtGui.QApplication.UnicodeUTF8))
        self.city_text.setText(QtGui.QApplication.translate("InterviewStart", "City of residence :", None, QtGui.QApplication.UnicodeUTF8))
        self.user_group_text.setText(QtGui.QApplication.translate("InterviewStart", "Rec. fishing user group :", None, QtGui.QApplication.UnicodeUTF8))
        self.user_group_comboBox.addItem(QtGui.QApplication.translate("InterviewStart", "Operator of Com. Pass. Fishing Vessels", None, QtGui.QApplication.UnicodeUTF8))
        self.user_group_comboBox.addItem(QtGui.QApplication.translate("InterviewStart", "Private boat rec. anglers", None, QtGui.QApplication.UnicodeUTF8))
        self.user_group_comboBox.addItem(QtGui.QApplication.translate("InterviewStart", "Kayak-based anglers", None, QtGui.QApplication.UnicodeUTF8))
        self.user_group_comboBox.addItem(QtGui.QApplication.translate("InterviewStart", "Pier and shore anglers", None, QtGui.QApplication.UnicodeUTF8))
        self.interviewer.setTitle(QtGui.QApplication.translate("InterviewStart", "Interviewer", None, QtGui.QApplication.UnicodeUTF8))
        self.date_text.setText(QtGui.QApplication.translate("InterviewStart", "Date of interview (mm/dd/yyyy) :", None, QtGui.QApplication.UnicodeUTF8))
        self.interviewer_1.setTitle(QtGui.QApplication.translate("InterviewStart", "Interviewer #1", None, QtGui.QApplication.UnicodeUTF8))
        self.interviewer1_first_name_text.setText(QtGui.QApplication.translate("InterviewStart", "First Name :", None, QtGui.QApplication.UnicodeUTF8))
        self.interviewer1_last_name_text.setText(QtGui.QApplication.translate("InterviewStart", "Last Name :", None, QtGui.QApplication.UnicodeUTF8))
        self.interviewer_2.setTitle(QtGui.QApplication.translate("InterviewStart", "Interviewer #2", None, QtGui.QApplication.UnicodeUTF8))
        self.interviewer2_first_name_text.setText(QtGui.QApplication.translate("InterviewStart", "First Name :", None, QtGui.QApplication.UnicodeUTF8))
        self.interviewer2_last_name_text.setText(QtGui.QApplication.translate("InterviewStart", "Last Name :", None, QtGui.QApplication.UnicodeUTF8))
        self.pbnCancel.setText(QtGui.QApplication.translate("InterviewStart", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.pbnSelectFishery.setText(QtGui.QApplication.translate("InterviewStart", "Select Fishery", None, QtGui.QApplication.UnicodeUTF8))

