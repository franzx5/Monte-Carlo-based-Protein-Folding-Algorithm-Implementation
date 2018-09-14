# -*- coding: utf-8 -*-

# Author: AKE Franz-Arnold
# Universite Paris-Diderot
# Projet Court: ...


#import library
import numpy as np
import residue


class VHSD(object):
    # class to compute VHSD mouvements
    def __init__(self, input_grille, input_conformation):
        self.grille = input_grille
        self.conformation = input_conformation

    # Methodes
    def end_mouvement(self, residu):
        if residu == self.conformation.conf[0] or residu == self.conformation.conf[len(self.conformation.conf)-1]:
            res_voisin = self.grille.get_voisins_adjacents(residu)[0][0]
            free_positions = self.grille.get_voisins_adjacents(res_voisin)[1]

            if len(free_positions) > 0:
                free_position = free_positions[np.random.choice(range(len(free_positions)))]
                if residu == self.conformation.conf[0]:
                    self.conformation.conf[0] = residue.Residue(residu.typeHP)
                    self.conformation.conf[0].coordX, self.conformation.conf[0].coordY = (free_position[0], free_position[1])
                else:
                    taille = len(self.conformation.conf) -1
                    self.conformation.conf[taille] = residue.Residue(residu.typeHP)
                    self.conformation.conf[taille].coordX, self.conformation.conf[taille].coordY = (free_position[0], free_position[1])
                return self.conformation
        else:
            print "Mauvais residu ! Pas un résidu d'extrémité ! Non valable pour le end_mouvement !!"

    def corner_mouvement(self, residu):
        if residu != self.conformation.conf[len(self.conformation.conf)-1]:
            res_voisin = self.grille.get_voisins_adjacents(residu)[0]
            if len(res_voisin) == 2:
                print "ok"
                free_positions_voisinA = self.grille.get_voisins_adjacents(res_voisin[0])[1]
                free_positions_voisinB = self.grille.get_voisins_adjacents(res_voisin[1])[1]

                for position in free_positions_voisinA:
                    if position in free_positions_voisinB:
                        if self.grille.grille[position[0], position[1]] == "*":
                            print "ok2"
                            index = self.conformation.conf.values().index(residu)
                            self.conformation.conf[index] = residue.Residue(residu.typeHP)
                            self.conformation.conf[index].coordX, self.conformation.conf[index].coordY = (position[0], position[1])
                            return self.conformation
        else:
            print "Résidu de fin ! Non valable pour le corner_mouvement !!"

    def cranckshaft_mouvement(self, residu):
        x, y = (residu.coordX, residu.coordY)
        coords_a_verif_vert_gauche = {"i-1":(x,y+1), "i-2":(x-1,y+1), "i+1":(x+1,y), "i+2":(x+1,y+1), "i+3":(x+2,y+1)}
        coords_a_verif_horiz_haut = {"i-1":(x+1,y+1), "i-2":(x+1,<)}

        for element in coords_a_verif.values():
            print (element[0], element[1])
            if self.grille.grille[element[0], element[1]] == "*":
                print "input residue is not a part of a u_shaped bend"
                return False
        indexA = self.conformation.conf.values().index(residu)
        indexB = self.grille.grille(x+1,y)
        self.conformation.conf[indexA] = residue.Residue(residu.typeHP)
        self.conformation.conf[indexA].coordX, self.conformation.conf[indexA].coordY = (residu.coordX, residu.coordY+2)
        self.conformation.conf[indexB].coordX, self.conformation.conf[indexB].coordY = (residu.coordX+1, residu.coordY+2)
        return self.conformation
