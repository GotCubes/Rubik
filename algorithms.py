#! /usr/bin/env python3.4

from moves import *

def bEdges(cube):
    # Yellow / Green edge.
    if cube.puz[5, 4] == "G" and cube.puz[6, 4] == "Y": pass
    elif cube.puz[5, 4] == "Y" and cube.puz[6, 4] == "G": cube.execute([Fp, Rp, Dp])
    elif cube.puz[4, 2] == "G" and cube.puz[4, 3] == "Y": cube.execute([L, D])
    elif cube.puz[4, 2] == "Y" and cube.puz[4, 3] == "G": cube.execute([Fp])
    elif cube.puz[2, 4] == "G" and cube.puz[3, 4] == "Y": cube.execute([Up, Rp, F])
    elif cube.puz[2, 4] == "Y" and cube.puz[3, 4] == "G": cube.execute([F2])
    elif cube.puz[4, 5] == "G" and cube.puz[4, 6] == "Y": cube.execute([F])
    elif cube.puz[4, 5] == "Y" and cube.puz[4, 6] == "G": cube.execute([Rp, Dp])
    elif cube.puz[4, 8] == "G" and cube.puz[4, 9] == "Y": cube.execute([R, Dp])
    elif cube.puz[4, 8] == "Y" and cube.puz[4, 9] == "G": cube.execute([Bp, D2])
    elif cube.puz[3, 1] == "G" and cube.puz[1, 3] == "Y": cube.execute([Up, F2])
    elif cube.puz[3, 1] == "Y" and cube.puz[1, 3] == "G": cube.execute([L, Fp])
    elif cube.puz[1, 5] == "G" and cube.puz[3, 7] == "Y": cube.execute([Rp, F])
    elif cube.puz[1, 5] == "Y" and cube.puz[3, 7] == "G": cube.execute([U, F2])
    elif cube.puz[5, 7] == "G" and cube.puz[7, 5] == "Y": cube.execute([Dp])
    elif cube.puz[5, 7] == "Y" and cube.puz[7, 5] == "G": cube.execute([R, F])
    elif cube.puz[7, 3] == "G" and cube.puz[5, 1] == "Y": cube.execute([Lp, Fp])
    elif cube.puz[7, 3] == "Y" and cube.puz[5, 1] == "G": cube.execute([D])
    elif cube.puz[4, 0] == "G" and cube.puz[4, 11] == "Y": cube.execute([Lp, D])
    elif cube.puz[4, 0] == "Y" and cube.puz[4, 11] == "G": cube.execute([L2, Fp])
    elif cube.puz[0, 4] == "G" and cube.puz[3, 10] == "Y": cube.execute([U, Rp, F])
    elif cube.puz[0, 4] == "Y" and cube.puz[3, 10] == "G": cube.execute([U2, F2])
    elif cube.puz[5, 10] == "G" and cube.puz[8, 4] == "Y": cube.execute([D2])
    else: cube.execute([Dp, R, F])

    # Yellow / Orange edge.
    if cube.puz[7, 3] == "Y" and cube.puz[5, 1] == "O": pass
    elif cube.puz[4, 2] == "O" and cube.puz[4, 3] == "Y": cube.execute([L])
    elif cube.puz[4, 2] == "Y" and cube.puz[4, 3] == "O": cube.execute([Fp, Dp, F])
    elif cube.puz[2, 4] == "O" and cube.puz[3, 4] == "Y": cube.execute([Fp, L, F])
    elif cube.puz[2, 4] == "Y" and cube.puz[3, 4] == "O": cube.execute([U, L2])
    elif cube.puz[4, 5] == "O" and cube.puz[4, 6] == "Y": cube.execute([F, Dp, Fp])
    elif cube.puz[4, 5] == "Y" and cube.puz[4, 6] == "O": cube.execute([R, U2, L2])
    elif cube.puz[4, 8] == "O" and cube.puz[4, 9] == "Y": cube.execute([Rp, U2, L2])
    elif cube.puz[4, 8] == "Y" and cube.puz[4, 9] == "O": cube.execute([Dp, Bp, D])
    elif cube.puz[3, 1] == "O" and cube.puz[1, 3] == "Y": cube.execute([L2])
    elif cube.puz[3, 1] == "Y" and cube.puz[1, 3] == "O": cube.execute([L, Fp, Dp, F])
    elif cube.puz[1, 5] == "O" and cube.puz[3, 7] == "Y": cube.execute([U, Fp, L, F])
    elif cube.puz[1, 5] == "Y" and cube.puz[3, 7] == "O": cube.execute([U2, L2])
    elif cube.puz[5, 7] == "O" and cube.puz[7, 5] == "Y": cube.execute([R2, U2, L2])
    elif cube.puz[5, 7] == "Y" and cube.puz[7, 5] == "O": cube.execute([R, F, Dp, Fp])
    elif cube.puz[7, 3] == "O" and cube.puz[5, 1] == "Y": cube.execute([Lp, Fp, Dp, F])
    elif cube.puz[4, 0] == "O" and cube.puz[4, 11] == "Y": cube.execute([Lp])
    elif cube.puz[4, 0] == "Y" and cube.puz[4, 11] == "O": cube.execute([Dp, B, D])
    elif cube.puz[0, 4] == "O" and cube.puz[3, 10] == "Y": cube.execute([B, Lp])
    elif cube.puz[0, 4] == "Y" and cube.puz[3, 10] == "O": cube.execute([Up, L2])
    elif cube.puz[5, 10] == "O" and cube.puz[8, 4] == "Y": cube.execute([B2, Up, L2])
    else: cube.execute([Bp, Lp])

    # Yellow / Blue edge.
    if cube.puz[8, 4] == "Y" and cube.puz[5, 10] == "B": pass
    elif cube.puz[4, 2] == "B" and cube.puz[4, 3] == "Y": cube.execute([D, L, Dp])
    elif cube.puz[4, 2] == "Y" and cube.puz[4, 3] == "B": cube.execute([D2, Fp, D2])
    elif cube.puz[2, 4] == "B" and cube.puz[3, 4] == "Y": cube.execute([Up, R, Bp])
    elif cube.puz[2, 4] == "Y" and cube.puz[3, 4] == "B": cube.execute([U2, B2])
    elif cube.puz[4, 5] == "B" and cube.puz[4, 6] == "Y": cube.execute([R2, Bp])
    elif cube.puz[4, 5] == "Y" and cube.puz[4, 6] == "B": cube.execute([Dp, Rp, D])
    elif cube.puz[4, 8] == "B" and cube.puz[4, 9] == "Y": cube.execute([Dp, R, D])
    elif cube.puz[4, 8] == "Y" and cube.puz[4, 9] == "B": cube.execute([Bp])
    elif cube.puz[3, 1] == "B" and cube.puz[1, 3] == "Y": cube.execute([U, B2])
    elif cube.puz[3, 1] == "Y" and cube.puz[1, 3] == "B": cube.execute([Lp, B, L])
    elif cube.puz[1, 5] == "B" and cube.puz[3, 7] == "Y": cube.execute([R, Bp])
    elif cube.puz[1, 5] == "Y" and cube.puz[3, 7] == "B": cube.execute([Up, B2])
    elif cube.puz[5, 7] == "B" and cube.puz[7, 5] == "Y": cube.execute([R2, Up, B2])
    elif cube.puz[5, 7] == "Y" and cube.puz[7, 5] == "B": cube.execute([Rp, Bp])
    elif cube.puz[4, 0] == "B" and cube.puz[4, 11] == "Y": cube.execute([D, Lp, Dp])
    elif cube.puz[4, 0] == "Y" and cube.puz[4, 11] == "B": cube.execute([B])
    elif cube.puz[0, 4] == "B" and cube.puz[3, 10] == "Y": cube.execute([U, R, Bp])
    elif cube.puz[0, 4] == "Y" and cube.puz[3, 10] == "B": cube.execute([B2])
    else: cube.execute([B, Dp, R, D])

    # Yellow / Red edge.
    if cube.puz[7, 5] == "Y" and cube.puz[5, 7] == "R": pass
    elif cube.puz[4, 2] == "R" and cube.puz[4, 3] == "Y": cube.execute([D2, L, D2])
    elif cube.puz[4, 2] == "Y" and cube.puz[4, 3] == "R": cube.execute([Dp, Fp, D])
    elif cube.puz[2, 4] == "R" and cube.puz[3, 4] == "Y": cube.execute([F, Rp, Fp])
    elif cube.puz[2, 4] == "Y" and cube.puz[3, 4] == "R": cube.execute([Up, R2])
    elif cube.puz[4, 5] == "R" and cube.puz[4, 6] == "Y": cube.execute([Dp, F, D])
    elif cube.puz[4, 5] == "Y" and cube.puz[4, 6] == "R": cube.execute([Rp])
    elif cube.puz[4, 8] == "R" and cube.puz[4, 9] == "Y": cube.execute([R])
    elif cube.puz[4, 8] == "Y" and cube.puz[4, 9] == "R": cube.execute([D, Bp, Dp])
    elif cube.puz[3, 1] == "R" and cube.puz[1, 3] == "Y": cube.execute([U2, R2])
    elif cube.puz[3, 1] == "Y" and cube.puz[1, 3] == "R": cube.execute([Up, F, Rp, Fp])
    elif cube.puz[1, 5] == "R" and cube.puz[3, 7] == "Y": cube.execute([U, F, Rp, Fp])
    elif cube.puz[1, 5] == "Y" and cube.puz[3, 7] == "R": cube.execute([R2])
    elif cube.puz[5, 7] == "Y" and cube.puz[7, 5] == "R": cube.execute([R, Dp, F, D])
    elif cube.puz[4, 0] == "R" and cube.puz[4, 11] == "Y": cube.execute([D2, Lp, D2])
    elif cube.puz[4, 0] == "Y" and cube.puz[4, 11] == "R": cube.execute([D, B, Dp])
    elif cube.puz[0, 4] == "R" and cube.puz[3, 10] == "Y": cube.execute([Bp, R, B])
    else: cube.execute([U, R2])


