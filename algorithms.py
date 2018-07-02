#! /usr/bin/env python3.4

from moves import *

def locateEdge(cube, c1, c2):
    # Return the location of the (c1, c2) edge.
    for edge in cube.edges:
        if cube.puz[edge[0]] == c1 and cube.puz[edge[1]] == c2: return edge[0], edge[1]
        elif cube.puz[edge[1]] == c1 and cube.puz[edge[0]] == c2: return edge[1], edge[0]

def locateCorner(cube, c1, c2, c3):
    # Return the location of the (c1, c2, c3) corner.
    for corner in cube.corners:
        if cube.puz[corner[0]] == c1 and cube.puz[corner[1]] == c2 and cube.puz[corner[2]] == c3: return corner[0], corner[1], corner[2]
        elif cube.puz[corner[1]] == c1 and cube.puz[corner[2]] == c2 and cube.puz[corner[0]] == c3: return corner[1], corner[2], corner[0]
        elif cube.puz[corner[2]] == c1 and cube.puz[corner[0]] == c2 and cube.puz[corner[1]] == c3: return corner[2], corner[0], corner[1]

def locateEdgeOri(cube):
    # Return the edge orientation case.
    case = ()
    for facet in [(2, 4), (1, 3), (0, 4), (1, 5)]:
        if cube.puz[facet] == "W": case += facet,
    return case

def locateCornerOri(cube):
    # Return the corner orientation case.
    case = ()
    for facet in [(3, 0), (3, 2), (3, 3), (3, 5), (3, 6), (3, 8), (3, 9), (3, 11)]:
        if cube.puz[facet] == "W": case += facet,
    return case

def locateCornerPerm(cube):
    # Return the corner permutation case.
    case = ()
    for pair in [((3, 0), (3, 2)), ((3, 3), (3, 5)), ((3, 6), (3, 8)), ((3, 9), (3, 11))]:
        if cube.puz[pair[0]] == cube.puz[pair[1]]: case += pair
    return case

def locateEdgePerm(cube):
    # Return the edge permutation case.
    case = ()
    for pair in [((3, 0), (3, 1)), ((3, 3), (3, 4)), ((3, 6), (3, 7)), ((3, 9), (3, 10)),
                 ((3, 1), (3, 3)), ((3, 4), (3, 6)), ((3, 7), (3, 9)), ((3, 10), (3, 0)),
                 ((3, 1), (3, 11)), ((3, 10), (3, 8)), ((3, 7), (3, 5)), ((3, 4), (3, 2))]:
        if cube.puz[pair[0]] == cube.puz[pair[1]]: case += pair
    return case

# Yellow / Green edge.
algsYG = {((6, 4), (5, 4)): [],
          ((5, 4), (6, 4)): [Fp, Rp, Dp],
          ((7, 3), (5, 1)): [D],
          ((5, 1), (7, 3)): [Lp, Fp],
          ((8, 4), (5, 10)): [D2],
          ((5, 10), (8, 4)): [Dp, R, F],
          ((7, 5), (5, 7)): [Dp],
          ((5, 7), (7, 5)): [R, F],
          ((4, 3), (4, 2)): [L, D],
          ((4, 2), (4, 3)): [Fp],
          ((4, 0), (4, 11)): [L2, Fp],
          ((4, 11), (4, 0)): [Lp, D],
          ((4, 9), (4, 8)): [R, Dp],
          ((4, 8), (4, 9)): [Bp, D2],
          ((4, 6), (4, 5)): [F],
          ((4, 5), (4, 6)): [Rp, Dp],
          ((2, 4), (3, 4)): [F2],
          ((3, 4), (2, 4)): [Up, Rp, F],
          ((1, 3), (3, 1)): [Up, F2],
          ((3, 1), (1, 3)): [L, Fp],
          ((0, 4), (3, 10)): [U2, F2],
          ((3, 10), (0, 4)): [U, Rp, F],
          ((1, 5), (3, 7)): [U, F2],
          ((3, 7), (1, 5)): [Rp, F]}

