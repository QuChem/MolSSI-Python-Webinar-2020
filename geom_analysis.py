import numpy as np
import os
import argparse

def calculate_distance(atom1_coord, atom2_coord):
    """
    Calculates the distance between two points in 3D space.
    """
    x_distance = atom1_coord[0] - atom2_coord[0]
    y_distance = atom1_coord[1] - atom2_coord[1]
    z_distance = atom1_coord[2] - atom2_coord[2]
    atom_distance = np.sqrt(x_distance ** 2 + y_distance ** 2 + z_distance ** 2)
    return atom_distance


def open_xyz(file_name):
    """
    This function 
    """
    xyz_file = np.genfromtxt(fname = file_name, skip_header=2, dtype='unicode')
    symbols = xyz_file[:, 0]
    coordinates = xyz_file[:, 1:]
    coordinates = coordinates.astype(np.float)
    return symbols, coordinates


def bond_check(distance):
    if distance > 0 and distance <= 1.5:
        return True
    else:
        return False

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description='The scrip')
    parser.add_argument('xyz_file', help='The filepath for the xyz file to analyse.')
    args = parser.parse_args()
    
    xyzfilename = args.xyz_file
    symbols, coords = open_xyz(xyzfilename)
    num_atoms = len(symbols)
    for num1 in range(0, num_atoms):
        for num2 in range(0, num_atoms):
            if num1 < num2:
                atom_distance = calculate_distance(coords[num1], coords[num2])
                if bond_check(atom_distance) is True:
                    print(F'{symbols[num1]} to {symbols[num2]} : {atom_distance:.3f}')