def bCorners(cube):
    # Yellow / Orange / Green corner.
    if cube.puz[6, 3] == "Y" and cube.puz[5, 2] == "O" and cube.puz[5, 3] == "G": pass
    elif cube.puz[6, 3] == "G" and cube.puz[5, 2] == "Y" and cube.puz[5, 3] == "O": cube.execute([F, Up, Fp, Lp, Up, L])
    elif cube.puz[6, 3] == "O" and cube.puz[5, 2] == "G" and cube.puz[5, 3] == "Y": cube.execute([Lp, U, L, F, U, Fp])
    elif cube.puz[8, 3] == "Y" and cube.puz[5, 11] == "O" and cube.puz[5, 0] == "G": cube.execute([Bp, Up, B, F, U, Fp])
    elif cube.puz[8, 3] == "G" and cube.puz[5, 11] == "Y" and cube.puz[5, 0] == "O": cube.execute([Bp, Up, B, Lp, Up, L])
    elif cube.puz[8, 3] == "O" and cube.puz[5, 11] == "G" and cube.puz[5, 0] == "Y": cube.execute([L, Up, L, Fp, L2, F])
    elif cube.puz[8, 5] == "Y" and cube.puz[5, 8] == "O" and cube.puz[5, 9] == "G": cube.execute([Rp, U2, R, F, U, Fp])
    elif cube.puz[8, 5] == "G" and cube.puz[5, 8] == "Y" and cube.puz[5, 9] == "O": cube.execute([Rp, U2, R, Lp, Up, L])
    elif cube.puz[8, 5] == "O" and cube.puz[5, 8] == "G" and cube.puz[5, 9] == "Y": cube.execute([B, U2, Bp, F, U, Fp])
    elif cube.puz[6, 5] == "Y" and cube.puz[5, 5] == "O" and cube.puz[5, 6] == "G": cube.execute([R, U, Rp, Lp, Up, L])
    elif cube.puz[6, 5] == "G" and cube.puz[5, 5] == "Y" and cube.puz[5, 6] == "O": cube.execute([Fp, U2, F2, Up, Fp])
    elif cube.puz[6, 5] == "O" and cube.puz[5, 5] == "G" and cube.puz[5, 6] == "Y": cube.execute([R, U, Rp, F, U, Fp])
    elif cube.puz[2, 3] == "Y" and cube.puz[3, 3] == "O" and cube.puz[3, 2] == "G": cube.execute([F, U2, Fp, Up, F, U, Fp])
    elif cube.puz[2, 3] == "G" and cube.puz[3, 3] == "Y" and cube.puz[3, 2] == "O": cube.execute([F, U, Fp])
    elif cube.puz[2, 3] == "O" and cube.puz[3, 3] == "G" and cube.puz[3, 2] == "Y": cube.execute([Lp, Up, L])
    elif cube.puz[0, 3] == "Y" and cube.puz[3, 0] == "O" and cube.puz[3, 11] == "G": cube.execute([L2, Fp, L2, F])
    elif cube.puz[0, 3] == "G" and cube.puz[3, 0] == "Y" and cube.puz[3, 11] == "O": cube.execute([Up, L, Fp, Lp, F])
    elif cube.puz[0, 3] == "O" and cube.puz[3, 0] == "G" and cube.puz[3, 11] == "Y": cube.execute([Up, Lp, Up, L])
    elif cube.puz[0, 5] == "Y" and cube.puz[3, 9] == "O" and cube.puz[3, 8] == "G": cube.execute([U, F2, L, F2, Lp])
    elif cube.puz[0, 5] == "G" and cube.puz[3, 9] == "Y" and cube.puz[3, 8] == "O": cube.execute([U2, F, U, Fp])
    elif cube.puz[0, 5] == "O" and cube.puz[3, 9] == "G" and cube.puz[3, 8] == "Y": cube.execute([U2, Lp, Up, L])
    elif cube.puz[2, 5] == "Y" and cube.puz[3, 6] == "O" and cube.puz[3, 5] == "G": cube.execute([F2, L, F2, Lp])
    elif cube.puz[2, 5] == "G" and cube.puz[3, 6] == "Y" and cube.puz[3, 5] == "O": cube.execute([Lp, U, L])
    else: cube.execute([U, Lp, Up, L])

    # Yellow / Blue / Orange corner.
    if cube.puz[8, 3] == "Y" and cube.puz[5, 11] == "B" and cube.puz[5, 0] == "O": pass
    elif cube.puz[8, 3] == "O" and cube.puz[5, 11] == "Y" and cube.puz[5, 0] == "B": cube.execute([L, Up, Lp, Bp, Up, B])
    elif cube.puz[8, 3] == "B" and cube.puz[5, 11] == "O" and cube.puz[5, 0] == "Y": cube.execute([Bp, U, B, L, U, Lp])
    elif cube.puz[8, 5] == "Y" and cube.puz[5, 8] == "B" and cube.puz[5, 9] == "O": cube.execute([Rp, Up, R, L, U, Lp])
    elif cube.puz[8, 5] == "O" and cube.puz[5, 8] == "Y" and cube.puz[5, 9] == "B": cube.execute([Rp, Up, R, Bp, Up, B])
    elif cube.puz[8, 5] == "B" and cube.puz[5, 8] == "O" and cube.puz[5, 9] == "Y": cube.execute([Rp, U, R, Up, L, U, Lp])
    elif cube.puz[6, 5] == "Y" and cube.puz[5, 5] == "B" and cube.puz[5, 6] == "O": cube.execute([R2, B2, Lp, B2, L, R2])
    elif cube.puz[6, 5] == "O" and cube.puz[5, 5] == "Y" and cube.puz[5, 6] == "B": cube.execute([Fp, Up, F, L, Up, Lp])
    elif cube.puz[6, 5] == "B" and cube.puz[5, 5] == "O" and cube.puz[5, 6] == "Y": cube.execute([R, U, Rp, Bp, U, B])
    elif cube.puz[2, 3] == "Y" and cube.puz[3, 3] == "B" and cube.puz[3, 2] == "O": cube.execute([U2, B2, Lp, B2, L])
    elif cube.puz[2, 3] == "O" and cube.puz[3, 3] == "Y" and cube.puz[3, 2] == "B": cube.execute([Bp, U, B])
    elif cube.puz[2, 3] == "B" and cube.puz[3, 3] == "O" and cube.puz[3, 2] == "Y": cube.execute([U, Bp, Up, B])
    elif cube.puz[0, 3] == "Y" and cube.puz[3, 0] == "B" and cube.puz[3, 11] == "O": cube.execute([L, U2, Lp, Up, L, U, Lp])
    elif cube.puz[0, 3] == "O" and cube.puz[3, 0] == "Y" and cube.puz[3, 11] == "B": cube.execute([L, U, Lp])
    elif cube.puz[0, 3] == "B" and cube.puz[3, 0] == "O" and cube.puz[3, 11] == "Y": cube.execute([Bp, Up, B])
    elif cube.puz[0, 5] == "Y" and cube.puz[3, 9] == "B" and cube.puz[3, 8] == "O": cube.execute([B2, Lp, B2, L])
    elif cube.puz[0, 5] == "O" and cube.puz[3, 9] == "Y" and cube.puz[3, 8] == "B": cube.execute([Up, L, U, Lp])
    elif cube.puz[0, 5] == "B" and cube.puz[3, 9] == "O" and cube.puz[3, 8] == "Y": cube.execute([L, Up, Lp])
    elif cube.puz[2, 5] == "Y" and cube.puz[3, 6] == "B" and cube.puz[3, 5] == "O": cube.execute([Up, B2, Lp, B2, L])
    elif cube.puz[2, 5] == "O" and cube.puz[3, 6] == "Y" and cube.puz[3, 5] == "B": cube.execute([U2, L, U, Lp])
    else: cube.execute([U2, Bp, Up, B])

    # Yellow / Red / Blue corner.
    if cube.puz[8, 5] == "Y" and cube.puz[5, 8] == "R" and cube.puz[5, 9] == "B": pass
    elif cube.puz[8, 5] == "B" and cube.puz[5, 8] == "Y" and cube.puz[5, 9] == "R": cube.execute([B, Up, Bp, Rp, Up, R])
    elif cube.puz[8, 5] == "R" and cube.puz[5, 8] == "B" and cube.puz[5, 9] == "Y": cube.execute([Rp, U, R, B, U, Bp])
    elif cube.puz[6, 5] == "Y" and cube.puz[5, 5] == "R" and cube.puz[5, 6] == "B": cube.execute([Fp, Up, F, B, U, Bp])
    elif cube.puz[6, 5] == "B" and cube.puz[5, 5] == "Y" and cube.puz[5, 6] == "R": cube.execute([Fp, Up, F, Rp, Up, R])
    elif cube.puz[6, 5] == "R" and cube.puz[5, 5] == "B" and cube.puz[5, 6] == "Y": cube.execute([R, U2, R2, U, R])
    elif cube.puz[2, 3] == "Y" and cube.puz[3, 3] == "R" and cube.puz[3, 2] == "B": cube.execute([Up, R2, Bp, R2, B])
    elif cube.puz[2, 3] == "B" and cube.puz[3, 3] == "Y" and cube.puz[3, 2] == "R": cube.execute([U2, B, U, Bp])
    elif cube.puz[2, 3] == "R" and cube.puz[3, 3] == "B" and cube.puz[3, 2] == "Y": cube.execute([U2, Rp, Up, R])
    elif cube.puz[0, 3] == "Y" and cube.puz[3, 0] == "R" and cube.puz[3, 11] == "B": cube.execute([U2, R2, Bp, R2, B])
    elif cube.puz[0, 3] == "B" and cube.puz[3, 0] == "Y" and cube.puz[3, 11] == "R": cube.execute([U, B, U, Bp])
    elif cube.puz[0, 3] == "R" and cube.puz[3, 0] == "B" and cube.puz[3, 11] == "Y": cube.execute([U, Rp, Up, R])
    elif cube.puz[0, 5] == "Y" and cube.puz[3, 9] == "R" and cube.puz[3, 8] == "B": cube.execute([Rp, U2, R, U, Rp, Up, R])
    elif cube.puz[0, 5] == "B" and cube.puz[3, 9] == "Y" and cube.puz[3, 8] == "R": cube.execute([B, U, Bp])
    elif cube.puz[0, 5] == "R" and cube.puz[3, 9] == "B" and cube.puz[3, 8] == "Y": cube.execute([Rp, Up, R])
    elif cube.puz[2, 5] == "Y" and cube.puz[3, 6] == "R" and cube.puz[3, 5] == "B": cube.execute([R2, Bp, R2, B])
    elif cube.puz[2, 5] == "B" and cube.puz[3, 6] == "Y" and cube.puz[3, 5] == "R": cube.execute([Up, B, U, Bp])
    else: cube.execute([Up, Rp, Up, R])

    # Yellow / Green / Red corner.
    if cube.puz[6, 5] == "Y" and cube.puz[5, 5] == "G" and cube.puz[5, 6] == "R": pass
    elif cube.puz[6, 5] == "R" and cube.puz[5, 5] == "Y" and cube.puz[5, 6] == "G": cube.execute([R, Up, Rp, Fp, Up, F])
    elif cube.puz[6, 5] == "G" and cube.puz[5, 5] == "R" and cube.puz[5, 6] == "Y": cube.execute([Fp, U, F, R, U, Rp])
    elif cube.puz[2, 3] == "Y" and cube.puz[3, 3] == "G" and cube.puz[3, 2] == "R": cube.execute([Up, R, U2, Rp, Up, R, U, Rp])
    elif cube.puz[2, 3] == "R" and cube.puz[3, 3] == "Y" and cube.puz[3, 2] == "G": cube.execute([Up, R, U, Rp])
    elif cube.puz[2, 3] == "G" and cube.puz[3, 3] == "R" and cube.puz[3, 2] == "Y": cube.execute([R, Up, Rp])
    elif cube.puz[0, 3] == "Y" and cube.puz[3, 0] == "G" and cube.puz[3, 11] == "R": cube.execute([U2, R, U2, Rp, Up, R, U, Rp])
    elif cube.puz[0, 3] == "R" and cube.puz[3, 0] == "Y" and cube.puz[3, 11] == "G": cube.execute([U2, R, U, Rp])
    elif cube.puz[0, 3] == "G" and cube.puz[3, 0] == "R" and cube.puz[3, 11] == "Y": cube.execute([U2, Fp, Up, F])
    elif cube.puz[0, 5] == "Y" and cube.puz[3, 9] == "G" and cube.puz[3, 8] == "R": cube.execute([U, R, U2, Rp, Up, R, U, Rp])
    elif cube.puz[0, 5] == "R" and cube.puz[3, 9] == "Y" and cube.puz[3, 8] == "G": cube.execute([U, R, U, Rp])
    elif cube.puz[0, 5] == "G" and cube.puz[3, 9] == "R" and cube.puz[3, 8] == "Y": cube.execute([U, Fp, Up, F])
    elif cube.puz[2, 5] == "Y" and cube.puz[3, 6] == "G" and cube.puz[3, 5] == "R": cube.execute([R, U2, Rp, Up, R, U, Rp])
    elif cube.puz[2, 5] == "R" and cube.puz[3, 6] == "Y" and cube.puz[3, 5] == "G": cube.execute([R, U, Rp])
    else: cube.execute([Fp, Up, F])


