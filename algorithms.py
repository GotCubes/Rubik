#! /usr/bin/env python3.4

from moves import *

def bEdges(puzzle):
    # Yellow / Green edge.
    if puzzle.cube.puz[5, 4] == "G" and puzzle.cube.puz[6, 4] == "Y": pass
    elif puzzle.cube.puz[5, 4] == "Y" and puzzle.cube.puz[6, 4] == "G": puzzle.execute([Fp, Rp, Dp])
    elif puzzle.cube.puz[4, 2] == "G" and puzzle.cube.puz[4, 3] == "Y": puzzle.execute([L, D])
    elif puzzle.cube.puz[4, 2] == "Y" and puzzle.cube.puz[4, 3] == "G": puzzle.execute([Fp])
    elif puzzle.cube.puz[2, 4] == "G" and puzzle.cube.puz[3, 4] == "Y": puzzle.execute([Up, Rp, F])
    elif puzzle.cube.puz[2, 4] == "Y" and puzzle.cube.puz[3, 4] == "G": puzzle.execute([F2])
    elif puzzle.cube.puz[4, 5] == "G" and puzzle.cube.puz[4, 6] == "Y": puzzle.execute([F])
    elif puzzle.cube.puz[4, 5] == "Y" and puzzle.cube.puz[4, 6] == "G": puzzle.execute([Rp, Dp])
    elif puzzle.cube.puz[4, 8] == "G" and puzzle.cube.puz[4, 9] == "Y": puzzle.execute([R, Dp])
    elif puzzle.cube.puz[4, 8] == "Y" and puzzle.cube.puz[4, 9] == "G": puzzle.execute([Bp, D2])
    elif puzzle.cube.puz[3, 1] == "G" and puzzle.cube.puz[1, 3] == "Y": puzzle.execute([Up, F2])
    elif puzzle.cube.puz[3, 1] == "Y" and puzzle.cube.puz[1, 3] == "G": puzzle.execute([L, Fp])
    elif puzzle.cube.puz[1, 5] == "G" and puzzle.cube.puz[3, 7] == "Y": puzzle.execute([Rp, F])
    elif puzzle.cube.puz[1, 5] == "Y" and puzzle.cube.puz[3, 7] == "G": puzzle.execute([U, F2])
    elif puzzle.cube.puz[5, 7] == "G" and puzzle.cube.puz[7, 5] == "Y": puzzle.execute([Dp])
    elif puzzle.cube.puz[5, 7] == "Y" and puzzle.cube.puz[7, 5] == "G": puzzle.execute([R, F])
    elif puzzle.cube.puz[7, 3] == "G" and puzzle.cube.puz[5, 1] == "Y": puzzle.execute([Lp, Fp])
    elif puzzle.cube.puz[7, 3] == "Y" and puzzle.cube.puz[5, 1] == "G": puzzle.execute([D])
    elif puzzle.cube.puz[4, 0] == "G" and puzzle.cube.puz[4, 11] == "Y": puzzle.execute([Lp, D])
    elif puzzle.cube.puz[4, 0] == "Y" and puzzle.cube.puz[4, 11] == "G": puzzle.execute([L2, Fp])
    elif puzzle.cube.puz[0, 4] == "G" and puzzle.cube.puz[3, 10] == "Y": puzzle.execute([U, Rp, F])
    elif puzzle.cube.puz[0, 4] == "Y" and puzzle.cube.puz[3, 10] == "G": puzzle.execute([U2, F2])
    elif puzzle.cube.puz[5, 10] == "G" and puzzle.cube.puz[8, 4] == "Y": puzzle.execute([D2])
    else: puzzle.execute([Dp, R, F])

    # Yellow / Orange edge.
    if puzzle.cube.puz[7, 3] == "Y" and puzzle.cube.puz[5, 1] == "O": pass
    elif puzzle.cube.puz[4, 2] == "O" and puzzle.cube.puz[4, 3] == "Y": puzzle.execute([L])
    elif puzzle.cube.puz[4, 2] == "Y" and puzzle.cube.puz[4, 3] == "O": puzzle.execute([Fp, Dp, F])
    elif puzzle.cube.puz[2, 4] == "O" and puzzle.cube.puz[3, 4] == "Y": puzzle.execute([Fp, L, F])
    elif puzzle.cube.puz[2, 4] == "Y" and puzzle.cube.puz[3, 4] == "O": puzzle.execute([U, L2])
    elif puzzle.cube.puz[4, 5] == "O" and puzzle.cube.puz[4, 6] == "Y": puzzle.execute([F, Dp, Fp])
    elif puzzle.cube.puz[4, 5] == "Y" and puzzle.cube.puz[4, 6] == "O": puzzle.execute([R, U2, L2])
    elif puzzle.cube.puz[4, 8] == "O" and puzzle.cube.puz[4, 9] == "Y": puzzle.execute([Rp, U2, L2])
    elif puzzle.cube.puz[4, 8] == "Y" and puzzle.cube.puz[4, 9] == "O": puzzle.execute([Dp, Bp, D])
    elif puzzle.cube.puz[3, 1] == "O" and puzzle.cube.puz[1, 3] == "Y": puzzle.execute([L2])
    elif puzzle.cube.puz[3, 1] == "Y" and puzzle.cube.puz[1, 3] == "O": puzzle.execute([L, Fp, Dp, F])
    elif puzzle.cube.puz[1, 5] == "O" and puzzle.cube.puz[3, 7] == "Y": puzzle.execute([U, Fp, L, F])
    elif puzzle.cube.puz[1, 5] == "Y" and puzzle.cube.puz[3, 7] == "O": puzzle.execute([U2, L2])
    elif puzzle.cube.puz[5, 7] == "O" and puzzle.cube.puz[7, 5] == "Y": puzzle.execute([R2, U2, L2])
    elif puzzle.cube.puz[5, 7] == "Y" and puzzle.cube.puz[7, 5] == "O": puzzle.execute([R, F, Dp, Fp])
    elif puzzle.cube.puz[7, 3] == "O" and puzzle.cube.puz[5, 1] == "Y": puzzle.execute([Lp, Fp, Dp, F])
    elif puzzle.cube.puz[4, 0] == "O" and puzzle.cube.puz[4, 11] == "Y": puzzle.execute([Lp])
    elif puzzle.cube.puz[4, 0] == "Y" and puzzle.cube.puz[4, 11] == "O": puzzle.execute([Dp, B, D])
    elif puzzle.cube.puz[0, 4] == "O" and puzzle.cube.puz[3, 10] == "Y": puzzle.execute([B, Lp])
    elif puzzle.cube.puz[0, 4] == "Y" and puzzle.cube.puz[3, 10] == "O": puzzle.execute([Up, L2])
    elif puzzle.cube.puz[5, 10] == "O" and puzzle.cube.puz[8, 4] == "Y": puzzle.execute([B2, Up, L2])
    else: puzzle.execute([Bp, Lp])

    # Yellow / Blue edge.
    if puzzle.cube.puz[8, 4] == "Y" and puzzle.cube.puz[5, 10] == "B": pass
    elif puzzle.cube.puz[4, 2] == "B" and puzzle.cube.puz[4, 3] == "Y": puzzle.execute([D, L, Dp])
    elif puzzle.cube.puz[4, 2] == "Y" and puzzle.cube.puz[4, 3] == "B": puzzle.execute([D2, Fp, D2])
    elif puzzle.cube.puz[2, 4] == "B" and puzzle.cube.puz[3, 4] == "Y": puzzle.execute([Up, R, Bp])
    elif puzzle.cube.puz[2, 4] == "Y" and puzzle.cube.puz[3, 4] == "B": puzzle.execute([U2, B2])
    elif puzzle.cube.puz[4, 5] == "B" and puzzle.cube.puz[4, 6] == "Y": puzzle.execute([R2, Bp])
    elif puzzle.cube.puz[4, 5] == "Y" and puzzle.cube.puz[4, 6] == "B": puzzle.execute([Dp, Rp, D])
    elif puzzle.cube.puz[4, 8] == "B" and puzzle.cube.puz[4, 9] == "Y": puzzle.execute([Dp, R, D])
    elif puzzle.cube.puz[4, 8] == "Y" and puzzle.cube.puz[4, 9] == "B": puzzle.execute([Bp])
    elif puzzle.cube.puz[3, 1] == "B" and puzzle.cube.puz[1, 3] == "Y": puzzle.execute([U, B2])
    elif puzzle.cube.puz[3, 1] == "Y" and puzzle.cube.puz[1, 3] == "B": puzzle.execute([Lp, B, L])
    elif puzzle.cube.puz[1, 5] == "B" and puzzle.cube.puz[3, 7] == "Y": puzzle.execute([R, Bp])
    elif puzzle.cube.puz[1, 5] == "Y" and puzzle.cube.puz[3, 7] == "B": puzzle.execute([Up, B2])
    elif puzzle.cube.puz[5, 7] == "B" and puzzle.cube.puz[7, 5] == "Y": puzzle.execute([R2, Up, B2])
    elif puzzle.cube.puz[5, 7] == "Y" and puzzle.cube.puz[7, 5] == "B": puzzle.execute([Rp, Bp])
    elif puzzle.cube.puz[4, 0] == "B" and puzzle.cube.puz[4, 11] == "Y": puzzle.execute([D, Lp, Dp])
    elif puzzle.cube.puz[4, 0] == "Y" and puzzle.cube.puz[4, 11] == "B": puzzle.execute([B])
    elif puzzle.cube.puz[0, 4] == "B" and puzzle.cube.puz[3, 10] == "Y": puzzle.execute([U, R, Bp])
    elif puzzle.cube.puz[0, 4] == "Y" and puzzle.cube.puz[3, 10] == "B": puzzle.execute([B2])
    else: puzzle.execute([B, Dp, R, D])

    # Yellow / Red edge.
    if puzzle.cube.puz[7, 5] == "Y" and puzzle.cube.puz[5, 7] == "R": pass
    elif puzzle.cube.puz[4, 2] == "R" and puzzle.cube.puz[4, 3] == "Y": puzzle.execute([D2, L, D2])
    elif puzzle.cube.puz[4, 2] == "Y" and puzzle.cube.puz[4, 3] == "R": puzzle.execute([Dp, Fp, D])
    elif puzzle.cube.puz[2, 4] == "R" and puzzle.cube.puz[3, 4] == "Y": puzzle.execute([F, Rp, Fp])
    elif puzzle.cube.puz[2, 4] == "Y" and puzzle.cube.puz[3, 4] == "R": puzzle.execute([Up, R2])
    elif puzzle.cube.puz[4, 5] == "R" and puzzle.cube.puz[4, 6] == "Y": puzzle.execute([Dp, F, D])
    elif puzzle.cube.puz[4, 5] == "Y" and puzzle.cube.puz[4, 6] == "R": puzzle.execute([Rp])
    elif puzzle.cube.puz[4, 8] == "R" and puzzle.cube.puz[4, 9] == "Y": puzzle.execute([R])
    elif puzzle.cube.puz[4, 8] == "Y" and puzzle.cube.puz[4, 9] == "R": puzzle.execute([D, Bp, Dp])
    elif puzzle.cube.puz[3, 1] == "R" and puzzle.cube.puz[1, 3] == "Y": puzzle.execute([U2, R2])
    elif puzzle.cube.puz[3, 1] == "Y" and puzzle.cube.puz[1, 3] == "R": puzzle.execute([Up, F, Rp, Fp])
    elif puzzle.cube.puz[1, 5] == "R" and puzzle.cube.puz[3, 7] == "Y": puzzle.execute([U, F, Rp, Fp])
    elif puzzle.cube.puz[1, 5] == "Y" and puzzle.cube.puz[3, 7] == "R": puzzle.execute([R2])
    elif puzzle.cube.puz[5, 7] == "Y" and puzzle.cube.puz[7, 5] == "R": puzzle.execute([R, Dp, F, D])
    elif puzzle.cube.puz[4, 0] == "R" and puzzle.cube.puz[4, 11] == "Y": puzzle.execute([D2, Lp, D2])
    elif puzzle.cube.puz[4, 0] == "Y" and puzzle.cube.puz[4, 11] == "R": puzzle.execute([D, B, Dp])
    elif puzzle.cube.puz[0, 4] == "R" and puzzle.cube.puz[3, 10] == "Y": puzzle.execute([Bp, R, B])
    else: puzzle.execute([U, R2])


