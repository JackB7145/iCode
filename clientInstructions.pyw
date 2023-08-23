import socket
import time 
import datetime
from email_validator import validate_email
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random
import cv2
from win32gui import GetForegroundWindow
import psutil
import win32process
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QGridLayout
from pyqt_toast import Toast
from PyQt5.QtCore import QPoint
import os
from pathlib import Path

path = os.path.dirname(__file__)
ip_address = ""
filePath = path+r"\data\emailAndBacklog.txt"

file = open(filePath, "a")
readFile = open(filePath, "r")

userData = readFile.readline()
email = None
code = None

#GUI

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(800, 893)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: #0398fc;")
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 60, 681, 661))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(path+r"\rescources\logo.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(100, 20, 601, 801))
        self.graphicsView.setStyleSheet("background-color: rgba(92, 71, 255, 220);\n"
"border-radius: 50%;\n"
"")
        
        self.graphicsView.setFrameShadow(QtWidgets.QFrame.Raised)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 100))
        brush.setStyle(QtCore.Qt.Dense7Pattern)
        self.graphicsView.setBackgroundBrush(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.Dense7Pattern)
        self.graphicsView.setForegroundBrush(brush)
        self.graphicsView.setObjectName("graphicsView")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 80, 231, 101))
        self.label.setStyleSheet("background-color: white;\n"
"")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(path+r"\rescources\ICodeLabel.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")




        self.label0 = QtWidgets.QLabel(self.centralwidget)
        self.label0.setGeometry(QtCore.QRect(280, 685, 231, 101))
        self.label0.setStyleSheet("background-color: rgba(92, 71, 255, 0);\n"
"")
        self.label0.setObjectName("Error Messages")




        
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_2.setGeometry(QtCore.QRect(100, 230, 601, 91))
        self.graphicsView_2.setStyleSheet("background-color: white;\n"
"")
        self.graphicsView_2.setFrameShadow(QtWidgets.QFrame.Raised)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 100))
        brush.setStyle(QtCore.Qt.Dense7Pattern)
        self.graphicsView_2.setBackgroundBrush(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.Dense7Pattern)
        self.graphicsView_2.setForegroundBrush(brush)
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(330, 360, 131, 71))
        self.pushButton.setStyleSheet("QPushButton{\n"
"border-radius: 25%;\n"
"font-size: 20px;\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(84, 161, 255);\n"
"}\n"
"\n"
"\n"
"")
        self.pushButton.setCheckable(False)
        self.pushButton.setChecked(False)
        self.pushButton.setObjectName("pushButton")

        self.pushButton.clicked.connect(self.getEmail)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(100, 230, 601, 91))
        self.lineEdit.setStyleSheet("QLineEdit:focus{\n"
"background-color: rgb(242, 242, 255);\n"
"}\n"
"\n"
"QLineEdit{\n"
"background-color: white;\n"
"font-size: 25px;\n"
"padding-left: 20px; \n"
"}\n"
"\n"
"")
        self.lineEdit.setFrame(False)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 480, 601, 91))
        self.lineEdit_2.setStyleSheet("QLineEdit:focus{\n"
"background-color: rgb(242, 242, 255);\n"
"}\n"
"\n"
"QLineEdit{\n"
"background-color: white;\n"
"font-size: 25px;\n"
"padding-left: 20px; \n"
"}\n"
"")
        self.lineEdit_2.setFrame(False)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(330, 610, 131, 71))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"border-radius: 25%;\n"
"font-size: 20px;\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(84, 161, 255);\n"
"}")
        self.pushButton_2.setCheckable(False)
        self.pushButton_2.setChecked(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.rightCode)
        self.graphicsView_3 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_3.setGeometry(QtCore.QRect(100, 480, 601, 91))
        self.graphicsView_3.setStyleSheet("background-color: white;\n"
"")
        self.graphicsView_3.setFrameShadow(QtWidgets.QFrame.Raised)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 100))
        brush.setStyle(QtCore.Qt.Dense7Pattern)
        self.graphicsView_3.setBackgroundBrush(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.Dense7Pattern)
        self.graphicsView_3.setForegroundBrush(brush)
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.label_2.raise_()
        self.graphicsView.raise_()
        self.label.raise_()
        self.label0.raise_()
        self.graphicsView_2.raise_()
        self.pushButton.raise_()
        self.lineEdit.raise_()
        self.pushButton_2.raise_()
        self.graphicsView_3.raise_()
        self.lineEdit_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Submit"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Enter Your Email"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Enter Your Verification Code"))
        self.pushButton_2.setText(_translate("MainWindow", "Verify"))

    def displayToast(self, text):
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
        toast = Toast(text=text, duration=2, parent=self.label0)
        toast.setBackgroundColor("red")
        toast.setOpacity(0.9)
        toast.setForegroundColor("white")
        toast.show()



