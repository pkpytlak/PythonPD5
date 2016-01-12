#!/opt/anaconda34/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore

class MainWindow(QtGui.QMainWindow):
    def __init__(self, names):
        super(MainWindow, self).__init__()
        self.names = names
        closeAction = QtGui.QAction(QtGui.QIcon('challenger.jpg'), '&Close', self)        
        closeAction.setShortcut('Ctrl+Q')
        closeAction.triggered.connect(QtGui.qApp.quit)
        optionsAction = QtGui.QAction(QtGui.QIcon('challenger2.jpg') , '&Options' , self)          
        optionsAction.setShortcut('Ctrl+O')
        optionsAction.triggered.connect(self.options)
        helpAction = QtGui.QAction(QtGui.QIcon('challenger3.jpg'), '&About', self)        
        helpAction.setShortcut('Ctrl+H')
        helpAction.triggered.connect(self.about)
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(optionsAction)
        fileMenu.addAction(closeAction)
        helpMenu = menubar.addMenu('&Help')
        helpMenu.addAction(helpAction)
        self.initUI()
    def initUI(self):
        self.widget = Sudoku(self.names)
        self.setCentralWidget(self.widget)
        self.setGeometry(200, 75, 600, 600)
        self.setWindowTitle('Sudoku')
        self.show()
    def about(self):
        aw = QtGui.QDialog(self)
        aw.label = QtGui.QLabel('This is a "Sudoku" game. Enjoy!', aw)
        aw.label.move(10, 10)
        aw.setWindowTitle('About')
        aw.setGeometry(300, 125, 450, 450)
        aw.show()
    def options(self):
        ow = QtGui.QDialog(self)
        ow.label = QtGui.QLabel('Choose a board from the list below:', ow)
        ow.label.move(10, 10)
        boards = ['Board 1 (default)', 'Board 2', 'Board 3']
        boardNumber = len(boards)
        rb = []
        a = 0
        for board in boards:
            rb.append(QtGui.QRadioButton(board, ow))
            a = a + 1
        a = 0
        for board in boards:
            rb[a].move(10, 40+20*a)
            a = a + 1
        ow.setWindowTitle('Options')
        ow.setGeometry(300, 125, 450, 450)
        ow.show()
        #rb[0].setChecked(True)
        rb[0].toggled.connect(lambda: self.selectBoard1(rb[0]))
        rb[1].toggled.connect(lambda: self.selectBoard2(rb[1]))
        rb[2].toggled.connect(lambda: self.selectBoard3(rb[2]))
    def selectBoard1(self, button):
        names1 = ['.', '5', '.', '3', '.', '6', '.', '.', '7',
                  '.', '.', '.', '.', '8', '5', '.', '2', '4',
                  '.', '9', '8', '4', '2', '.', '6', '.', '3',
                  '9', '.', '1', '.', '.', '3', '2', '.', '6',
                  '.', '3', '.', '.', '.', '.', '.', '1', '.',
                  '5', '.', '7', '2', '6', '.', '9', '.', '8',
                  '4', '.', '5', '.', '9', '.', '3', '8', '.',
                  '.', '1', '.', '5', '7', '.', '.', '.', '2',
                  '8', '.', '.', '1', '.', '4', '.', '7', '.']
        if button.isChecked() == True:
            self.names = names1
            self.initUI()
            self.setWindowTitle('Sudoku: Board1')
    def selectBoard2(self, button):
        names2 = ['7', '.', '6', '.', '.', '1', '.', '8', '.',
                 '8', '.', '.', '7', '8', '5', '.', '4', '9',
                 '.', '1', '3', '.', '5', '4', '2', '.', '7',
                 '.', '.', '4', '3', '.', '7', '.', '5', '.',
                 '6', '2', '.', '9', '.', '5', '.', '.', '1',
                 '.', '3', '.', '6', '.', '2', '8', '.', '.',
                 '2', '.', '5', '4', '3', '.', '9', '1', '.',
                 '3', '.', '.', '.', '.', '9', '.', '.', '8',
                 '4', '8', '.', '1', '2', '.', '7', '.', '.']
        if button.isChecked() == True:
            self.names = names2
            self.initUI()
            self.setWindowTitle('Sudoku: Board2')
    def selectBoard3(self, button):
        names3 = ['.', '9', '2', '5', '.', '.', '4', '.', '.',
                  '1', '.', '.', '.', '3', '.', '.', '9', '6',
                  '8', '.', '6', '.', '9', '7', '3', '.', '1',
                  '.', '.', '8', '.', '7', '3', '6', '2', '.',
                  '7', '.', '3', '1', '.', '5', '8', '.', '9',
                  '.', '5', '4', '9', '6', '.', '7', '.', '.',
                  '5', '.', '1', '6', '8', '.', '.', '7', '4',
                  '4', '2', '.', '.', '5', '.', '.', '.', '.',
                  '.', '.', '9', '.', '.', '1', '.', '3', '2']
        if button.isChecked() == True:
            self.names = names3
            self.initUI()
            self.setWindowTitle('Sudoku: Board3')

