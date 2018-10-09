#-*- coding: utf-8 -*-

#Author: AKE Franz-Arnold
#Universite Paris-Diderot
#Projet Court: ...


#import library
import collections
import residue

class Conformation(object):
    """
    Class Conformation
    ==================
    Class to compute an object Conformation constituted by an ensemble of residues objects
    stocked in an Ordered dictionnary
    contains several function to make operations on it
    :input : sequence Hydrophobic / Polar (String)
    """
    def __init__(self, sequence):
        """
        compute conformation object with an Hydrophobic / Polar sequence (String)
        :input : sequence HP
        :attribute 1 : conf     -> an OrderedDict of residues (OrderedDict)
        :attribute 2 : energy   -> energy of the conformation (int)
        """
        dic = collections.OrderedDict()
        for i, res in enumerate(sequence):
            dic[i] = residue.Residue(i, res)
        self.conf = dic
        self.energy = 0

    #Methodes
    def getTaille(self):
        """
        #Getting length of the conformation
        :input : None
        :output : size of the conformation (int)
        """
        return len(self.conf)
    def equals(self, other_conformation):
        """
        Check if two conformation are equals
        in terms of each attributes of both conformation (compare all attributes)
        :input : conformation to compare
        :output : True or False
        """
        if len(self.conf) == other_conformation.getTaille():
            for i in range(len(self.conf)):
                if self.conf[i].get_attributes() != other_conformation.conf[i].get_attributes():
                    return False
            return True
        else:
            return False
    def start_structure_initialisation(self):
        """
        give coords to all residues in the conformation in order to fix it in the center of the lattice..
        """
        for i in range(len(self.conf)):
            self.conf[i].coordX = len(self.conf)
            self.conf[i].coordY = len(self.conf) + i
    def get_connected(self, input_residu):
        """
        return list of connected residu to input_residu
        """
        output = []
        for res in self.conf.items():
            if input_residu.check_connected(res[1]):
                output.append(res[1])
        return output
    def compute_energy(self, grille):
        """
        calculate the energy of the conformation and return it
        """
        l_resH = [] #liste_residus H
        l_resH_pairs = [] #liste_residu H pairs
        l_resH_adjacents = [] #liste_residu H adjacents
        l_resH_consecutif = []

        for res in self.conf.items(): #obtenir liste residus H
            if res[1].typeHP == "H":
                l_resH.append(res[1])
        for res1 in l_resH:
            for res2 in l_resH:
                l_resH_pairs.append((res1,res2))
        for pair in l_resH_pairs:
            if pair[0].get_coords() in grille.get_topological_voisins_all(pair[1].get_coords()):
                l_resH_adjacents.append(pair)
        for pair in l_resH_adjacents:
            if pair[0].check_connected(pair[1]) == False:
                l_resH_consecutif.append(pair)

        return int(-len(l_resH_consecutif)/2)
