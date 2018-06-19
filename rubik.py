#! /usr/bin/env python3.4

import numpy as np

class Cube:
    def __init__(self):
        self.puz = np.chararray((9, 12))
        self.puz[:] = '_'
        self.puz[0:3, 3:6] = 'W'
        self.puz[3:6, 0:3] = 'O'
        self.puz[3:6, 3:6] = 'G'
        self.puz[3:6, 6:9] = 'R'
        self.puz[3:6, 9:12] = 'B'
        self.puz[6:9, 3:6] = 'Y'

    #  Up face operations.
    def U(self):
        self.puz[3] = np.roll(self.puz[3], -3)
        self.puz[0:3, 3:6] = np.rot90(self.puz[0:3, 3:6], -1)

    def Up(self):
        self.puz[3] = np.roll(self.puz[3], 3)
        self.puz[0:3, 3:6] = np.rot90(self.puz[0:3, 3:6], 1)

    def U2(self):
        self.puz[3] = np.roll(self.puz[3], 6)
        self.puz[0:3, 3:6] = np.rot90(self.puz[0:3, 3:6], 2)

    # Down face operations.
    def D(self):
        self.puz[5] = np.roll(self.puz[5], 3)
        self.puz[6:9, 3:6] = np.rot90(self.puz[6:9, 3:6], -1)

    def Dp(self):
        self.puz[5] = np.roll(self.puz[5], -3)
        self.puz[6:9, 3:6] = np.rot90(self.puz[6:9, 3:6], 1)

    def D2(self):
        self.puz[5] = np.roll(self.puz[5], 6)
        self.puz[6:9, 3:6] = np.rot90(self.puz[6:9, 3:6], 2)

    # Front face operations.
    def F(self):
        self.puz[2:7, 2:7] = np.rot90(self.puz[2:7, 2:7], -1)

    def Fp(self):
        self.puz[2:7, 2:7] = np.rot90(self.puz[2:7, 2:7], 1)

    def F2(self):
        self.puz[2:7, 2:7] = np.rot90(self.puz[2:7, 2:7], 2)

    # Back face operations.
    def B(self):
        self.puz[3] = np.roll(self.puz[3], 6)
        self.puz[4] = np.roll(self.puz[4], 6)
        self.puz[5] = np.roll(self.puz[5], 6)
        self.puz[0:3, 3:6] = np.rot90(self.puz[0:3, 3:6], 2)
        self.puz[6:9, 3:6] = np.rot90(self.puz[6:9, 3:6], 2)
        self.puz[2:7, 2:7] = np.rot90(self.puz[2:7, 2:7], -1)
        self.puz[6:9, 3:6] = np.rot90(self.puz[6:9, 3:6], 2)
        self.puz[0:3, 3:6] = np.rot90(self.puz[0:3, 3:6], 2)
        self.puz[3] = np.roll(self.puz[3], -6)
        self.puz[4] = np.roll(self.puz[4], -6)
        self.puz[5] = np.roll(self.puz[5], -6)

    def Bp(self):
        self.puz[3] = np.roll(self.puz[3], 6)
        self.puz[4] = np.roll(self.puz[4], 6)
        self.puz[5] = np.roll(self.puz[5], 6)
        self.puz[0:3, 3:6] = np.rot90(self.puz[0:3, 3:6], 2)
        self.puz[6:9, 3:6] = np.rot90(self.puz[6:9, 3:6], 2)
        self.puz[2:7, 2:7] = np.rot90(self.puz[2:7, 2:7], 1)
        self.puz[6:9, 3:6] = np.rot90(self.puz[6:9, 3:6], 2)
        self.puz[0:3, 3:6] = np.rot90(self.puz[0:3, 3:6], 2)
        self.puz[3] = np.roll(self.puz[3], -6)
        self.puz[4] = np.roll(self.puz[4], -6)
        self.puz[5] = np.roll(self.puz[5], -6)

    def B2(self):
        self.puz[3] = np.roll(self.puz[3], 6)
        self.puz[4] = np.roll(self.puz[4], 6)
        self.puz[5] = np.roll(self.puz[5], 6)
        self.puz[0:3, 3:6] = np.rot90(self.puz[0:3, 3:6], 2)
        self.puz[6:9, 3:6] = np.rot90(self.puz[6:9, 3:6], 2)
        self.puz[2:7, 2:7] = np.rot90(self.puz[2:7, 2:7], 2)
        self.puz[6:9, 3:6] = np.rot90(self.puz[6:9, 3:6], 2)
        self.puz[0:3, 3:6] = np.rot90(self.puz[0:3, 3:6], 2)
        self.puz[3] = np.roll(self.puz[3], -6)
        self.puz[4] = np.roll(self.puz[4], -6)
        self.puz[5] = np.roll(self.puz[5], -6)

    # Left face operations.
    def L(self):
        self.puz[3] = np.roll(self.puz[3], 3)
        self.puz[4] = np.roll(self.puz[4], 3)
        self.puz[5] = np.roll(self.puz[5], 3)
        self.puz[0:3, 3:6] = np.rot90(self.puz[0:3, 3:6], 1)
        self.puz[6:9, 3:6] = np.rot90(self.puz[6:9, 3:6], -1)
        self.puz[2:7, 2:7] = np.rot90(self.puz[2:7, 2:7], -1)
        self.puz[6:9, 3:6] = np.rot90(self.puz[6:9, 3:6], 1)
        self.puz[0:3, 3:6] = np.rot90(self.puz[0:3, 3:6], -1)
        self.puz[3] = np.roll(self.puz[3], -3)
        self.puz[4] = np.roll(self.puz[4], -3)
        self.puz[5] = np.roll(self.puz[5], -3)

    def Lp(self):
        self.puz[3] = np.roll(self.puz[3], 3)
        self.puz[4] = np.roll(self.puz[4], 3)
        self.puz[5] = np.roll(self.puz[5], 3)
        self.puz[0:3, 3:6] = np.rot90(self.puz[0:3, 3:6], 1)
        self.puz[6:9, 3:6] = np.rot90(self.puz[6:9, 3:6], -1)
        self.puz[2:7, 2:7] = np.rot90(self.puz[2:7, 2:7], 1)
        self.puz[6:9, 3:6] = np.rot90(self.puz[6:9, 3:6], 1)
        self.puz[0:3, 3:6] = np.rot90(self.puz[0:3, 3:6], -1)
        self.puz[3] = np.roll(self.puz[3], -3)
        self.puz[4] = np.roll(self.puz[4], -3)
        self.puz[5] = np.roll(self.puz[5], -3)

    def L2(self):
        self.puz[3] = np.roll(self.puz[3], 3)
        self.puz[4] = np.roll(self.puz[4], 3)
        self.puz[5] = np.roll(self.puz[5], 3)
        self.puz[0:3, 3:6] = np.rot90(self.puz[0:3, 3:6], 1)
        self.puz[6:9, 3:6] = np.rot90(self.puz[6:9, 3:6], -1)
        self.puz[2:7, 2:7] = np.rot90(self.puz[2:7, 2:7], 2)
        self.puz[6:9, 3:6] = np.rot90(self.puz[6:9, 3:6], 1)
        self.puz[0:3, 3:6] = np.rot90(self.puz[0:3, 3:6], -1)
        self.puz[3] = np.roll(self.puz[3], -3)
        self.puz[4] = np.roll(self.puz[4], -3)
        self.puz[5] = np.roll(self.puz[5], -3)

    # Right face operations.
    def R(self):
        self.puz[3] = np.roll(self.puz[3], -3)
        self.puz[4] = np.roll(self.puz[4], -3)
        self.puz[5] = np.roll(self.puz[5], -3)
        self.puz[0:3, 3:6] = np.rot90(self.puz[0:3, 3:6], -1)
        self.puz[6:9, 3:6] = np.rot90(self.puz[6:9, 3:6], 1)
        self.puz[2:7, 2:7] = np.rot90(self.puz[2:7, 2:7], -1)
        self.puz[6:9, 3:6] = np.rot90(self.puz[6:9, 3:6], -1)
        self.puz[0:3, 3:6] = np.rot90(self.puz[0:3, 3:6], 1)
        self.puz[3] = np.roll(self.puz[3], 3)
        self.puz[4] = np.roll(self.puz[4], 3)
        self.puz[5] = np.roll(self.puz[5], 3)

    def Rp(self):
        self.puz[3] = np.roll(self.puz[3], -3)
        self.puz[4] = np.roll(self.puz[4], -3)
        self.puz[5] = np.roll(self.puz[5], -3)
        self.puz[0:3, 3:6] = np.rot90(self.puz[0:3, 3:6], -1)
        self.puz[6:9, 3:6] = np.rot90(self.puz[6:9, 3:6], 1)
        self.puz[2:7, 2:7] = np.rot90(self.puz[2:7, 2:7], 1)
        self.puz[6:9, 3:6] = np.rot90(self.puz[6:9, 3:6], -1)
        self.puz[0:3, 3:6] = np.rot90(self.puz[0:3, 3:6], 1)
        self.puz[3] = np.roll(self.puz[3], 3)
        self.puz[4] = np.roll(self.puz[4], 3)
        self.puz[5] = np.roll(self.puz[5], 3)

    def R2(self):
        self.puz[3] = np.roll(self.puz[3], -3)
        self.puz[4] = np.roll(self.puz[4], -3)
        self.puz[5] = np.roll(self.puz[5], -3)
        self.puz[0:3, 3:6] = np.rot90(self.puz[0:3, 3:6], -1)
        self.puz[6:9, 3:6] = np.rot90(self.puz[6:9, 3:6], 1)
        self.puz[2:7, 2:7] = np.rot90(self.puz[2:7, 2:7], 2)
        self.puz[6:9, 3:6] = np.rot90(self.puz[6:9, 3:6], -1)
        self.puz[0:3, 3:6] = np.rot90(self.puz[0:3, 3:6], 1)
        self.puz[3] = np.roll(self.puz[3], 3)
        self.puz[4] = np.roll(self.puz[4], 3)
        self.puz[5] = np.roll(self.puz[5], 3)

if __name__ == "__main__":
    cube = Cube()

    # Superflip
    cube.U()
    cube.R2()
    cube.F()
    cube.B()
    cube.R()
    cube.B2()
    cube.R()
    cube.U2()
    cube.L()
    cube.B2()
    cube.R()
    cube.Up()
    cube.Dp()
    cube.R2()
    cube.F()
    cube.Rp()
    cube.L()
    cube.B2()
    cube.U2()
    cube.F2()

    print(cube.puz)