def bCorners(puzzle):
    # Yellow / Orange / Green corner.
    if puzzle.cube.puz[6, 3] == "Y" and puzzle.cube.puz[5, 2] == "O" and puzzle.cube.puz[5, 3] == "G": pass
    elif puzzle.cube.puz[6, 3] == "G" and puzzle.cube.puz[5, 2] == "Y" and puzzle.cube.puz[5, 3] == "O": puzzle.execute([F, Up, Fp, Lp, Up, L])
    elif puzzle.cube.puz[6, 3] == "O" and puzzle.cube.puz[5, 2] == "G" and puzzle.cube.puz[5, 3] == "Y": puzzle.execute([Lp, U, L, F, U, Fp])
    elif puzzle.cube.puz[8, 3] == "Y" and puzzle.cube.puz[5, 11] == "O" and puzzle.cube.puz[5, 0] == "G": puzzle.execute([Bp, Up, B, F, U, Fp])
    elif puzzle.cube.puz[8, 3] == "G" and puzzle.cube.puz[5, 11] == "Y" and puzzle.cube.puz[5, 0] == "O": puzzle.execute([Bp, Up, B, Lp, Up, L])
    elif puzzle.cube.puz[8, 3] == "O" and puzzle.cube.puz[5, 11] == "G" and puzzle.cube.puz[5, 0] == "Y": puzzle.execute([L, Up, L, Fp, L2, F])
    elif puzzle.cube.puz[8, 5] == "Y" and puzzle.cube.puz[5, 8] == "O" and puzzle.cube.puz[5, 9] == "G": puzzle.execute([Rp, U2, R, F, U, Fp])
    elif puzzle.cube.puz[8, 5] == "G" and puzzle.cube.puz[5, 8] == "Y" and puzzle.cube.puz[5, 9] == "O": puzzle.execute([Rp, U2, R, Lp, Up, L])
    elif puzzle.cube.puz[8, 5] == "O" and puzzle.cube.puz[5, 8] == "G" and puzzle.cube.puz[5, 9] == "Y": puzzle.execute([B, U2, Bp, F, U, Fp])
    elif puzzle.cube.puz[6, 5] == "Y" and puzzle.cube.puz[5, 5] == "O" and puzzle.cube.puz[5, 6] == "G": puzzle.execute([R, U, Rp, Lp, Up, L])
    elif puzzle.cube.puz[6, 5] == "G" and puzzle.cube.puz[5, 5] == "Y" and puzzle.cube.puz[5, 6] == "O": puzzle.execute([Fp, U2, F2, Up, Fp])
    elif puzzle.cube.puz[6, 5] == "O" and puzzle.cube.puz[5, 5] == "G" and puzzle.cube.puz[5, 6] == "Y": puzzle.execute([R, U, Rp, F, U, Fp])
    elif puzzle.cube.puz[2, 3] == "Y" and puzzle.cube.puz[3, 3] == "O" and puzzle.cube.puz[3, 2] == "G": puzzle.execute([F, U2, Fp, Up, F, U, Fp])
    elif puzzle.cube.puz[2, 3] == "G" and puzzle.cube.puz[3, 3] == "Y" and puzzle.cube.puz[3, 2] == "O": puzzle.execute([F, U, Fp])
    elif puzzle.cube.puz[2, 3] == "O" and puzzle.cube.puz[3, 3] == "G" and puzzle.cube.puz[3, 2] == "Y": puzzle.execute([Lp, Up, L])
    elif puzzle.cube.puz[0, 3] == "Y" and puzzle.cube.puz[3, 0] == "O" and puzzle.cube.puz[3, 11] == "G": puzzle.execute([L2, Fp, L2, F])
    elif puzzle.cube.puz[0, 3] == "G" and puzzle.cube.puz[3, 0] == "Y" and puzzle.cube.puz[3, 11] == "O": puzzle.execute([Up, L, Fp, Lp, F])
    elif puzzle.cube.puz[0, 3] == "O" and puzzle.cube.puz[3, 0] == "G" and puzzle.cube.puz[3, 11] == "Y": puzzle.execute([Up, Lp, Up, L])
    elif puzzle.cube.puz[0, 5] == "Y" and puzzle.cube.puz[3, 9] == "O" and puzzle.cube.puz[3, 8] == "G": puzzle.execute([U, F2, L, F2, Lp])
    elif puzzle.cube.puz[0, 5] == "G" and puzzle.cube.puz[3, 9] == "Y" and puzzle.cube.puz[3, 8] == "O": puzzle.execute([U2, F, U, Fp])
    elif puzzle.cube.puz[0, 5] == "O" and puzzle.cube.puz[3, 9] == "G" and puzzle.cube.puz[3, 8] == "Y": puzzle.execute([U2, Lp, Up, L])
    elif puzzle.cube.puz[2, 5] == "Y" and puzzle.cube.puz[3, 6] == "O" and puzzle.cube.puz[3, 5] == "G": puzzle.execute([F2, L, F2, Lp])
    elif puzzle.cube.puz[2, 5] == "G" and puzzle.cube.puz[3, 6] == "Y" and puzzle.cube.puz[3, 5] == "O": puzzle.execute([Lp, U, L])
    else: puzzle.execute([U, Lp, Up, L])

    # Yellow / Blue / Orange corner.
    if puzzle.cube.puz[8, 3] == "Y" and puzzle.cube.puz[5, 11] == "B" and puzzle.cube.puz[5, 0] == "O": pass
    elif puzzle.cube.puz[8, 3] == "O" and puzzle.cube.puz[5, 11] == "Y" and puzzle.cube.puz[5, 0] == "B": puzzle.execute([L, Up, Lp, Bp, Up, B])
    elif puzzle.cube.puz[8, 3] == "B" and puzzle.cube.puz[5, 11] == "O" and puzzle.cube.puz[5, 0] == "Y": puzzle.execute([Bp, U, B, L, U, Lp])
    elif puzzle.cube.puz[8, 5] == "Y" and puzzle.cube.puz[5, 8] == "B" and puzzle.cube.puz[5, 9] == "O": puzzle.execute([Rp, Up, R, L, U, Lp])
    elif puzzle.cube.puz[8, 5] == "O" and puzzle.cube.puz[5, 8] == "Y" and puzzle.cube.puz[5, 9] == "B": puzzle.execute([Rp, Up, R, Bp, Up, B])
    elif puzzle.cube.puz[8, 5] == "B" and puzzle.cube.puz[5, 8] == "O" and puzzle.cube.puz[5, 9] == "Y": puzzle.execute([Rp, U, R, Up, L, U, Lp])
    elif puzzle.cube.puz[6, 5] == "Y" and puzzle.cube.puz[5, 5] == "B" and puzzle.cube.puz[5, 6] == "O": puzzle.execute([R2, B2, Lp, B2, L, R2])
    elif puzzle.cube.puz[6, 5] == "O" and puzzle.cube.puz[5, 5] == "Y" and puzzle.cube.puz[5, 6] == "B": puzzle.execute([Fp, Up, F, L, Up, Lp])
    elif puzzle.cube.puz[6, 5] == "B" and puzzle.cube.puz[5, 5] == "O" and puzzle.cube.puz[5, 6] == "Y": puzzle.execute([R, U, Rp, Bp, U, B])
    elif puzzle.cube.puz[2, 3] == "Y" and puzzle.cube.puz[3, 3] == "B" and puzzle.cube.puz[3, 2] == "O": puzzle.execute([U2, B2, Lp, B2, L])
    elif puzzle.cube.puz[2, 3] == "O" and puzzle.cube.puz[3, 3] == "Y" and puzzle.cube.puz[3, 2] == "B": puzzle.execute([Bp, U, B])
    elif puzzle.cube.puz[2, 3] == "B" and puzzle.cube.puz[3, 3] == "O" and puzzle.cube.puz[3, 2] == "Y": puzzle.execute([U, Bp, Up, B])
    elif puzzle.cube.puz[0, 3] == "Y" and puzzle.cube.puz[3, 0] == "B" and puzzle.cube.puz[3, 11] == "O": puzzle.execute([L, U2, Lp, Up, L, U, Lp])
    elif puzzle.cube.puz[0, 3] == "O" and puzzle.cube.puz[3, 0] == "Y" and puzzle.cube.puz[3, 11] == "B": puzzle.execute([L, U, Lp])
    elif puzzle.cube.puz[0, 3] == "B" and puzzle.cube.puz[3, 0] == "O" and puzzle.cube.puz[3, 11] == "Y": puzzle.execute([Bp, Up, B])
    elif puzzle.cube.puz[0, 5] == "Y" and puzzle.cube.puz[3, 9] == "B" and puzzle.cube.puz[3, 8] == "O": puzzle.execute([B2, Lp, B2, L])
    elif puzzle.cube.puz[0, 5] == "O" and puzzle.cube.puz[3, 9] == "Y" and puzzle.cube.puz[3, 8] == "B": puzzle.execute([Up, L, U, Lp])
    elif puzzle.cube.puz[0, 5] == "B" and puzzle.cube.puz[3, 9] == "O" and puzzle.cube.puz[3, 8] == "Y": puzzle.execute([L, Up, Lp])
    elif puzzle.cube.puz[2, 5] == "Y" and puzzle.cube.puz[3, 6] == "B" and puzzle.cube.puz[3, 5] == "O": puzzle.execute([Up, B2, Lp, B2, L])
    elif puzzle.cube.puz[2, 5] == "O" and puzzle.cube.puz[3, 6] == "Y" and puzzle.cube.puz[3, 5] == "B": puzzle.execute([U2, L, U, Lp])
    else: puzzle.execute([U2, Bp, Up, B])

    # Yellow / Red / Blue corner.
    if puzzle.cube.puz[8, 5] == "Y" and puzzle.cube.puz[5, 8] == "R" and puzzle.cube.puz[5, 9] == "B": pass
    elif puzzle.cube.puz[8, 5] == "B" and puzzle.cube.puz[5, 8] == "Y" and puzzle.cube.puz[5, 9] == "R": puzzle.execute([B, Up, Bp, Rp, Up, R])
    elif puzzle.cube.puz[8, 5] == "R" and puzzle.cube.puz[5, 8] == "B" and puzzle.cube.puz[5, 9] == "Y": puzzle.execute([Rp, U, R, B, U, Bp])
    elif puzzle.cube.puz[6, 5] == "Y" and puzzle.cube.puz[5, 5] == "R" and puzzle.cube.puz[5, 6] == "B": puzzle.execute([Fp, Up, F, B, U, Bp])
    elif puzzle.cube.puz[6, 5] == "B" and puzzle.cube.puz[5, 5] == "Y" and puzzle.cube.puz[5, 6] == "R": puzzle.execute([Fp, Up, F, Rp, Up, R])
    elif puzzle.cube.puz[6, 5] == "R" and puzzle.cube.puz[5, 5] == "B" and puzzle.cube.puz[5, 6] == "Y": puzzle.execute([R, U2, R2, U, R])
    elif puzzle.cube.puz[2, 3] == "Y" and puzzle.cube.puz[3, 3] == "R" and puzzle.cube.puz[3, 2] == "B": puzzle.execute([Up, R2, Bp, R2, B])
    elif puzzle.cube.puz[2, 3] == "B" and puzzle.cube.puz[3, 3] == "Y" and puzzle.cube.puz[3, 2] == "R": puzzle.execute([U2, B, U, Bp])
    elif puzzle.cube.puz[2, 3] == "R" and puzzle.cube.puz[3, 3] == "B" and puzzle.cube.puz[3, 2] == "Y": puzzle.execute([U2, Rp, Up, R])
    elif puzzle.cube.puz[0, 3] == "Y" and puzzle.cube.puz[3, 0] == "R" and puzzle.cube.puz[3, 11] == "B": puzzle.execute([U2, R2, Bp, R2, B])
    elif puzzle.cube.puz[0, 3] == "B" and puzzle.cube.puz[3, 0] == "Y" and puzzle.cube.puz[3, 11] == "R": puzzle.execute([U, B, U, Bp])
    elif puzzle.cube.puz[0, 3] == "R" and puzzle.cube.puz[3, 0] == "B" and puzzle.cube.puz[3, 11] == "Y": puzzle.execute([U, Rp, Up, R])
    elif puzzle.cube.puz[0, 5] == "Y" and puzzle.cube.puz[3, 9] == "R" and puzzle.cube.puz[3, 8] == "B": puzzle.execute([Rp, U2, R, U, Rp, Up, R])
    elif puzzle.cube.puz[0, 5] == "B" and puzzle.cube.puz[3, 9] == "Y" and puzzle.cube.puz[3, 8] == "R": puzzle.execute([B, U, Bp])
    elif puzzle.cube.puz[0, 5] == "R" and puzzle.cube.puz[3, 9] == "B" and puzzle.cube.puz[3, 8] == "Y": puzzle.execute([Rp, Up, R])
    elif puzzle.cube.puz[2, 5] == "Y" and puzzle.cube.puz[3, 6] == "R" and puzzle.cube.puz[3, 5] == "B": puzzle.execute([R2, Bp, R2, B])
    elif puzzle.cube.puz[2, 5] == "B" and puzzle.cube.puz[3, 6] == "Y" and puzzle.cube.puz[3, 5] == "R": puzzle.execute([Up, B, U, Bp])
    else: puzzle.execute([Up, Rp, Up, R])

    # Yellow / Green / Red corner.
    if puzzle.cube.puz[6, 5] == "Y" and puzzle.cube.puz[5, 5] == "G" and puzzle.cube.puz[5, 6] == "R": pass
    elif puzzle.cube.puz[6, 5] == "R" and puzzle.cube.puz[5, 5] == "Y" and puzzle.cube.puz[5, 6] == "G": puzzle.execute([R, Up, Rp, Fp, Up, F])
    elif puzzle.cube.puz[6, 5] == "G" and puzzle.cube.puz[5, 5] == "R" and puzzle.cube.puz[5, 6] == "Y": puzzle.execute([Fp, U, F, R, U, Rp])
    elif puzzle.cube.puz[2, 3] == "Y" and puzzle.cube.puz[3, 3] == "G" and puzzle.cube.puz[3, 2] == "R": puzzle.execute([Up, R, U2, Rp, Up, R, U, Rp])
    elif puzzle.cube.puz[2, 3] == "R" and puzzle.cube.puz[3, 3] == "Y" and puzzle.cube.puz[3, 2] == "G": puzzle.execute([Up, R, U, Rp])
    elif puzzle.cube.puz[2, 3] == "G" and puzzle.cube.puz[3, 3] == "R" and puzzle.cube.puz[3, 2] == "Y": puzzle.execute([R, Up, Rp])
    elif puzzle.cube.puz[0, 3] == "Y" and puzzle.cube.puz[3, 0] == "G" and puzzle.cube.puz[3, 11] == "R": puzzle.execute([U2, R, U2, Rp, Up, R, U, Rp])
    elif puzzle.cube.puz[0, 3] == "R" and puzzle.cube.puz[3, 0] == "Y" and puzzle.cube.puz[3, 11] == "G": puzzle.execute([U2, R, U, Rp])
    elif puzzle.cube.puz[0, 3] == "G" and puzzle.cube.puz[3, 0] == "R" and puzzle.cube.puz[3, 11] == "Y": puzzle.execute([U2, Fp, Up, F])
    elif puzzle.cube.puz[0, 5] == "Y" and puzzle.cube.puz[3, 9] == "G" and puzzle.cube.puz[3, 8] == "R": puzzle.execute([U, R, U2, Rp, Up, R, U, Rp])
    elif puzzle.cube.puz[0, 5] == "R" and puzzle.cube.puz[3, 9] == "Y" and puzzle.cube.puz[3, 8] == "G": puzzle.execute([U, R, U, Rp])
    elif puzzle.cube.puz[0, 5] == "G" and puzzle.cube.puz[3, 9] == "R" and puzzle.cube.puz[3, 8] == "Y": puzzle.execute([U, Fp, Up, F])
    elif puzzle.cube.puz[2, 5] == "Y" and puzzle.cube.puz[3, 6] == "G" and puzzle.cube.puz[3, 5] == "R": puzzle.execute([R, U2, Rp, Up, R, U, Rp])
    elif puzzle.cube.puz[2, 5] == "R" and puzzle.cube.puz[3, 6] == "Y" and puzzle.cube.puz[3, 5] == "G": puzzle.execute([R, U, Rp])
    else: puzzle.execute([Fp, Up, F])


