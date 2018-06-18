#! /usr/bin/env python3.4

class Cube:
    def __init__(self):
        self.puz = [["W", "W", "W", "W", "W", "W", "W", "W", "W"],
                    ["O", "O", "O", "O", "O", "O", "O", "O", "O"],
                    ["G", "G", "G", "G", "G", "G", "G", "G", "G"],
                    ["R", "R", "R", "R", "R", "R", "R", "R", "R"],
                    ["B", "B", "B", "B", "B", "B", "B", "B", "B"],
                    ["Y", "Y", "Y", "Y", "Y", "Y", "Y", "Y", "Y"]]

    def __str__(self):
        ret = "      +-----+\n"
        ret += "      |{} {} {}|\n".format(self.puz[0][0], self.puz[0][1], self.puz[0][2])
        ret += "      |{} {} {}|\n".format(self.puz[0][3], self.puz[0][4], self.puz[0][5])
        ret += "      |{} {} {}|\n".format(self.puz[0][6], self.puz[0][7], self.puz[0][8])
        ret += "+-----+-----+-----+-----+\n"
        ret += "|{} {} {}|".format(self.puz[1][0], self.puz[1][1], self.puz[1][2])
        ret += "{} {} {}|".format(self.puz[2][0], self.puz[2][1], self.puz[2][2])
        ret += "{} {} {}|".format(self.puz[3][0], self.puz[3][1], self.puz[3][2])
        ret += "{} {} {}|\n".format(self.puz[4][0], self.puz[4][1], self.puz[4][2])
        ret += "|{} {} {}|".format(self.puz[1][3], self.puz[1][4], self.puz[1][5])
        ret += "{} {} {}|".format(self.puz[2][3], self.puz[2][4], self.puz[2][5])
        ret += "{} {} {}|".format(self.puz[3][3], self.puz[3][4], self.puz[3][5])
        ret += "{} {} {}|\n".format(self.puz[4][3], self.puz[4][4], self.puz[4][5])
        ret += "|{} {} {}|".format(self.puz[1][6], self.puz[1][7], self.puz[1][8])
        ret += "{} {} {}|".format(self.puz[2][6], self.puz[2][7], self.puz[2][8])
        ret += "{} {} {}|".format(self.puz[3][6], self.puz[3][7], self.puz[3][8])
        ret += "{} {} {}|\n".format(self.puz[4][6], self.puz[4][7], self.puz[4][8])
        ret += "+-----+-----+-----+-----+\n"
        ret += "      |{} {} {}|\n".format(self.puz[5][0], self.puz[5][1], self.puz[5][2])
        ret += "      |{} {} {}|\n".format(self.puz[5][3], self.puz[5][4], self.puz[5][5])
        ret += "      |{} {} {}|\n".format(self.puz[5][6], self.puz[5][7], self.puz[5][8])
        ret += "      +-----+"
        return ret

    def U(self):
        # Rotate adjacent faces clockwise.
        temp = [self.puz[2][0], self.puz[2][1], self.puz[2][2]]
        [self.puz[2][0], self.puz[2][1], self.puz[2][2]] = [self.puz[3][0], self.puz[3][1], self.puz[3][2]]
        [self.puz[3][0], self.puz[3][1], self.puz[3][2]] = [self.puz[4][0], self.puz[4][1], self.puz[4][2]]
        [self.puz[4][0], self.puz[4][1], self.puz[4][2]] = [self.puz[1][0], self.puz[1][1], self.puz[1][2]]
        [self.puz[1][0], self.puz[1][1], self.puz[1][2]] = temp

        # Rotate up corners clockwise.
        temp = self.puz[0][0]
        self.puz[0][0] = self.puz[0][6]
        self.puz[0][6] = self.puz[0][8]
        self.puz[0][8] = self.puz[0][2]
        self.puz[0][2] = temp

        # Rotate up edges clockwise.
        temp = self.puz[0][1]
        self.puz[0][1] = self.puz[0][3]
        self.puz[0][3] = self.puz[0][7]
        self.puz[0][7] = self.puz[0][5]
        self.puz[0][5] = temp

    def D(self):
        # Rotate adjacent faces clockwise.
        temp = [self.puz[2][6], self.puz[2][7], self.puz[2][8]]
        [self.puz[2][6], self.puz[2][7], self.puz[2][8]] = [self.puz[1][6], self.puz[1][7], self.puz[1][8]]
        [self.puz[1][6], self.puz[1][7], self.puz[1][8]] = [self.puz[4][6], self.puz[4][7], self.puz[4][8]]
        [self.puz[4][6], self.puz[4][7], self.puz[4][8]] = [self.puz[3][6], self.puz[3][7], self.puz[3][8]]
        [self.puz[3][6], self.puz[3][7], self.puz[3][8]] = temp

        # Rotate down corners clockwise.
        temp = self.puz[5][0]
        self.puz[5][0] = self.puz[5][6]
        self.puz[5][6] = self.puz[5][8]
        self.puz[5][8] = self.puz[5][2]
        self.puz[5][2] = temp

        # Rotate down edges clockwise.
        temp = self.puz[5][1]
        self.puz[5][1] = self.puz[5][3]
        self.puz[5][3] = self.puz[5][7]
        self.puz[5][7] = self.puz[5][5]
        self.puz[5][5] = temp

    def F(self):
        # Rotate adjacent faces clockwise.
        temp = [self.puz[0][6], self.puz[0][7], self.puz[0][8]]
        [self.puz[0][6], self.puz[0][7], self.puz[0][8]] = [self.puz[1][8], self.puz[1][5], self.puz[1][2]]
        [self.puz[1][8], self.puz[1][5], self.puz[1][2]] = [self.puz[5][2], self.puz[5][1], self.puz[5][0]]
        [self.puz[5][2], self.puz[5][1], self.puz[5][0]] = [self.puz[3][0], self.puz[3][3], self.puz[3][6]]
        [self.puz[3][0], self.puz[3][3], self.puz[3][6]] = temp

        # Rotate front corners clockwise.
        temp = self.puz[2][0]
        self.puz[2][0] = self.puz[2][6]
        self.puz[2][6] = self.puz[2][8]
        self.puz[2][8] = self.puz[2][2]
        self.puz[2][2] = temp

        # Rotate front edges clockwise.
        temp = self.puz[2][1]
        self.puz[2][1] = self.puz[2][3]
        self.puz[2][3] = self.puz[2][7]
        self.puz[2][7] = self.puz[2][5]
        self.puz[2][5] = temp

    def B(self):
        # Rotate adjacent faces clockwise.
        temp = [self.puz[0][0], self.puz[0][1], self.puz[0][2]]
        [self.puz[0][0], self.puz[0][1], self.puz[0][2]] = [self.puz[3][2], self.puz[3][5], self.puz[3][8]]
        [self.puz[3][2], self.puz[3][5], self.puz[3][8]] = [self.puz[5][8], self.puz[5][7], self.puz[5][6]]
        [self.puz[5][8], self.puz[5][7], self.puz[5][6]] = [self.puz[1][6], self.puz[1][3], self.puz[1][0]]
        [self.puz[1][6], self.puz[1][3], self.puz[1][0]] = temp

        # Rotate back corners clockwise.
        temp = self.puz[4][0]
        self.puz[4][0] = self.puz[4][6]
        self.puz[4][6] = self.puz[4][8]
        self.puz[4][8] = self.puz[4][2]
        self.puz[4][2] = temp

        # Rotate back edges clockwise.
        temp = self.puz[4][1]
        self.puz[4][1] = self.puz[4][3]
        self.puz[4][3] = self.puz[4][7]
        self.puz[4][7] = self.puz[4][5]
        self.puz[4][5] = temp

    def L(self):
        # Rotate adjacent faces clockwise.
        temp = [self.puz[2][0], self.puz[2][3], self.puz[2][6]]
        [self.puz[2][0], self.puz[2][3], self.puz[2][6]] = [self.puz[0][0], self.puz[0][3], self.puz[0][6]]
        [self.puz[0][0], self.puz[0][3], self.puz[0][6]] = [self.puz[4][8], self.puz[4][5], self.puz[4][2]]
        [self.puz[4][8], self.puz[4][5], self.puz[4][2]] = [self.puz[5][0], self.puz[5][3], self.puz[5][6]]
        [self.puz[5][0], self.puz[5][3], self.puz[5][6]] = temp

        # Rotate left corners clockwise.
        temp = self.puz[1][0]
        self.puz[1][0] = self.puz[1][6]
        self.puz[1][6] = self.puz[1][8]
        self.puz[1][8] = self.puz[1][2]
        self.puz[1][2] = temp

        # Rotate left edges clockwise.
        temp = self.puz[1][1]
        self.puz[1][1] = self.puz[1][3]
        self.puz[1][3] = self.puz[1][7]
        self.puz[1][7] = self.puz[1][5]
        self.puz[1][5] = temp

    def R(self):
        # Rotate adjacent faces clockwise.
        temp = [self.puz[2][2], self.puz[2][5], self.puz[2][8]]
        [self.puz[2][2], self.puz[2][5], self.puz[2][8]] = [self.puz[5][2], self.puz[5][5], self.puz[5][8]]
        [self.puz[5][2], self.puz[5][5], self.puz[5][8]] = [self.puz[4][6], self.puz[4][3], self.puz[4][0]]
        [self.puz[4][6], self.puz[4][3], self.puz[4][0]] = [self.puz[0][2], self.puz[0][5], self.puz[0][8]]
        [self.puz[0][2], self.puz[0][5], self.puz[0][8]] = temp

        # Rotate right corners clockwise.
        temp = self.puz[3][0]
        self.puz[3][0] = self.puz[3][6]
        self.puz[3][6] = self.puz[3][8]
        self.puz[3][8] = self.puz[3][2]
        self.puz[3][2] = temp

        # Rotate right edges clockwise.
        temp = self.puz[3][1]
        self.puz[3][1] = self.puz[3][3]
        self.puz[3][3] = self.puz[3][7]
        self.puz[3][7] = self.puz[3][5]
        self.puz[3][5] = temp

if __name__ == "__main__":
    cube = Cube()
    print(cube)
    cube.U()
    cube.U()
    cube.D()
    cube.D()
    cube.L()
    cube.L()
    cube.R()
    cube.R()
    cube.F()
    cube.F()
    cube.B()
    cube.B()
    print(cube)