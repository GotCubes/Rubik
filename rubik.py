#! /usr/bin/env python3.4

import numpy as np

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
        self.scramble = []
        self.solution = []
        self.solLen = 0

    def __str__(self):
        ret = ""
        for line in self.puz:
            for item in line:
                if item != "_" : ret += item + " "
                else: ret += "  "
            ret += "\n"

        return ret