def mEdges(cube):
    # Orange / Green edge.
    if cube.puz[4, 2] == "O" and cube.puz[4, 3] == "G": pass
    elif cube.puz[4, 2] == "G" and cube.puz[4, 3] == "O": cube.execute([L, U, L, U, L, Up, Lp, Up, Lp, U, Fp, Up, Fp, Up, Fp, U, F, U, F])
    elif cube.puz[4, 0] == "O" and cube.puz[4, 11] == "G": cube.execute([B, U, B, U, B, Up, Bp, Up, Bp, Fp, Up, Fp, Up, Fp, U, F, U, F])
    elif cube.puz[4, 0] == "G" and cube.puz[4, 11] == "O": cube.execute([B, U, B, U, B, Up, Bp, Up, Bp, U, L, U, L, U, L, Up, Lp, Up, Lp])
    elif cube.puz[4, 8] == "O" and cube.puz[4, 9] == "G": cube.execute([R, U, R, U, R, Up, Rp, Up, Rp, L, U, L, U, L, Up, Lp, Up, Lp])
    elif cube.puz[4, 8] == "G" and cube.puz[4, 9] == "O": cube.execute([R, U, R, U, R, Up, Rp, Up, Rp, Up, Fp, Up, Fp, Up, Fp, U, F, U, F])
    elif cube.puz[4, 5] == "O" and cube.puz[4, 6] == "G": cube.execute([Rp, Up, Rp, Up, Rp, U, R, U, R, Up, Fp, Up, Fp, Up, Fp, U, F, U, F])
    elif cube.puz[4, 5] == "G" and cube.puz[4, 6] == "O": cube.execute([Rp, Up, Rp, Up, Rp, U, R, U, R, L, U, L, U, L, Up, Lp, Up, Lp])
    elif cube.puz[2, 4] == "O" and cube.puz[3, 4] == "G": cube.execute([Fp, Up, Fp, Up, Fp, U, F, U, F])
    elif cube.puz[2, 4] == "G" and cube.puz[3, 4] == "O": cube.execute([U, L, U, L, U, L, Up, Lp, Up, Lp])
    elif cube.puz[1, 3] == "O" and cube.puz[3, 1] == "G": cube.execute([Up, Fp, Up, Fp, Up, Fp, U, F, U, F])
    elif cube.puz[1, 3] == "G" and cube.puz[3, 1] == "O": cube.execute([L, U, L, U, L, Up, Lp, Up, Lp])
    elif cube.puz[0, 4] == "O" and cube.puz[3, 10] == "G": cube.execute([U2, Fp, Up, Fp, Up, Fp, U, F, U, F])
    elif cube.puz[0, 4] == "G" and cube.puz[3, 10] == "O": cube.execute([Up, L, U, L, U, L, Up, Lp, Up, Lp])
    elif cube.puz[1, 5] == "O" and cube.puz[3, 7] == "G": cube.execute([U, Fp, Up, Fp, Up, Fp, U, F, U, F])
    else: cube.execute([U2, L, U, L, U, L, Up, Lp, Up, Lp])

    # Blue / Orange edge.
    if cube.puz[4, 0] == "O" and cube.puz[4, 11] == "B": pass
    elif cube.puz[4, 0] == "B" and cube.puz[4, 11] == "O": cube.execute([B, U, B, U, B, Up, Bp, Up, Bp, U, Lp, Up, Lp, Up, Lp, U, L, U, L])
    elif cube.puz[4, 8] == "B" and cube.puz[4, 9] == "O": cube.execute([R, U, R, U, R, Up, Rp, Up, Rp, U, B, U, B, U, B, Up, Bp, Up, Bp])
    elif cube.puz[4, 8] == "O" and cube.puz[4, 9] == "B": cube.execute([R, U, R, U, R, Up, Rp, Up, Rp, Lp, Up, Lp, Up, Lp, U, L, U, L])
    elif cube.puz[4, 5] == "B" and cube.puz[4, 6] == "O": cube.execute([Rp, Up, Rp, Up, Rp, U, R, U, R, Lp, Up, Lp, Up, Lp, U, L, U, L])
    elif cube.puz[4, 5] == "O" and cube.puz[4, 6] == "B": cube.execute([Rp, Up, Rp, Up, Rp, U, R, U, R, U, B, U, B, U, B, Up, Bp, Up, Bp])
    elif cube.puz[2, 4] == "B" and cube.puz[3, 4] == "O": cube.execute([U, Lp, Up, Lp, Up, Lp, U, L, U, L])
    elif cube.puz[2, 4] == "O" and cube.puz[3, 4] == "B": cube.execute([U2, B, U, B, U, B, Up, Bp, Up, Bp])
    elif cube.puz[1, 3] == "B" and cube.puz[3, 1] == "O": cube.execute([Lp, Up, Lp, Up, Lp, U, L, U, L])
    elif cube.puz[1, 3] == "O" and cube.puz[3, 1] == "B": cube.execute([U, B, U, B, U, B, Up, Bp, Up, Bp])
    elif cube.puz[0, 4] == "B" and cube.puz[3, 10] == "O": cube.execute([Up, Lp, Up, Lp, Up, Lp, U, L, U, L])
    elif cube.puz[0, 4] == "O" and cube.puz[3, 10] == "B": cube.execute([B, U, B, U, B, Up, Bp, Up, Bp])
    elif cube.puz[1, 5] == "B" and cube.puz[3, 7] == "O": cube.execute([U2, Lp, Up, Lp, Up, Lp, U, L, U, L])
    else: cube.execute([Up, B, U, B, U, B, Up, Bp, Up, Bp])

    # Red / Blue edge.
    if cube.puz[4, 8] == "R" and cube.puz[4, 9] == "B": pass
    elif cube.puz[4, 8] == "B" and cube.puz[4, 9] == "R": cube.execute([R, U, R, U, R, Up, Rp, Up, Rp, U, Bp, Up, Bp, Up, Bp, U, B, U, B])
    elif cube.puz[4, 5] == "R" and cube.puz[4, 6] == "B": cube.execute([F, U, F, U, F, Up, Fp, Up, Fp, U, R, U, R, U, R, Up, Rp, Up, Rp])
    elif cube.puz[4, 5] == "B" and cube.puz[4, 6] == "R": cube.execute([Rp, Up, Rp, Up, Rp, U, R, U, R, U2, R, U, R, U, R, Up, Rp, Up, Rp])
    elif cube.puz[2, 4] == "R" and cube.puz[3, 4] == "B": cube.execute([U2, Bp, Up, Bp, Up, Bp, U, B, U, B])
    elif cube.puz[2, 4] == "B" and cube.puz[3, 4] == "R": cube.execute([Up, R, U, R, U, R, Up, Rp, Up, Rp])
    elif cube.puz[1, 3] == "R" and cube.puz[3, 1] == "B": cube.execute([U, Bp, Up, Bp, Up, Bp, U, B, U, B])
    elif cube.puz[1, 3] == "B" and cube.puz[3, 1] == "R": cube.execute([U2, R, U, R, U, R, Up, Rp, Up, Rp])
    elif cube.puz[0, 4] == "R" and cube.puz[3, 10] == "B": cube.execute([Bp, Up, Bp, Up, Bp, U, B, U, B])
    elif cube.puz[0, 4] == "B" and cube.puz[3, 10] == "R": cube.execute([U, R, U, R, U, R, Up, Rp, Up, Rp])
    elif cube.puz[1, 5] == "R" and cube.puz[3, 7] == "B": cube.execute([Up, Bp, Up, Bp, Up, Bp, U, B, U, B])
    else: cube.execute([R, U, R, U, R, Up, Rp, Up, Rp])

    # Green / Red edge.
    if cube.puz[4, 5] == "G" and cube.puz[4, 6] == "R": pass
    elif cube.puz[4, 5] == "R" and cube.puz[4, 6] == "G": cube.execute([Rp, Up, Rp, Up, Rp, U, R, U, R, Up, F, U, F, U, F, Up, Fp, Up, Fp])
    elif cube.puz[2, 4] == "R" and cube.puz[3, 4] == "G": cube.execute([F, U, F, U, F, Up, Fp, Up, Fp])
    elif cube.puz[2, 4] == "G" and cube.puz[3, 4] == "R": cube.execute([Up, Rp, Up, Rp, Up, Rp, U, R, U, R])
    elif cube.puz[1, 3] == "R" and cube.puz[3, 1] == "G": cube.execute([Up, F, U, F, U, F, Up, Fp, Up, Fp])
    elif cube.puz[1, 3] == "G" and cube.puz[3, 1] == "R": cube.execute([U2, Rp, Up, Rp, Up, Rp, U, R, U, R])
    elif cube.puz[0, 4] == "R" and cube.puz[3, 10] == "G": cube.execute([U2, F, U, F, U, F, Up, Fp, Up, Fp])
    elif cube.puz[0, 4] == "G" and cube.puz[3, 10] == "R": cube.execute([U, Rp, Up, Rp, Up, Rp, U, R, U, R])
    elif cube.puz[1, 5] == "R" and cube.puz[3, 7] == "G": cube.execute([U, F, U, F, U, F, Up, Fp, Up, Fp])
    else: cube.execute([Rp, Up, Rp, Up, Rp, U, R, U, R])


