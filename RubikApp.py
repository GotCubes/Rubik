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

        # Initialize cube.
        self.cube = Cube()
        self.speed = 100 - self.sliSpeed.value()
        self.buttons = [self.btnU, self.btnUp, self.btnU2,
                        self.btnD, self.btnDp, self.btnD2,
                        self.btnL, self.btnLp, self.btnL2,
                        self.btnR, self.btnRp, self.btnR2,
                        self.btnF, self.btnFp, self.btnF2,
                        self.btnB, self.btnBp, self.btnB2]
        self.moves = [U, Up, U2, D, Dp, D2, L, Lp, L2, R, Rp, R2, F, Fp, F2, B, Bp, B2]

        # Define connections.
        for i in range(18): self.buttons[i].clicked.connect(self.moveHandler(self.moves[i]))
        self.btnScramble.clicked.connect(self.scramble)
        self.btnSolve.clicked.connect(self.solve)
        self.sliSpeed.valueChanged.connect(self.setSpeed)
        self.proDone.hide()

        # Initialize facet colors.
        self.white = QGraphicsScene(); self.white.setBackgroundBrush(QColor(255, 255, 255))
        self.orange = QGraphicsScene(); self.orange.setBackgroundBrush(QColor(255, 192, 0))
        self.green = QGraphicsScene(); self.green.setBackgroundBrush(QColor(0, 175, 80))
        self.red = QGraphicsScene(); self.red.setBackgroundBrush(QColor(254, 0, 0))
        self.blue = QGraphicsScene(); self.blue.setBackgroundBrush(QColor(1, 176, 241))
        self.yellow = QGraphicsScene(); self.yellow.setBackgroundBrush(QColor(255, 255, 1))
        self.black = QGraphicsScene(); self.black.setBackgroundBrush(QColor(0, 0, 0))

        # Group facets.
        self.facets = [[0, 0, 0, self.q03, self.q04, self.q05, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, self.q13, self.q14, self.q15, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, self.q23, self.q24, self.q25, 0, 0, 0, 0, 0, 0],
                       [self.q30, self.q31, self.q32, self.q33, self.q34, self.q35, self.q36, self.q37, self.q38, self.q39, self.q310, self.q311],
                       [self.q40, self.q41, self.q42, self.q43, self.q44, self.q45, self.q46, self.q47, self.q48, self.q49, self.q410, self.q411],
                       [self.q50, self.q51, self.q52, self.q53, self.q54, self.q55, self.q56, self.q57, self.q58, self.q59, self.q510, self.q511],
                       [0, 0, 0, self.q63, self.q64, self.q65, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, self.q73, self.q74, self.q75, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, self.q83, self.q84, self.q85, 0, 0, 0, 0, 0, 0]]

        # Render colors.
        self.background = [self.qB1, self.qB2, self.qB3]
        for background in self.background:
            background.setScene(self.black)
        for row in self.facets:
            for facet in row:
                if facet: facet.raise_()
        self.lines = [self.l1, self.l2, self.l3, self.l4, self.l5, self.l6, self.l7, self.l8, self.l9, self.l10, self.l11, self.l12, self.l13]
        for line in self.lines:
            line.raise_()
        for button in self.buttons:
            button.raise_()
        self.btnScramble.raise_()
        self.btnSolve.raise_()
        self.sliSpeed.raise_()
        self.update()

    def moveHandler(self, func):
        def move():
            func(self.cube.puz)
            self.update()
        return move

    def setLock(self, op):
        # Disable / Enable relevant widgets.
        self.btnScramble.setEnabled(op)
        self.btnSolve.setEnabled(op)

    def setSpeed(self):
        self.speed = 100 - self.sliSpeed.value()

    def processScreen(self):
        # Update colors.
        self.update()

        # Break wait down to increase responsiveness.
        for i in range(self.speed):
            time.sleep(0.01)
            QApplication.processEvents()

    def update(self):
        # Set the color of each facet.
        for (i, j), facet in np.ndenumerate(self.cube.puz):
            if facet == "W": self.facets[i][j].setScene(self.white)
            elif facet == "O": self.facets[i][j].setScene(self.orange)
            elif facet == "G": self.facets[i][j].setScene(self.green)
            elif facet == "R": self.facets[i][j].setScene(self.red)
            elif facet == "B": self.facets[i][j].setScene(self.blue)
            elif facet == "Y": self.facets[i][j].setScene(self.yellow)

    def execute(self, algorithm):
        # Add algorithm to running solution.
        self.cube.solution += " ".join([move.__name__ for move in algorithm]) + "\n"
        self.cube.solLen += len(algorithm)

        # Execute each move in the algorithm
        for move in algorithm:
            # Make the move, and update the screen.
            move(self.cube.puz)
            self.processScreen()

    def scramble(self):
        # Prepare cube.
        self.setLock(False)
        moves = [U, Up, U2, D, Dp, D2, R, Rp, R2, L, Lp, L2, F, Fp, F2, B, Bp, B2]
        scramble = []
        choice = random.choice(moves)

        # Make 20  random moves.
        for i in range(20):
            # Update scramble.
            scramble.append(choice.__name__)

            # Make the move, and update the screen.
            choice(self.cube.puz)
            self.processScreen()

            # Make a new random choice. Ensure the same face isn't selected.
            choice = random.choice([move for move in moves if move.__name__[0] != choice.__name__[0]])
        self.setLock(True)
        self.cube.scramble = "Generated the following scramble:\n" + " ".join(scramble) + "\n"
        print(self.cube.scramble)

    def solve(self):
        # Prepare cube.
        self.setLock(False)
        self.cube.solLen = 0
        self.proDone.setValue(0)
        self.proDone.show()

        # Execute steps.
        self.cube.solution = "=== Bottom Edges ===\n"; bEdges(self)
        self.proDone.setValue(15)
        self.cube.solution += "\n=== Bottom Corners ===\n"; bCorners(self)
        self.proDone.setValue(30)
        self.cube.solution += "\n=== Middle Edges ===\n"; mEdges(self)
        self.proDone.setValue(45)
        self.cube.solution += "\n=== Top Edge Orientation ===\n"; tEdgesO(self)
        self.proDone.setValue(60)
        self.cube.solution += "\n=== Top Corner Orientation ===\n"; tCornersO(self)
        self.proDone.setValue(75)
        self.cube.solution += "\n=== Top Corner Permutation ===\n"; tCornersP(self)
        self.proDone.setValue(90)
        self.cube.solution += "\n=== Top Edge Permutation ===\n"; tEdgesP(self)
        self.proDone.setValue(100)
        self.cube.solution += "\nSolution found in {} moves.\n".format(self.cube.solLen)

        self.setLock(True)
        print(self.cube.solution)
        self.proDone.hide()

if __name__ == "__main__":
    currentApp = QApplication(sys.argv)
    currentForm = RubikApp()

    currentForm.show()
    currentApp.exec_()