#-*- coding: utf-8 -*-

#Author: AKE Franz-Arnold
#Universite Paris-Diderot
#Projet Court: ...


#import library
import numpy as np
import residue


class VHSD(object):
    #class to compute VHSD mouvements
    def __init__(self, input_grille, input_conformation):
        self.grille = input_grille
        self.conformation = input_conformation

    #Methodes
    def end_mouvement(self, residu):
        if residu == self.conformation.conf[0] or residu == self.conformation.conf[len(self.conformation.conf)-1]:
            res_voisin = self.grille.get_voisins_adjacents(residu)[0][0]
            free_positions = self.grille.get_voisins_adjacents(res_voisin)[1]

            if len(free_positions)>0:
                free_position = free_positions[np.random.choice(range(len(free_positions)))]
                if residu == self.conformation.conf[0]:
                    self.conformation.conf[0] = residue.Residue(residu.typeHP)
                    self.conformation.conf[0].coordX = free_position[0]
                    self.conformation.conf[0].coordY = free_position[1]
                else:
                    self.conformation.conf[len(self.conformation.conf)-1] = residue.Residue(residu.typeHP)
                    self.conformation.conf[len(self.conformation.conf)-1].coordX = free_position[0]
                    self.conformation.conf[len(self.conformation.conf)-1].coordY = free_position[1]
                return self.conformation
        else:
            print "Mauvais residu ! Pas un résidu d'extrémité ! Non valable pour le end_mouvement"

    def corner_mouvement(self, residu):
        res_voisin = self.grille.get_voisins_adjacents(residu)[0]
        if len(res_voisin) == 2:
            free_positions_voisinA = self.grille.get_voisins_adjacents(res_voisin[0])[1]
            free_positions_voisinB = self.grille.get_voisins_adjacents(res_voisin[1])[1]

            for position in free_positions_voisinA:
                if position in free_positions_voisinB:
                    #check si la position est vide
                    if self.grille.grille[position[0], position[1]] == "*":
                        index = self.conformation.conf.values().index(residu)
                        self.conformation.conf[index] = residue.Residue(residu.typeHP)
                        self.conformation.conf[index].coordX = position[0]
                        self.conformation.conf[index].coordY = position[1]
                        return self.conformation
