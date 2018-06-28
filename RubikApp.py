import sys
from PySide.QtCore import *
from PySide.QtGui import *
from rubikUI import *
from rubik import *
from algorithms import *
import random
import time

class RubikApp(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(RubikApp, self).__init__(parent)
        self.setupUi(self)

        self.cube = Cube()

        self.btnMix.clicked.connect(self.scramble)
        self.btnSolve.clicked.connect(self.solve)

        self.white = QGraphicsScene(); self.white.setBackgroundBrush(QColor(255, 255, 255))
        self.orange = QGraphicsScene(); self.orange.setBackgroundBrush(QColor(255, 192, 0))
        self.green = QGraphicsScene(); self.green.setBackgroundBrush(QColor(0, 175, 80))
        self.red = QGraphicsScene(); self.red.setBackgroundBrush(QColor(254, 0, 0))
        self.blue = QGraphicsScene(); self.blue.setBackgroundBrush(QColor(1, 176, 241))
        self.yellow = QGraphicsScene(); self.yellow.setBackgroundBrush(QColor(255, 255, 1))

        self.facets = [[0, 0, 0, self.q03, self.q04, self.q05, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, self.q13, self.q14, self.q15, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, self.q23, self.q24, self.q25, 0, 0, 0, 0, 0, 0],
                       [self.q30, self.q31, self.q32, self.q33, self.q34, self.q35, self.q36, self.q37, self.q38, self.q39, self.q310, self.q311],
                       [self.q40, self.q41, self.q42, self.q43, self.q44, self.q45, self.q46, self.q47, self.q48, self.q49, self.q410, self.q411],
                       [self.q50, self.q51, self.q52, self.q53, self.q54, self.q55, self.q56, self.q57, self.q58, self.q59, self.q510, self.q511],
                       [0, 0, 0, self.q63, self.q64, self.q65, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, self.q73, self.q74, self.q75, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, self.q83, self.q84, self.q85, 0, 0, 0, 0, 0, 0]]
        self.update()

    def update(self):
        for (i, j), facet in np.ndenumerate(self.cube.puz):
            if facet == "W": self.facets[i][j].setScene(self.white)
            elif facet == "O": self.facets[i][j].setScene(self.orange)
            elif facet == "G": self.facets[i][j].setScene(self.green)
            elif facet == "R": self.facets[i][j].setScene(self.red)
            elif facet == "B": self.facets[i][j].setScene(self.blue)
            elif facet == "Y": self.facets[i][j].setScene(self.yellow)

    def scramble(self):
        moves = [U, Up, U2, D, Dp, D2, R, Rp, R2, L, Lp, L2, F, Fp, F2, B, Bp, B2]
        self.cube.scramble = []
        choice = random.choice(moves)
        for i in range(20):
            self.cube.scramble.append(choice)
            choice = random.choice([move for move in moves if move.__name__[0] != choice.__name__[0]])
        self.execute(self.cube.scramble)

    def execute(self, algorithm):
        self.cube.solution.extend(algorithm)
        self.cube.solLen += len(algorithm)
        for move in algorithm:
            move(self.cube.puz)
            self.update()
            time.sleep(0.05)
            QApplication.processEvents()

    def solve(self):
        self.cube.solution = []
        self.cube.solLen = 0
        bEdges(self)
        bCorners(self)
        mEdges(self)
        OLL(self)
        PLL(self)

if __name__ == "__main__":
    currentApp = QApplication(sys.argv)
    currentForm = RubikApp()

    currentForm.show()
currentApp.exec_()