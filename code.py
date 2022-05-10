import RPi.GPIO as GPIO
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton
from PyQt5.QtCore import pyqtSlot
import sys

GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)

def window():
	app = QApplication(sys.argv)
	win = QMainWindow()
	win.setGeometry(200,200,300,300)
	win.setWindowTitle("LED Choice")
	ledA = QPushButton('LED A', win)
	ledB = QPushButton('LED B', win)
	ledC = QPushButton('LED C', win)
	ledA.move(100,70)
	ledB.move(100,120)
	ledC.move(100,170)
	ledA.clicked.connect(handleA)
	ledB.clicked.connect(handleB)
	ledC.clicked.connect(handleC)
	win.show()
	sys.exit(app.exec ())

def clearAll():
	GPIO.output(18, GPIO.LOW)
	GPIO.output(23, GPIO.LOW)
	GPIO.output(24, GPIO.LOW)

def handleA(self):
	clearAll()
	GPIO.output(18, GPIO.HIGH)

def handleB(self):
	clearAll()
	GPIO.output(23, GPIO.HIGH)	

def handleC(self):
	clearAll()
	GPIO.output(24, GPIO.HIGH)	

window()