class GridButton(QtGui.QPushButton):
    def __init__(self, name):
        super(GridButton, self).__init__(name)
        self.setAcceptDrops(True)
        self.button_name = name
    def dragEnterEvent(self, event):
        if self.button_name == '.':
            event.accept()
        else:
            event.ignore()
    def dropEvent(self, event):
        self.setText(event.mimeData().text())

class DigitButton1(QtGui.QPushButton):
    def __init__(self, name):
        super(DigitButton1, self).__init__(name)
    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            mimeData = QtCore.QMimeData()
            drag = QtGui.QDrag(self)
            mimeData.setText('1')
            drag.setMimeData(mimeData)
            drag.setHotSpot(event.pos())
            dropAction = drag.start(QtCore.Qt.MoveAction)

class DigitButton2(DigitButton1):
    def __init__(self, name):
        super(DigitButton2, self).__init__(name)
    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            mimeData = QtCore.QMimeData()
            drag = QtGui.QDrag(self)
            mimeData.setText('2')
            drag.setMimeData(mimeData)
            drag.setHotSpot(event.pos())
            dropAction = drag.start(QtCore.Qt.MoveAction)

class DigitButton3(DigitButton1):
    def __init__(self, name):
        super(DigitButton3, self).__init__(name)
    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            mimeData = QtCore.QMimeData()
            drag = QtGui.QDrag(self)
            mimeData.setText('3')
            drag.setMimeData(mimeData)
            drag.setHotSpot(event.pos())
            dropAction = drag.start(QtCore.Qt.MoveAction)

class DigitButton4(DigitButton1):
    def __init__(self, name):
        super(DigitButton4, self).__init__(name)
    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            mimeData = QtCore.QMimeData()
            drag = QtGui.QDrag(self)
            mimeData.setText('4')
            drag.setMimeData(mimeData)
            drag.setHotSpot(event.pos())
            dropAction = drag.start(QtCore.Qt.MoveAction)            

class DigitButton5(DigitButton1):
    def __init__(self, name):
        super(DigitButton5, self).__init__(name)
    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            mimeData = QtCore.QMimeData()
            drag = QtGui.QDrag(self)
            mimeData.setText('5')
            drag.setMimeData(mimeData)
            drag.setHotSpot(event.pos())
            dropAction = drag.start(QtCore.Qt.MoveAction)

class DigitButton6(DigitButton1):
    def __init__(self, name):
        super(DigitButton6, self).__init__(name)
    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            mimeData = QtCore.QMimeData()
            drag = QtGui.QDrag(self)
            mimeData.setText('6')
            drag.setMimeData(mimeData)
            drag.setHotSpot(event.pos())
            dropAction = drag.start(QtCore.Qt.MoveAction)
            
class DigitButton7(DigitButton1):
    def __init__(self, name):
        super(DigitButton7, self).__init__(name)
    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            mimeData = QtCore.QMimeData()
            drag = QtGui.QDrag(self)
            mimeData.setText('7')
            drag.setMimeData(mimeData)
            drag.setHotSpot(event.pos())
            dropAction = drag.start(QtCore.Qt.MoveAction)