# Yellow / Orange edge.
algsYO = {((7, 3), (5, 1)): [],
          ((5, 1), (7, 3)): [Lp, Fp, Dp, F],
          ((8, 4), (5, 10)): [B2, Up, L2],
          ((5, 10), (8, 4)): [Bp, Lp],
          ((7, 5), (5, 7)): [R2, U2, L2],
          ((5, 7), (7, 5)): [R, F, Dp, Fp],
          ((4, 3), (4, 2)): [L],
          ((4, 2), (4, 3)): [Fp, Dp, F],
          ((4, 0), (4, 11)): [Dp, B, D],
          ((4, 11), (4, 0)): [Lp],
          ((4, 9), (4, 8)): [Rp, U2, L2],
          ((4, 8), (4, 9)): [Dp, Bp, D],
          ((4, 6), (4, 5)): [F, Dp, Fp],
          ((4, 5), (4, 6)): [R, U2, L2],
          ((2, 4), (3, 4)): [U, L2],
          ((3, 4), (2, 4)): [Fp, L, F],
          ((1, 3), (3, 1)): [L2],
          ((3, 1), (1, 3)): [L, Fp, Dp, F],
          ((0, 4), (3, 10)): [Up, L2],
          ((3, 10), (0, 4)): [B, Lp],
          ((1, 5), (3, 7)): [U2, L2],
          ((3, 7), (1, 5)): [U, Fp, L, F]}

# Yellow / Blue edge.
algsYB = {((8, 4), (5, 10)): [],
          ((5, 10), (8, 4)): [B, Dp, R, D],
          ((7, 5), (5, 7)): [R2, Up, B2],
          ((5, 7), (7, 5)): [Rp, Bp],
          ((4, 3), (4, 2)): [D, L, Dp],
          ((4, 2), (4, 3)): [D2, Fp, D2],
          ((4, 0), (4, 11)): [B],
          ((4, 11), (4, 0)): [D, Lp, Dp],
          ((4, 9), (4, 8)): [Dp, R, D],
          ((4, 8), (4, 9)): [Bp],
          ((4, 6), (4, 5)): [R2, Bp],
          ((4, 5), (4, 6)): [Dp, Rp, D],
          ((2, 4), (3, 4)): [U2, B2],
          ((3, 4), (2, 4)): [Up, R, Bp],
          ((1, 3), (3, 1)): [U, B2],
          ((3, 1), (1, 3)): [Lp, B, L],
          ((0, 4), (3, 10)): [B2],
          ((3, 10), (0, 4)): [U, R, Bp],
          ((1, 5), (3, 7)): [Up, B2],
          ((3, 7), (1, 5)): [R, Bp]}

# Yellow / Red edge.
algsYR = {((7, 5), (5, 7)): [],
          ((5, 7), (7, 5)): [R, Dp, F, D],
          ((4, 3), (4, 2)): [D2, L, D2],
          ((4, 2), (4, 3)): [Dp, Fp, D],
          ((4, 0), (4, 11)): [D, B, Dp],
          ((4, 11), (4, 0)): [D2, Lp, D2],
          ((4, 9), (4, 8)): [R],
          ((4, 8), (4, 9)): [D, Bp, Dp],
          ((4, 6), (4, 5)): [Dp, F, D],
          ((4, 5), (4, 6)): [Rp],
          ((2, 4), (3, 4)): [Up, R2],
          ((3, 4), (2, 4)): [F, Rp, Fp],
          ((1, 3), (3, 1)): [U2, R2],
          ((3, 1), (1, 3)): [Up, F, Rp, Fp],
          ((0, 4), (3, 10)): [U, R2],
          ((3, 10), (0, 4)): [Bp, R, B],
          ((1, 5), (3, 7)): [R2],
          ((3, 7), (1, 5)): [U, F, Rp, Fp]}

