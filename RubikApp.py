import sys
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
        self.buttons = [self.btnU, self.btnUp, self.btnU2,
                        self.btnD, self.btnDp, self.btnD2,
                        self.btnL, self.btnLp, self.btnL2,
                        self.btnR, self.btnRp, self.btnR2,
                        self.btnF, self.btnFp, self.btnF2,
                        self.btnB, self.btnBp, self.btnB2]
        self.moves = [U, Up, U2, D, Dp, D2, L, Lp, L2, R, Rp, R2, F, Fp, F2, B, Bp, B2]

        # Define connections.
        for i in range(18): self.buttons[i].clicked.connect(self.moveHandler(self.moves[i]))
        self.btnBlank.clicked.connect(self.blank)
        self.btnScramble.clicked.connect(self.scramble)
        self.btnSolve.clicked.connect(self.solve)
        self.proDone.hide()

        # Initialize facet colors.
        self.white = QGraphicsScene(); self.white.setBackgroundBrush(QColor(255, 255, 255))
        self.orange = QGraphicsScene(); self.orange.setBackgroundBrush(QColor(255, 192, 0))
        self.green = QGraphicsScene(); self.green.setBackgroundBrush(QColor(0, 175, 80))
        self.red = QGraphicsScene(); self.red.setBackgroundBrush(QColor(254, 0, 0))
        self.blue = QGraphicsScene(); self.blue.setBackgroundBrush(QColor(1, 176, 241))
        self.yellow = QGraphicsScene(); self.yellow.setBackgroundBrush(QColor(255, 255, 1))
        self.black = QGraphicsScene(); self.black.setBackgroundBrush(QColor(0, 0, 0))
        self.dRed = QGraphicsScene(); self.dRed.setBackgroundBrush(QColor(139, 0, 0))
        self.colorSel = None
        self.colors = {"W": self.white, "O": self.orange, "G": self.green,
                       "R": self.red, "B": self.blue, "Y": self.yellow, "X": self.black}

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
        self.btnFacets = [[0, 0, 0, self.btn03, self.btn04, self.btn05, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, self.btn13, 0, self.btn15, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, self.btn23, self.btn24, self.btn25, 0, 0, 0, 0, 0, 0],
                         [self.btn30, self.btn31, self.btn32, self.btn33, self.btn34, self.btn35, self.btn36, self.btn37, self.btn38, self.btn39, self.btn310, self.btn311],
                         [self.btn40, 0, self.btn42, self.btn43, 0, self.btn45, self.btn46, 0, self.btn48, self.btn49, 0, self.btn411],
                         [self.btn50, self.btn51, self.btn52, self.btn53, self.btn54, self.btn55, self.btn56, self.btn57, self.btn58, self.btn59, self.btn510, self.btn511],
                         [0, 0, 0, self.btn63, self.btn64, self.btn65, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, self.btn73, 0, self.btn75, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, self.btn83, self.btn84, self.btn85, 0, 0, 0, 0, 0, 0]]

        # Render colors.
        self.background = [self.qB1, self.qB2, self.qB3, self.qB4, self.qB5, self.qB6, self.qB7, self.qB8, self.qB9, self.qB10, self.qB11, self.qB12, self.qB13]
        for background in self.background:
            background.setScene(self.black)

        self.drops = [self.qWhite, self.qOrange, self.qGreen, self.qRed, self.qBlue, self.qYellow]
        self.btnDrops = [self.btnWhite, self.btnOrange, self.btnGreen, self.btnRed, self.btnBlue, self.btnYellow]
        self.dropBacks = [self.qB8, self.qB9, self.qB10, self.qB11, self.qB12, self.qB13]

        for i, color in enumerate(["W", "O", "G", "R", "B", "Y"]):
            self.drops[i].raise_()
            self.drops[i].setScene(self.colors[color])

            self.btnDrops[i].raise_()
            self.btnDrops[i].setStyleSheet("border: 0px; background: transparent;")
            self.btnDrops[i].clicked.connect(self.colorSelect(color, i))

        for i in range(9):
            for j in range(12):
                if self.facets[i][j]:
                    self.facets[i][j].raise_()
                if self.btnFacets[i][j]:
                    self.btnFacets[i][j].raise_()
                    self.btnFacets[i][j].setStyleSheet("border: 0px; background: transparent;")
                    self.btnFacets[i][j].clicked.connect(self.colorSet(i, j))

        for button in self.buttons:
            button.raise_()

        self.btnScramble.raise_()
        self.btnSolve.raise_()
        self.sliSpeed.raise_()
        self.update()

    def colorSelect(self, color, i):
        def sel():
            self.colorSel = color
            for j, back in enumerate(self.dropBacks):
                if j == i: back.setScene(self.dRed)
                else: back.setScene(self.black)
        return sel

    def colorSet(self, i, j):
        def set():
            if self.colorSel:
                self.cube.puz[i, j] = self.colorSel
                self.update()
        return set

    def moveHandler(self, func):
        def move():
            func(self.cube.puz)
            self.update()
        return move

    def setLock(self, op):
        # Disable / Enable relevant widgets.
        self.btnBlank.setEnabled(op)
        self.btnScramble.setEnabled(op)
        self.btnSolve.setEnabled(op)

        for button in self.buttons:
            button.setEnabled(op)

        for i in range(9):
            for j in range(12):
                if self.btnFacets[i][j]: self.btnFacets[i][j].setEnabled(op)

    def update(self):
        # Set the color of each facet.
        for (i, j), facet in np.ndenumerate(self.cube.puz):
            if facet != "_": self.facets[i][j].setScene(self.colors[facet])

        # Update text boxes.
        self.leScramble.setText(self.cube.scramble)
        self.txtSolution.setText(self.cube.solution)
        self.txtSolution.verticalScrollBar().setValue(self.txtSolution.verticalScrollBar().maximum())

    def processScreen(self):
        # Update colors.
        self.update()

        # Break wait down to increase responsiveness.
        for i in range(100 - self.sliSpeed.value()):
            time.sleep(0.005)
            QApplication.processEvents()

    def default(self):
        self.cube.puz[0:3, 3:6] = 'W'
        self.cube.puz[3:6, 0:3] = 'O'
        self.cube.puz[3:6, 3:6] = 'G'
        self.cube.puz[3:6, 6:9] = 'R'
        self.cube.puz[3:6, 9:12] = 'B'
        self.cube.puz[6:9, 3:6] = 'Y'
        self.update()

    def execute(self, algorithm):
        # Add algorithm to running solution.
        self.cube.solLen += len(algorithm)

        if algorithm:
            # Execute each move in the algorithm
            for move in algorithm:
                # Make the move, and update the screen.
                self.cube.solution += move.__name__.replace("p", "'") + " "
                move(self.cube.puz)
                self.processScreen()
            self.cube.solution += "\n"

    def isValid(self):
        return locateEdge(self.cube, "Y", "G") and locateEdge(self.cube, "Y", "O") and \
               locateEdge(self.cube, "Y", "B") and locateEdge(self.cube, "Y", "R") and \
               locateEdge(self.cube, "G", "O") and locateEdge(self.cube, "O", "B") and \
               locateEdge(self.cube, "B", "R") and locateEdge(self.cube, "R", "G") and \
               locateEdge(self.cube, "W", "G") and locateEdge(self.cube, "W", "O") and \
               locateEdge(self.cube, "W", "B") and locateEdge(self.cube, "W", "R") and \
               locateCorner(self.cube, "Y", "O", "G") and locateCorner(self.cube, "Y", "B", "O") and \
               locateCorner(self.cube, "Y", "R", "B") and locateCorner(self.cube, "Y", "G", "R") and \
               locateCorner(self.cube, "W", "G", "O") and locateCorner(self.cube, "W", "O", "B") and \
               locateCorner(self.cube, "W", "B", "R") and locateCorner(self.cube, "W", "R", "G")

    def blank(self):
        self.cube.scramble = ""
        self.cube.solution = ""
        for i in range(9):
            for j in range(12):
                if self.btnFacets[i][j]:
                    self.cube.puz[i][j] = "X"
        self.update()

    def scramble(self):
        if self.isValid():
            # Prepare cube.
            self.setLock(False)
            self.cube.scramble = ""
            self.cube.solution = ""
            self.default()
            scramble = []
            choice = random.choice(self.moves)

            # Make 20 random moves.
            for i in range(20):
                # Update scramble.
                scramble.append(choice.__name__)

                # Make the move, and update the screen.
                self.cube.scramble += choice.__name__.replace("p", "'") + " "
                choice(self.cube.puz)
                self.processScreen()

                # Make a new random choice. Ensure the same face isn't selected.
                choice = random.choice([move for move in self.moves if move.__name__[0] != choice.__name__[0]])
            self.setLock(True)
        else:
            self.cube.scramble = "Cube in an invalid state. Reverted to solved state."
            self.default()

    def solve(self):
        if self.isValid():
            # Prepare cube.
            self.setLock(False)
            self.cube.solution = ""
            self.cube.solLen = 0
            self.proDone.setValue(0)
            self.proDone.show()

            # Bottom edges.
            self.cube.solution += "=== Bottom Edges ===\n"
            self.execute(algsYG[locateEdge(self.cube, "Y", "G")])
            self.proDone.setValue(6)
            self.execute(algsYO[locateEdge(self.cube, "Y", "O")])
            self.proDone.setValue(12)
            self.execute(algsYB[locateEdge(self.cube, "Y", "B")])
            self.proDone.setValue(18)
            self.execute(algsYR[locateEdge(self.cube, "Y", "R")])
            self.proDone.setValue(24)

            # Bottom corners.
            self.cube.solution += "\n=== Bottom Corners ===\n"
            self.execute(algsYOG[locateCorner(self.cube, "Y", "O", "G")])
            self.proDone.setValue(30)
            self.execute(algsYBO[locateCorner(self.cube, "Y", "B", "O")])
            self.proDone.setValue(36)
            self.execute(algsYRB[locateCorner(self.cube, "Y", "R", "B")])
            self.proDone.setValue(42)
            self.execute(algsYGR[locateCorner(self.cube, "Y", "G", "R")])
            self.proDone.setValue(48)

            # Middle edges.
            self.cube.solution += "\n=== Middle Edges ===\n"
            self.execute(algsGO[locateEdge(self.cube, "G", "O")])
            self.proDone.setValue(54)
            self.execute(algsOB[locateEdge(self.cube, "O", "B")])
            self.proDone.setValue(60)
            self.execute(algsBR[locateEdge(self.cube, "B", "R")])
            self.proDone.setValue(66)
            self.execute(algsRG[locateEdge(self.cube, "R", "G")])
            self.proDone.setValue(72)

            # Top edge orientation.
            self.cube.solution += "\n=== Top Edge Orientation ===\n"
            self.execute(algsEO[locateEdgeOri(self.cube)])
            self.proDone.setValue(78)

            # Top corner orientation
            self.cube.solution += "\n=== Top Corner Orientation ===\n"
            self.execute(algsCO[locateCornerOri(self.cube)])
            self.proDone.setValue(84)

            # Top corner permutation.
            self.cube.solution += "\n=== Top Corner Permutation ===\n"
            self.execute(algsCP[locateCornerPerm(self.cube)])
            self.proDone.setValue(90)

            # Top edge permutation.
            self.cube.solution += "\n=== Top Edge Permutation ===\n"
            self.execute(algsEP[locateEdgePerm(self.cube)])
            self.proDone.setValue(96)
            self.execute(algsFA[self.cube.puz[3, 4]])
            self.proDone.setValue(100)

            # Print solution.
            self.cube.solution += "\nSolution found in {} moves.".format(self.cube.solLen)
            self.update()
            self.setLock(True)
            self.proDone.hide()
        else:
            self.cube.solution = "Cube in an invalid state. Reverted to solved state."
            self.default()

if __name__ == "__main__":
    currentApp = QApplication(sys.argv)
    currentForm = RubikApp()

    currentForm.show()
    currentApp.exec_()