# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rubikUI.ui'
#
# Created: Mon Jul  2 09:59:15 2018
#      by: PyQt4 UI code generator 4.6.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(950, 800)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.q30 = QtGui.QGraphicsView(self.centralwidget)
        self.q30.setGeometry(QtCore.QRect(25, 175, 40, 40))
        self.q30.setFrameShape(QtGui.QFrame.NoFrame)
        self.q30.setObjectName("q30")
        self.q31 = QtGui.QGraphicsView(self.centralwidget)
        self.q31.setGeometry(QtCore.QRect(75, 175, 40, 40))
        self.q31.setFrameShape(QtGui.QFrame.NoFrame)
        self.q31.setObjectName("q31")
        self.q52 = QtGui.QGraphicsView(self.centralwidget)
        self.q52.setGeometry(QtCore.QRect(125, 275, 40, 40))
        self.q52.setFrameShape(QtGui.QFrame.NoFrame)
        self.q52.setObjectName("q52")
        self.q32 = QtGui.QGraphicsView(self.centralwidget)
        self.q32.setGeometry(QtCore.QRect(125, 175, 40, 40))
        self.q32.setFrameShape(QtGui.QFrame.NoFrame)
        self.q32.setObjectName("q32")
        self.q40 = QtGui.QGraphicsView(self.centralwidget)
        self.q40.setGeometry(QtCore.QRect(25, 225, 40, 40))
        self.q40.setFrameShape(QtGui.QFrame.NoFrame)
        self.q40.setObjectName("q40")
        self.q41 = QtGui.QGraphicsView(self.centralwidget)
        self.q41.setGeometry(QtCore.QRect(75, 225, 40, 40))
        self.q41.setFrameShape(QtGui.QFrame.NoFrame)
        self.q41.setInteractive(False)
        self.q41.setObjectName("q41")
        self.q42 = QtGui.QGraphicsView(self.centralwidget)
        self.q42.setGeometry(QtCore.QRect(125, 225, 40, 40))
        self.q42.setFrameShape(QtGui.QFrame.NoFrame)
        self.q42.setObjectName("q42")
        self.q50 = QtGui.QGraphicsView(self.centralwidget)
        self.q50.setGeometry(QtCore.QRect(25, 275, 40, 40))
        self.q50.setFrameShape(QtGui.QFrame.NoFrame)
        self.q50.setObjectName("q50")
        self.q51 = QtGui.QGraphicsView(self.centralwidget)
        self.q51.setGeometry(QtCore.QRect(75, 275, 40, 40))
        self.q51.setFrameShape(QtGui.QFrame.NoFrame)
        self.q51.setObjectName("q51")
        self.q23 = QtGui.QGraphicsView(self.centralwidget)
        self.q23.setGeometry(QtCore.QRect(180, 120, 40, 40))
        self.q23.setFrameShape(QtGui.QFrame.NoFrame)
        self.q23.setObjectName("q23")
        self.q03 = QtGui.QGraphicsView(self.centralwidget)
        self.q03.setGeometry(QtCore.QRect(180, 20, 40, 40))
        self.q03.setFrameShape(QtGui.QFrame.NoFrame)
        self.q03.setObjectName("q03")
        self.q14 = QtGui.QGraphicsView(self.centralwidget)
        self.q14.setGeometry(QtCore.QRect(230, 70, 40, 40))
        self.q14.setFrameShape(QtGui.QFrame.NoFrame)
        self.q14.setInteractive(False)
        self.q14.setObjectName("q14")
        self.q24 = QtGui.QGraphicsView(self.centralwidget)
        self.q24.setGeometry(QtCore.QRect(230, 120, 40, 40))
        self.q24.setFrameShape(QtGui.QFrame.NoFrame)
        self.q24.setObjectName("q24")
        self.q25 = QtGui.QGraphicsView(self.centralwidget)
        self.q25.setGeometry(QtCore.QRect(280, 120, 40, 40))
        self.q25.setFrameShape(QtGui.QFrame.NoFrame)
        self.q25.setObjectName("q25")
        self.q05 = QtGui.QGraphicsView(self.centralwidget)
        self.q05.setGeometry(QtCore.QRect(280, 20, 40, 40))
        self.q05.setFrameShape(QtGui.QFrame.NoFrame)
        self.q05.setObjectName("q05")
        self.q15 = QtGui.QGraphicsView(self.centralwidget)
        self.q15.setGeometry(QtCore.QRect(280, 70, 40, 40))
        self.q15.setFrameShape(QtGui.QFrame.NoFrame)
        self.q15.setObjectName("q15")
        self.q04 = QtGui.QGraphicsView(self.centralwidget)
        self.q04.setGeometry(QtCore.QRect(230, 20, 40, 40))
        self.q04.setFrameShape(QtGui.QFrame.NoFrame)
        self.q04.setObjectName("q04")
        self.q13 = QtGui.QGraphicsView(self.centralwidget)
        self.q13.setGeometry(QtCore.QRect(180, 70, 40, 40))
        self.q13.setFrameShape(QtGui.QFrame.NoFrame)
        self.q13.setObjectName("q13")
        self.q44 = QtGui.QGraphicsView(self.centralwidget)
        self.q44.setGeometry(QtCore.QRect(230, 225, 40, 40))
        self.q44.setFrameShape(QtGui.QFrame.NoFrame)
        self.q44.setInteractive(False)
        self.q44.setObjectName("q44")
        self.q34 = QtGui.QGraphicsView(self.centralwidget)
        self.q34.setGeometry(QtCore.QRect(230, 175, 40, 40))
        self.q34.setFrameShape(QtGui.QFrame.NoFrame)
        self.q34.setObjectName("q34")
        self.q35 = QtGui.QGraphicsView(self.centralwidget)
        self.q35.setGeometry(QtCore.QRect(280, 175, 40, 40))
        self.q35.setFrameShape(QtGui.QFrame.NoFrame)
        self.q35.setObjectName("q35")
        self.q33 = QtGui.QGraphicsView(self.centralwidget)
        self.q33.setGeometry(QtCore.QRect(180, 175, 40, 40))
        self.q33.setFrameShape(QtGui.QFrame.NoFrame)
        self.q33.setObjectName("q33")
        self.q55 = QtGui.QGraphicsView(self.centralwidget)
        self.q55.setGeometry(QtCore.QRect(280, 275, 40, 40))
        self.q55.setFrameShape(QtGui.QFrame.NoFrame)
        self.q55.setObjectName("q55")
        self.q45 = QtGui.QGraphicsView(self.centralwidget)
        self.q45.setGeometry(QtCore.QRect(280, 225, 40, 40))
        self.q45.setFrameShape(QtGui.QFrame.NoFrame)
        self.q45.setObjectName("q45")
        self.q54 = QtGui.QGraphicsView(self.centralwidget)
        self.q54.setGeometry(QtCore.QRect(230, 275, 40, 40))
        self.q54.setFrameShape(QtGui.QFrame.NoFrame)
        self.q54.setObjectName("q54")
        self.q53 = QtGui.QGraphicsView(self.centralwidget)
        self.q53.setGeometry(QtCore.QRect(180, 275, 40, 40))
        self.q53.setFrameShape(QtGui.QFrame.NoFrame)
        self.q53.setObjectName("q53")
        self.q43 = QtGui.QGraphicsView(self.centralwidget)
        self.q43.setGeometry(QtCore.QRect(180, 225, 40, 40))
        self.q43.setFrameShape(QtGui.QFrame.NoFrame)
        self.q43.setObjectName("q43")
        self.q47 = QtGui.QGraphicsView(self.centralwidget)
        self.q47.setGeometry(QtCore.QRect(385, 225, 40, 40))
        self.q47.setFrameShape(QtGui.QFrame.NoFrame)
        self.q47.setInteractive(False)
        self.q47.setObjectName("q47")
        self.q37 = QtGui.QGraphicsView(self.centralwidget)
        self.q37.setGeometry(QtCore.QRect(385, 175, 40, 40))
        self.q37.setFrameShape(QtGui.QFrame.NoFrame)
        self.q37.setObjectName("q37")
        self.q38 = QtGui.QGraphicsView(self.centralwidget)
        self.q38.setGeometry(QtCore.QRect(435, 175, 40, 40))
        self.q38.setFrameShape(QtGui.QFrame.NoFrame)
        self.q38.setObjectName("q38")
        self.q36 = QtGui.QGraphicsView(self.centralwidget)
        self.q36.setGeometry(QtCore.QRect(335, 175, 40, 40))
        self.q36.setFrameShape(QtGui.QFrame.NoFrame)
        self.q36.setObjectName("q36")
        self.q58 = QtGui.QGraphicsView(self.centralwidget)
        self.q58.setGeometry(QtCore.QRect(435, 275, 40, 40))
        self.q58.setFrameShape(QtGui.QFrame.NoFrame)
        self.q58.setObjectName("q58")
        self.q48 = QtGui.QGraphicsView(self.centralwidget)
        self.q48.setGeometry(QtCore.QRect(435, 225, 40, 40))
        self.q48.setFrameShape(QtGui.QFrame.NoFrame)
        self.q48.setObjectName("q48")
        self.q57 = QtGui.QGraphicsView(self.centralwidget)
        self.q57.setGeometry(QtCore.QRect(385, 275, 40, 40))
        self.q57.setFrameShape(QtGui.QFrame.NoFrame)
        self.q57.setObjectName("q57")
        self.q56 = QtGui.QGraphicsView(self.centralwidget)
        self.q56.setGeometry(QtCore.QRect(335, 275, 40, 40))
        self.q56.setFrameShape(QtGui.QFrame.NoFrame)
        self.q56.setObjectName("q56")
        self.q46 = QtGui.QGraphicsView(self.centralwidget)
        self.q46.setGeometry(QtCore.QRect(335, 225, 40, 40))
        self.q46.setFrameShape(QtGui.QFrame.NoFrame)
        self.q46.setObjectName("q46")
        self.q410 = QtGui.QGraphicsView(self.centralwidget)
        self.q410.setGeometry(QtCore.QRect(540, 225, 40, 40))
        self.q410.setFrameShape(QtGui.QFrame.NoFrame)
        self.q410.setInteractive(False)
        self.q410.setObjectName("q410")
        self.q310 = QtGui.QGraphicsView(self.centralwidget)
        self.q310.setGeometry(QtCore.QRect(540, 175, 40, 40))
        self.q310.setFrameShape(QtGui.QFrame.NoFrame)
        self.q310.setObjectName("q310")
        self.q311 = QtGui.QGraphicsView(self.centralwidget)
        self.q311.setGeometry(QtCore.QRect(590, 175, 40, 40))
        self.q311.setFrameShape(QtGui.QFrame.NoFrame)
        self.q311.setObjectName("q311")
        self.q39 = QtGui.QGraphicsView(self.centralwidget)
        self.q39.setGeometry(QtCore.QRect(490, 175, 40, 40))
        self.q39.setFrameShape(QtGui.QFrame.NoFrame)
        self.q39.setObjectName("q39")
        self.q511 = QtGui.QGraphicsView(self.centralwidget)
        self.q511.setGeometry(QtCore.QRect(590, 275, 40, 40))
        self.q511.setFrameShape(QtGui.QFrame.NoFrame)
        self.q511.setObjectName("q511")
        self.q411 = QtGui.QGraphicsView(self.centralwidget)
        self.q411.setGeometry(QtCore.QRect(590, 225, 40, 40))
        self.q411.setFrameShape(QtGui.QFrame.NoFrame)
        self.q411.setObjectName("q411")
        self.q510 = QtGui.QGraphicsView(self.centralwidget)
        self.q510.setGeometry(QtCore.QRect(540, 275, 40, 40))
        self.q510.setFrameShape(QtGui.QFrame.NoFrame)
        self.q510.setObjectName("q510")
        self.q59 = QtGui.QGraphicsView(self.centralwidget)
        self.q59.setGeometry(QtCore.QRect(490, 275, 40, 40))
        self.q59.setFrameShape(QtGui.QFrame.NoFrame)
        self.q59.setObjectName("q59")
        self.q49 = QtGui.QGraphicsView(self.centralwidget)
        self.q49.setGeometry(QtCore.QRect(490, 225, 40, 40))
        self.q49.setFrameShape(QtGui.QFrame.NoFrame)
        self.q49.setObjectName("q49")
        self.q74 = QtGui.QGraphicsView(self.centralwidget)
        self.q74.setGeometry(QtCore.QRect(230, 380, 40, 40))
        self.q74.setFrameShape(QtGui.QFrame.NoFrame)
        self.q74.setInteractive(False)
        self.q74.setObjectName("q74")
        self.q64 = QtGui.QGraphicsView(self.centralwidget)
        self.q64.setGeometry(QtCore.QRect(230, 330, 40, 40))
        self.q64.setFrameShape(QtGui.QFrame.NoFrame)
        self.q64.setObjectName("q64")
        self.q65 = QtGui.QGraphicsView(self.centralwidget)
        self.q65.setGeometry(QtCore.QRect(280, 330, 40, 40))
        self.q65.setFrameShape(QtGui.QFrame.NoFrame)
        self.q65.setObjectName("q65")
        self.q63 = QtGui.QGraphicsView(self.centralwidget)
        self.q63.setGeometry(QtCore.QRect(180, 330, 40, 40))
        self.q63.setFrameShape(QtGui.QFrame.NoFrame)
        self.q63.setObjectName("q63")
        self.q85 = QtGui.QGraphicsView(self.centralwidget)
        self.q85.setGeometry(QtCore.QRect(280, 430, 40, 40))
        self.q85.setFrameShape(QtGui.QFrame.NoFrame)
        self.q85.setObjectName("q85")
        self.q75 = QtGui.QGraphicsView(self.centralwidget)
        self.q75.setGeometry(QtCore.QRect(280, 380, 40, 40))
        self.q75.setFrameShape(QtGui.QFrame.NoFrame)
        self.q75.setObjectName("q75")
        self.q84 = QtGui.QGraphicsView(self.centralwidget)
        self.q84.setGeometry(QtCore.QRect(230, 430, 40, 40))
        self.q84.setFrameShape(QtGui.QFrame.NoFrame)
        self.q84.setObjectName("q84")
        self.q83 = QtGui.QGraphicsView(self.centralwidget)
        self.q83.setGeometry(QtCore.QRect(180, 430, 40, 40))
        self.q83.setFrameShape(QtGui.QFrame.NoFrame)
        self.q83.setObjectName("q83")
        self.q73 = QtGui.QGraphicsView(self.centralwidget)
        self.q73.setGeometry(QtCore.QRect(180, 380, 40, 40))
        self.q73.setFrameShape(QtGui.QFrame.NoFrame)
        self.q73.setObjectName("q73")
        self.btnScramble = QtGui.QPushButton(self.centralwidget)
        self.btnScramble.setGeometry(QtCore.QRect(840, 320, 80, 80))
        self.btnScramble.setObjectName("btnScramble")
        self.btnSolve = QtGui.QPushButton(self.centralwidget)
        self.btnSolve.setGeometry(QtCore.QRect(840, 420, 80, 80))
        self.btnSolve.setObjectName("btnSolve")
        self.sliSpeed = QtGui.QSlider(self.centralwidget)
        self.sliSpeed.setGeometry(QtCore.QRect(675, 535, 241, 20))
        self.sliSpeed.setSliderPosition(80)
        self.sliSpeed.setOrientation(QtCore.Qt.Horizontal)
        self.sliSpeed.setTickPosition(QtGui.QSlider.NoTicks)
        self.sliSpeed.setObjectName("sliSpeed")
        self.proDone = QtGui.QProgressBar(self.centralwidget)
        self.proDone.setEnabled(True)
        self.proDone.setGeometry(QtCore.QRect(30, 490, 591, 23))
        self.proDone.setProperty("value", 100)
        self.proDone.setOrientation(QtCore.Qt.Horizontal)
        self.proDone.setTextDirection(QtGui.QProgressBar.TopToBottom)
        self.proDone.setObjectName("proDone")
        self.btnU = QtGui.QPushButton(self.centralwidget)
        self.btnU.setGeometry(QtCore.QRect(670, 200, 50, 50))
        self.btnU.setObjectName("btnU")
        self.btnU2 = QtGui.QPushButton(self.centralwidget)
        self.btnU2.setGeometry(QtCore.QRect(780, 200, 50, 50))
        self.btnU2.setObjectName("btnU2")
        self.btnUp = QtGui.QPushButton(self.centralwidget)
        self.btnUp.setGeometry(QtCore.QRect(725, 200, 50, 50))
        self.btnUp.setObjectName("btnUp")
        self.btnD = QtGui.QPushButton(self.centralwidget)
        self.btnD.setGeometry(QtCore.QRect(670, 255, 50, 50))
        self.btnD.setObjectName("btnD")
        self.btnDp = QtGui.QPushButton(self.centralwidget)
        self.btnDp.setGeometry(QtCore.QRect(725, 255, 50, 50))
        self.btnDp.setObjectName("btnDp")
        self.btnD2 = QtGui.QPushButton(self.centralwidget)
        self.btnD2.setGeometry(QtCore.QRect(780, 255, 50, 50))
        self.btnD2.setObjectName("btnD2")
        self.btnL = QtGui.QPushButton(self.centralwidget)
        self.btnL.setGeometry(QtCore.QRect(670, 310, 50, 50))
        self.btnL.setObjectName("btnL")
        self.btnLp = QtGui.QPushButton(self.centralwidget)
        self.btnLp.setGeometry(QtCore.QRect(725, 310, 50, 50))
        self.btnLp.setObjectName("btnLp")
        self.btnL2 = QtGui.QPushButton(self.centralwidget)
        self.btnL2.setGeometry(QtCore.QRect(780, 310, 50, 50))
        self.btnL2.setObjectName("btnL2")
        self.btnR = QtGui.QPushButton(self.centralwidget)
        self.btnR.setGeometry(QtCore.QRect(670, 365, 50, 50))
        self.btnR.setObjectName("btnR")
        self.btnRp = QtGui.QPushButton(self.centralwidget)
        self.btnRp.setGeometry(QtCore.QRect(725, 365, 50, 50))
        self.btnRp.setObjectName("btnRp")
        self.btnR2 = QtGui.QPushButton(self.centralwidget)
        self.btnR2.setGeometry(QtCore.QRect(780, 365, 50, 50))
        self.btnR2.setObjectName("btnR2")
        self.btnF = QtGui.QPushButton(self.centralwidget)
        self.btnF.setGeometry(QtCore.QRect(670, 420, 50, 50))
        self.btnF.setObjectName("btnF")
        self.btnFp = QtGui.QPushButton(self.centralwidget)
        self.btnFp.setGeometry(QtCore.QRect(725, 420, 50, 50))
        self.btnFp.setObjectName("btnFp")
        self.btnF2 = QtGui.QPushButton(self.centralwidget)
        self.btnF2.setGeometry(QtCore.QRect(780, 420, 50, 50))
        self.btnF2.setObjectName("btnF2")
        self.btnB = QtGui.QPushButton(self.centralwidget)
        self.btnB.setGeometry(QtCore.QRect(670, 475, 50, 50))
        self.btnB.setObjectName("btnB")
        self.btnBp = QtGui.QPushButton(self.centralwidget)
        self.btnBp.setGeometry(QtCore.QRect(725, 475, 50, 50))
        self.btnBp.setObjectName("btnBp")
        self.btnB2 = QtGui.QPushButton(self.centralwidget)
        self.btnB2.setGeometry(QtCore.QRect(780, 475, 50, 50))
        self.btnB2.setObjectName("btnB2")
        self.qB7 = QtGui.QGraphicsView(self.centralwidget)
        self.qB7.setGeometry(QtCore.QRect(660, 190, 270, 375))
        self.qB7.setFrameShape(QtGui.QFrame.NoFrame)
        self.qB7.setObjectName("qB7")
        self.qB2 = QtGui.QGraphicsView(self.centralwidget)
        self.qB2.setGeometry(QtCore.QRect(20, 170, 150, 150))
        self.qB2.setFrameShape(QtGui.QFrame.NoFrame)
        self.qB2.setObjectName("qB2")
        self.qB5 = QtGui.QGraphicsView(self.centralwidget)
        self.qB5.setGeometry(QtCore.QRect(485, 170, 150, 150))
        self.qB5.setFrameShape(QtGui.QFrame.NoFrame)
        self.qB5.setObjectName("qB5")
        self.qB4 = QtGui.QGraphicsView(self.centralwidget)
        self.qB4.setGeometry(QtCore.QRect(330, 170, 150, 150))
        self.qB4.setFrameShape(QtGui.QFrame.NoFrame)
        self.qB4.setObjectName("qB4")
        self.qB3 = QtGui.QGraphicsView(self.centralwidget)
        self.qB3.setGeometry(QtCore.QRect(175, 170, 150, 150))
        self.qB3.setFrameShape(QtGui.QFrame.NoFrame)
        self.qB3.setObjectName("qB3")
        self.qB1 = QtGui.QGraphicsView(self.centralwidget)
        self.qB1.setGeometry(QtCore.QRect(175, 15, 150, 150))
        self.qB1.setFrameShape(QtGui.QFrame.NoFrame)
        self.qB1.setFrameShadow(QtGui.QFrame.Sunken)
        self.qB1.setObjectName("qB1")
        self.qB6 = QtGui.QGraphicsView(self.centralwidget)
        self.qB6.setGeometry(QtCore.QRect(175, 325, 150, 150))
        self.qB6.setFrameShape(QtGui.QFrame.NoFrame)
        self.qB6.setObjectName("qB6")
        self.btnBlank = QtGui.QPushButton(self.centralwidget)
        self.btnBlank.setGeometry(QtCore.QRect(840, 220, 80, 80))
        self.btnBlank.setObjectName("btnBlank")
        self.qB12 = QtGui.QGraphicsView(self.centralwidget)
        self.qB12.setGeometry(QtCore.QRect(755, 100, 80, 80))
        self.qB12.setFrameShape(QtGui.QFrame.NoFrame)
        self.qB12.setObjectName("qB12")
        self.qB13 = QtGui.QGraphicsView(self.centralwidget)
        self.qB13.setGeometry(QtCore.QRect(850, 100, 80, 80))
        self.qB13.setFrameShape(QtGui.QFrame.NoFrame)
        self.qB13.setObjectName("qB13")
        self.qB8 = QtGui.QGraphicsView(self.centralwidget)
        self.qB8.setGeometry(QtCore.QRect(660, 10, 80, 80))
        self.qB8.setFrameShape(QtGui.QFrame.NoFrame)
        self.qB8.setObjectName("qB8")
        self.qB9 = QtGui.QGraphicsView(self.centralwidget)
        self.qB9.setGeometry(QtCore.QRect(755, 10, 80, 80))
        self.qB9.setFrameShape(QtGui.QFrame.NoFrame)
        self.qB9.setObjectName("qB9")
        self.qB10 = QtGui.QGraphicsView(self.centralwidget)
        self.qB10.setGeometry(QtCore.QRect(850, 10, 80, 80))
        self.qB10.setFrameShape(QtGui.QFrame.NoFrame)
        self.qB10.setObjectName("qB10")
        self.qB11 = QtGui.QGraphicsView(self.centralwidget)
        self.qB11.setGeometry(QtCore.QRect(660, 100, 80, 80))
        self.qB11.setFrameShape(QtGui.QFrame.NoFrame)
        self.qB11.setObjectName("qB11")
        self.qWhite = QtGui.QGraphicsView(self.centralwidget)
        self.qWhite.setGeometry(QtCore.QRect(670, 20, 60, 60))
        self.qWhite.setFrameShape(QtGui.QFrame.NoFrame)
        self.qWhite.setObjectName("qWhite")
        self.qOrange = QtGui.QGraphicsView(self.centralwidget)
        self.qOrange.setGeometry(QtCore.QRect(765, 20, 60, 60))
        self.qOrange.setFrameShape(QtGui.QFrame.NoFrame)
        self.qOrange.setObjectName("qOrange")
        self.qGreen = QtGui.QGraphicsView(self.centralwidget)
        self.qGreen.setGeometry(QtCore.QRect(860, 20, 60, 60))
        self.qGreen.setFrameShape(QtGui.QFrame.NoFrame)
        self.qGreen.setObjectName("qGreen")
        self.qRed = QtGui.QGraphicsView(self.centralwidget)
        self.qRed.setGeometry(QtCore.QRect(670, 110, 60, 60))
        self.qRed.setFrameShape(QtGui.QFrame.NoFrame)
        self.qRed.setObjectName("qRed")
        self.qBlue = QtGui.QGraphicsView(self.centralwidget)
        self.qBlue.setGeometry(QtCore.QRect(765, 110, 60, 60))
        self.qBlue.setFrameShape(QtGui.QFrame.NoFrame)
        self.qBlue.setObjectName("qBlue")
        self.qYellow = QtGui.QGraphicsView(self.centralwidget)
        self.qYellow.setGeometry(QtCore.QRect(860, 110, 60, 60))
        self.qYellow.setFrameShape(QtGui.QFrame.NoFrame)
        self.qYellow.setObjectName("qYellow")
        self.btn03 = QtGui.QPushButton(self.centralwidget)
        self.btn03.setGeometry(QtCore.QRect(180, 20, 40, 40))
        self.btn03.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.btn03.setObjectName("btn03")
        self.btn04 = QtGui.QPushButton(self.centralwidget)
        self.btn04.setGeometry(QtCore.QRect(230, 20, 40, 40))
        self.btn04.setObjectName("btn04")
        self.btn05 = QtGui.QPushButton(self.centralwidget)
        self.btn05.setGeometry(QtCore.QRect(280, 20, 40, 40))
        self.btn05.setObjectName("btn05")
        self.btn13 = QtGui.QPushButton(self.centralwidget)
        self.btn13.setGeometry(QtCore.QRect(180, 70, 40, 40))
        self.btn13.setObjectName("btn13")
        self.btn15 = QtGui.QPushButton(self.centralwidget)
        self.btn15.setGeometry(QtCore.QRect(280, 70, 40, 40))
        self.btn15.setObjectName("btn15")
        self.btn23 = QtGui.QPushButton(self.centralwidget)
        self.btn23.setGeometry(QtCore.QRect(180, 120, 40, 40))
        self.btn23.setObjectName("btn23")
        self.btn24 = QtGui.QPushButton(self.centralwidget)
        self.btn24.setGeometry(QtCore.QRect(230, 120, 40, 40))
        self.btn24.setObjectName("btn24")
        self.btn25 = QtGui.QPushButton(self.centralwidget)
        self.btn25.setGeometry(QtCore.QRect(280, 120, 40, 40))
        self.btn25.setObjectName("btn25")
        self.btn30 = QtGui.QPushButton(self.centralwidget)
        self.btn30.setGeometry(QtCore.QRect(25, 175, 40, 40))
        self.btn30.setObjectName("btn30")
        self.btn31 = QtGui.QPushButton(self.centralwidget)
        self.btn31.setGeometry(QtCore.QRect(75, 175, 40, 40))
        self.btn31.setObjectName("btn31")
        self.btn32 = QtGui.QPushButton(self.centralwidget)
        self.btn32.setGeometry(QtCore.QRect(125, 175, 40, 40))
        self.btn32.setObjectName("btn32")
        self.btn40 = QtGui.QPushButton(self.centralwidget)
        self.btn40.setGeometry(QtCore.QRect(25, 225, 40, 40))
        self.btn40.setObjectName("btn40")
        self.btn42 = QtGui.QPushButton(self.centralwidget)
        self.btn42.setGeometry(QtCore.QRect(125, 225, 40, 40))
        self.btn42.setObjectName("btn42")
        self.btn50 = QtGui.QPushButton(self.centralwidget)
        self.btn50.setGeometry(QtCore.QRect(25, 275, 40, 40))
        self.btn50.setObjectName("btn50")
        self.btn51 = QtGui.QPushButton(self.centralwidget)
        self.btn51.setGeometry(QtCore.QRect(75, 275, 40, 40))
        self.btn51.setObjectName("btn51")
        self.btn52 = QtGui.QPushButton(self.centralwidget)
        self.btn52.setGeometry(QtCore.QRect(125, 275, 40, 40))
        self.btn52.setObjectName("btn52")
        self.btn33 = QtGui.QPushButton(self.centralwidget)
        self.btn33.setGeometry(QtCore.QRect(180, 175, 40, 40))
        self.btn33.setObjectName("btn33")
        self.btn34 = QtGui.QPushButton(self.centralwidget)
        self.btn34.setGeometry(QtCore.QRect(230, 175, 40, 40))
        self.btn34.setObjectName("btn34")
        self.btn35 = QtGui.QPushButton(self.centralwidget)
        self.btn35.setGeometry(QtCore.QRect(280, 175, 40, 40))
        self.btn35.setObjectName("btn35")
        self.btn39 = QtGui.QPushButton(self.centralwidget)
        self.btn39.setGeometry(QtCore.QRect(490, 175, 40, 40))
        self.btn39.setObjectName("btn39")
        self.btn310 = QtGui.QPushButton(self.centralwidget)
        self.btn310.setGeometry(QtCore.QRect(540, 175, 40, 40))
        self.btn310.setObjectName("btn310")
        self.btn311 = QtGui.QPushButton(self.centralwidget)
        self.btn311.setGeometry(QtCore.QRect(590, 175, 40, 40))
        self.btn311.setObjectName("btn311")
        self.btn43 = QtGui.QPushButton(self.centralwidget)
        self.btn43.setGeometry(QtCore.QRect(180, 225, 40, 40))
        self.btn43.setObjectName("btn43")
        self.btn45 = QtGui.QPushButton(self.centralwidget)
        self.btn45.setGeometry(QtCore.QRect(280, 225, 40, 40))
        self.btn45.setObjectName("btn45")
        self.btn49 = QtGui.QPushButton(self.centralwidget)
        self.btn49.setGeometry(QtCore.QRect(490, 225, 40, 40))
        self.btn49.setObjectName("btn49")
        self.btn411 = QtGui.QPushButton(self.centralwidget)
        self.btn411.setGeometry(QtCore.QRect(590, 225, 40, 40))
        self.btn411.setObjectName("btn411")
        self.btn46 = QtGui.QPushButton(self.centralwidget)
        self.btn46.setGeometry(QtCore.QRect(335, 225, 40, 40))
        self.btn46.setObjectName("btn46")
        self.btn48 = QtGui.QPushButton(self.centralwidget)
        self.btn48.setGeometry(QtCore.QRect(435, 225, 40, 40))
        self.btn48.setObjectName("btn48")
        self.btn36 = QtGui.QPushButton(self.centralwidget)
        self.btn36.setGeometry(QtCore.QRect(335, 175, 40, 40))
        self.btn36.setObjectName("btn36")
        self.btn37 = QtGui.QPushButton(self.centralwidget)
        self.btn37.setGeometry(QtCore.QRect(385, 175, 40, 40))
        self.btn37.setObjectName("btn37")
        self.btn38 = QtGui.QPushButton(self.centralwidget)
        self.btn38.setGeometry(QtCore.QRect(435, 175, 40, 40))
        self.btn38.setObjectName("btn38")
        self.btn53 = QtGui.QPushButton(self.centralwidget)
        self.btn53.setGeometry(QtCore.QRect(180, 275, 40, 40))
        self.btn53.setObjectName("btn53")
        self.btn54 = QtGui.QPushButton(self.centralwidget)
        self.btn54.setGeometry(QtCore.QRect(230, 275, 40, 40))
        self.btn54.setObjectName("btn54")
        self.btn55 = QtGui.QPushButton(self.centralwidget)
        self.btn55.setGeometry(QtCore.QRect(280, 275, 40, 40))
        self.btn55.setObjectName("btn55")
        self.btn56 = QtGui.QPushButton(self.centralwidget)
        self.btn56.setGeometry(QtCore.QRect(335, 275, 40, 40))
        self.btn56.setObjectName("btn56")
        self.btn57 = QtGui.QPushButton(self.centralwidget)
        self.btn57.setGeometry(QtCore.QRect(385, 275, 40, 40))
        self.btn57.setObjectName("btn57")
        self.btn58 = QtGui.QPushButton(self.centralwidget)
        self.btn58.setGeometry(QtCore.QRect(435, 275, 40, 40))
        self.btn58.setObjectName("btn58")
        self.btn59 = QtGui.QPushButton(self.centralwidget)
        self.btn59.setGeometry(QtCore.QRect(490, 275, 40, 40))
        self.btn59.setObjectName("btn59")
        self.btn510 = QtGui.QPushButton(self.centralwidget)
        self.btn510.setGeometry(QtCore.QRect(540, 275, 40, 40))
        self.btn510.setObjectName("btn510")
        self.btn511 = QtGui.QPushButton(self.centralwidget)
        self.btn511.setGeometry(QtCore.QRect(590, 275, 40, 40))
        self.btn511.setObjectName("btn511")
        self.btn63 = QtGui.QPushButton(self.centralwidget)
        self.btn63.setGeometry(QtCore.QRect(180, 330, 40, 40))
        self.btn63.setObjectName("btn63")
        self.btn64 = QtGui.QPushButton(self.centralwidget)
        self.btn64.setGeometry(QtCore.QRect(230, 330, 40, 40))
        self.btn64.setObjectName("btn64")
        self.btn65 = QtGui.QPushButton(self.centralwidget)
        self.btn65.setGeometry(QtCore.QRect(280, 330, 40, 40))
        self.btn65.setObjectName("btn65")
        self.btn73 = QtGui.QPushButton(self.centralwidget)
        self.btn73.setGeometry(QtCore.QRect(180, 380, 40, 40))
        self.btn73.setObjectName("btn73")
        self.btn75 = QtGui.QPushButton(self.centralwidget)
        self.btn75.setGeometry(QtCore.QRect(280, 380, 40, 40))
        self.btn75.setObjectName("btn75")
        self.btn83 = QtGui.QPushButton(self.centralwidget)
        self.btn83.setGeometry(QtCore.QRect(180, 430, 40, 40))
        self.btn83.setObjectName("btn83")
        self.btn84 = QtGui.QPushButton(self.centralwidget)
        self.btn84.setGeometry(QtCore.QRect(230, 430, 40, 40))
        self.btn84.setObjectName("btn84")
        self.btn85 = QtGui.QPushButton(self.centralwidget)
        self.btn85.setGeometry(QtCore.QRect(280, 430, 40, 40))
        self.btn85.setObjectName("btn85")
        self.btnWhite = QtGui.QPushButton(self.centralwidget)
        self.btnWhite.setGeometry(QtCore.QRect(670, 20, 60, 60))
        self.btnWhite.setObjectName("btnWhite")
        self.btnOrange = QtGui.QPushButton(self.centralwidget)
        self.btnOrange.setGeometry(QtCore.QRect(765, 20, 60, 60))
        self.btnOrange.setObjectName("btnOrange")
        self.btnGreen = QtGui.QPushButton(self.centralwidget)
        self.btnGreen.setGeometry(QtCore.QRect(860, 20, 60, 60))
        self.btnGreen.setObjectName("btnGreen")
        self.btnRed = QtGui.QPushButton(self.centralwidget)
        self.btnRed.setGeometry(QtCore.QRect(670, 110, 60, 60))
        self.btnRed.setObjectName("btnRed")
        self.btnBlue = QtGui.QPushButton(self.centralwidget)
        self.btnBlue.setGeometry(QtCore.QRect(765, 110, 60, 60))
        self.btnBlue.setObjectName("btnBlue")
        self.btnYellow = QtGui.QPushButton(self.centralwidget)
        self.btnYellow.setGeometry(QtCore.QRect(860, 110, 60, 60))
        self.btnYellow.setObjectName("btnYellow")
        self.leScramble = QtGui.QLineEdit(self.centralwidget)
        self.leScramble.setGeometry(QtCore.QRect(30, 550, 591, 27))
        self.leScramble.setReadOnly(True)
        self.leScramble.setObjectName("leScramble")
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 530, 71, 17))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 590, 71, 17))
        self.label_2.setObjectName("label_2")
        self.txtSolution = QtGui.QTextEdit(self.centralwidget)
        self.txtSolution.setGeometry(QtCore.QRect(30, 610, 591, 171))
        self.txtSolution.setReadOnly(True)
        self.txtSolution.setObjectName("txtSolution")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.btnScramble.setText(QtGui.QApplication.translate("MainWindow", "Scramble", None, QtGui.QApplication.UnicodeUTF8))
        self.btnSolve.setText(QtGui.QApplication.translate("MainWindow", "Solve", None, QtGui.QApplication.UnicodeUTF8))
        self.btnU.setText(QtGui.QApplication.translate("MainWindow", "U", None, QtGui.QApplication.UnicodeUTF8))
        self.btnU2.setText(QtGui.QApplication.translate("MainWindow", "U2", None, QtGui.QApplication.UnicodeUTF8))
        self.btnUp.setText(QtGui.QApplication.translate("MainWindow", "U\'", None, QtGui.QApplication.UnicodeUTF8))
        self.btnD.setText(QtGui.QApplication.translate("MainWindow", "D", None, QtGui.QApplication.UnicodeUTF8))
        self.btnDp.setText(QtGui.QApplication.translate("MainWindow", "D\'", None, QtGui.QApplication.UnicodeUTF8))
        self.btnD2.setText(QtGui.QApplication.translate("MainWindow", "D2", None, QtGui.QApplication.UnicodeUTF8))
        self.btnL.setText(QtGui.QApplication.translate("MainWindow", "L", None, QtGui.QApplication.UnicodeUTF8))
        self.btnLp.setText(QtGui.QApplication.translate("MainWindow", "L\'", None, QtGui.QApplication.UnicodeUTF8))
        self.btnL2.setText(QtGui.QApplication.translate("MainWindow", "L2", None, QtGui.QApplication.UnicodeUTF8))
        self.btnR.setText(QtGui.QApplication.translate("MainWindow", "R", None, QtGui.QApplication.UnicodeUTF8))
        self.btnRp.setText(QtGui.QApplication.translate("MainWindow", "R\'", None, QtGui.QApplication.UnicodeUTF8))
        self.btnR2.setText(QtGui.QApplication.translate("MainWindow", "R2", None, QtGui.QApplication.UnicodeUTF8))
        self.btnF.setText(QtGui.QApplication.translate("MainWindow", "F", None, QtGui.QApplication.UnicodeUTF8))
        self.btnFp.setText(QtGui.QApplication.translate("MainWindow", "F\'", None, QtGui.QApplication.UnicodeUTF8))
        self.btnF2.setText(QtGui.QApplication.translate("MainWindow", "F2", None, QtGui.QApplication.UnicodeUTF8))
        self.btnB.setText(QtGui.QApplication.translate("MainWindow", "B", None, QtGui.QApplication.UnicodeUTF8))
        self.btnBp.setText(QtGui.QApplication.translate("MainWindow", "B\'", None, QtGui.QApplication.UnicodeUTF8))
        self.btnB2.setText(QtGui.QApplication.translate("MainWindow", "B2", None, QtGui.QApplication.UnicodeUTF8))
        self.btnBlank.setText(QtGui.QApplication.translate("MainWindow", "Blank", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Scramble:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Solution:", None, QtGui.QApplication.UnicodeUTF8))

