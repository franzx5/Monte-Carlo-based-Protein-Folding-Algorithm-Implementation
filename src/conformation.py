#-*- coding: utf-8 -*-

#Author: AKE Franz-Arnold
#Universite Paris-Diderot
#Projet Court: ...


#import library


class Conformation(object):
    #Class to compute the conformation

    def __init__(self, OrderedDict_residues, Energy_conf):
        self.conf = OrderedDict_residues
        self.energy = Energy_conf