def mEdges(puzzle):
    # Orange / Green edge.
    if puzzle.cube.puz[4, 2] == "O" and puzzle.cube.puz[4, 3] == "G": pass
    elif puzzle.cube.puz[4, 2] == "G" and puzzle.cube.puz[4, 3] == "O": puzzle.execute([L, U, L, U, L, Up, Lp, Up, Lp, U, Fp, Up, Fp, Up, Fp, U, F, U, F])
    elif puzzle.cube.puz[4, 0] == "O" and puzzle.cube.puz[4, 11] == "G": puzzle.execute([B, U, B, U, B, Up, Bp, Up, Bp, Fp, Up, Fp, Up, Fp, U, F, U, F])
    elif puzzle.cube.puz[4, 0] == "G" and puzzle.cube.puz[4, 11] == "O": puzzle.execute([B, U, B, U, B, Up, Bp, Up, Bp, U, L, U, L, U, L, Up, Lp, Up, Lp])
    elif puzzle.cube.puz[4, 8] == "O" and puzzle.cube.puz[4, 9] == "G": puzzle.execute([R, U, R, U, R, Up, Rp, Up, Rp, L, U, L, U, L, Up, Lp, Up, Lp])
    elif puzzle.cube.puz[4, 8] == "G" and puzzle.cube.puz[4, 9] == "O": puzzle.execute([R, U, R, U, R, Up, Rp, Up, Rp, Up, Fp, Up, Fp, Up, Fp, U, F, U, F])
    elif puzzle.cube.puz[4, 5] == "O" and puzzle.cube.puz[4, 6] == "G": puzzle.execute([Rp, Up, Rp, Up, Rp, U, R, U, R, Up, Fp, Up, Fp, Up, Fp, U, F, U, F])
    elif puzzle.cube.puz[4, 5] == "G" and puzzle.cube.puz[4, 6] == "O": puzzle.execute([Rp, Up, Rp, Up, Rp, U, R, U, R, L, U, L, U, L, Up, Lp, Up, Lp])
    elif puzzle.cube.puz[2, 4] == "O" and puzzle.cube.puz[3, 4] == "G": puzzle.execute([Fp, Up, Fp, Up, Fp, U, F, U, F])
    elif puzzle.cube.puz[2, 4] == "G" and puzzle.cube.puz[3, 4] == "O": puzzle.execute([U, L, U, L, U, L, Up, Lp, Up, Lp])
    elif puzzle.cube.puz[1, 3] == "O" and puzzle.cube.puz[3, 1] == "G": puzzle.execute([Up, Fp, Up, Fp, Up, Fp, U, F, U, F])
    elif puzzle.cube.puz[1, 3] == "G" and puzzle.cube.puz[3, 1] == "O": puzzle.execute([L, U, L, U, L, Up, Lp, Up, Lp])
    elif puzzle.cube.puz[0, 4] == "O" and puzzle.cube.puz[3, 10] == "G": puzzle.execute([U2, Fp, Up, Fp, Up, Fp, U, F, U, F])
    elif puzzle.cube.puz[0, 4] == "G" and puzzle.cube.puz[3, 10] == "O": puzzle.execute([Up, L, U, L, U, L, Up, Lp, Up, Lp])
    elif puzzle.cube.puz[1, 5] == "O" and puzzle.cube.puz[3, 7] == "G": puzzle.execute([U, Fp, Up, Fp, Up, Fp, U, F, U, F])
    else: puzzle.execute([U2, L, U, L, U, L, Up, Lp, Up, Lp])

    # Blue / Orange edge.
    if puzzle.cube.puz[4, 0] == "O" and puzzle.cube.puz[4, 11] == "B": pass
    elif puzzle.cube.puz[4, 0] == "B" and puzzle.cube.puz[4, 11] == "O": puzzle.execute([B, U, B, U, B, Up, Bp, Up, Bp, U, Lp, Up, Lp, Up, Lp, U, L, U, L])
    elif puzzle.cube.puz[4, 8] == "B" and puzzle.cube.puz[4, 9] == "O": puzzle.execute([R, U, R, U, R, Up, Rp, Up, Rp, U, B, U, B, U, B, Up, Bp, Up, Bp])
    elif puzzle.cube.puz[4, 8] == "O" and puzzle.cube.puz[4, 9] == "B": puzzle.execute([R, U, R, U, R, Up, Rp, Up, Rp, Lp, Up, Lp, Up, Lp, U, L, U, L])
    elif puzzle.cube.puz[4, 5] == "B" and puzzle.cube.puz[4, 6] == "O": puzzle.execute([Rp, Up, Rp, Up, Rp, U, R, U, R, Lp, Up, Lp, Up, Lp, U, L, U, L])
    elif puzzle.cube.puz[4, 5] == "O" and puzzle.cube.puz[4, 6] == "B": puzzle.execute([Rp, Up, Rp, Up, Rp, U, R, U, R, U, B, U, B, U, B, Up, Bp, Up, Bp])
    elif puzzle.cube.puz[2, 4] == "B" and puzzle.cube.puz[3, 4] == "O": puzzle.execute([U, Lp, Up, Lp, Up, Lp, U, L, U, L])
    elif puzzle.cube.puz[2, 4] == "O" and puzzle.cube.puz[3, 4] == "B": puzzle.execute([U2, B, U, B, U, B, Up, Bp, Up, Bp])
    elif puzzle.cube.puz[1, 3] == "B" and puzzle.cube.puz[3, 1] == "O": puzzle.execute([Lp, Up, Lp, Up, Lp, U, L, U, L])
    elif puzzle.cube.puz[1, 3] == "O" and puzzle.cube.puz[3, 1] == "B": puzzle.execute([U, B, U, B, U, B, Up, Bp, Up, Bp])
    elif puzzle.cube.puz[0, 4] == "B" and puzzle.cube.puz[3, 10] == "O": puzzle.execute([Up, Lp, Up, Lp, Up, Lp, U, L, U, L])
    elif puzzle.cube.puz[0, 4] == "O" and puzzle.cube.puz[3, 10] == "B": puzzle.execute([B, U, B, U, B, Up, Bp, Up, Bp])
    elif puzzle.cube.puz[1, 5] == "B" and puzzle.cube.puz[3, 7] == "O": puzzle.execute([U2, Lp, Up, Lp, Up, Lp, U, L, U, L])
    else: puzzle.execute([Up, B, U, B, U, B, Up, Bp, Up, Bp])

    # Red / Blue edge.
    if puzzle.cube.puz[4, 8] == "R" and puzzle.cube.puz[4, 9] == "B": pass
    elif puzzle.cube.puz[4, 8] == "B" and puzzle.cube.puz[4, 9] == "R": puzzle.execute([R, U, R, U, R, Up, Rp, Up, Rp, U, Bp, Up, Bp, Up, Bp, U, B, U, B])
    elif puzzle.cube.puz[4, 5] == "R" and puzzle.cube.puz[4, 6] == "B": puzzle.execute([F, U, F, U, F, Up, Fp, Up, Fp, U, R, U, R, U, R, Up, Rp, Up, Rp])
    elif puzzle.cube.puz[4, 5] == "B" and puzzle.cube.puz[4, 6] == "R": puzzle.execute([Rp, Up, Rp, Up, Rp, U, R, U, R, U2, R, U, R, U, R, Up, Rp, Up, Rp])
    elif puzzle.cube.puz[2, 4] == "R" and puzzle.cube.puz[3, 4] == "B": puzzle.execute([U2, Bp, Up, Bp, Up, Bp, U, B, U, B])
    elif puzzle.cube.puz[2, 4] == "B" and puzzle.cube.puz[3, 4] == "R": puzzle.execute([Up, R, U, R, U, R, Up, Rp, Up, Rp])
    elif puzzle.cube.puz[1, 3] == "R" and puzzle.cube.puz[3, 1] == "B": puzzle.execute([U, Bp, Up, Bp, Up, Bp, U, B, U, B])
    elif puzzle.cube.puz[1, 3] == "B" and puzzle.cube.puz[3, 1] == "R": puzzle.execute([U2, R, U, R, U, R, Up, Rp, Up, Rp])
    elif puzzle.cube.puz[0, 4] == "R" and puzzle.cube.puz[3, 10] == "B": puzzle.execute([Bp, Up, Bp, Up, Bp, U, B, U, B])
    elif puzzle.cube.puz[0, 4] == "B" and puzzle.cube.puz[3, 10] == "R": puzzle.execute([U, R, U, R, U, R, Up, Rp, Up, Rp])
    elif puzzle.cube.puz[1, 5] == "R" and puzzle.cube.puz[3, 7] == "B": puzzle.execute([Up, Bp, Up, Bp, Up, Bp, U, B, U, B])
    else: puzzle.execute([R, U, R, U, R, Up, Rp, Up, Rp])

    # Green / Red edge.
    if puzzle.cube.puz[4, 5] == "G" and puzzle.cube.puz[4, 6] == "R": pass
    elif puzzle.cube.puz[4, 5] == "R" and puzzle.cube.puz[4, 6] == "G": puzzle.execute([Rp, Up, Rp, Up, Rp, U, R, U, R, Up, F, U, F, U, F, Up, Fp, Up, Fp])
    elif puzzle.cube.puz[2, 4] == "R" and puzzle.cube.puz[3, 4] == "G": puzzle.execute([F, U, F, U, F, Up, Fp, Up, Fp])
    elif puzzle.cube.puz[2, 4] == "G" and puzzle.cube.puz[3, 4] == "R": puzzle.execute([Up, Rp, Up, Rp, Up, Rp, U, R, U, R])
    elif puzzle.cube.puz[1, 3] == "R" and puzzle.cube.puz[3, 1] == "G": puzzle.execute([Up, F, U, F, U, F, Up, Fp, Up, Fp])
    elif puzzle.cube.puz[1, 3] == "G" and puzzle.cube.puz[3, 1] == "R": puzzle.execute([U2, Rp, Up, Rp, Up, Rp, U, R, U, R])
    elif puzzle.cube.puz[0, 4] == "R" and puzzle.cube.puz[3, 10] == "G": puzzle.execute([U2, F, U, F, U, F, Up, Fp, Up, Fp])
    elif puzzle.cube.puz[0, 4] == "G" and puzzle.cube.puz[3, 10] == "R": puzzle.execute([U, Rp, Up, Rp, Up, Rp, U, R, U, R])
    elif puzzle.cube.puz[1, 5] == "R" and puzzle.cube.puz[3, 7] == "G": puzzle.execute([U, F, U, F, U, F, Up, Fp, Up, Fp])
    else: puzzle.execute([Rp, Up, Rp, Up, Rp, U, R, U, R])


