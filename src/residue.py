 #*-* coding: utf-8 *-*

#Author: AKE Franz-Arnold
#Universite Paris-Diderot
#Projet Court: ...

#import library


class Residue(object):
    #Class to compute residues

    def __init__(self, char_residue):
        self.typeHP = char_residue
        self.coordX = 0
        self.coordY = 0

    #Methodes
    def get_attributes(self):
        #Getting attributes of the residue...
        return(self.typeHP, self.coordX, self.coordY)
