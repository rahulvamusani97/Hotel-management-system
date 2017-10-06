# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Hotel.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_Hotel(object):
    
    
    

    

    

    def setupUi(self, Hotel):
        Hotel.setObjectName("Hotel")
        Hotel.resize(1062, 825)
        self.centralwidget = QtWidgets.QWidget(Hotel)
        self.centralwidget.setObjectName("centralwidget")
        self.sprice = 0
        self.dprice = 0
        self.vpiz= 0
        self.nvpiz = 0
        self.vbur = 0
        self.nvbur = 0
        self.vbir = 0
        self.nvbir = 0
        self.cus_head = QtWidgets.QLabel(self.centralwidget)
        self.cus_head.setGeometry(QtCore.QRect(20, 30, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.cus_head.setFont(font)
        self.cus_head.setObjectName("cus_head")
        self.name_label = QtWidgets.QLabel(self.centralwidget)
        self.name_label.setGeometry(QtCore.QRect(50, 130, 72, 18))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.name_label.setFont(font)
        self.name_label.setObjectName("name_label")
        self.email_label = QtWidgets.QLabel(self.centralwidget)
        self.email_label.setGeometry(QtCore.QRect(50, 180, 72, 18))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.email_label.setFont(font)
        self.email_label.setObjectName("email_label")
        self.uname_label = QtWidgets.QLabel(self.centralwidget)
        self.uname_label.setGeometry(QtCore.QRect(50, 80, 121, 18))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.uname_label.setFont(font)
        self.uname_label.setObjectName("uname_label")
        self.addr_line = QtWidgets.QTextEdit(self.centralwidget)
        self.addr_line.setGeometry(QtCore.QRect(200, 230, 211, 91))
        self.addr_line.setObjectName("addr_line")
        self.uname_line = QtWidgets.QLineEdit(self.centralwidget)
        self.uname_line.setGeometry(QtCore.QRect(200, 80, 211, 26))
        self.uname_line.setObjectName("uname_line")
        self.name_line = QtWidgets.QLineEdit(self.centralwidget)
        self.name_line.setGeometry(QtCore.QRect(200, 130, 211, 26))
        self.name_line.setObjectName("name_line")
        self.email_line = QtWidgets.QLineEdit(self.centralwidget)
        self.email_line.setGeometry(QtCore.QRect(200, 170, 211, 26))
        self.email_line.setObjectName("email_line")
        self.addr_label = QtWidgets.QLabel(self.centralwidget)
        self.addr_label.setGeometry(QtCore.QRect(50, 230, 101, 18))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.addr_label.setFont(font)
        self.addr_label.setObjectName("addr_label")
        self.room_head = QtWidgets.QLabel(self.centralwidget)
        self.room_head.setGeometry(QtCore.QRect(20, 410, 201, 18))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.room_head.setFont(font)
        self.room_head.setObjectName("room_head")
        
        self.food_head = QtWidgets.QLabel(self.centralwidget)
        self.food_head.setGeometry(QtCore.QRect(530, 40, 191, 18))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.food_head.setFont(font)
        self.food_head.setObjectName("food_head")
        self.veg_label = QtWidgets.QLabel(self.centralwidget)
        self.veg_label.setGeometry(QtCore.QRect(570, 90, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.veg_label.setFont(font)
        self.veg_label.setObjectName("veg_label")
        self.nonveg_label = QtWidgets.QLabel(self.centralwidget)
        self.nonveg_label.setGeometry(QtCore.QRect(770, 90, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.nonveg_label.setFont(font)
        self.nonveg_label.setObjectName("nonveg_label")
        self.food_price = QtWidgets.QLabel(self.centralwidget)
        self.food_price.setGeometry(QtCore.QRect(580, 430, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.food_price.setFont(font)
        self.food_price.setObjectName("food_price")
        self.fprice_line = QtWidgets.QLineEdit(self.centralwidget)
        self.fprice_line.setGeometry(QtCore.QRect(680, 430, 171, 26))
        self.fprice_line.setObjectName("fprice_line")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(703, 90, 20, 251))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.final_button = QtWidgets.QPushButton(self.centralwidget)
        self.final_button.setGeometry(QtCore.QRect(742, 676, 191, 51))
        self.final_button.setObjectName("final_button")
        ######################################################
        self.final_button.clicked.connect(self.data_insert)
        ######################################################
        self.suite_box = QtWidgets.QCheckBox(self.centralwidget)
        self.suite_box.setGeometry(QtCore.QRect(90, 490, 102, 24))
        ######################################################
        self.suite_box.stateChanged.connect(self.suite_price)
        ####################################################
        font = QtGui.QFont()
        font.setPointSize(12)
        self.suite_box.setFont(font)
        self.suite_box.setObjectName("suite_box")
        self.delux_box = QtWidgets.QCheckBox(self.centralwidget)
        self.delux_box.setGeometry(QtCore.QRect(280, 490, 102, 24))
        ###########################################
        self.delux_box.stateChanged.connect(self.delux_price)
        ###########################################
        font = QtGui.QFont()
        font.setPointSize(12)
        self.delux_box.setFont(font)
        self.delux_box.setObjectName("delux_box")
        self.vegpiz_box = QtWidgets.QCheckBox(self.centralwidget)
        self.vegpiz_box.setGeometry(QtCore.QRect(560, 160, 102, 24))
        ###########################################################
        self.vegpiz_box.stateChanged.connect(self.vpizza)
        ###########################################################
        font = QtGui.QFont()
        font.setPointSize(12)
        self.vegpiz_box.setFont(font)
        self.vegpiz_box.setObjectName("vegpiz_box")
        self.vegbur_box = QtWidgets.QCheckBox(self.centralwidget)
        self.vegbur_box.setGeometry(QtCore.QRect(560, 220, 102, 24))
        ############################################################
        self.vegbur_box.stateChanged.connect(self.vburger)
        ############################################################
        font = QtGui.QFont()
        font.setPointSize(12)
        self.vegbur_box.setFont(font)
        self.vegbur_box.setObjectName("vegbur_box")
        self.vegbir_box = QtWidgets.QCheckBox(self.centralwidget)
        self.vegbir_box.setGeometry(QtCore.QRect(560, 280, 102, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.vegbir_box.setFont(font)
        self.vegbir_box.setObjectName("vegbir_box")
        ###########################################################
        self.vegbir_box.stateChanged.connect(self.vbiryani)
        ###########################################################
        self.nvegpiz_box = QtWidgets.QCheckBox(self.centralwidget)
        self.nvegpiz_box.setGeometry(QtCore.QRect(760, 160, 102, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.nvegpiz_box.setFont(font)
        self.nvegpiz_box.setObjectName("nvegpiz_box")
        ######################################################
        self.nvegpiz_box.stateChanged.connect(self.nvpizza)
        ######################################################
        self.nvegbur_box = QtWidgets.QCheckBox(self.centralwidget)
        self.nvegbur_box.setGeometry(QtCore.QRect(760, 220, 102, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.nvegbur_box.setFont(font)
        self.nvegbur_box.setObjectName("nvegbur_box")
        #######################################################
        self.nvegbur_box.stateChanged.connect(self.nvburger)
        #######################################################
        self.nvegbir_box = QtWidgets.QCheckBox(self.centralwidget)
        self.nvegbir_box.setGeometry(QtCore.QRect(760, 280, 102, 24))
        
        font = QtGui.QFont()
        font.setPointSize(12)
        self.nvegbir_box.setFont(font)
        self.nvegbir_box.setObjectName("nvegbir_box")
        #######################################################
        self.nvegbir_box.stateChanged.connect(self.nvbiryani)
        #######################################################
        Hotel.setCentralWidget(self.centralwidget)

        self.retranslateUi(Hotel)
        QtCore.QMetaObject.connectSlotsByName(Hotel)

    def retranslateUi(self, Hotel):
        _translate = QtCore.QCoreApplication.translate
        Hotel.setWindowTitle(_translate("Hotel", "MainWindow"))
        self.cus_head.setText(_translate("Hotel", "Customer details:"))
        self.name_label.setText(_translate("Hotel", "Name:"))
        self.email_label.setText(_translate("Hotel", "Email:"))
        self.uname_label.setText(_translate("Hotel", "User ID:"))
        self.addr_label.setText(_translate("Hotel", "Address:"))
        self.room_head.setText(_translate("Hotel", "Room Details:"))
        self.food_head.setText(_translate("Hotel", "Food details:"))
        self.veg_label.setText(_translate("Hotel", "Veg"))
        self.nonveg_label.setText(_translate("Hotel", "Non - Veg"))
        self.food_price.setText(_translate("Hotel", "Total:"))
        self.final_button.setText(_translate("Hotel", "OK"))
        self.suite_box.setText(_translate("Hotel", "Suite"))
        self.delux_box.setText(_translate("Hotel", "Delux"))
        self.vegpiz_box.setText(_translate("Hotel", "Pizza"))
        self.vegbur_box.setText(_translate("Hotel", "Burger"))
        self.vegbir_box.setText(_translate("Hotel", "Biryani"))
        self.nvegpiz_box.setText(_translate("Hotel", "Pizza"))
        self.nvegbur_box.setText(_translate("Hotel", "Burger"))
        self.nvegbir_box.setText(_translate("Hotel", "Biryani"))



    def nvbiryani(self, state):
        if state == QtCore.Qt.Checked:
            con = sqlite3.connect('hotel.db')
            cur = con.cursor()
            result = cur.execute("SELECT price FROM food WHERE foodname = 'nvegpiz'")
            con.commit()
            result = tuple(result)
            print(result)
            self.nvbir = result[0][0]
           
            
        else:
            self.nvbir = 0

    def nvburger(self, state):
        if state == QtCore.Qt.Checked:
            con = sqlite3.connect('hotel.db')
            cur = con.cursor()
            result = cur.execute("SELECT price FROM food WHERE foodname = 'nvegpiz'")
            con.commit()
            result = tuple(result)
            print(result)
            self.nvbur = result[0][0]
           
            
        else:
            self.nvbur = 0

    def nvpizza(self, state):
        if state == QtCore.Qt.Checked:
            con = sqlite3.connect('hotel.db')
            cur = con.cursor()
            result = cur.execute("SELECT price FROM food WHERE foodname = 'nvegpiz'")
            con.commit()
            result = tuple(result)
            print(result)
            self.nvpiz = result[0][0]
           
            
        else:
            self.nvpiz = 0

    def vbiryani(self, state):
        if state == QtCore.Qt.Checked:
            con = sqlite3.connect('hotel.db')
            cur = con.cursor()
            result = cur.execute("SELECT price FROM food WHERE foodname = 'vegbir'")
            con.commit()
            result = tuple(result)
            print(result)
            self.vbir = result[0][0]
           
            
        else:
            self.vbir = 0

    def vburger(self, state):
        if state == QtCore.Qt.Checked:
            con = sqlite3.connect('hotel.db')
            cur = con.cursor()
            result = cur.execute("SELECT price FROM food WHERE foodname = 'vegbur'")
            con.commit()
            result = tuple(result)
            print(result)
            self.vbur = result[0][0]
           
            
        else:
            self.vbur = 0
            

    def vpizza(self, state):
        if state == QtCore.Qt.Checked:
            con = sqlite3.connect('hotel.db')
            cur = con.cursor()
            result = cur.execute("SELECT price FROM food WHERE foodname = 'vegpiz'")
            con.commit()
            result = tuple(result)
            print(result)
            self.vpiz = result[0][0]
           
            
        else:
            self.vpiz = 0
            


    def suite_price(self, state):
        if state == QtCore.Qt.Checked:
            con = sqlite3.connect('hotel.db')
            cur = con.cursor()
            result = cur.execute("SELECT roomcharge FROM room WHERE roomtype = 'suite'")
            con.commit()
            result = tuple(result)
            print(result)
            self.sprice = result[0][0]
            
        else:
            self.sprice = 0
            


    def delux_price(self, state):
        if state == QtCore.Qt.Checked:
            con = sqlite3.connect('hotel.db')
            cur = con.cursor()
            result = cur.execute("SELECT roomcharge FROM room WHERE roomtype = 'deluxe'")
            result = tuple(result)
            print(result)
            self.dprice = result[0][0]
            
        else:
            self.dprice = 0



    def data_insert(self):
        con = sqlite3.connect('hotel.db')
        cur = con.cursor()
        cur.execute("INSERT INTO customer VALUES(?,?,?,?)", (self.uname_line.text(), self.name_line.text(), self.email_line.text(), self.addr_line.toPlainText()))
        con.commit()
        total =  int(self.sprice)+ int(self.dprice) + int(self.vpiz)+int(self.nvpiz) +int(self.vbur) +int(self.nvbur) +int(self.vbir) +int(self.nvbir)

        self.fprice_line.setText(str(total))
            
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Hotel = QtWidgets.QMainWindow()
    ui = Ui_Hotel()
    ui.setupUi(Hotel)
    Hotel.show()
    sys.exit(app.exec_())

