#-*- coding: utf-8 -*-

#Author: AKE Franz-Arnold
#Universite Paris-Diderot
#Projet Court: ...


#import library
import collections

class Conformation(object):
    #Class to compute the conformation

    def __init__(self, OrderedDict_residues, Energy_conf):
        self.conf = OrderedDict_residues
        self.energy = Energy_conf

    #Methodes
    def getTaille(self):
        #Getting length of the conformation
        return len(self.conf)

    def equals(self, other_conformation):
        #Check if two conformation are equals...
        if len(self.conf) == other_conformation.getTaille():
            for i in range(len(self.conf)):
                if self.conf[i].get_attributes() != other_conformation.conf[i].get_attributes():
                    return False
            return True
        else:
            return False

    def start_structure_initialisation(self):
        #Coords of all residues for the first initialisation in lattice...
        for i in range(len(self.conf)):
            self.conf[i].coordX = len(self.conf)
            self.conf[i].coordY = len(self.conf) + i
