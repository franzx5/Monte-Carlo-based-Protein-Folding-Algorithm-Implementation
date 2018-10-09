 #*-* coding: utf-8 *-*

#Author: AKE Franz-Arnold
#Universite Paris-Diderot
#Projet Court: ...

#import library


class Residue(object):
    """
    Class Residue
    =============
    Class to compute an object Residue wich contains :
    index of the residue in the input sequence , type of the residue, and its coords.
    contains several function to make operations on it
    :input 1:  index of the residue in the sequence (int)
    :input 2: residue (char)
    """
    def __init__(self, input_index, char_residue):
        """
        create Residue object...
        input_1 :     index of the residu
        input_2 :     symbol of the residu
        attribute_1 : index_seq     -> index of the residu in the sequence (int)
        attribute_2 : typeHP        -> type of the residu ; Hydrophobic or Polar (char)
        """
        self.index_seq = input_index
        self.typeHP = char_residue
        self.coordX = 0
        self.coordY = 0
        self.spepdb = char_residue + str(input_index)

    #Methodes
    def get_attributes(self):
        """
        Getting attributes of the residue...
        output : tuple of object's attributes
        """
        return(self.index_seq,self.typeHP, self.coordX, self.coordY)
    def get_coords(self):
        """
        return coords of the residu object
        """
        return(self.coordX, self.coordY)
    def set_coords(self,tuple):
        """
        set coords of the residu object from the input_tuple
        """
        self.coordX, self.coordY = tuple
    def check_connected(self, residu):
        """
        check if the input residu is connected to the actual residu (self)
        """
        if residu.index_seq == self.index_seq + 1 or residu.index_seq == self.index_seq -1: #verifier les indexs de sequence
            return True
        else:
            return False
