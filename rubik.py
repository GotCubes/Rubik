#! /usr/bin/env python3.4

import random
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

    def scramble(self):
        moves = [U, Up, U2, D, Dp, D2, R, Rp, R2, L, Lp, L2, F, Fp, F2, B, Bp, B2]
        for i in range(100):
            random.choice(moves)(self.puz)

    def execute(self, algorithm):
        for move in algorithm:
            move(self.puz)

    def YCross(self):
        # Green / Yellow edge.
        if self.puz[5, 4] == "Y" and self.puz[6, 4] == "G":
            self.execute([Fp, Rp, Dp])
        elif self.puz[4, 2] == "G" and self.puz[4, 3] == "Y":
            self.execute([L, D])
        elif self.puz[4, 2] == "Y" and self.puz[4, 3] == "G":
            self.execute([Fp])
        elif self.puz[2, 4] == "G" and self.puz[3, 4] == "Y":
            self.execute([Up, Rp, F])
        elif self.puz[2, 4] == "Y" and self.puz[3, 4] == "G":
            self.execute([F2])
        elif self.puz[4, 5] == "G" and self.puz[4, 6] == "Y":
            self.execute([F])
        elif self.puz[4, 5] == "Y" and self.puz[4, 6] == "G":
            self.execute([Rp, Dp])
        elif self.puz[4, 8] == "G" and self.puz[4, 9] == "Y":
            self.execute([R, Dp])
        elif self.puz[4, 8] == "Y" and self.puz[4, 9] == "G":
            self.execute([Bp, D2])
        elif self.puz[3, 1] == "G" and self.puz[1, 3] == "Y":
            self.execute([Up, F2])
        elif self.puz[3, 1] == "Y" and self.puz[1, 3] == "G":
            self.execute([L, Fp])
        elif self.puz[1, 5] == "G" and self.puz[3, 7] == "Y":
            self.execute([Rp, F])
        elif self.puz[1, 5] == "Y" and self.puz[3, 7] == "G":
            self.execute([U, F2])
        elif self.puz[5, 7] == "G" and self.puz[7, 5] == "Y":
            self.execute([Dp])
        elif self.puz[5, 7] == "Y" and self.puz[7, 5] == "G":
            self.execute([R, F])
        elif self.puz[7, 3] == "G" and self.puz[5, 1] == "Y":
            self.execute([Lp, Fp])
        elif self.puz[7, 3] == "Y" and self.puz[5, 1] == "G":
            self.execute([D])
        elif self.puz[4, 0] == "G" and self.puz[4, 11] == "Y":
            self.execute([Lp, D])
        elif self.puz[4, 0] == "Y" and self.puz[4, 11] == "G":
            self.execute([L2, Fp])
        elif self.puz[0, 4] == "G" and self.puz[3, 10] == "Y":
            self.execute([U, Rp, F])
        elif self.puz[0, 4] == "Y" and self.puz[3, 10] == "G":
            self.execute([U2, F2])
        elif self.puz[5, 10] == "G" and self.puz[8, 4] == "Y":
            self.execute([D2])
        elif self.puz[5, 10] == "Y" and self.puz[8, 4] == "G":
            self.execute([Dp, R, F])

        # Orange / Yellow edge.
        if self.puz[4, 2] == "O" and self.puz[4, 3] == "Y":
            self.execute([L])
        elif self.puz[4, 2] == "Y" and self.puz[4, 3] == "O":
            self.execute([Fp, Dp, F])
        elif self.puz[2, 4] == "O" and self.puz[3, 4] == "Y":
            self.execute([Fp, L, F])
        elif self.puz[2, 4] == "Y" and self.puz[3, 4] == "O":
            self.execute([U, L2])
        elif self.puz[4, 5] == "O" and self.puz[4, 6] == "Y":
            self.execute([F, Dp, Fp])
        elif self.puz[4, 5] == "Y" and self.puz[4, 6] == "O":
            self.execute([R, U2, L2])
        elif self.puz[4, 8] == "O" and self.puz[4, 9] == "Y":
            self.execute([Rp, U2, L2])
        elif self.puz[4, 8] == "Y" and self.puz[4, 9] == "O":
            self.execute([Dp, Bp, D])
        elif self.puz[3, 1] == "O" and self.puz[1, 3] == "Y":
            self.execute([L2])
        elif self.puz[3, 1] == "Y" and self.puz[1, 3] == "O":
            self.execute([L, Fp, Dp, F])
        elif self.puz[1, 5] == "O" and self.puz[3, 7] == "Y":
            self.execute([U, Fp, L, F])
        elif self.puz[1, 5] == "Y" and self.puz[3, 7] == "O":
            self.execute([U2, L2])
        elif self.puz[5, 7] == "O" and self.puz[7, 5] == "Y":
            self.execute([R2, U2, L2])
        elif self.puz[5, 7] == "Y" and self.puz[7, 5] == "O":
            self.execute([R, F, Dp, Fp])
        elif self.puz[7, 3] == "O" and self.puz[5, 1] == "Y":
            self.execute([Lp, Fp, Dp, F])
        elif self.puz[4, 0] == "O" and self.puz[4, 11] == "Y":
            self.execute([Lp])
        elif self.puz[4, 0] == "Y" and self.puz[4, 11] == "O":
            self.execute([Dp, B, D])
        elif self.puz[0, 4] == "O" and self.puz[3, 10] == "Y":
            self.execute([B, Lp])
        elif self.puz[0, 4] == "Y" and self.puz[3, 10] == "O":
            self.execute([Up, L2])
        elif self.puz[5, 10] == "O" and self.puz[8, 4] == "Y":
            self.execute([B2, Up, L2])
        elif self.puz[5, 10] == "Y" and self.puz[8, 4] == "O":
            self.execute([Bp, Lp])

        # Blue / Yellow edge.
        if self.puz[4, 2] == "B" and self.puz[4, 3] == "Y":
            self.execute([D, L, Dp])
        elif self.puz[4, 2] == "Y" and self.puz[4, 3] == "B":
            self.execute([D2, Fp, D2])
        elif self.puz[2, 4] == "B" and self.puz[3, 4] == "Y":
            self.execute([Up, R, Bp])
        elif self.puz[2, 4] == "Y" and self.puz[3, 4] == "B":
            self.execute([U2, B2])
        elif self.puz[4, 5] == "B" and self.puz[4, 6] == "Y":
            self.execute([R2, Bp])
        elif self.puz[4, 5] == "Y" and self.puz[4, 6] == "B":
            self.execute([Dp, Rp, D])
        elif self.puz[4, 8] == "B" and self.puz[4, 9] == "Y":
            self.execute([Dp, R, D])
        elif self.puz[4, 8] == "Y" and self.puz[4, 9] == "B":
            self.execute([Bp])
        elif self.puz[3, 1] == "B" and self.puz[1, 3] == "Y":
            self.execute([U, B2])
        elif self.puz[3, 1] == "Y" and self.puz[1, 3] == "B":
            self.execute([Lp, B, L])
        elif self.puz[1, 5] == "B" and self.puz[3, 7] == "Y":
            self.execute([R, Bp])
        elif self.puz[1, 5] == "Y" and self.puz[3, 7] == "B":
            self.execute([Up, B2])
        elif self.puz[5, 7] == "B" and self.puz[7, 5] == "Y":
            self.execute([R2, Up, B2])
        elif self.puz[5, 7] == "Y" and self.puz[7, 5] == "B":
            self.execute([Rp, Bp])
        elif self.puz[4, 0] == "B" and self.puz[4, 11] == "Y":
            self.execute([D, Lp, Dp])
        elif self.puz[4, 0] == "Y" and self.puz[4, 11] == "B":
            self.execute([B])
        elif self.puz[0, 4] == "B" and self.puz[3, 10] == "Y":
            self.execute([U, R, Bp])
        elif self.puz[0, 4] == "Y" and self.puz[3, 10] == "B":
            self.execute([B2])
        elif self.puz[5, 10] == "Y" and self.puz[8, 4] == "B":
            self.execute([B, Dp, R, D])

        # Red / Yellow edge.
        if self.puz[4, 2] == "R" and self.puz[4, 3] == "Y":
            self.execute([D2, L, D2])
        elif self.puz[4, 2] == "Y" and self.puz[4, 3] == "R":
            self.execute([Dp, Fp, D])
        elif self.puz[2, 4] == "R" and self.puz[3, 4] == "Y":
            self.execute([F, Rp, Fp])
        elif self.puz[2, 4] == "Y" and self.puz[3, 4] == "R":
            self.execute([Up, R2])
        elif self.puz[4, 5] == "R" and self.puz[4, 6] == "Y":
            self.execute([Dp, F, D])
        elif self.puz[4, 5] == "Y" and self.puz[4, 6] == "R":
            self.execute([Rp])
        elif self.puz[4, 8] == "R" and self.puz[4, 9] == "Y":
            self.execute([R])
        elif self.puz[4, 8] == "Y" and self.puz[4, 9] == "R":
            self.execute([D, Bp, Dp])
        elif self.puz[3, 1] == "R" and self.puz[1, 3] == "Y":
            self.execute([U2, R2])
        elif self.puz[3, 1] == "Y" and self.puz[1, 3] == "R":
            self.execute([Up, F, Rp, Fp])
        elif self.puz[1, 5] == "R" and self.puz[3, 7] == "Y":
            self.execute([U, F, Rp, Fp])
        elif self.puz[1, 5] == "Y" and self.puz[3, 7] == "R":
            self.execute([R2])
        elif self.puz[5, 7] == "Y" and self.puz[7, 5] == "R":
            self.execute([R, Dp, F, D])
        elif self.puz[4, 0] == "R" and self.puz[4, 11] == "Y":
            self.execute([D2, Lp, D2])
        elif self.puz[4, 0] == "Y" and self.puz[4, 11] == "R":
            self.execute([D, B, Dp])
        elif self.puz[0, 4] == "R" and self.puz[3, 10] == "Y":
            self.execute([Bp, R, B])
        elif self.puz[0, 4] == "Y" and self.puz[3, 10] == "R":
            self.execute([U, R2])

if __name__ == "__main__":
    cube = Cube()
    checkerboard = [U2, D2, R2, L2, F2, B2]
    superflip = [U, R2, F, B, R, B2, R, U2, L, B2, R, Up, Dp, R2, F, Rp, L, B2, U2, F2]

    cube.scramble()
    print(cube)
    cube.YCross()
    print(cube)