# Yellow / Orange / Green corner.
algsYOG = {((6, 3), (5, 2), (5, 3)): [],
           ((5, 3), (6, 3), (5, 2)): [Lp, U, L, F, U, Fp],
           ((5, 2), (5, 3), (6, 3)): [F, Up, Fp, Lp, Up, L],
           ((8, 3), (5, 11), (5, 0)): [Bp, Up, B, F, U, Fp],
           ((5, 0), (8, 3), (5, 11)): [L, Up, L, Fp, L2, F],
           ((5, 11), (5, 0), (8, 3)): [Bp, Up, B, Lp, Up, L],
           ((8, 5), (5, 8), (5, 9)): [Rp, U2, R, F, U, Fp],
           ((5, 9), (8, 5), (5, 8)): [B, U2, Bp, F, U, Fp],
           ((5, 8), (5, 9), (8, 5)): [Rp, U2, R, Lp, Up, L],
           ((6, 5), (5, 5), (5, 6)): [R, U, Rp, Lp, Up, L],
           ((5, 6), (6, 5), (5, 5)): [R, U, Rp, F, U, Fp],
           ((5, 5), (5, 6), (6, 5)): [Fp, U2, F2, Up, Fp],
           ((2, 3), (3, 3), (3, 2)): [F, U2, Fp, Up, F, U, Fp],
           ((3, 2), (2, 3), (3, 3)): [Lp, Up, L],
           ((3, 3), (3, 2), (2, 3)): [F, U, Fp],
           ((0, 3), (3, 0), (3, 11)): [L2, Fp, L2, F],
           ((3, 11), (0, 3), (3, 0)): [Up, Lp, Up, L],
           ((3, 0), (3, 11), (0, 3)): [Up, L, Fp, Lp, F],
           ((0, 5), (3, 9), (3, 8)): [U, F2, L, F2, Lp],
           ((3, 8), (0, 5), (3, 9)): [U2, Lp, Up, L],
           ((3, 9), (3, 8), (0, 5)): [U2, F, U, Fp],
           ((2, 5), (3, 6), (3, 5)): [F2, L, F2, Lp],
           ((3, 5), (2, 5), (3, 6)): [U, Lp, Up, L],
           ((3, 6), (3, 5), (2, 5)): [Lp, U, L]}

# Yellow / Blue / Orange corner.
algsYBO = {((8, 3), (5, 11), (5, 0)): [],
           ((5, 0), (8, 3), (5, 11)): [Bp, U, B, L, U, Lp],
           ((5, 11), (5, 0), (8, 3)): [L, Up, Lp, Bp, Up, B],
           ((8, 5), (5, 8), (5, 9)): [Rp, Up, R, L, U, Lp],
           ((5, 9), (8, 5), (5, 8)): [Rp, U, R, Up, L, U, Lp],
           ((5, 8), (5, 9), (8, 5)): [Rp, Up, R, Bp, Up, B],
           ((6, 5), (5, 5), (5, 6)): [R2, B2, Lp, B2, L, R2],
           ((5, 6), (6, 5), (5, 5)): [R, U, Rp, Bp, U, B],
           ((5, 5), (5, 6), (6, 5)): [Fp, Up, F, L, Up, Lp],
           ((2, 3), (3, 3), (3, 2)): [U2, B2, Lp, B2, L],
           ((3, 2), (2, 3), (3, 3)): [U, Bp, Up, B],
           ((3, 3), (3, 2), (2, 3)): [Bp, U, B],
           ((0, 3), (3, 0), (3, 11)): [L, U2, Lp, Up, L, U, Lp],
           ((3, 11), (0, 3), (3, 0)): [Bp, Up, B],
           ((3, 0), (3, 11), (0, 3)): [L, U, Lp],
           ((0, 5), (3, 9), (3, 8)): [B2, Lp, B2, L],
           ((3, 8), (0, 5), (3, 9)): [L, Up, Lp],
           ((3, 9), (3, 8), (0, 5)): [Up, L, U, Lp],
           ((2, 5), (3, 6), (3, 5)): [Up, B2, Lp, B2, L],
           ((3, 5), (2, 5), (3, 6)): [U2, Bp, Up, B],
           ((3, 6), (3, 5), (2, 5)): [U2, L, U, Lp]}