def tEdgesO(puzzle):
    # Top layer edge orientation.
    if puzzle.cube.puz[2, 4] == "W" and puzzle.cube.puz[1, 3] == "W" and puzzle.cube.puz[0, 4] == "W" and puzzle.cube.puz[1, 5] == "W": pass
    elif puzzle.cube.puz[2, 4] != "W" and puzzle.cube.puz[1, 3] != "W" and puzzle.cube.puz[0, 4] != "W" and puzzle.cube.puz[1, 5] != "W": puzzle.execute([F, R, U, Rp, Up, Fp, B, U, L, Up, Lp, Bp])
    elif puzzle.cube.puz[1, 3] == "W" and puzzle.cube.puz[1, 5] == "W": puzzle.execute([F, R, U, Rp, Up, Fp])
    elif puzzle.cube.puz[0, 4] == "W" and puzzle.cube.puz[2, 4] == "W": puzzle.execute([L, F, U, Fp, Up, Lp])
    elif puzzle.cube.puz[2, 4] == "W" and puzzle.cube.puz[1, 5] == "W": puzzle.execute([B, U, L, Up, Lp, Bp])
    elif puzzle.cube.puz[1, 3] == "W" and puzzle.cube.puz[2, 4] == "W": puzzle.execute([R, U, B, Up, Bp, Rp])
    elif puzzle.cube.puz[0, 4] == "W" and puzzle.cube.puz[1, 3] == "W": puzzle.execute([F, U, R, Up, Rp, Fp])
    else: puzzle.execute([L, U, F, Up, Fp, Lp])