def OLL(cube):
    # Top layer edge orientation.
    if cube.puz[2, 4] == "W" and cube.puz[1, 3] == "W" and cube.puz[0, 4] == "W" and cube.puz[1, 5] == "W": pass
    elif cube.puz[2, 4] != "W" and cube.puz[1, 3] != "W" and cube.puz[0, 4] != "W" and cube.puz[1, 5] != "W": cube.execute([F, R, U, Rp, Up, Fp, B, U, L, Up, Lp, Bp])
    elif cube.puz[1, 3] == "W" and cube.puz[1, 5] == "W": cube.execute([F, R, U, Rp, Up, Fp])
    elif cube.puz[0, 4] == "W" and cube.puz[2, 4] == "W": cube.execute([L, F, U, Fp, Up, Lp])
    elif cube.puz[2, 4] == "W" and cube.puz[1, 5] == "W": cube.execute([B, U, L, Up, Lp, Bp])
    elif cube.puz[1, 3] == "W" and cube.puz[2, 4] == "W": cube.execute([R, U, B, Up, Bp, Rp])
    elif cube.puz[0, 4] == "W" and cube.puz[1, 3] == "W": cube.execute([F, U, R, Up, Rp, Fp])
    else: cube.execute([L, U, F, Up, Fp, Lp])

    # Top layer corner orientation.
    if cube.puz[0, 3] == "W" and cube.puz[0, 5] == "W" and cube.puz[2, 3] == "W" and cube.puz[2, 5] == "W": pass
    elif cube.puz[3, 0] == "W" and cube.puz[3, 2] == "W" and cube.puz[3, 5] == "W" and cube.puz[3, 9] == "W": cube.execute([R, U2, R2, Up, R2, Up, R2, U2, R])
    elif cube.puz[3, 9] == "W" and cube.puz[3, 11] == "W" and cube.puz[3, 2] == "W" and cube.puz[3, 6] == "W": cube.execute([F, U2, F2, Up, F2, Up, F2, U2, F])
    elif cube.puz[3, 6] == "W" and cube.puz[3, 8] == "W" and cube.puz[3, 3] == "W" and cube.puz[3, 11] == "W": cube.execute([L, U2, L2, Up, L2, Up, L2, U2, L])
    elif cube.puz[3, 3] == "W" and cube.puz[3, 5] == "W" and cube.puz[3, 0] == "W" and cube.puz[3, 8] == "W": cube.execute([B, U2, B2, Up, B2, Up, B2, U2, B])
    elif cube.puz[3, 3] == "W" and cube.puz[3, 5] == "W" and cube.puz[3, 9] == "W" and cube.puz[3, 11] == "W": cube.execute([B, U, Bp, U, B, Up, Bp, U, B, U2, Bp])
    elif cube.puz[3, 0] == "W" and cube.puz[3, 2] == "W" and cube.puz[3, 6] == "W" and cube.puz[3, 8] == "W": cube.execute([R, U, Rp, U, R, Up, Rp, U, R, U2, Rp])
    elif cube.puz[3, 5] == "W" and cube.puz[3, 8] == "W" and cube.puz[3, 11] == "W": cube.execute([R, U, Rp, U, R, U2, Rp])
    elif cube.puz[3, 8] == "W" and cube.puz[3, 11] == "W" and cube.puz[3, 2] == "W": cube.execute([B, U, Bp, U, B, U2, Bp])
    elif cube.puz[3, 11] == "W" and cube.puz[3, 2] == "W" and cube.puz[3, 5] == "W": cube.execute([L, U, Lp, U, L, U2, Lp])
    elif cube.puz[3, 2] == "W" and cube.puz[3, 5] == "W" and cube.puz[3, 8] == "W": cube.execute([F, U, Fp, U, F, U2, Fp])
    elif cube.puz[3, 3] == "W" and cube.puz[3, 6] == "W" and cube.puz[3, 9] == "W": cube.execute([Rp, Up, R, Up, Rp, U2, R])
    elif cube.puz[3, 6] == "W" and cube.puz[3, 9] == "W" and cube.puz[3, 0] == "W": cube.execute([Bp, Up, B, Up, Bp, U2, B])
    elif cube.puz[3, 9] == "W" and cube.puz[3, 0] == "W" and cube.puz[3, 3] == "W": cube.execute([Lp, Up, L, Up, Lp, U2, L])
    elif cube.puz[3, 0] == "W" and cube.puz[3, 3] == "W" and cube.puz[3, 6] == "W": cube.execute([Fp, Up, F, Up, Fp, U2, F])
    elif cube.puz[3, 5] == "W" and cube.puz[3, 9] == "W": cube.execute([Rp, Fp, L, F, R, Fp, Lp, F])
    elif cube.puz[3, 8] == "W" and cube.puz[3, 0] == "W": cube.execute([Bp, Rp, F, R, B, Rp, Fp, R])
    elif cube.puz[3, 11] == "W" and cube.puz[3, 3] == "W": cube.execute([Lp, Bp, R, B, L, Bp, Rp, B])
    elif cube.puz[3, 2] == "W" and cube.puz[3, 6] == "W": cube.execute([Fp, Lp, B, L, F, Lp, Bp, L])
    elif cube.puz[3, 3] == "W" and cube.puz[3, 5] == "W": cube.execute([R2, D, Rp, U2, R, Dp, Rp, U2, Rp])
    elif cube.puz[3, 6] == "W" and cube.puz[3, 8] == "W": cube.execute([B2, D, Bp, U2, B, Dp, Bp, U2, Bp])
    elif cube.puz[3, 9] == "W" and cube.puz[3, 11] == "W": cube.execute([L2, D, Lp, U2, L, Dp, Lp, U2, Lp])
    elif cube.puz[3, 0] == "W" and cube.puz[3, 2] == "W": cube.execute([F2, D, Fp, U2, F, Dp, Fp, U2, Fp])
    elif cube.puz[3, 2] == "W" and cube.puz[3, 9] == "W": cube.execute([Rp, Fp, Lp, F, R, Fp, L, F])
    elif cube.puz[3, 5] == "W" and cube.puz[3, 0] == "W": cube.execute([Bp, Rp, Fp, R, B, Rp, F, R])
    elif cube.puz[3, 8] == "W" and cube.puz[3, 3] == "W": cube.execute([Lp, Bp, Rp, B, L, Bp, R, B])
    else: cube.execute([Fp, Lp, Bp, L, F, Lp, B, L])


