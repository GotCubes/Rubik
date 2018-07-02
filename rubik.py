#! /usr/bin/env python3.4

from moves import *

class Cube:
    def __init__(self):
        self.puz = np.chararray((9, 12))
        self.puz[:] = "_"
        self.puz[0:3, 3:6] = 'W'
        self.puz[3:6, 0:3] = 'O'
        self.puz[3:6, 3:6] = 'G'
        self.puz[3:6, 6:9] = 'R'
        self.puz[3:6, 9:12] = 'B'
        self.puz[6:9, 3:6] = 'Y'

        self.moves = [U, Up, U2, D, Dp, D2, L, Lp, L2, R, Rp, R2, F, Fp, F2, B, Bp, B2]

        self.edges = [[(6, 4), (5, 4)], [(7, 3), (5, 1)], [(8, 4), (5, 10)], [(7, 5), (5, 7)],
                      [(4, 3), (4, 2)], [(4, 0), (4, 11)], [(4, 9), (4, 8)], [(4, 6), (4, 5)],
                      [(2, 4), (3, 4)], [(1, 3), (3, 1)], [(0, 4), (3, 10)], [(1, 5), (3, 7)]]

        self.corners = [[(6, 3), (5, 2), (5, 3)], [(8, 3), (5, 11), (5, 0)], [(8, 5), (5, 8), (5, 9)], [(6, 5), (5, 5), (5, 6)],
                        [(2, 3), (3, 3), (3, 2)], [(0, 3), (3, 0), (3, 11)], [(0, 5), (3, 9), (3, 8)], [(2, 5), (3, 6), (3, 5)]]

        self.scramble = ""
        self.solution = ""
        self.solLen = 0

    def __str__(self):
        ret = ""
        for line in self.puz:
            for item in line:
                if item != "_": ret += item + " "
                else: ret += "  "
            ret += "\n"

        return ret