def tCornersO(puzzle):
    # Top layer corner orientation.
    if puzzle.cube.puz[0, 3] == "W" and puzzle.cube.puz[0, 5] == "W" and puzzle.cube.puz[2, 3] == "W" and puzzle.cube.puz[2, 5] == "W": pass
    elif puzzle.cube.puz[3, 0] == "W" and puzzle.cube.puz[3, 2] == "W" and puzzle.cube.puz[3, 5] == "W" and puzzle.cube.puz[3, 9] == "W": puzzle.execute([R, U2, R2, Up, R2, Up, R2, U2, R])
    elif puzzle.cube.puz[3, 9] == "W" and puzzle.cube.puz[3, 11] == "W" and puzzle.cube.puz[3, 2] == "W" and puzzle.cube.puz[3, 6] == "W": puzzle.execute([F, U2, F2, Up, F2, Up, F2, U2, F])
    elif puzzle.cube.puz[3, 6] == "W" and puzzle.cube.puz[3, 8] == "W" and puzzle.cube.puz[3, 3] == "W" and puzzle.cube.puz[3, 11] == "W": puzzle.execute([L, U2, L2, Up, L2, Up, L2, U2, L])
    elif puzzle.cube.puz[3, 3] == "W" and puzzle.cube.puz[3, 5] == "W" and puzzle.cube.puz[3, 0] == "W" and puzzle.cube.puz[3, 8] == "W": puzzle.execute([B, U2, B2, Up, B2, Up, B2, U2, B])
    elif puzzle.cube.puz[3, 3] == "W" and puzzle.cube.puz[3, 5] == "W" and puzzle.cube.puz[3, 9] == "W" and puzzle.cube.puz[3, 11] == "W": puzzle.execute([B, U, Bp, U, B, Up, Bp, U, B, U2, Bp])
    elif puzzle.cube.puz[3, 0] == "W" and puzzle.cube.puz[3, 2] == "W" and puzzle.cube.puz[3, 6] == "W" and puzzle.cube.puz[3, 8] == "W": puzzle.execute([R, U, Rp, U, R, Up, Rp, U, R, U2, Rp])
    elif puzzle.cube.puz[3, 5] == "W" and puzzle.cube.puz[3, 8] == "W" and puzzle.cube.puz[3, 11] == "W": puzzle.execute([R, U, Rp, U, R, U2, Rp])
    elif puzzle.cube.puz[3, 8] == "W" and puzzle.cube.puz[3, 11] == "W" and puzzle.cube.puz[3, 2] == "W": puzzle.execute([B, U, Bp, U, B, U2, Bp])
    elif puzzle.cube.puz[3, 11] == "W" and puzzle.cube.puz[3, 2] == "W" and puzzle.cube.puz[3, 5] == "W": puzzle.execute([L, U, Lp, U, L, U2, Lp])
    elif puzzle.cube.puz[3, 2] == "W" and puzzle.cube.puz[3, 5] == "W" and puzzle.cube.puz[3, 8] == "W": puzzle.execute([F, U, Fp, U, F, U2, Fp])
    elif puzzle.cube.puz[3, 3] == "W" and puzzle.cube.puz[3, 6] == "W" and puzzle.cube.puz[3, 9] == "W": puzzle.execute([Rp, Up, R, Up, Rp, U2, R])
    elif puzzle.cube.puz[3, 6] == "W" and puzzle.cube.puz[3, 9] == "W" and puzzle.cube.puz[3, 0] == "W": puzzle.execute([Bp, Up, B, Up, Bp, U2, B])
    elif puzzle.cube.puz[3, 9] == "W" and puzzle.cube.puz[3, 0] == "W" and puzzle.cube.puz[3, 3] == "W": puzzle.execute([Lp, Up, L, Up, Lp, U2, L])
    elif puzzle.cube.puz[3, 0] == "W" and puzzle.cube.puz[3, 3] == "W" and puzzle.cube.puz[3, 6] == "W": puzzle.execute([Fp, Up, F, Up, Fp, U2, F])
    elif puzzle.cube.puz[3, 5] == "W" and puzzle.cube.puz[3, 9] == "W": puzzle.execute([Rp, Fp, L, F, R, Fp, Lp, F])
    elif puzzle.cube.puz[3, 8] == "W" and puzzle.cube.puz[3, 0] == "W": puzzle.execute([Bp, Rp, F, R, B, Rp, Fp, R])
    elif puzzle.cube.puz[3, 11] == "W" and puzzle.cube.puz[3, 3] == "W": puzzle.execute([Lp, Bp, R, B, L, Bp, Rp, B])
    elif puzzle.cube.puz[3, 2] == "W" and puzzle.cube.puz[3, 6] == "W": puzzle.execute([Fp, Lp, B, L, F, Lp, Bp, L])
    elif puzzle.cube.puz[3, 3] == "W" and puzzle.cube.puz[3, 5] == "W": puzzle.execute([R2, D, Rp, U2, R, Dp, Rp, U2, Rp])
    elif puzzle.cube.puz[3, 6] == "W" and puzzle.cube.puz[3, 8] == "W": puzzle.execute([B2, D, Bp, U2, B, Dp, Bp, U2, Bp])
    elif puzzle.cube.puz[3, 9] == "W" and puzzle.cube.puz[3, 11] == "W": puzzle.execute([L2, D, Lp, U2, L, Dp, Lp, U2, Lp])
    elif puzzle.cube.puz[3, 0] == "W" and puzzle.cube.puz[3, 2] == "W": puzzle.execute([F2, D, Fp, U2, F, Dp, Fp, U2, Fp])
    elif puzzle.cube.puz[3, 2] == "W" and puzzle.cube.puz[3, 9] == "W": puzzle.execute([Rp, Fp, Lp, F, R, Fp, L, F])
    elif puzzle.cube.puz[3, 5] == "W" and puzzle.cube.puz[3, 0] == "W": puzzle.execute([Bp, Rp, Fp, R, B, Rp, F, R])
    elif puzzle.cube.puz[3, 8] == "W" and puzzle.cube.puz[3, 3] == "W": puzzle.execute([Lp, Bp, Rp, B, L, Bp, R, B])
    else: puzzle.execute([Fp, Lp, Bp, L, F, Lp, B, L])