# Yellow / Red / Blue corner.
algsYRB = {((8, 5), (5, 8), (5, 9)): [],
           ((5, 9), (8, 5), (5, 8)): [Rp, U, R, B, U, Bp],
           ((5, 8), (5, 9), (8, 5)): [B, Up, Bp, Rp, Up, R],
           ((6, 5), (5, 5), (5, 6)): [Fp, Up, F, B, U, Bp],
           ((5, 6), (6, 5), (5, 5)): [R, U2, R2, U, R],
           ((5, 5), (5, 6), (6, 5)): [Fp, Up, F, Rp, Up, R],
           ((2, 3), (3, 3), (3, 2)): [Up, R2, Bp, R2, B],
           ((3, 2), (2, 3), (3, 3)): [U2, Rp, Up, R],
           ((3, 3), (3, 2), (2, 3)): [U2, B, U, Bp],
           ((0, 3), (3, 0), (3, 11)): [U2, R2, Bp, R2, B],
           ((3, 11), (0, 3), (3, 0)): [U, Rp, Up, R],
           ((3, 0), (3, 11), (0, 3)): [U, B, U, Bp],
           ((0, 5), (3, 9), (3, 8)): [Rp, U2, R, U, Rp, Up, R],
           ((3, 8), (0, 5), (3, 9)): [Rp, Up, R],
           ((3, 9), (3, 8), (0, 5)): [B, U, Bp],
           ((2, 5), (3, 6), (3, 5)): [R2, Bp, R2, B],
           ((3, 5), (2, 5), (3, 6)): [Up, Rp, Up, R],
           ((3, 6), (3, 5), (2, 5)): [Up, B, U, Bp]}

# Yellow / Green / Red corner.
algsYGR = {((6, 5), (5, 5), (5, 6)): [],
           ((5, 6), (6, 5), (5, 5)): [Fp, U, F, R, U, Rp],
           ((5, 5), (5, 6), (6, 5)): [R, Up, Rp, Fp, Up, F],
           ((2, 3), (3, 3), (3, 2)): [Up, R, U2, Rp, Up, R, U, Rp],
           ((3, 2), (2, 3), (3, 3)): [R, Up, Rp],
           ((3, 3), (3, 2), (2, 3)): [Up, R, U, Rp],
           ((0, 3), (3, 0), (3, 11)): [U2, R, U2, Rp, Up, R, U, Rp],
           ((3, 11), (0, 3), (3, 0)): [U2, Fp, Up, F],
           ((3, 0), (3, 11), (0, 3)): [U2, R, U, Rp],
           ((0, 5), (3, 9), (3, 8)): [U, R, U2, Rp, Up, R, U, Rp],
           ((3, 8), (0, 5), (3, 9)): [U, Fp, Up, F],
           ((3, 9), (3, 8), (0, 5)): [U, R, U, Rp],
           ((2, 5), (3, 6), (3, 5)): [R, U2, Rp, Up, R, U, Rp],
           ((3, 5), (2, 5), (3, 6)): [Fp, Up, F],
           ((3, 6), (3, 5), (2, 5)): [R, U, Rp]}

