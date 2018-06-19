#! /usr/bin/env python3.4

import numpy as np

def translate(puz, num):
    puz[3] = np.roll(puz[3], 3 * num)
    puz[4] = np.roll(puz[4], 3 * num)
    puz[5] = np.roll(puz[5], 3 * num)
    puz[0:3, 3:6] = np.rot90(puz[0:3, 3:6], num)
    puz[6:9, 3:6] = np.rot90(puz[6:9, 3:6], -num)

# Up face operations
def U(puz):
    puz[3] = np.roll(puz[3], -3)
    puz[0:3, 3:6] = np.rot90(puz[0:3, 3:6], -1)

def Up(puz):
    puz[3] = np.roll(puz[3], 3)
    puz[0:3, 3:6] = np.rot90(puz[0:3, 3:6], 1)

def U2(puz):
    puz[3] = np.roll(puz[3], 6)
    puz[0:3, 3:6] = np.rot90(puz[0:3, 3:6], 2)

# Down face operations.
def D(puz):
    puz[5] = np.roll(puz[5], 3)
    puz[6:9, 3:6] = np.rot90(puz[6:9, 3:6], -1)

def Dp(puz):
    puz[5] = np.roll(puz[5], -3)
    puz[6:9, 3:6] = np.rot90(puz[6:9, 3:6], 1)

def D2(puz):
    puz[5] = np.roll(puz[5], 6)
    puz[6:9, 3:6] = np.rot90(puz[6:9, 3:6], 2)

# Front face operations.
def F(puz):
    puz[2:7, 2:7] = np.rot90(puz[2:7, 2:7], -1)

def Fp(puz):
    puz[2:7, 2:7] = np.rot90(puz[2:7, 2:7], 1)

def F2(puz):
    puz[2:7, 2:7] = np.rot90(puz[2:7, 2:7], 2)

# Back face operations.
def B(puz):
    translate(puz, 2)
    puz[2:7, 2:7] = np.rot90(puz[2:7, 2:7], -1)
    translate(puz, -2)

def Bp(puz):
    translate(puz, 2)
    puz[2:7, 2:7] = np.rot90(puz[2:7, 2:7], 1)
    translate(puz, -2)

def B2(puz):
    translate(puz, 2)
    puz[2:7, 2:7] = np.rot90(puz[2:7, 2:7], 2)
    translate(puz, -2)

# Left face operations.
def L(puz):
    translate(puz, 1)
    puz[2:7, 2:7] = np.rot90(puz[2:7, 2:7], -1)
    translate(puz, -1)

def Lp(puz):
    translate(puz, 1)
    puz[2:7, 2:7] = np.rot90(puz[2:7, 2:7], 1)
    translate(puz, -1)

def L2(puz):
    translate(puz, 1)
    puz[2:7, 2:7] = np.rot90(puz[2:7, 2:7], 2)
    translate(puz, -1)

# Right face operations.
def R(puz):
    translate(puz, -1)
    puz[2:7, 2:7] = np.rot90(puz[2:7, 2:7], -1)
    translate(puz, 1)

def Rp(puz):
    translate(puz, -1)
    puz[2:7, 2:7] = np.rot90(puz[2:7, 2:7], 1)
    translate(puz, 1)

def R2(puz):
    translate(puz, -1)
    puz[2:7, 2:7] = np.rot90(puz[2:7, 2:7], 2)
    translate(puz, 1)