class DigitButton8(DigitButton1):
    def __init__(self, name):
        super(DigitButton8, self).__init__(name)
    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            mimeData = QtCore.QMimeData()
            drag = QtGui.QDrag(self)
            mimeData.setText('8')
            drag.setMimeData(mimeData)
            drag.setHotSpot(event.pos())
            dropAction = drag.start(QtCore.Qt.MoveAction) 

class DigitButton9(DigitButton1):
    def __init__(self, name):
        super(DigitButton9, self).__init__(name)
    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            mimeData = QtCore.QMimeData()
            drag = QtGui.QDrag(self)
            mimeData.setText('9')
            drag.setMimeData(mimeData)
            drag.setHotSpot(event.pos())
            dropAction = drag.start(QtCore.Qt.MoveAction)      
    
class Digits(QtGui.QWidget):
    def __init__(self):
        super(Digits, self).__init__()
        self.initUI()
    def initUI(self):
        grid = QtGui.QGridLayout()
        self.setLayout(grid)
        names = ['1','2','3','4','5','6','7','8','9']
        positions = [(i,j) for i in range(9) for j in range(1)]
        button1 = DigitButton1(names[0])
        button2 = DigitButton2(names[1])
        button3 = DigitButton3(names[2])
        button4 = DigitButton4(names[3])
        button5 = DigitButton5(names[4])
        button6 = DigitButton6(names[5])
        button7 = DigitButton7(names[6])
        button8 = DigitButton8(names[7])
        button9 = DigitButton9(names[8])
        grid.addWidget(button1, *positions[0])
        grid.addWidget(button2, *positions[1])
        grid.addWidget(button3, *positions[2])
        grid.addWidget(button4, *positions[3])
        grid.addWidget(button5, *positions[4])
        grid.addWidget(button6, *positions[5])
        grid.addWidget(button7, *positions[6])
        grid.addWidget(button8, *positions[7])
        grid.addWidget(button9, *positions[8])


class Board(QtGui.QWidget):
    def __init__(self, names):
        super(Board, self).__init__()
        self.names = names
        self.initUI()
    def initUI(self):
        grid = QtGui.QGridLayout()
        self.grid = grid
        self.grid.setSpacing(0)
        self.setLayout(grid)
        positions = [(i,j) for i in range(9) for j in range(9)]
        for position, name in zip(positions, self.names):
            if name == '':
                continue
            if name != '.':
                button = GridButton(name)
                button.setStyleSheet('QPushButton {background-color: orange; color: black;}')
            else:
                button = GridButton(name)
            grid.addWidget(button, *position)


class Sudoku(QtGui.QWidget):
    def __init__(self, names):
        super(Sudoku, self).__init__()
        self.names = names
        self.initUI()
    def initUI(self):
        vbox = QtGui.QVBoxLayout(self)
        splitter = QtGui.QSplitter(QtCore.Qt.Horizontal)
        splitter.addWidget(Board(self.names))
        splitter.addWidget(Digits())
        vbox.addWidget(splitter)
        self.setLayout(vbox)
        self.setAcceptDrops(True)
        

def main():
    app = QtGui.QApplication(sys.argv)
    names0 = ['.', '5', '.', '3', '.', '6', '.', '.', '7',
              '.', '.', '.', '.', '8', '5', '.', '2', '4',
              '.', '9', '8', '4', '2', '.', '6', '.', '3',
              '9', '.', '1', '.', '.', '3', '2', '.', '6',
              '.', '3', '.', '.', '.', '.', '.', '1', '.',
              '5', '.', '7', '2', '6', '.', '9', '.', '8',
              '4', '.', '5', '.', '9', '.', '3', '8', '.',
              '.', '1', '.', '5', '7', '.', '.', '.', '2',
              '8', '.', '.', '1', '.', '4', '.', '7', '.']
    main = MainWindow(names0)
    app.exec_()
    
if __name__ == '__main__':
    main()