# Green / Orange edge.
algsGO = {((4, 3), (4, 2)): [],
          ((4, 2), (4, 3)): [F, U, Fp, Up, Lp, Up, L, Up, F, Up, Fp, Up, Lp, U, L],
          ((4, 0), (4, 11)): [L, Up, Lp, Up, Bp, U, B, Up, Lp, U, L, U, F, Up, Fp],
          ((4, 11), (4, 0)): [L, Up, Lp, Up, Bp, U, B, U2, F, Up, Fp, Up, Lp, U, L],
          ((4, 9), (4, 8)): [B, U, Bp, Up, Rp, Up, R, U2, Lp, U, L, U, F, Up, Fp],
          ((4, 8), (4, 9)): [B, U, Bp, Up, Rp, Up, R, U, F, Up, Fp, Up, Lp, U, L],
          ((4, 6), (4, 5)): [Fp, U, F, U, R, Up, Rp, U, F, Up, Fp, Up, Lp, U, L],
          ((4, 5), (4, 6)): [Fp, U, F, U, R, Up, Rp, U2, Lp, U, L, U, F, Up, Fp],
          ((2, 4), (3, 4)): [U2, F, Up, Fp, Up, Lp, U, L],
          ((3, 4), (2, 4)): [Up, Lp, U, L, U, F, Up, Fp],
          ((1, 3), (3, 1)): [U, F, Up, Fp, Up, Lp, U, L],
          ((3, 1), (1, 3)): [U2, Lp, U, L, U, F, Up, Fp],
          ((0, 4), (3, 10)): [F, Up, Fp, Up, Lp, U, L],
          ((3, 10), (0, 4)): [U, Lp, U, L, U, F, Up, Fp],
          ((1, 5), (3, 7)): [Up, F, Up, Fp, Up, Lp, U, L],
          ((3, 7), (1, 5)): [Lp, U, L, U, F, Up, Fp]}

# Orange / Blue edge.
algsOB = {((4, 0), (4, 11)): [],
          ((4, 11), (4, 0)): [L, U, Lp, Up, Bp, Up, B, Up, L, U, Lp, Up, Bp, Up, B],
          ((4, 9), (4, 8)): [B, U, Bp, Up, Rp, Up, R, Up, Bp, U, B, U, L, Up, Lp],
          ((4, 8), (4, 9)): [B, U, Bp, Up, Rp, Up, R, U2, L, Up, Lp, Up, Bp, U, B],
          ((4, 6), (4, 5)): [R, U, Rp, Up, Fp, Up, F, U2, Bp, U, B, U, L, Up, Lp],
          ((4, 5), (4, 6)): [R, U, Rp, Up, Fp, Up, F, U, L, Up, Lp, Up, Bp, U, B],
          ((2, 4), (3, 4)): [Up, L, Up, Lp, Up, Bp, U, B],
          ((3, 4), (2, 4)): [Bp, U, B, U, L, Up, Lp],
          ((1, 3), (3, 1)): [U2, L, Up, Lp, Up, Bp, U, B],
          ((3, 1), (1, 3)): [Up, Bp, U, B, U, L, Up, Lp],
          ((0, 4), (3, 10)): [U, L, Up, Lp, Up, Bp, U, B],
          ((3, 10), (0, 4)): [U2, Bp, U, B, U, L, Up, Lp],
          ((1, 5), (3, 7)): [L, Up, Lp, Up, Bp, U, B],
          ((3, 7), (1, 5)): [U, Bp, U, B, U, L, Up, Lp]}

# Blue / Red edge.
algsBR = {((4, 9), (4, 8)): [],
          ((4, 8), (4, 9)): [B, U, Bp, Up, Rp, Up, R, Up, B, U, Bp, Up, Rp, Up, R],
          ((4, 6), (4, 5)): [R, U, Rp, Up, Fp, Up, F, Up, Rp, U, R, U, B, Up, Bp],
          ((4, 5), (4, 6)): [R, U, Rp, Up, Fp, Up, F, U2, B, Up, Bp, Up, Rp, U, R],
          ((2, 4), (3, 4)): [B, Up, Bp, Up, Rp, U, R],
          ((3, 4), (2, 4)): [U, Rp, U, R, U, B, Up, Bp],
          ((1, 3), (3, 1)): [Up, B, Up, Bp, Up, Rp, U, R],
          ((3, 1), (1, 3)): [Rp, U, R, U, B, Up, Bp],
          ((0, 4), (3, 10)): [U2, B, Up, Bp, Up, Rp, U, R],
          ((3, 10), (0, 4)): [Up, Rp, U, R, U, B, Up, Bp],
          ((1, 5), (3, 7)): [U, B, Up, Bp, Up, Rp, U, R],
          ((3, 7), (1, 5)): [U2, Rp, U, R, U, B, Up, Bp]}

