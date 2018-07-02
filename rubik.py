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

        # Define moveset.
        self.moves = [U, Up, U2, D, Dp, D2, L, Lp, L2, R, Rp, R2, F, Fp, F2, B, Bp, B2]

        # Define edge connections.
        self.edges = [[(6, 4), (5, 4)], [(7, 3), (5, 1)], [(8, 4), (5, 10)], [(7, 5), (5, 7)],
                      [(4, 3), (4, 2)], [(4, 0), (4, 11)], [(4, 9), (4, 8)], [(4, 6), (4, 5)],
                      [(2, 4), (3, 4)], [(1, 3), (3, 1)], [(0, 4), (3, 10)], [(1, 5), (3, 7)]]

        # Define corner connections.
        self.corners = [[(6, 3), (5, 2), (5, 3)], [(8, 3), (5, 11), (5, 0)], [(8, 5), (5, 8), (5, 9)], [(6, 5), (5, 5), (5, 6)],
                        [(2, 3), (3, 3), (3, 2)], [(0, 3), (3, 0), (3, 11)], [(0, 5), (3, 9), (3, 8)], [(2, 5), (3, 6), (3, 5)]]

        # Scramble / Solution data.
        self.scramble = ""
        self.solution = ""
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

    def execute(self, algorithm):
        # Perform each operation in the algorithm.
        for move in algorithm:
            move(self.puz)

    def scramble_(self):
        # Make 20 random moves.
        choice = random.choice(self.moves)
        for i in range(20):
            choice(self.puz)
            choice = random.choice([move for move in self.moves if move.__name__[0] != choice.__name__[0]])

    def solve(self):
        # Fetch the proper algorithm at each step and execute it.
        self.execute(algsYG[locateEdge(self, "Y", "G")])
        self.execute(algsYO[locateEdge(self, "Y", "O")])
        self.execute(algsYB[locateEdge(self, "Y", "B")])
        self.execute(algsYR[locateEdge(self, "Y", "R")])
        self.execute(algsYOG[locateCorner(self, "Y", "O", "G")])
        self.execute(algsYBO[locateCorner(self, "Y", "B", "O")])
        self.execute(algsYRB[locateCorner(self, "Y", "R", "B")])
        self.execute(algsYGR[locateCorner(self, "Y", "G", "R")])
        self.execute(algsGO[locateEdge(self, "G", "O")])
        self.execute(algsOB[locateEdge(self, "O", "B")])
        self.execute(algsBR[locateEdge(self, "B", "R")])
        self.execute(algsRG[locateEdge(self, "R", "G")])
        self.execute(algsEO[locateEdgeOri(self)])
        self.execute(algsCO[locateCornerOri(self)])
        self.execute(algsCP[locateCornerPerm(self)])
        self.execute(algsEP[locateEdgePerm(self)])
        self.execute(algsFA[self.puz[3, 4]])

if __name__ == "__main__":
    cube = Cube()
    times = []

    # Stress test. Solve several cubes and print the average time.
    for i in range(1000):
        cube.scramble_()
        start = time.time()
        cube.solve()
        end = time.time()
        times.append(end - start)
        print("Solved in {} seconds.".format(end - start))
    print("Solved {} cubes in an average of {} seconds.".format(i + 1, sum(times) / len(times)))
