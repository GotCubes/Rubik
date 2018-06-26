#! /usr/bin/env python3.4

import time
import random
from algorithms import *

class Cube:
    def __init__(self):
        self.puz = np.chararray((9, 12))
        self.puz[0:3, 3:6] = 'W'
        self.puz[3:6, 0:3] = 'O'
        self.puz[3:6, 3:6] = 'G'
        self.puz[3:6, 6:9] = 'R'
        self.puz[3:6, 9:12] = 'B'
        self.puz[6:9, 3:6] = 'Y'
        self.solution = []
        self.solLen = 0

    def __str__(self):
        ret = ""
        for line in self.puz:
            for item in line:
                if item in ["W", "O", "G", "R", "B", "Y"]: ret += item + " "
                else: ret += "  "
            ret += "\n"

        return ret

    def scramble(self):
        moves = [U, Up, U2, D, Dp, D2, R, Rp, R2, L, Lp, L2, F, Fp, F2, B, Bp, B2]
        for i in range(100):
            random.choice(moves)(self.puz)

    def execute(self, algorithm):
        self.solution.extend([move.__name__ for move in algorithm])
        self.solLen += len(algorithm)
        for move in algorithm:
            move(self.puz)

    def solve(self):
        self.solution = []
        self.solLen = 0
        bEdges(self)
        bCorners(self)
        mEdges(self)
        OLL(self)
        PLL(self)

if __name__ == "__main__":
    cube = Cube()
    times = []
    moves = []

    for i in range(100):
        cube.scramble()
        start = time.time()
        cube.solve()
        end = time.time()
        times.append(end - start)
        moves.append(cube.solLen)
        print("Solved a cube in {} moves, in {} seconds.".format(cube.solLen, end - start))

    print("Solved 100 cubes in an average of {} moves, in an average time of {} seconds.".format(sum(moves) / len(moves), sum(times) / len(times)))