# Red / Green edge.
algsRG = {((4, 6), (4, 5)): [],
          ((4, 5), (4, 6)): [R, U, Rp, Up, Fp, Up, F, Up, R, U, Rp, Up, Fp, Up, F],
          ((2, 4), (3, 4)): [U, R, Up, Rp, Up, Fp, U, F],
          ((3, 4), (2, 4)): [U2, Fp, U, F, U, R, Up, Rp],
          ((1, 3), (3, 1)): [R, Up, Rp, Up, Fp, U, F],
          ((3, 1), (1, 3)): [U, Fp, U, F, U, R, Up, Rp],
          ((0, 4), (3, 10)): [Up, R, Up, Rp, Up, Fp, U, F],
          ((3, 10), (0, 4)): [Fp, U, F, U, R, Up, Rp],
          ((1, 5), (3, 7)): [U2, R, Up, Rp, Up, Fp, U, F],
          ((3, 7), (1, 5)): [Up, Fp, U, F, U, R, Up, Rp]}

# Top layer edge orientation.
algsEO = {((2, 4), (1, 3), (0, 4), (1, 5)): [],
          (): [F, R, U, Rp, Up, Fp, B, U, L, Up, Lp, Bp],
          ((2, 4), (0, 4)): [L, F, U, Fp, Up, Lp],
          ((1, 3), (1, 5)): [F, R, U, Rp, Up, Fp],
          ((2, 4), (1, 5)): [B, U, L, Up, Lp, Bp],
          ((2, 4), (1, 3)): [R, U, B, Up, Bp, Rp],
          ((1, 3), (0, 4)): [F, U, R, Up, Rp, Fp],
          ((0, 4), (1, 5)): [L, U, F, Up, Fp, Lp]}

# Top layer corner orientation.
algsCO = {(): [],
          ((3, 0), (3, 2), (3, 5), (3, 9)): [R, U2, R2, Up, R2, Up, R2, U2, R],
          ((3, 2), (3, 6), (3, 9), (3, 11)): [F, U2, F2, Up, F2, Up, F2, U2, F],
          ((3, 3), (3, 6), (3, 8), (3, 11)): [L, U2, L2, Up, L2, Up, L2, U2, L],
          ((3, 0), (3, 3), (3, 5), (3, 8)): [B, U2, B2, Up, B2, Up, B2, U2, B],
          ((3, 3), (3, 5), (3, 9), (3, 11)): [B, U, Bp, U, B, Up, Bp, U, B, U2, Bp],
          ((3, 0), (3, 2), (3, 6), (3, 8)): [R, U, Rp, U, R, Up, Rp, U, R, U2, Rp],
          ((3, 5), (3, 8), (3, 11)): [R, U, Rp, U, R, U2, Rp],
          ((3, 2), (3, 8), (3, 11)): [B, U, Bp, U, B, U2, Bp],
          ((3, 2), (3, 5), (3, 11)): [L, U, Lp, U, L, U2, Lp],
          ((3, 2), (3, 5), (3, 8)): [F, U, Fp, U, F, U2, Fp],
          ((3, 3), (3, 6), (3, 9)): [Rp, Up, R, Up, Rp, U2, R],
          ((3, 0), (3, 6), (3, 9)): [Bp, Up, B, Up, Bp, U2, B],
          ((3, 0), (3, 3), (3, 9)): [Lp, Up, L, Up, Lp, U2, L],
          ((3, 0), (3, 3), (3, 6)): [Fp, Up, F, Up, Fp, U2, F],
          ((3, 5), (3, 9)): [Rp, Fp, L, F, R, Fp, Lp, F],
          ((3, 0), (3, 8)): [Bp, Rp, F, R, B, Rp, Fp, R],
          ((3, 3), (3, 11)): [Lp, Bp, R, B, L, Bp, Rp, B],
          ((3, 2), (3, 6)): [Fp, Lp, B, L, F, Lp, Bp, L],
          ((3, 3), (3, 5)): [R2, D, Rp, U2, R, Dp, Rp, U2, Rp],
          ((3, 6), (3, 8)): [B2, D, Bp, U2, B, Dp, Bp, U2, Bp],
          ((3, 9), (3, 11)): [L2, D, Lp, U2, L, Dp, Lp, U2, Lp],
          ((3, 0), (3, 2)): [F2, D, Fp, U2, F, Dp, Fp, U2, Fp],
          ((3, 2), (3, 9)): [Rp, Fp, Lp, F, R, Fp, L, F],
          ((3, 0), (3, 5)): [Bp, Rp, Fp, R, B, Rp, F, R],
          ((3, 3), (3, 8)): [Lp, Bp, Rp, B, L, Bp, R, B],
          ((3, 6), (3, 11)): [Fp, Lp, Bp, L, F, Lp, B, L]}