def tCornersP(puzzle):
    # Top layer corner permutation.
    if puzzle.cube.puz[3, 3] == puzzle.cube.puz[3, 5] and puzzle.cube.puz[3, 6] == puzzle.cube.puz[3, 8] and puzzle.cube.puz[3, 9] == puzzle.cube.puz[3, 11] and puzzle.cube.puz[3, 0] == puzzle.cube.puz[3, 2]: pass
    elif puzzle.cube.puz[3, 3] != puzzle.cube.puz[3, 5] and puzzle.cube.puz[3, 6] != puzzle.cube.puz[3, 8] and puzzle.cube.puz[3, 9] != puzzle.cube.puz[3, 11] and puzzle.cube.puz[3, 0] != puzzle.cube.puz[3, 2]: puzzle.execute([R, Bp, Rp, F, R, B, Rp, Fp, R, B, Rp, F, R, Bp, Rp, Fp])
    elif puzzle.cube.puz[3, 3] == puzzle.cube.puz[3, 5]: puzzle.execute([Lp, B, Lp, F2, L, Bp, Lp, F2, L2])
    elif puzzle.cube.puz[3, 6] == puzzle.cube.puz[3, 8]: puzzle.execute([Fp, L, Fp, R2, F, Lp, Fp, R2, F2])
    elif puzzle.cube.puz[3, 9] == puzzle.cube.puz[3, 11]: puzzle.execute([Rp, F, Rp, B2, R, Fp, Rp, B2, R2])
    else: puzzle.execute([Bp, R, Bp, L2, B, Rp, Bp, L2, B2])

