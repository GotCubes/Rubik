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
        if algorithm == []: print("Skip!")
        else:
            for move in algorithm:
                move(self.puz)
            print(" ".join([move.__name__ for move in algorithm]))


    def bEdges(self):
        # Yellow / Green edge.
        if self.puz[5, 4] == "G" and self.puz[6, 4] == "Y":
            self.execute([])
        elif self.puz[5, 4] == "Y" and self.puz[6, 4] == "G":
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
        else: self.execute([Dp, R, F])

        # Yellow / Orange edge.
        if self.puz[7, 3] == "Y" and self.puz[5, 1] == "O":
            self.execute([])
        elif self.puz[4, 2] == "O" and self.puz[4, 3] == "Y":
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
        else: self.execute([Bp, Lp])

        # Yellow / Blue edge.
        if self.puz[8, 4] == "Y" and self.puz[5, 10] == "B":
            self.execute([])
        elif self.puz[4, 2] == "B" and self.puz[4, 3] == "Y":
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
        else: self.execute([B, Dp, R, D])

        # Yellow / Red edge.
        if self.puz[7, 5] == "Y" and self.puz[5, 7] == "R":
            self.execute([])
        elif self.puz[4, 2] == "R" and self.puz[4, 3] == "Y":
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
        else: self.execute([U, R2])

    def bCorners(self):
        # Yellow / Orange / Green corner.
        if self.puz[6, 3] == "Y" and self.puz[5, 2] == "O" and self.puz[5, 3] == "G":
            self.execute([])
        elif self.puz[6, 3] == "G" and self.puz[5, 2] == "Y" and self.puz[5, 3] == "O":
            self.execute([F, Up, Fp, Lp, Up, L])
        elif self.puz[6, 3] == "O" and self.puz[5, 2] == "G" and self.puz[5, 3] == "Y":
            self.execute([Lp, U, L, F, U, Fp])
        elif self.puz[8, 3] == "Y" and self.puz[5, 11] == "O" and self.puz[5, 0] == "G":
            self.execute([Bp, Up, B, F, U, Fp])
        elif self.puz[8, 3] == "G" and self.puz[5, 11] == "Y" and self.puz[5, 0] == "O":
            self.execute([Bp, Up, B, Lp, Up, L])
        elif self.puz[8, 3] == "O" and self.puz[5, 11] == "G" and self.puz[5, 0] == "Y":
            self.execute([L, Up, L, Fp, L2, F])
        elif self.puz[8, 5] == "Y" and self.puz[5, 8] == "O" and self.puz[5, 9] == "G":
            self.execute([Rp, U2, R, F, U, Fp])
        elif self.puz[8, 5] == "G" and self.puz[5, 8] == "Y" and self.puz[5, 9] == "O":
            self.execute([Rp, U2, R, Lp, Up, L])
        elif self.puz[8, 5] == "O" and self.puz[5, 8] == "G" and self.puz[5, 9] == "Y":
            self.execute([B, U2, Bp, F, U, Fp])
        elif self.puz[6, 5] == "Y" and self.puz[5, 5] == "O" and self.puz[5, 6] == "G":
            self.execute([R, U, Rp, Lp, Up, L])
        elif self.puz[6, 5] == "G" and self.puz[5, 5] == "Y" and self.puz[5, 6] == "O":
            self.execute([Fp, U2, F2, Up, Fp])
        elif self.puz[6, 5] == "O" and self.puz[5, 5] == "G" and self.puz[5, 6] == "Y":
            self.execute([R, U, Rp, F, U, Fp])
        elif self.puz[2, 3] == "Y" and self.puz[3, 3] == "O" and self.puz[3, 2] == "G":
            self.execute([F, U2, Fp, Up, F, U, Fp])
        elif self.puz[2, 3] == "G" and self.puz[3, 3] == "Y" and self.puz[3, 2] == "O":
            self.execute([F, U, Fp])
        elif self.puz[2, 3] == "O" and self.puz[3, 3] == "G" and self.puz[3, 2] == "Y":
            self.execute([Lp, Up, L])
        elif self.puz[0, 3] == "Y" and self.puz[3, 0] == "O" and self.puz[3, 11] == "G":
            self.execute([L2, Fp, L2, F])
        elif self.puz[0, 3] == "G" and self.puz[3, 0] == "Y" and self.puz[3, 11] == "O":
            self.execute([Up, L, Fp, Lp, F])
        elif self.puz[0, 3] == "O" and self.puz[3, 0] == "G" and self.puz[3, 11] == "Y":
            self.execute([Up, Lp, Up, L])
        elif self.puz[0, 5] == "Y" and self.puz[3, 9] == "O" and self.puz[3, 8] == "G":
            self.execute([U, F2, L, F2, Lp])
        elif self.puz[0, 5] == "G" and self.puz[3, 9] == "Y" and self.puz[3, 8] == "O":
            self.execute([U2, F, U, Fp])
        elif self.puz[0, 5] == "O" and self.puz[3, 9] == "G" and self.puz[3, 8] == "Y":
            self.execute([U2, Lp, Up, L])
        elif self.puz[2, 5] == "Y" and self.puz[3, 6] == "O" and self.puz[3, 5] == "G":
            self.execute([F2, L, F2, Lp])
        elif self.puz[2, 5] == "G" and self.puz[3, 6] == "Y" and self.puz[3, 5] == "O":
            self.execute([Lp, U, L])
        else: self.execute([U, Lp, Up, L])

        # Yellow / Blue / Orange corner.
        if self.puz[8, 3] == "Y" and self.puz[5, 11] == "B" and self.puz[5, 0] == "O":
            self.execute([])
        elif self.puz[8, 3] == "O" and self.puz[5, 11] == "Y" and self.puz[5, 0] == "B":
            self.execute([L, Up, Lp, Bp, Up, B])
        elif self.puz[8, 3] == "B" and self.puz[5, 11] == "O" and self.puz[5, 0] == "Y":
            self.execute([Bp, U, B, L, U, Lp])
        elif self.puz[8, 5] == "Y" and self.puz[5, 8] == "B" and self.puz[5, 9] == "O":
            self.execute([Rp, Up, R, L, U, Lp])
        elif self.puz[8, 5] == "O" and self.puz[5, 8] == "Y" and self.puz[5, 9] == "B":
            self.execute([Rp, Up, R, Bp, Up, B])
        elif self.puz[8, 5] == "B" and self.puz[5, 8] == "O" and self.puz[5, 9] == "Y":
            self.execute([Rp, U, R, Up, L, U, Lp])
        elif self.puz[6, 5] == "Y" and self.puz[5, 5] == "B" and self.puz[5, 6] == "O":
            self.execute([R2, B2, Lp, B2, L, R2])
        elif self.puz[6, 5] == "O" and self.puz[5, 5] == "Y" and self.puz[5, 6] == "B":
            self.execute([Fp, Up, F, L, Up, Lp])
        elif self.puz[6, 5] == "B" and self.puz[5, 5] == "O" and self.puz[5, 6] == "Y":
            self.execute([R, U, Rp, Bp, U, B])
        elif self.puz[2, 3] == "Y" and self.puz[3, 3] == "B" and self.puz[3, 2] == "O":
            self.execute([U2, B2, Lp, B2, L])
        elif self.puz[2, 3] == "O" and self.puz[3, 3] == "Y" and self.puz[3, 2] == "B":
            self.execute([Bp, U, B])
        elif self.puz[2, 3] == "B" and self.puz[3, 3] == "O" and self.puz[3, 2] == "Y":
            self.execute([U, Bp, Up, B])
        elif self.puz[0, 3] == "Y" and self.puz[3, 0] == "B" and self.puz[3, 11] == "O":
            self.execute([L, U2, Lp, Up, L, U, Lp])
        elif self.puz[0, 3] == "O" and self.puz[3, 0] == "Y" and self.puz[3, 11] == "B":
            self.execute([L, U, Lp])
        elif self.puz[0, 3] == "B" and self.puz[3, 0] == "O" and self.puz[3, 11] == "Y":
            self.execute([Bp, Up, B])
        elif self.puz[0, 5] == "Y" and self.puz[3, 9] == "B" and self.puz[3, 8] == "O":
            self.execute([B2, Lp, B2, L])
        elif self.puz[0, 5] == "O" and self.puz[3, 9] == "Y" and self.puz[3, 8] == "B":
            self.execute([Up, L, U, Lp])
        elif self.puz[0, 5] == "B" and self.puz[3, 9] == "O" and self.puz[3, 8] == "Y":
            self.execute([L, Up, Lp])
        elif self.puz[2, 5] == "Y" and self.puz[3, 6] == "B" and self.puz[3, 5] == "O":
            self.execute([Up, B2, Lp, B2, L])
        elif self.puz[2, 5] == "O" and self.puz[3, 6] == "Y" and self.puz[3, 5] == "B":
            self.execute([U2, L, U, Lp])
        else: self.execute([U2, Bp, Up, B])

        # Yellow / Red / Blue corner.
        if self.puz[8, 5] == "Y" and self.puz[5, 8] == "R" and self.puz[5, 9] == "B":
            self.execute([])
        elif self.puz[8, 5] == "B" and self.puz[5, 8] == "Y" and self.puz[5, 9] == "R":
            self.execute([B, Up, Bp, Rp, Up, R])
        elif self.puz[8, 5] == "R" and self.puz[5, 8] == "B" and self.puz[5, 9] == "Y":
            self.execute([Rp, U, R, B, U, Bp])
        elif self.puz[6, 5] == "Y" and self.puz[5, 5] == "R" and self.puz[5, 6] == "B":
            self.execute([Fp, Up, F, B, U, Bp])
        elif self.puz[6, 5] == "B" and self.puz[5, 5] == "Y" and self.puz[5, 6] == "R":
            self.execute([Fp, Up, F, Rp, Up, R])
        elif self.puz[6, 5] == "R" and self.puz[5, 5] == "B" and self.puz[5, 6] == "Y":
            self.execute([R, U2, R2, U, R])
        elif self.puz[2, 3] == "Y" and self.puz[3, 3] == "R" and self.puz[3, 2] == "B":
            self.execute([Up, R2, Bp, R2, B])
        elif self.puz[2, 3] == "B" and self.puz[3, 3] == "Y" and self.puz[3, 2] == "R":
            self.execute([U2, B, U, Bp])
        elif self.puz[2, 3] == "R" and self.puz[3, 3] == "B" and self.puz[3, 2] == "Y":
            self.execute([U2, Rp, Up, R])
        elif self.puz[0, 3] == "Y" and self.puz[3, 0] == "R" and self.puz[3, 11] == "B":
            self.execute([U2, R2, Bp, R2, B])
        elif self.puz[0, 3] == "B" and self.puz[3, 0] == "Y" and self.puz[3, 11] == "R":
            self.execute([U, B, U, Bp])
        elif self.puz[0, 3] == "R" and self.puz[3, 0] == "B" and self.puz[3, 11] == "Y":
            self.execute([U, Rp, Up, R])
        elif self.puz[0, 5] == "Y" and self.puz[3, 9] == "R" and self.puz[3, 8] == "B":
            self.execute([Rp, U2, R, U, Rp, Up, R])
        elif self.puz[0, 5] == "B" and self.puz[3, 9] == "Y" and self.puz[3, 8] == "R":
            self.execute([B, U, Bp])
        elif self.puz[0, 5] == "R" and self.puz[3, 9] == "B" and self.puz[3, 8] == "Y":
            self.execute([Rp, Up, R])
        elif self.puz[2, 5] == "Y" and self.puz[3, 6] == "R" and self.puz[3, 5] == "B":
            self.execute([R2, Bp, R2, B])
        elif self.puz[2, 5] == "B" and self.puz[3, 6] == "Y" and self.puz[3, 5] == "R":
            self.execute([Up, B, U, Bp])
        else: self.execute([Up, Rp, Up, R])

        # Yellow / Green / Red corner.
        if self.puz[6, 5] == "Y" and self.puz[5, 5] == "G" and self.puz[5, 6] == "R":
            self.execute([])
        elif self.puz[6, 5] == "R" and self.puz[5, 5] == "Y" and self.puz[5, 6] == "G":
            self.execute([R, Up, Rp, Fp, Up, F])
        elif self.puz[6, 5] == "G" and self.puz[5, 5] == "R" and self.puz[5, 6] == "Y":
            self.execute([Fp, U, F, R, U, Rp])
        elif self.puz[2, 3] == "Y" and self.puz[3, 3] == "G" and self.puz[3, 2] == "R":
            self.execute([Up, R, U2, Rp, Up, R, U, Rp])
        elif self.puz[2, 3] == "R" and self.puz[3, 3] == "Y" and self.puz[3, 2] == "G":
            self.execute([Up, R, U, Rp])
        elif self.puz[2, 3] == "G" and self.puz[3, 3] == "R" and self.puz[3, 2] == "Y":
            self.execute([R, Up, Rp])
        elif self.puz[0, 3] == "Y" and self.puz[3, 0] == "G" and self.puz[3, 11] == "R":
            self.execute([U2, R, U2, Rp, Up, R, U, Rp])
        elif self.puz[0, 3] == "R" and self.puz[3, 0] == "Y" and self.puz[3, 11] == "G":
            self.execute([U2, R, U, Rp])
        elif self.puz[0, 3] == "G" and self.puz[3, 0] == "R" and self.puz[3, 11] == "Y":
            self.execute([U2, Fp, Up, F])
        elif self.puz[0, 5] == "Y" and self.puz[3, 9] == "G" and self.puz[3, 8] == "R":
            self.execute([U, R, U2, Rp, Up, R, U, Rp])
        elif self.puz[0, 5] == "R" and self.puz[3, 9] == "Y" and self.puz[3, 8] == "G":
            self.execute([U, R, U, Rp])
        elif self.puz[0, 5] == "G" and self.puz[3, 9] == "R" and self.puz[3, 8] == "Y":
            self.execute([U, Fp, Up, F])
        elif self.puz[2, 5] == "Y" and self.puz[3, 6] == "G" and self.puz[3, 5] == "R":
            self.execute([R, U2, Rp, Up, R, U, Rp])
        elif self.puz[2, 5] == "R" and self.puz[3, 6] == "Y" and self.puz[3, 5] == "G":
            self.execute([R, U, Rp])
        else: self.execute([Fp, Up, F])

    def mEdges(self):
        # Orange / Green edge.
        if self.puz[4, 2] == "O" and self.puz[4, 3] == "G":
            self.execute([])
        elif self.puz[4, 2] == "G" and self.puz[4, 3] == "O":
            self.execute([L, U, L, U, L, Up, Lp, Up, Lp, U, Fp, Up, Fp, Up, Fp, U, F, U, F])
        elif self.puz[4, 0] == "O" and self.puz[4, 11] == "G":
            self.execute([B, U, B, U, B, Up, Bp, Up, Bp, Fp, Up, Fp, Up, Fp, U, F, U, F])
        elif self.puz[4, 0] == "G" and self.puz[4, 11] == "O":
            self.execute([B, U, B, U, B, Up, Bp, Up, Bp, U, L, U, L, U, L, Up, Lp, Up, Lp])
        elif self.puz[4, 8] == "O" and self.puz[4, 9] == "G":
            self.execute([R, U, R, U, R, Up, Rp, Up, Rp, L, U, L, U, L, Up, Lp, Up, Lp])
        elif self.puz[4, 8] == "G" and self.puz[4, 9] == "O":
            self.execute([R, U, R, U, R, Up, Rp, Up, Rp, Up, Fp, Up, Fp, Up, Fp, U, F, U, F])
        elif self.puz[4, 5] == "O" and self.puz[4, 6] == "G":
            self.execute([Rp, Up, Rp, Up, Rp, U, R, U, R, Up, Fp, Up, Fp, Up, Fp, U, F, U, F])
        elif self.puz[4, 5] == "G" and self.puz[4, 6] == "O":
            self.execute([Rp, Up, Rp, Up, Rp, U, R, U, R, L, U, L, U, L, Up, Lp, Up, Lp])
        elif self.puz[2, 4] == "O" and self.puz[3, 4] == "G":
            self.execute([Fp, Up, Fp, Up, Fp, U, F, U, F])
        elif self.puz[2, 4] == "G" and self.puz[3, 4] == "O":
            self.execute([U, L, U, L, U, L, Up, Lp, Up, Lp])
        elif self.puz[1, 3] == "O" and self.puz[3, 1] == "G":
            self.execute([Up, Fp, Up, Fp, Up, Fp, U, F, U, F])
        elif self.puz[1, 3] == "G" and self.puz[3, 1] == "O":
            self.execute([L, U, L, U, L, Up, Lp, Up, Lp])
        elif self.puz[0, 4] == "O" and self.puz[3, 10] == "G":
            self.execute([U2, Fp, Up, Fp, Up, Fp, U, F, U, F])
        elif self.puz[0, 4] == "G" and self.puz[3, 10] == "O":
            self.execute([Up, L, U, L, U, L, Up, Lp, Up, Lp])
        elif self.puz[1, 5] == "O" and self.puz[3, 7] == "G":
            self.execute([U, Fp, Up, Fp, Up, Fp, U, F, U, F])
        else: self.execute([U2, L, U, L, U, L, Up, Lp, Up, Lp])

        # Blue / Orange edge.
        if self.puz[4, 0] == "O" and self.puz[4, 11] == "B":
            self.execute([])
        elif self.puz[4, 0] == "B" and self.puz[4, 11] == "O":
            self.execute([B, U, B, U, B, Up, Bp, Up, Bp, U, Lp, Up, Lp, Up, Lp, U, L, U, L])
        elif self.puz[4, 8] == "B" and self.puz[4, 9] == "O":
            self.execute([R, U, R, U, R, Up, Rp, Up, Rp, U, B, U, B, U, B, Up, Bp, Up, Bp])
        elif self.puz[4, 8] == "O" and self.puz[4, 9] == "B":
            self.execute([R, U, R, U, R, Up, Rp, Up, Rp, Lp, Up, Lp, Up, Lp, U, L, U, L])
        elif self.puz[4, 5] == "B" and self.puz[4, 6] == "O":
            self.execute([Rp, Up, Rp, Up, Rp, U, R, U, R, Lp, Up, Lp, Up, Lp, U, L, U, L])
        elif self.puz[4, 5] == "O" and self.puz[4, 6] == "B":
            self.execute([Rp, Up, Rp, Up, Rp, U, R, U, R, U, B, U, B, U, B, Up, Bp, Up, Bp])
        elif self.puz[2, 4] == "B" and self.puz[3, 4] == "O":
            self.execute([U, Lp, Up, Lp, Up, Lp, U, L, U, L])
        elif self.puz[2, 4] == "O" and self.puz[3, 4] == "B":
            self.execute([U2, B, U, B, U, B, Up, Bp, Up, Bp])
        elif self.puz[1, 3] == "B" and self.puz[3, 1] == "O":
            self.execute([Lp, Up, Lp, Up, Lp, U, L, U, L])
        elif self.puz[1, 3] == "O" and self.puz[3, 1] == "B":
            self.execute([U, B, U, B, U, B, Up, Bp, Up, Bp])
        elif self.puz[0, 4] == "B" and self.puz[3, 10] == "O":
            self.execute([Up, Lp, Up, Lp, Up, Lp, U, L, U, L])
        elif self.puz[0, 4] == "O" and self.puz[3, 10] == "B":
            self.execute([B, U, B, U, B, Up, Bp, Up, Bp])
        elif self.puz[1, 5] == "B" and self.puz[3, 7] == "O":
            self.execute([U2, Lp, Up, Lp, Up, Lp, U, L, U, L])
        else: self.execute([Up, B, U, B, U, B, Up, Bp, Up, Bp])

        # Red / Blue edge.
        if self.puz[4, 8] == "R" and self.puz[4, 9] == "B":
            self.execute([])
        elif self.puz[4, 8] == "B" and self.puz[4, 9] == "R":
            self.execute([R, U, R, U, R, Up, Rp, Up, Rp, U, Bp, Up, Bp, Up, Bp, U, B, U, B])
        elif self.puz[4, 5] == "R" and self.puz[4, 6] == "B":
            self.execute([F, U, F, U, F, Up, Fp, Up, Fp, U, R, U, R, U, R, Up, Rp, Up, Rp])
        elif self.puz[4, 5] == "B" and self.puz[4, 6] == "R":
            self.execute([Rp, Up, Rp, Up, Rp, U, R, U, R, U2, R, U, R, U, R, Up, Rp, Up, Rp])
        elif self.puz[2, 4] == "R" and self.puz[3, 4] == "B":
            self.execute([U2, Bp, Up, Bp, Up, Bp, U, B, U, B])
        elif self.puz[2, 4] == "B" and self.puz[3, 4] == "R":
            self.execute([Up, R, U, R, U, R, Up, Rp, Up, Rp])
        elif self.puz[1, 3] == "R" and self.puz[3, 1] == "B":
            self.execute([U, Bp, Up, Bp, Up, Bp, U, B, U, B])
        elif self.puz[1, 3] == "B" and self.puz[3, 1] == "R":
            self.execute([U2, R, U, R, U, R, Up, Rp, Up, Rp])
        elif self.puz[0, 4] == "R" and self.puz[3, 10] == "B":
            self.execute([Bp, Up, Bp, Up, Bp, U, B, U, B])
        elif self.puz[0, 4] == "B" and self.puz[3, 10] == "R":
            self.execute([U, R, U, R, U, R, Up, Rp, Up, Rp])
        elif self.puz[1, 5] == "R" and self.puz[3, 7] == "B":
            self.execute([Up, Bp, Up, Bp, Up, Bp, U, B, U, B])
        else: self.execute([R, U, R, U, R, Up, Rp, Up, Rp])

        # Green / Red edge.
        if self.puz[4, 5] == "G" and self.puz[4, 6] == "R":
            self.execute([])
        elif self.puz[4, 5] == "R" and self.puz[4, 6] == "G":
            self.execute([Rp, Up, Rp, Up, Rp, U, R, U, R, Up, F, U, F, U, F, Up, Fp, Up, Fp])
        elif self.puz[2, 4] == "R" and self.puz[3, 4] == "G":
            self.execute([F, U, F, U, F, Up, Fp, Up, Fp])
        elif self.puz[2, 4] == "G" and self.puz[3, 4] == "R":
            self.execute([Up, Rp, Up, Rp, Up, Rp, U, R, U, R])
        elif self.puz[1, 3] == "R" and self.puz[3, 1] == "G":
            self.execute([Up, F, U, F, U, F, Up, Fp, Up, Fp])
        elif self.puz[1, 3] == "G" and self.puz[3, 1] == "R":
            self.execute([U2, Rp, Up, Rp, Up, Rp, U, R, U, R])
        elif self.puz[0, 4] == "R" and self.puz[3, 10] == "G":
            self.execute([U2, F, U, F, U, F, Up, Fp, Up, Fp])
        elif self.puz[0, 4] == "G" and self.puz[3, 10] == "R":
            self.execute([U, Rp, Up, Rp, Up, Rp, U, R, U, R])
        elif self.puz[1, 5] == "R" and self.puz[3, 7] == "G":
            self.execute([U, F, U, F, U, F, Up, Fp, Up, Fp])
        else: self.execute([Rp, Up, Rp, Up, Rp, U, R, U, R])

    def tEdges(self):
        if self.puz[2, 4] == "W" and self.puz[1, 3] == "W" and self.puz[0, 4] == "W" and self.puz[1, 5] == "W":
            self.execute([])
        elif self.puz[2, 4] != "W" and self.puz[1, 3] != "W" and self.puz[0, 4] != "W" and self.puz[1, 5] != "W":
            self.execute([F, R, U, Rp, Up, Fp, B, U, L, Up, Lp, Bp])
        elif self.puz[1, 3] == "W" and self.puz[1, 5] == "W":
            self.execute([F, R, U, Rp, Up, Fp])
        elif self.puz[0, 4] == "W" and self.puz[2, 4] == "W":
            self.execute([L, F, U, Fp, Up, Lp])
        elif self.puz[2, 4] == "W" and self.puz[1, 5] == "W":
            self.execute([B, U, L, Up, Lp, Bp])
        elif self.puz[1, 3] == "W" and self.puz[2, 4] == "W":
            self.execute([R, U, B, Up, Bp, Rp])
        elif self.puz[0, 4] == "W" and self.puz[1, 3] == "W":
            self.execute([F, U, R, Up, Rp, Fp])
        else: self.execute([L, U, F, Up, Fp, Lp])

    def OLL(self):
        if self.puz[3, 0] == "W" and self.puz[3, 2] == "W" and self.puz[3, 5] == "W" and self.puz[3, 9] == "W":
            self.execute([R, U2, R2, Up, R2, Up, R2, U2, R])
        elif self.puz[3, 9] == "W" and self.puz[3, 11] == "W" and self.puz[3, 2] == "W" and self.puz[3, 6] == "W":
            self.execute([F, U2, F2, Up, F2, Up, F2, U2, F])
        elif self.puz[3, 6] == "W" and self.puz[3, 8] == "W" and self.puz[3, 3] == "W" and self.puz[3, 11] == "W":
            self.execute([L, U2, L2, Up, L2, Up, L2, U2, L])
        elif self.puz[3, 3] == "W" and self.puz[3, 5] == "W" and self.puz[3, 0] == "W" and self.puz[3, 8] == "W":
            self.execute([B, U2, B2, Up, B2, Up, B2, U2, B])
        elif self.puz[3, 3] == "W" and self.puz[3, 5] == "W" and self.puz[3, 9] == "W" and self.puz[3, 11] == "W":
            self.execute([B, U, Bp, U, B, Up, Bp, U, B, U2, Bp])
        elif self.puz[3, 0] == "W" and self.puz[3, 2] == "W" and self.puz[3, 6] == "W" and self.puz[3, 8] == "W":
            self.execute([R, U, Rp, U, R, Up, Rp, U, R, U2, Rp])
        elif self.puz[3, 5] == "W" and self.puz[3, 8] == "W" and self.puz[3, 11] == "W":
            self.execute([R, U, Rp, U, R, U2, Rp])
        elif self.puz[3, 8] == "W" and self.puz[3, 11] == "W" and self.puz[3, 2] == "W":
            self.execute([B, U, Bp, U, B, U2, Bp])
        elif self.puz[3, 11] == "W" and self.puz[3, 2] == "W" and self.puz[3, 5] == "W":
            self.execute([L, U, Lp, U, L, U2, Lp])
        elif self.puz[3, 2] == "W" and self.puz[3, 5] == "W" and self.puz[3, 8] == "W":
            self.execute([F, U, Fp, U, F, U2, Fp])
        elif self.puz[3, 3] == "W" and self.puz[3, 6] == "W" and self.puz[3, 9] == "W":
            self.execute([Rp, Up, R, Up, Rp, U2, R])
        elif self.puz[3, 6] == "W" and self.puz[3, 9] == "W" and self.puz[3, 0] == "W":
            self.execute([Bp, Up, B, Up, Bp, U2, B])
        elif self.puz[3, 9] == "W" and self.puz[3, 0] == "W" and self.puz[3, 3] == "W":
            self.execute([Lp, Up, L, Up, Lp, U2, L])
        elif self.puz[3, 0] == "W" and self.puz[3, 3] == "W" and self.puz[3, 6] == "W":
            self.execute([Fp, Up, F, Up, Fp, U2, F])
        elif self.puz[3, 5] == "W" and self.puz[3, 9] == "W":
            self.execute([Rp, Fp, L, F, R, Fp, Lp, F])
        elif self.puz[3, 8] == "W" and self.puz[3, 0] == "W":
            self.execute([Bp, Rp, F, R, B, Rp, Fp, R])
        elif self.puz[3, 11] == "W" and self.puz[3, 3] == "W":
            self.execute([Lp, Bp, R, B, L, Bp, Rp, B])
        elif self.puz[3, 2] == "W" and self.puz[3, 6] == "W":
            self.execute([Fp, Lp, B, L, F, Lp, Bp, L])
        elif self.puz[3, 3] == "W" and self.puz[3, 5] == "W":
            self.execute([R2, D, Rp, U2, R, Dp, Rp, U2, Rp])
        elif self.puz[3, 6] == "W" and self.puz[3, 8] == "W":
            self.execute([B2, D, Bp, U2, B, Dp, Bp, U2, Bp])
        elif self.puz[3, 9] == "W" and self.puz[3, 11] == "W":
            self.execute([L2, D, Lp, U2, L, Dp, Lp, U2, Lp])
        elif self.puz[3, 0] == "W" and self.puz[3, 2] == "W":
            self.execute([F2, D, Fp, U2, F, Dp, Fp, U2, Fp])
        elif self.puz[3, 2] == "W" and self.puz[3, 9] == "W":
            self.execute([Rp, Fp, Lp, F, R, Fp, L, F])
        elif self.puz[3, 5] == "W" and self.puz[3, 0] == "W":
            self.execute([Bp, Rp, Fp, R, B, Rp, F, R])
        elif self.puz[3, 8] == "W" and self.puz[3, 3] == "W":
            self.execute([Lp, Bp, Rp, B, L, Bp, R, B])
        else: self.execute([Fp, Lp, Bp, L, F, Lp, B, L])


if __name__ == "__main__":
    cube = Cube()
    checkerboard = [U2, D2, R2, L2, F2, B2]
    superflip = [U, R2, F, B, R, B2, R, U2, L, B2, R, Up, Dp, R2, F, Rp, L, B2, U2, F2]

    for i in range(100):
        cube.scramble()
        cube.bEdges()
        cube.bCorners()
        cube.mEdges()
        cube.tEdges()
        cube.OLL()
        print(cube)