#########################################################################
   #GUI Functions
    def closed(self):
           MainWindow.close()
    def getEmail(self):
                global code, email
                try:
                        email = self.lineEdit.text()

                        email = validate_email(email).email
                        try:
                                # Email configuration
                                sender_email = "icodeemailer@gmail.com"
                                receiver_email = email
                                subject = "Confirmation Email"
                                code = random.randint(1000, 9999)
                                body = "This is a confirmation email sent to "+str(email)+"\n\nYour confirmation code is: "+str(code)

                                # Create the MIME message
                                message = MIMEMultipart()
                                message["From"] = sender_email
                                message["To"] = receiver_email
                                message["Subject"] = subject
                                message.attach(MIMEText(body, "plain"))

                                # Establish a connection to the SMTP server
                                smtp_server = "smtp.gmail.com"  
                                smtp_port = 587  
                                smtp_username = "icodeemailer@gmail.com"
                                smtp_password = "oiqvabvjjqpdsydu"

                                # Connect to the SMTP server and start TLS encryption
                                server = smtplib.SMTP(smtp_server, smtp_port)
                                server.starttls()

                                # Login to your email account
                                server.login(smtp_username, smtp_password)

                                # Send the email
                                server.sendmail(sender_email, receiver_email, message.as_string())

                                # Quit the server
                                server.quit()
                        except:
                                print("Confirmation email was unsuccesfull!")
                except:
                        self.displayToast("Invalid Email Entered!")
    def rightCode(self):
            global code, userData, file, readFile, MainWindow, email, mainClicked
            try:
                received = int(self.lineEdit_2.text())
                
                if received == code:
                        file.write(email+" 0 0 0 0 0 0 0 0") 
                        userData = email+" 0 0 0 0 0 0 0 0"
                        self.graphicsView.hide()
                        self.graphicsView_2.hide()
                        self.graphicsView_3.hide()
                        self.label.hide()
                        self.pushButton_2.hide()
                        self.lineEdit.hide()
                        self.lineEdit_2.hide()
                        self.label_2.setPixmap(QtGui.QPixmap(path+r"\rescources\StartupAppsSetup.png"))
                        self.label_2.setGeometry(QtCore.QRect(0, 0, 800, 893))
                        self.pushButton.setGeometry(QtCore.QRect(420, 788, 310, 67))
                        self.pushButton.setStyleSheet("QPushButton{\n"
                        "border-radius: 30%;\n"
                        "font-size: 20px;\n"
                        "color: white;\n"
                        "}\n"
                        "\n"
                        "QPushButton:hover{\n"
                        "background-color: rgb(84, 161, 255);\n"
                        "}\n"
                        "\n"
                        "\n"
                        "")
                        self.pushButton.setText("Close")
                        self.pushButton.clicked.disconnect()
                        self.pushButton.clicked.connect(self.closed)
                        self.pushButton.raise_()
            except:
                   self.displayToast("Invalid Verification Code Entered!")
                  
full_msg = ''
if userData == "":
        
        email = ""
        import sys
        app = QtWidgets.QApplication(sys.argv)
        ui = Ui_MainWindow()
        MainWindow = QtWidgets.QMainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        app.exec()
                       
        try:            
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((ip_address, 7145))
                s.send(userData.encode())
                userData = userData.split()
                s.close()
        except:
                print("Connection Error")
        readFile.close()
        readFile = open(filePath, "r")
        # Load the pre-trained face detection model from OpenCV
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

        # Initialize the webcam
        cap = cv2.VideoCapture(0)

        ready = False
        while True:
                try:
                        time.sleep(1)
                        weekDay = datetime.date.weekday(datetime.date.today())
                        # Capture frame-by-frame
                        ret, frame = cap.read()

                        # Convert the frame to grayscale for face detection
                        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                        # Detect faces in the frame
                        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=10, minSize=(30, 30))

                        if len(faces):
                                looking = True
                        else:
                                looking = False
                        try:
                                current_app = psutil.Process(win32process.GetWindowThreadProcessId(GetForegroundWindow())[1]).name().replace(".exe", "")
                        except:
                                current_app = None
                                print("Switched Tabs Too Fast!")

                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        s.connect((ip_address, 7145))
                        s.setblocking(False)

                        file = open(filePath, "a")
                        readFile = open(filePath, "r")
                        userData = readFile.readline()
                        userData = userData.split()
                        print(userData)

                        if weekDay == 0 and ready:
                                
                                file.truncate(0)
                                weeklyTotal = sum([int(userData[x]) for x in range(2, 9)])

                                if weeklyTotal > int(userData[1]):
                                        userData[1] = weeklyTotal

                                file.write(userData[0]+" "+str(userData[1])+" 0 0 0 0 0 0 0 0")
                                ready = False
                        elif weekDay == 6:
                                ready = True


                        if looking and current_app == "Code":
                                
                                
                                weekDay = datetime.date.weekday(datetime.date.today())
                                userData[weekDay+2] = str(int(userData[weekDay+2]) + 1)
                                file.truncate(0)
                                newData = " ".join(userData)
                                file.write(newData)
                                s.send(newData.encode())
                        file.close()
                        readFile.close()
                        s.close()
                except:
                        print("Error Detected")