# Top layer corner permutation.
algsCP = {((3, 0), (3, 2), (3, 3), (3, 5), (3, 6), (3, 8), (3, 9), (3, 11)): [],
          (): [R, Bp, Rp, F, R, B, Rp, Fp, R, B, Rp, F, R, Bp, Rp, Fp],
          ((3, 3), (3, 5)): [Lp, B, Lp, F2, L, Bp, Lp, F2, L2],
          ((3, 6), (3, 8)): [Fp, L, Fp, R2, F, Lp, Fp, R2, F2],
          ((3, 9), (3, 11)): [Rp, F, Rp, B2, R, Fp, Rp, B2, R2],
          ((3, 0), (3, 2)): [Bp, R, Bp, L2, B, Rp, Bp, L2, B2]}

# Top layer edge permutation.
algsEP = {(): [R2, U2, R2, U2, R2, U, R2, U2, R2, U2, R2],
          ((3, 0), (3, 1), (3, 3), (3, 4), (3, 6), (3, 7), (3, 9), (3, 10)): [],
          ((3, 9), (3, 10), (3, 1), (3, 3), (3, 4), (3, 6)): [R, Up, R, U, R, U, R, Up, Rp, Up, R2],
          ((3, 9), (3, 10), (3, 7), (3, 5), (3, 4), (3, 2)): [R2, U, R, U, Rp, Up, Rp, Up, Rp, U, Rp],
          ((3, 0), (3, 1), (3, 4), (3, 6), (3, 7), (3, 9)): [B, Up, B, U, B, U, B, Up, Bp, Up, B2],
          ((3, 0), (3, 1), (3, 10), (3, 8), (3, 7), (3, 5)): [B2, U, B, U, Bp, Up, Bp, Up, Bp, U, Bp],
          ((3, 3), (3, 4), (3, 7), (3, 9), (3, 10), (3, 0)): [L, Up, L, U, L, U, L, Up, Lp, Up, L2],
          ((3, 3), (3, 4), (3, 1), (3, 11), (3, 10), (3, 8)): [L2, U, L, U, Lp, Up, Lp, Up, Lp, U, Lp],
          ((3, 6), (3, 7), (3, 1), (3, 3), (3, 10), (3, 0)): [F, Up, F, U, F, U, F, Up, Fp, Up, F2],
          ((3, 6), (3, 7), (3, 1), (3, 11), (3, 4), (3, 2)): [F2, U, F, U, Fp, Up, Fp, Up, Fp, U, Fp],
          ((3, 1), (3, 3), (3, 7), (3, 9), (3, 10), (3, 8), (3, 4), (3, 2)): [Fp, Up, F2, U, F, U, Fp, Up, F, U, F, Up, F, Up, Fp],
          ((3, 4), (3, 6), (3, 10), (3, 0), (3, 1), (3, 11), (3, 7), (3, 5)): [Rp, Up, R2, U, R, U, Rp, Up, R, U, R, Up, R, Up, Rp]}

# Final alignment.
algsFA = {"G": [],
          "R": [Up],
          "B": [U2],
          "O": [U]}