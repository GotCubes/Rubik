#! /usr/bin/env python3.4

import time
import random
from algorithms import *

class Cube:
    def __init__(self):
        # Define puzzle colors.
        self.puz = np.chararray((9, 12))
        self.puz[:] = "_"
        self.puz[0:3, 3:6] = 'W'
        self.puz[3:6, 0:3] = 'O'
        self.puz[3:6, 3:6] = 'G'
        self.puz[3:6, 6:9] = 'R'
        self.puz[3:6, 9:12] = 'B'
        self.puz[6:9, 3:6] = 'Y'

        # Define orientation.
        self.cU = 'W'
        self.cD = 'Y'
        self.cF = 'G'
        self.cB = 'B'
        self.cL = 'O'
        self.cR = 'R'

        # Define moveset.
        self.moves = [U, Up, U2,
                      D, Dp, D2,
                      L, Lp, L2,
                      R, Rp, R2,
                      F, Fp, F2,
                      B, Bp, B2]

        # Define edge connections.
        self.edges = [[(6, 4), (5, 4)], [(7, 3), (5, 1)], [(8, 4), (5, 10)], [(7, 5), (5, 7)],
                      [(4, 3), (4, 2)], [(4, 0), (4, 11)], [(4, 9), (4, 8)], [(4, 6), (4, 5)],
                      [(2, 4), (3, 4)], [(1, 3), (3, 1)], [(0, 4), (3, 10)], [(1, 5), (3, 7)]]

        # Define corner connections.
        self.corners = [[(6, 3), (5, 2), (5, 3)], [(8, 3), (5, 11), (5, 0)],
                        [(8, 5), (5, 8), (5, 9)], [(6, 5), (5, 5), (5, 6)],
                        [(2, 3), (3, 3), (3, 2)], [(0, 3), (3, 0), (3, 11)],
                        [(0, 5), (3, 9), (3, 8)], [(2, 5), (3, 6), (3, 5)]]

        # Scramble / Solution data.
        self.scramble = ""
        self.solution = ""
        self.algorithm = []
        self.solLen = 0

    def __str__(self):
        # Return a string representation of the cube.
        ret = ""
        for line in self.puz:
            for item in line:
                if item != "_": ret += item + " "
                else: ret += "  "
            ret += "\n"

        return ret

    def setOrientation(self):
        self.cU = self.puz[1, 4]
        self.cD = self.puz[7, 4]
        self.cF = self.puz[4, 4]
        self.cB = self.puz[4, 10]
        self.cL = self.puz[4, 1]
        self.cR = self.puz[4, 7]

    def execute(self, algorithm):
        # Perform each operation in the algorithm.
        self.solLen += len(algorithm)
        for move in algorithm:
            move(self.puz)

    def scramble_(self):
        # Make 20 random moves.
        self.solLen = 0
        choice = random.choice(self.moves)
        for i in range(20):
            choice(self.puz)
            choice = random.choice([move for move in self.moves if move.__name__[0] != choice.__name__[0]])

    def solve(self):
        # Get the proper orientation of the scramble cube.
        self.setOrientation()

        # Fetch the proper algorithm at each step and execute it.
        self.execute(algsDF[locateEdge(self, self.cD, self.cF)])
        self.execute(algsDL[locateEdge(self, self.cD, self.cL)])
        self.execute(algsDB[locateEdge(self, self.cD, self.cB)])
        self.execute(algsDR[locateEdge(self, self.cD, self.cR)])
        self.execute(algsDLF[locateCorner(self, self.cD, self.cL, self.cF)])
        self.execute(algsDBL[locateCorner(self, self.cD, self.cB, self.cL)])
        self.execute(algsDRB[locateCorner(self, self.cD, self.cR, self.cB)])
        self.execute(algsDFR[locateCorner(self, self.cD, self.cF, self.cR)])
        self.execute(algsFL[locateEdge(self, self.cF, self.cL)])
        self.execute(algsLB[locateEdge(self, self.cL, self.cB)])
        self.execute(algsBR[locateEdge(self, self.cB, self.cR)])
        self.execute(algsRF[locateEdge(self, self.cR, self.cF)])
        self.execute(algsEO[locateEdgeOri(self)])
        self.execute(algsCO[locateCornerOri(self)])
        self.execute(algsCP[locateCornerPerm(self)])
        self.execute(algsEP[locateEdgePerm(self)])
        self.execute(algsFA[locateFinalAlignment(self)])

if __name__ == "__main__":
    cube = Cube()

    times = []
    moves = []

    # Stress test. Solve several cubes and print the average time.
    for i in range(1000):
        cube.scramble_()
        start = time.time()
        cube.solve()
        end = time.time()
        times.append(end - start)
        moves.append(cube.solLen)
        print("Solved cube #" + str(i + 1).zfill(4) + " in %.6f seconds, with " % (end - start) + str(cube.solLen).zfill(3) + " moves.")
    print("\nSolved {} cubes in {} seconds, using a total of {} moves.".format(i + 1, sum(times), sum(moves)))
    print("Average time: {} seconds.".format(sum(times) / len(times)))
    print("Average moves: {}.".format(sum(moves) / len(moves)))
    print("Times ranged from {} to {} seconds.".format(min(times), max(times)))
    print("Moves ranged from {} to {}.".format(min(moves), max(moves)))