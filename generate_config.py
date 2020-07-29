from math import cos, sin, sqrt
import random


class Atom:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.type = 1
        v0 = 2.0
        z = random.random()*2.0-1
        s = random.random()*3.14*2.0
        self.vx = v0*sqrt(1.0-z**2)*cos(s)
        self.vy = v0*sqrt(1.0-z**2)*sin(s)
        self.vz = v0*z


def add_ball():
    atoms = []
    r = 4
    s = 1.7
    h = 0.5 * s
    for ix in range(-r, r):
        for iy in range(-r, r):
            for iz in range(-r, r):
                x = ix * s
                y = iy * s
                z = iz * s
                atoms.append(Atom(x, y, z))
                atoms.append(Atom(x, y+h, z+h))
                atoms.append(Atom(x+h, y, z+h))
                atoms.append(Atom(x+h, y+h, z))
    print(f"{len(atoms)} atoms")
    return atoms


def save_file(filename, atoms):
    with open(filename, "w") as f:
        f.write("Position Data\n\n")
        f.write("{} atoms\n".format(len(atoms)))
        f.write("1 atom types\n\n")
        f.write("-10.00 10.00 xlo xhi\n")
        f.write("-10.00 10.00 ylo yhi\n")
        f.write("-10.00 10.00 zlo zhi\n")
        f.write("\n")
        f.write("Atoms\n\n")
        for i, a in enumerate(atoms):
            f.write("{} {} {} {} {}\n".format(i+1, a.type, a.x, a.y, a.z))
        f.write("\n")
        f.write("Velocities\n\n")
        for i, a in enumerate(atoms):
            f.write("{} {} {} {}\n".format(i+1, a.vx, a.vy, a.vz))
    print("Generated {}".format(filename))


save_file("config.atoms", add_ball())
