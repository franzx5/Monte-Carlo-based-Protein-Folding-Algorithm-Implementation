#-*- coding: utf-8 -*-

#Author: AKE Franz-Arnold
#Universite Paris-Diderot
#Projet Court: ...

#import library
import numpy as np

class Grille(object):
    #class to compute the lattice
    def __init__(self, input_conformation):
        self.grille_taille = 2 * input_conformation.getTaille() + 1
        self.grille_midpoint = (input_conformation.getTaille(), input_conformation.getTaille())
        self.grille = np.chararray((self.grille_taille, self.grille_taille))
        self.grille[:] = "*"
        self.input_conformt = input_conformation

        for i, res in enumerate(input_conformation.conf.items()):
            self.grille[res[1].coordX, res[1].coordY] = i

    #Methodes
    def draw_grille(self):
        #Drawing lattice...
        for i in range(self.grille_taille):
            for j in range(self.grille_taille):
                if  self.grille[i,j] == "*":
                    print self.grille[i,j], "\t",
                else:
                    print self.input_conformt.conf[int(self.grille[i,j])].typeHP, "\t",
            print "\n"

    def actualiser_grille(self, input_conf):
        #Actualise grid_state with input_conformation...
        self.__init__(input_conf)


    def get_voisins_adjacents(self, residu):
        #return list of 1/ list of indice of adjacent neigbhours to residu and
        #2/ list of tuples of adjacent free neigbhours to residu...
        x, y = (residu.coordX,residu.coordY)
        coords_adjacent = {"N":(x-1, y), "S":(x+1,y), "E":(x,y+1), "W":(x,y-1)}
        voisins_adjacents = []
        voisins_libres = []
        for element in coords_adjacent.values():
            if self.grille[element[0], element[1]] != "*":
                output_res = self.input_conformt.conf[int(self.grille[element[0], element[1]])]
                voisins_adjacents.append(output_res)
            else:
                voisins_libres.append(element)
        return [voisins_adjacents, voisins_libres]

    def check_FC(self,tuple_coord):
        #check in the lattice if an input position is free
        if self.grille[tuple_coord[0],tuple_coord[1]] == "*":
            return True
        else:
            return False