def tEdgesP(puzzle):
    # Top layer edge permutation.
    if puzzle.cube.puz[3, 3] == puzzle.cube.puz[3, 4] and puzzle.cube.puz[3, 6] == puzzle.cube.puz[3, 7] and puzzle.cube.puz[3, 9] == puzzle.cube.puz[3, 10] and puzzle.cube.puz[3, 0] == puzzle.cube.puz[3, 1]: pass
    elif puzzle.cube.puz[3, 9] == puzzle.cube.puz[3, 10] and puzzle.cube.puz[3, 4] == puzzle.cube.puz[3, 6]: puzzle.execute([R, Up, R, U, R, U, R, Up, Rp, Up, R2])
    elif puzzle.cube.puz[3, 9] == puzzle.cube.puz[3, 10] and puzzle.cube.puz[3, 4] == puzzle.cube.puz[3, 2]: puzzle.execute([R2, U, R, U, Rp, Up, Rp, Up, Rp, U, Rp])
    elif puzzle.cube.puz[3, 0] == puzzle.cube.puz[3, 1] and puzzle.cube.puz[3, 7] == puzzle.cube.puz[3, 9]: puzzle.execute([B, Up, B, U, B, U, B, Up, Bp, Up, B2])
    elif puzzle.cube.puz[3, 0] == puzzle.cube.puz[3, 1] and puzzle.cube.puz[3, 7] == puzzle.cube.puz[3, 5]: puzzle.execute([B2, U, B, U, Bp, Up, Bp, Up, Bp, U, Bp])
    elif puzzle.cube.puz[3, 3] == puzzle.cube.puz[3, 4] and puzzle.cube.puz[3, 10] == puzzle.cube.puz[3, 0]: puzzle.execute([L, Up, L, U, L, U, L, Up, Lp, Up, L2])
    elif puzzle.cube.puz[3, 3] == puzzle.cube.puz[3, 4] and puzzle.cube.puz[3, 10] == puzzle.cube.puz[3, 8]: puzzle.execute([L2, U, L, U, Lp, Up, Lp, Up, Lp, U, Lp])
    elif puzzle.cube.puz[3, 6] == puzzle.cube.puz[3, 7] and puzzle.cube.puz[3, 1] == puzzle.cube.puz[3, 3]: puzzle.execute([F, Up, F, U, F, U, F, Up, Fp, Up, F2])
    elif puzzle.cube.puz[3, 6] == puzzle.cube.puz[3, 7] and puzzle.cube.puz[3, 1] == puzzle.cube.puz[3, 11]: puzzle.execute([F2, U, F, U, Fp, Up, Fp, Up, Fp, U, Fp])
    elif puzzle.cube.puz[3, 4] == puzzle.cube.puz[3, 2]: puzzle.execute([Fp, Up, F2, U, F, U, Fp, Up, F, U, F, Up, F, Up, Fp])
    elif puzzle.cube.puz[3, 4] == puzzle.cube.puz[3, 6]: puzzle.execute([Rp, Up, R2, U, R, U, Rp, Up, R, U, R, Up, R, Up, Rp])
    else: puzzle.execute([R2, U2, R2, U2, R2, U, R2, U2, R2, U2, R2])

    # Final alignment.
    if puzzle.cube.puz[3, 4] == "G": pass
    elif puzzle.cube.puz[3, 4] == "O": puzzle.execute([U])
    elif puzzle.cube.puz[3, 4] == "B": puzzle.execute([U2])
    else: puzzle.execute([Up])