def PLL(cube):
    # Top layer corner permutation.
    if cube.puz[3, 3] == cube.puz[3, 5] and cube.puz[3, 6] == cube.puz[3, 8] and cube.puz[3, 9] == cube.puz[3, 11] and cube.puz[3, 0] == cube.puz[3, 2]: pass
    elif cube.puz[3, 3] != cube.puz[3, 5] and cube.puz[3, 6] != cube.puz[3, 8] and cube.puz[3, 9] != cube.puz[3, 11] and cube.puz[3, 0] != cube.puz[3, 2]: cube.execute([R, Bp, Rp, F, R, B, Rp, Fp, R, B, Rp, F, R, Bp, Rp, Fp])
    elif cube.puz[3, 3] == cube.puz[3, 5]: cube.execute([Lp, B, Lp, F2, L, Bp, Lp, F2, L2])
    elif cube.puz[3, 6] == cube.puz[3, 8]: cube.execute([Fp, L, Fp, R2, F, Lp, Fp, R2, F2])
    elif cube.puz[3, 9] == cube.puz[3, 11]: cube.execute([Rp, F, Rp, B2, R, Fp, Rp, B2, R2])
    else: cube.execute([Bp, R, Bp, L2, B, Rp, Bp, L2, B2])

    # Top layer edge permutation.
    if cube.puz[3, 3] == cube.puz[3, 4] and cube.puz[3, 6] == cube.puz[3, 7] and cube.puz[3, 9] == cube.puz[3, 10] and cube.puz[3, 0] == cube.puz[3, 1]: pass
    elif cube.puz[3, 9] == cube.puz[3, 10] and cube.puz[3, 4] == cube.puz[3, 6]: cube.execute([R, Up, R, U, R, U, R, Up, Rp, Up, R2])
    elif cube.puz[3, 9] == cube.puz[3, 10] and cube.puz[3, 4] == cube.puz[3, 2]: cube.execute([R2, U, R, U, Rp, Up, Rp, Up, Rp, U, Rp])
    elif cube.puz[3, 0] == cube.puz[3, 1] and cube.puz[3, 7] == cube.puz[3, 9]: cube.execute([B, Up, B, U, B, U, B, Up, Bp, Up, B2])
    elif cube.puz[3, 0] == cube.puz[3, 1] and cube.puz[3, 7] == cube.puz[3, 5]: cube.execute([B2, U, B, U, Bp, Up, Bp, Up, Bp, U, Bp])
    elif cube.puz[3, 3] == cube.puz[3, 4] and cube.puz[3, 10] == cube.puz[3, 0]: cube.execute([L, Up, L, U, L, U, L, Up, Lp, Up, L2])
    elif cube.puz[3, 3] == cube.puz[3, 4] and cube.puz[3, 10] == cube.puz[3, 8]: cube.execute([L2, U, L, U, Lp, Up, Lp, Up, Lp, U, Lp])
    elif cube.puz[3, 6] == cube.puz[3, 7] and cube.puz[3, 1] == cube.puz[3, 3]: cube.execute([F, Up, F, U, F, U, F, Up, Fp, Up, F2])
    elif cube.puz[3, 6] == cube.puz[3, 7] and cube.puz[3, 1] == cube.puz[3, 11]: cube.execute([F2, U, F, U, Fp, Up, Fp, Up, Fp, U, Fp])
    elif cube.puz[3, 4] == cube.puz[3, 2]: cube.execute([Fp, Up, F2, U, F, U, Fp, Up, F, U, F, Up, F, Up, Fp])
    elif cube.puz[3, 4] == cube.puz[3, 6]: cube.execute([Rp, Up, R2, U, R, U, Rp, Up, R, U, R, Up, R, Up, Rp])
    else: cube.execute([R2, U2, R2, U2, R2, U, R2, U2, R2, U2, R2, Up])

    # Final alignment.
    if cube.puz[3, 4] == "G": pass
    elif cube.puz[3, 4] == "O": cube.execute([U])
    elif cube.puz[3, 4] == "B": cube.execute([U2])
    else: cube.execute([Up])