#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 13:35:51 2017

@author: tracy
"""
import sys, math
import platform
from PyQt5.QtWidgets import (QMainWindow,QFileDialog, QMessageBox, QAction, QWidget, QPushButton, QCheckBox, QLabel, QLineEdit, 
     QGridLayout, QApplication)
from PyQt5.QtGui import (QPainter,QFont, QColor)
from PyQt5 import QtGui, QtCore


from PyQt5.QtCore import QT_VERSION_STR, PYQT_VERSION_STR

class GRAPHIC(QMainWindow):
    
    def __init__(self, MSDG):
        super(GRAPHIC, self).__init__(MSDG)
        
        self.setGeometry(300, 100, 450, 450)
        self.setWindowTitle('Diagram')
 
        global text1, text2, text3, text4, M
        
  
    def paintEvent(self, MSDG):
        global x, y, Angles
     
        qp = QPainter()
        qp.begin(self)
        self.drawArrows(qp)
        self.drawEllipses(qp)
        self.drawText(qp)
        qp.end()
        
    def drawArrows(self, qp):
       
        self.pen = QtGui.QPen(QtGui.QColor(0,0,0))          # set lineColor
        self.pen.setWidth(2)                                # set lineWidth
        self.brush = QtGui.QBrush(QtGui.QColor(1,1,1))      # set fillColor  
        qp.setPen(self.pen)
        qp.setBrush(self.brush)
        
       #Create Arrow Tips
        if M[0][1] == 2:
            self.polygon = self.createPoly(3,6,Angles[0],1,56)          # polygon with n points, radius, angle of the first point      
            qp.drawPolygon(self.polygon)
        if M[0][2] == 2:
            self.polygon = self.createPoly(3,6,Angles[1],2,56)        
            qp.drawPolygon(self.polygon)
        if M[0][3] == 2:
            self.polygon = self.createPoly(3,6,Angles[2],3,56)           
            qp.drawPolygon(self.polygon)
        if M[1][0] == 2:
            self.polygon = self.createPoly(3,6,Angles[3],0,56)           
            qp.drawPolygon(self.polygon)
            
        if M[1][2] == 2:
            self.polygon = self.createPoly(3,6,Angles[4],2,56)
            qp.drawPolygon(self.polygon)
        if M[1][3] == 2:
            self.polygon = self.createPoly(3,6,Angles[5],3,56)
            qp.drawPolygon(self.polygon)
        if M[2][0] == 2:
            self.polygon = self.createPoly(3,6,Angles[6],0,56)
            qp.drawPolygon(self.polygon)
        if M[2][1] == 2:
            self.polygon = self.createPoly(3,6,Angles[7],1,56)         
            qp.drawPolygon(self.polygon)
            
        if M[2][3] == 2:
            self.polygon = self.createPoly(3,6,Angles[8],3,56)            
            qp.drawPolygon(self.polygon)
        if M[3][0] == 2:
            self.polygon = self.createPoly(3,6,Angles[9],0,56)            
            qp.drawPolygon(self.polygon)
        if M[3][1] == 2:
            self.polygon = self.createPoly(3,6,Angles[10],1,56)           
            qp.drawPolygon(self.polygon)
        if M[3][2] == 2:
            self.polygon = self.createPoly(3,6,Angles[11],2,56)            
            qp.drawPolygon(self.polygon)
            
            
        
        for i in range(0,4):                                                # Draw Arrow Lines
            if M[i][0] == 2:
                qp.drawLine(x[i] + 50, y[i] + 50, x[0] + 50, y[0] + 50)
            if M[i][1] == 2:
                qp.drawLine(x[i] + 50, y[i] + 50, x[1] + 50, y[1] + 50)
            if M[i][2] == 2:
                qp.drawLine(x[i] + 50, y[i] + 50, x[2] + 50, y[2] + 50)
            if M[i][3] == 2:
                qp.drawLine(x[i] + 50, y[i] + 50, x[3] + 50, y[3] + 50)
        
#        qp.drawPolygon(self.polygon)
                        
    def drawEllipses(self, qp):                         #draw ellipses for states
        self.pen = QtGui.QPen(QtGui.QColor(0,0,0))       # set lineColor
        self.pen.setWidth(2)                                #set line width
        qp.setPen(self.pen)

        if len(text1) > 0:
            qp.setBrush(QColor(255, 255, 255))          #set fill color 
            qp.drawEllipse(x[0], y[0], 100, 100)
        if len(text2) > 0:
            qp.drawEllipse(x[1], y[1], 100, 100)
        if len(text3) > 0:
            qp.drawEllipse(x[2], y[2], 100, 100)
        if len(text4) > 0:
            qp.drawEllipse(x[3], y[3], 100, 100)
                             
    def drawText(self, qp):
      
        qp.setPen(QColor(168, 34, 3))
        qp.setFont(QFont('Decorative', 12))
        qp.drawText(x[0] + 10, y[0] + 55, text1)
        qp.drawText(x[1] + 10, y[1] + 55, text2)
        qp.drawText(x[2] + 10, y[2] + 55, text3)
        qp.drawText(x[3] + 10, y[3] + 55, text4)
        
    def createPoly(self, n, r, s, c, r2):
            
            horizontal = r2*math.cos(math.radians(s))                       #calculate x difference on circle using polar coordinates to rectangular
            vertical = r2*math.sin(math.radians(s))                         #calculate y difference on circle using polar coordinates to rectangular
                        
            polygon = QtGui.QPolygonF() 
            w = 360/n                                                       # angle per step
            for i in range(n):                                              # add the points of polygon
                t = w*i + s
                z = r*math.cos(math.radians(t))
                zz = r*math.sin(math.radians(t))
                polygon.append(QtCore.QPointF(x[c] + 50 - horizontal + z, y[c] + 50 - vertical + zz))       #assign points of the arrowhead
            return polygon


class MSDG(QMainWindow):
    
    def __init__(self, parent=None):
        super(MSDG, self).__init__(parent)
        
        self.initUI()
            
        self.dialog = GRAPHIC(self)
        
    def initUI(self):
        
        ########################################################################
        # ADD MENU ITEMS
        ########################################################################
        
        # Create the File menu
        self.menuFile = self.menuBar().addMenu("&File")
        self.actionSaveAs = QAction("&Save As", self)
        self.actionSaveAs.triggered.connect(self.saveas)
        self.actionQuit = QAction("&Quit", self)
        self.actionQuit.triggered.connect(self.close)
        self.menuFile.addActions([self.actionSaveAs, self.actionQuit])
        
        # Create the Help menu
        self.menuHelp = self.menuBar().addMenu("&Help")
        self.actionAbout = QAction("&About",self)
        self.actionAbout.triggered.connect(self.about)
        self.menuHelp.addActions([self.actionAbout])
        
        ########################################################################
        # CREATE CENTRAL WIDGET
        ########################################################################
        
        self.widget = QWidget()
        
        columntitle1 = QLabel('States')
        list1 = QLabel('A')
        list2 = QLabel('B')
        list3 = QLabel('C')
        list4 = QLabel('D')
        
        columntitle2 = QLabel('     Name')
        self.name1 = QLineEdit()
        self.name2 = QLineEdit()
        self.name3 = QLineEdit()
        self.name4 = QLineEdit()
        
        grid = QGridLayout()
        grid.setSpacing(5)

        grid.addWidget(columntitle1, 1, 0)
        grid.addWidget(list1, 2, 0)
        grid.addWidget(list2, 3, 0)
        grid.addWidget(list3, 4, 0)
        grid.addWidget(list4, 5, 0)
        
        grid.addWidget(columntitle2, 1, 1)
        grid.addWidget(self.name1, 2, 1)
        grid.addWidget(self.name2, 3, 1)
        grid.addWidget(self.name3, 4, 1)
        grid.addWidget(self.name4, 5, 1)
        
        grid.addWidget(QLabel('A'), 1, 2)
        grid.addWidget(QLabel('B'), 1, 3)        
        grid.addWidget(QLabel('C'), 1, 4)
        grid.addWidget(QLabel('D'), 1, 5)
        
#       Create Checkboxes
        self.cb1 = QCheckBox()
        self.cb2 = QCheckBox()
        self.cb3 = QCheckBox()
        self.cb4 = QCheckBox()
        self.cb5 = QCheckBox()
        self.cb6 = QCheckBox()
        self.cb7 = QCheckBox()
        self.cb8 = QCheckBox()
        self.cb9 = QCheckBox()
        self.cb10 = QCheckBox()
        self.cb11 = QCheckBox()
        self.cb12 = QCheckBox()
        self.cb13 = QCheckBox()
        self.cb14 = QCheckBox()
        self.cb15 = QCheckBox()
        self.cb16 = QCheckBox()
        
#       Implement Checkboxes
#        grid.addWidget(self.cb1, 2, 2)
        grid.addWidget(self.cb2, 2, 3)
        grid.addWidget(self.cb3, 2, 4)
        grid.addWidget(self.cb4, 2, 5)
        grid.addWidget(self.cb5, 3, 2)
#        grid.addWidget(self.cb6, 3, 3)
        grid.addWidget(self.cb7, 3, 4)
        grid.addWidget(self.cb8, 3, 5)
        grid.addWidget(self.cb9, 4, 2)
        grid.addWidget(self.cb10, 4, 3)
#        grid.addWidget(self.cb11, 4, 4)
        grid.addWidget(self.cb12, 4, 5)
        grid.addWidget(self.cb13, 5, 2)
        grid.addWidget(self.cb14, 5, 3)
        grid.addWidget(self.cb15, 5, 4)
#        grid.addWidget(self.cb16, 5, 5)
              
#       Create Button to Create Diagram
        self.generate = QPushButton('Generate')
        self.generate.clicked.connect(self.calculate)
        
        grid.addWidget(self.generate, 6, 8)
            
        self.widget.setLayout(grid) 
        self.setCentralWidget(self.widget)
        
        self.setGeometry(600, 250, 350, 100)
        self.setWindowTitle('Machine State Diagram Generator')    
        self.show()
            
    def calculate(self):
        global M      
        # Create State Connections Matrix
        M = [[self.cb1.checkState(), self.cb2.checkState(), self.cb3.checkState(),self.cb4.checkState()],
                   [self.cb5.checkState(), self.cb6.checkState(), self.cb7.checkState(), self.cb8.checkState()],
                   [self.cb9.checkState(), self.cb10.checkState(), self.cb11.checkState(), self.cb12.checkState()],
                   [self.cb13.checkState(), self.cb14.checkState(), self.cb15.checkState(), self.cb16.checkState()]]
        
#        print(M)
        
        #to find the state with the most connections i have done a boolean or
        #comparison between each states row of connections and column connections.
        count = 0
        connections = [None,None,None,None]
        for i in range(0,4):
            for j in range(0,4):
                if M[i][j] == 2 or M[j][i] == 2:
                    count = count + 1
            connections[i] = count
            count = 0
        print(connections)
#        A = con[0]
#        B = con[1]
#        C = con[2]
#        D = con[3]
        
        global x, y, Angles
        x = [None, None, None, None]
        y = [None, None, None, None]
        Angles = [None, None, None, None, None, None, None, None, None, None, None, None]       #these are the angles of the arrowheads that are passed to the Graphic class
      
        #this section creates the configuration of the state bubbles
        #This configuration is square although other shapes could be implemented
#        if A == B == C == D:
        y[0] = y[1] = 100
        y[2] = y[3] = 250
        x[0] = x[2] = 100
        x[1] = x[3] = 250
        Angles = [0,90,45,180,135,90,270,315,0,225,270,180]
                  
        global text1, text2, text3, text4
        text1= self.name1.text()
        text2= self.name2.text()
        text3= self.name3.text()
        text4= self.name4.text()

        self.dialog.show()                      #Create second window with the graphic
        
    def saveas(self):
        
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","","All Files (*);;Text Files (*.txt)", options=options)
        if fileName:
            print(fileName)
            file = open(fileName,'w')
            text = "x = " + self.edit1.text() + "\n" + "f(x) = " + self.edit2.text()
            file.write(text)
            file.close()
        
    def about(self):
        QMessageBox.about(self, 
            "About Machine State Diagram Generator",
            """<b>Machine State Diagram Generator</b>
               <p>Copyright &copy; 2017 Tracy Schmitz, All Rights Reserved.
               <p>Python %s -- Qt %s -- PyQt %s on %s""" %
            (platform.python_version(),
             QT_VERSION_STR, PYQT_VERSION_STR, platform.system()))
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = MSDG()
    sys.exit(app.exec_())