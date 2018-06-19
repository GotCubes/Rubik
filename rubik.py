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

    def __str__(self):
        ret = ""
        for line in self.puz:
            for item in line:
                if item != "_": ret += item + " "
                else: ret += "  "
            ret += "\n"

        return ret

    def execute(self, algorithm):
        for move in algorithm:
            move(self.puz)

if __name__ == "__main__":
    cube = Cube()
    checkerboard = [U2, D2, R2, L2, F2, B2]
    superflip = [U, R2, F, B, R, B2, R, U2, L, B2, R, Up, Dp, R2, F, Rp, L, B2, U2, F2]

    cube.execute(superflip)
    cube.execute(checkerboard)
    cube.execute(superflip)
    cube.execute(checkerboard)
    print(cube)