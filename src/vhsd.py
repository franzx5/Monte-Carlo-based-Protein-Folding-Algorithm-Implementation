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
                free_positions_voisinA = self.grille.get_voisins_adjacents(res_voisin[0])[1]
                free_positions_voisinB = self.grille.get_voisins_adjacents(res_voisin[1])[1]

                for position in free_positions_voisinA:
                    if position in free_positions_voisinB:
                        if self.grille.grille[position[0], position[1]] == "*":
                            index = self.conformation.conf.values().index(residu)
                            self.conformation.conf[index] = residue.Residue(residu.typeHP)
                            self.conformation.conf[index].coordX, self.conformation.conf[index].coordY = (position[0], position[1])
                            return self.conformation
        else:
            print "Résidu de fin ! Non valable pour le corner_mouvement !!"


    def cranckshaft_mouvement(self, residu):
        x, y = (residu.coordX, residu.coordY)
        horiz_case = ("HGH", "HGB", "HDH", "HDB")
        g = self.grille

        for ele in horiz_case:
            check = self.check_crankshaft_case(residu,ele)
            print check, ele
            if ele == "HGH" and check == True:
                if g.check_FC((x+2,y)) and g.check_FC((x+2,y+1)):
                    res_close = self.conformation.conf[int(g.grille[x,y+1])]
                    return self.turn_crankshaft(residu, res_close, (x+2,y), (x+2,y+1))
            if ele == "HGB" and check == True:
                if g.check_FC((x-2,y)) and g.check_FC((x-2,y+1)):
                    res_close = self.conformation.conf[int(g.grille[x,y+1])]
                    return self.turn_crankshaft(residu, res_close, (x-2,y), (x-2,y+1))
            if ele == "HDH" and check == True:
                if g.check_FC((x+2,y)) and g.check_FC((x+2,y-1)):
                    res_close = self.conformation.conf[int(g.grille[x,y-1])]
                    return self.turn_crankshaft(residu, res_close, (x+2,y), (x+2,y-1))
            if ele == "HDB" and check == True:
                if g.check_FC((x-2,y)) and g.check_FC((x-2,y-1)):
                    res_close = self.conformation.conf[int(g.grille[x,y-1])]
                    return self.turn_crankshaft(residu, res_close, (x-2,y), (x-2,y-1))



    def check_crankshaft_case(self, residu, case):
        x, y = (residu.coordX, residu.coordY)
        if case == "HGH":
            pos = ((x,y+1),(x+1,y-1),(x+1,y),(x+1,y+1),(x+1,y+2))
            if self.check_vect_pos(pos):
                return True
            return False
        if case == "HGB":
            pos = ((x,y+1),(x-1,y-1),(x-1,y),(x-1,y+1),(x-1,y+2))
            if self.check_vect_pos(pos):
                return True
            return False
        if case == "HDH":
            pos = ((x,y-1),(x+1,y-2),(x+1,y-1),(x+1,y),(x+1,y+1))
            if self.check_vect_pos(pos):
                return True
            return False
        if case == "HDB":
            pos = ((x,y-1),(x-1,y-2),(x-1,y-1),(x-1,y),(x-1,y+1))
            if self.check_vect_pos(pos):
                return True
            return False
        if case == "VGH":
            pos = ((x+1,y),(x,y+1),(x-1,y+1),(x+1,y+1),(x+2,y+1))
            if self.check_vect_pos(pos):
                return True
            return False
        if case == "VDH":
            pos = ((x+1,y),(x,y-1),(x-1,y-1),(x+1,y-1),(x+2,y-1))
            if self.check_vect_pos(pos):
                return True
            return False
        if case == "VGB":
            pos = ((x-1,y),(x-2,y+1),(x-1,y+1),(x,y+1),(x+1,y+1))
            if self.check_vect_pos(pos):
                return True
            return False
        if case == "VDB":
            pos = ((x-1,y),(x-2,y-1),(x-1,y-1),(x,y-1),(x+1,y-1))
            if self.check_vect_pos(pos):
                return True
            return False

    def check_vect_pos(self, pos):
        g = self.grille
        res = (g.check_FC(pos[0]), g.check_FC(pos[1]), g.check_FC(pos[2]), g.check_FC(pos[3]), g.check_FC(pos[4]))
        if res == tuple([False]*5) :
            return True
        else:
            return False

    def turn_crankshaft(self, residu, res_close, coordA, coordB):
        residu.coordX, residu.coordY = coordA
        res_close.coordX, res_close.coordY = coordB
        return self.conformation
