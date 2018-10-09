#-*- coding: utf-8 -*-

#Author: AKE Franz-Arnold
#Universite Paris-Diderot
#Projet Court: ...

#import library
import numpy as np

class Grille(object):
    """
    Class Grille
    ============
    Class to compute a Lattice in which a conformation could be integrated
    and contains several function to make operations on it
    :need no arguments for initialisation!
    """
    def __init__(self):
        """
        initialiser an Empty lattice

        :attribute_1 : grille_taille    -> Size of the Lattice (int)
        :attribute_2 : grille_midpoint  -> Midpoint of the Lattice (tuple of int)
        :attribute_3 : grille           -> Lattice (numpy_array)
        """
        self.grille_taille = 0
        self.grille_midpoint = (0,0)
        self.grille = np.chararray((self.grille_taille, self.grille_taille))
        self.grille[:] = "*"

    #Methodes
    def maj_grille(self, input_conformation):
        """
        integrate a conformation in the lattice object self !
        :input : conformation object
        """
        self.grille_taille = 2 * input_conformation.getTaille() + 1
        self.grille_midpoint = (input_conformation.getTaille(), input_conformation.getTaille())
        self.grille = np.chararray((self.grille_taille, self.grille_taille), itemsize=2)
        self.grille[:] = "*"
        for i, res in enumerate(input_conformation.conf.items()):
            self.grille[res[1].coordX, res[1].coordY] = res[1].index_seq
    def draw_grille(self):
        """
        Print _drawing the lattice in the terminal...
        :input : Nothing
        """
        for i in range(self.grille_taille):
            for j in range(self.grille_taille):
                if  self.grille[i,j] == "*":
                    print self.grille[i,j], "  ",
                else:
                    print self.grille[i,j], "  ",
            print "\n"
    def get_topological_free_voisins(self, input_tuple):
        """
        return for an input_coord, a list of the coords of free adjacents Position ...
        :input : tuple of position (x,y)
        :output : list of coord's tuples
        """
        x, y = (input_tuple[0], input_tuple[1])
        pos_a_verif = ((x,y+1),(x,y-1),(x-1,y),(x+1,y))
        output = []
        for tuple in pos_a_verif:
            if self.check_free(tuple):
                output.append(tuple)
        return output
    def check_free(self, input_tuple):
        """
        Check in an position is free
        :input : an tuple of coords
        :output : True or False
        """
        if self.grille[input_tuple] == "*":
            return True
        else:
            return False
    def get_topological_voisins(self, input_tuple):
        """
        return for an input_coord, a list of the coords of adjacent Residus
        :input : tuple of position (x,y)
        :output : list of coord's tuples
        """
        x, y = (input_tuple[0], input_tuple[1])
        pos_a_verif = ((x,y+1),(x,y-1),(x-1,y),(x+1,y))
        output = []
        for tuple in pos_a_verif:
            if self.check_free(tuple) == False:
                output.append(tuple)
        return output
    def get_topological_voisins_all(self, input_tuple):
        """
        return for an input_coord, a list of the coords of adjacent Positions
        :input : tuple of position (x,y)
        :output : list of coord's tuples
        """
        x, y = (input_tuple[0], input_tuple[1])
        pos_a_verif = ((x,y+1),(x,y-1),(x-1,y),(x+1,y))
        return pos_a_verif
    def check_adjacent_diag(self, tuple_A, tuple_B):
        """
        check if a coords of tuple_A if diagonally adjacent to another one, tuple_B
        :input1 : tuple A
        :input2 : tuple B
        :output : True or False
        """
        x, y = (tuple_A[0], tuple_A[1])
        pos_a_verif = ((x-1,y+1),(x-1,y-1),(x+1,y-1),(x+1,y+1))
        for tuple in pos_a_verif:
            if tuple == tuple_B:
                return True
        return False
    def check_adjacence(self, tuple_A, tuple_B):
        """
        check if a coords of tuple_A if adjacent to another one, tuple_B
        :input1 : tuple A
        :input2 : tuple B
        :output : True or False
        """
        x, y = (tuple_A[0], tuple_A[1])
        pos_a_verif = ((x,y+1),(x,y-1),(x-1,y),(x+1,y))
        for tuple in pos_a_verif:
            if tuple == tuple_B:
                return True
        return False
