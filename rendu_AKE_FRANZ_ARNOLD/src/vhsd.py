# -*- coding: utf-8 -*-

# Author: AKE Franz-Arnold
# Universite Paris-Diderot
# Projet Court: ...


#import library
import numpy as np
import residue
import copy


class VHSD(object):
    # class to compute VHSD mouvements
    def __init__(self, input_grille, input_conformation):
        self.grille = copy.deepcopy(input_grille)
        self.conformation = copy.deepcopy(input_conformation)
        self.type = "vhsd"

    # Methodes
    def end_mouvement(self, input_residu):
        """
        function to compute end_mouvement
        """
        if input_residu.index_seq == 0:
            voisin_connecte = self.conformation.conf[1] #residu 2
            pos_libres = self.grille.get_topological_free_voisins(voisin_connecte.get_coords()) #liste de positions libres
            pos_choisi = pos_libres[np.random.choice(range(len(pos_libres)))] #choisir une position libre
            if self.grille.check_free(pos_choisi):
                self.conformation.conf[0].set_coords(pos_choisi) #modifier coordonnées
            return self.conformation
        elif input_residu.index_seq == self.conformation.getTaille()-1:
            taille_conf = self.conformation.getTaille()
            voisin_connecte = self.conformation.conf[taille_conf-2] #residu n-1
            pos_libres = self.grille.get_topological_free_voisins(voisin_connecte.get_coords()) #liste de positions libres
            pos_choisi = pos_libres[np.random.choice(range(len(pos_libres)))] #choisir une position libre
            if self.grille.check_free(pos_choisi):
                self.conformation.conf[taille_conf-1].set_coords(pos_choisi) #modifier coordonées
            return self.conformation
        else:
            return self.conformation #sinon retourne la conformation d'entrée non modifiée

    def corner_mouvement(self, input_residu):
        """
        function to compute corner_mouvement
        """
        taille_conf = self.conformation.getTaille()
        if input_residu.index_seq != self.conformation.conf[taille_conf-1].index_seq and input_residu.index_seq != 0: #si le input residu n'est pas un résidu de fin
            index_input_residu = input_residu.index_seq
            free_adjacent_i_gauche_liste = self.grille.get_topological_free_voisins(self.conformation.conf[index_input_residu-1].get_coords())
            free_adjacent_i_droite_liste = self.grille.get_topological_free_voisins(self.conformation.conf[index_input_residu+1].get_coords())
            for free_voisins_i_gauche in free_adjacent_i_gauche_liste:
                if free_voisins_i_gauche in free_adjacent_i_droite_liste: # si position libre adjacente a i-1 et i+1
                    if self.grille.check_free(free_voisins_i_gauche):
                        self.conformation.conf[index_input_residu].set_coords(free_voisins_i_gauche)
                    return self.conformation
            return self.conformation #retourne la conformation d'entree ! condition non reunies pour corner_mouv

        else:
            return self.conformation #retourne la conformation d'entree ! conditions non reunies pour corner_mouv


    def cranckshaft_mouvement(self, input_residu):
        """
        function to compute cranckshaft_mouvement
        """
        case = ("HGH", "HGB", "HDH", "HDB","VGH", "VDH", "VGB", "VDB")
        x, y = input_residu.get_coords()
        for current_case in case:
            if current_case == "HGH":
                pos_a_verif = ((x,y+1),(x+1,y-1),(x+1,y),(x+1,y+1),(x+1,y+2)) #coordonées u_shaped à verifier
                pos_a_verif2 = ((x+2,y),(x+2,y+1)) #coords a verif pour le turn
                if self.check_crankshaft_case_ushaped(pos_a_verif): #si config u_shaped HGH
                    if self.check_turn_dispo(pos_a_verif2): #si turn possible
                        index_input_residu = input_residu.index_seq
                        res_close = self.conformation.conf[int(self.grille.grille[x,y+1])]
                        #Make turn
                        self.conformation.conf[index_input_residu].set_coords(pos_a_verif2[0])
                        self.conformation.conf[res_close.index_seq].set_coords(pos_a_verif2[1])
                        return self.conformation
                    else:
                        return self.conformation #retourne la conformation d'entree ! conditions non reunies pour crankshaft_mouv
                else:
                    return self.conformation #retourne la conformation d'entree ! conditions non reunies pour crankshaft_mouv
            elif current_case == "HGB":
                pos_a_verif = ((x,y+1),(x-1,y-1),(x-1,y),(x-1,y+1),(x-1,y+2)) #coordonées u_shaped à verifier
                pos_a_verif2 = ((x-2,y),(x-2,y+1)) #coords à verif pour le turn
                if self.check_crankshaft_case_ushaped(pos_a_verif): #si config u_shaped HGH
                    if self.check_turn_dispo(pos_a_verif2): #si turn possible
                        index_input_residu = input_residu.index_seq
                        res_close = self.conformation.conf[int(self.grille.grille[x,y+1])]
                        #Make turn
                        self.conformation.conf[index_input_residu].set_coords(pos_a_verif2[0])
                        self.conformation.conf[res_close.index_seq].set_coords(pos_a_verif2[1])
                        return self.conformation
                    else:
                        return self.conformation #retourne la conformation d'entree ! conditions non reunies pour crankshaft_mouv
                else:
                    return self.conformation #retourne la conformation d'entree ! conditions non reunies pour crankshaft_mouv
            elif current_case == "HDH":
                pos_a_verif = ((x,y-1),(x+1,y-2),(x+1,y-1),(x+1,y),(x+1,y+1)) #coordonées u_shaped à verifier
                pos_a_verif2 = ((x+2,y),(x+2,y-1)) #coords a verif pour le turn
                if self.check_crankshaft_case_ushaped(pos_a_verif): #si config u_shaped HGH
                    if self.check_turn_dispo(pos_a_verif2): #si turn possible
                        index_input_residu = input_residu.index_seq
                        res_close = self.conformation.conf[int(self.grille.grille[x,y-1])]
                        #Make turn
                        self.conformation.conf[index_input_residu].set_coords(pos_a_verif2[0])
                        self.conformation.conf[res_close.index_seq].set_coords(pos_a_verif2[1])
                        return self.conformation
                    else:
                        return self.conformation #retourne la conformation d'entree ! conditions non reunies pour crankshaft_mouv
                else:
                    return self.conformation #retourne la conformation d'entree ! conditions non reunies pour crankshaft_mouv
            elif current_case == "HDB":
                pos_a_verif = ((x,y-1),(x-1,y-2),(x-1,y-1),(x-1,y),(x-1,y+1)) #coordonées u_shaped à verifier
                pos_a_verif2 = ((x-2,y),(x-2,y-1)) #coords a verif pour le turn
                if self.check_crankshaft_case_ushaped(pos_a_verif): #si config u_shaped HGH
                    if self.check_turn_dispo(pos_a_verif2): #si turn possible
                        index_input_residu = input_residu.index_seq
                        res_close = self.conformation.conf[int(self.grille.grille[x,y-1])]
                        #Make turn
                        self.conformation.conf[index_input_residu].set_coords(pos_a_verif2[0])
                        self.conformation.conf[res_close.index_seq].set_coords(pos_a_verif2[1])
                        return self.conformation
                    else:
                        return self.conformation #retourne la conformation d'entree ! conditions non reunies pour crankshaft_mouv
                else:
                    return self.conformation #retourne la conformation d'entree ! conditions non reunies pour crankshaft_mouv
            elif current_case == "VGH":
                pos_a_verif = ((x+1,y),(x,y+1),(x-1,y+1),(x+1,y+1),(x+2,y+1)) #coordonées u_shaped à verifier
                pos_a_verif2 = ((x,y+2), (x+1,y+2))#coords a verif pour le turn
                if self.check_crankshaft_case_ushaped(pos_a_verif): #si config u_shaped HGH
                    if self.check_turn_dispo(pos_a_verif2): #si turn possible
                        index_input_residu = input_residu.index_seq
                        res_close = self.conformation.conf[int(self.grille.grille[x+1,y])]
                        #Make turn
                        self.conformation.conf[index_input_residu].set_coords(pos_a_verif2[0])
                        self.conformation.conf[res_close.index_seq].set_coords(pos_a_verif2[1])
                        return self.conformation
                    else:
                        return self.conformation #retourne la conformation d'entree ! conditions non reunies pour crankshaft_mouv
                else:
                    return self.conformation #retourne la conformation d'entree ! conditions non reunies pour crankshaft_mouv
            elif current_case == "VDH":
                pos_a_verif = ((x+1,y),(x,y-1),(x-1,y-1),(x+1,y-1),(x+2,y-1)) #coordonées u_shaped à verifier
                pos_a_verif2 = ((x,y-2), (x+1,y-2)) #coords a verif pour le turn
                if self.check_crankshaft_case_ushaped(pos_a_verif): #si config u_shaped HGH
                    if self.check_turn_dispo(pos_a_verif2): #si turn possible
                        index_input_residu = input_residu.index_seq
                        res_close = self.conformation.conf[int(self.grille.grille[x+1,y])]
                        #Make turn
                        self.conformation.conf[index_input_residu].set_coords(pos_a_verif2[0])
                        self.conformation.conf[res_close.index_seq].set_coords(pos_a_verif2[1])
                        return self.conformation
                    else:
                        return self.conformation #retourne la conformation d'entree ! conditions non reunies pour crankshaft_mouv
                else:
                    return self.conformation #retourne la conformation d'entree ! conditions non reunies pour crankshaft_mouv
            elif current_case == "VGB":
                pos_a_verif = ((x-1,y),(x-2,y+1),(x-1,y+1),(x,y+1),(x+1,y+1)) #coordonées u_shaped à verifier
                pos_a_verif2 = ((x,y+2), (x-1,y+2)) #coords a verifs pour le turn
                if self.check_crankshaft_case_ushaped(pos_a_verif): #si config u_shaped HGH
                    if self.check_turn_dispo(pos_a_verif2): #si turn possible
                        index_input_residu = input_residu.index_seq
                        res_close = self.conformation.conf[int(self.grille.grille[x-1,y])]
                        #Make turn
                        self.conformation.conf[index_input_residu].set_coords(pos_a_verif2[0])
                        self.conformation.conf[res_close.index_seq].set_coords(pos_a_verif2[1])
                        return self.conformation
                    else:
                        return self.conformation #retourne la conformation d'entree ! conditions non reunies pour crankshaft_mouv
                else:
                    return self.conformation #retourne la conformation d'entree ! conditions non reunies pour crankshaft_mouv
            elif current_case == "VDB":
                pos_a_verif = ((x-1,y),(x-2,y-1),(x-1,y-1),(x,y-1),(x+1,y-1)) #coordonées u_shaped à verifier
                pos_a_verif2 = ((x,y-2), (x-1,y-2)) #coords a verifs pour le turn
                if self.check_crankshaft_case_ushaped(pos_a_verif): #si config u_shaped HGH
                    if self.check_turn_dispo(pos_a_verif2): #si turn possible
                        index_input_residu = input_residu.index_seq
                        res_close = self.conformation.conf[int(self.grille.grille[x-1,y])]
                        #Make turn
                        self.conformation.conf[index_input_residu].set_coords(pos_a_verif2[0])
                        self.conformation.conf[res_close.index_seq].set_coords(pos_a_verif2[1])
                        return self.conformation
                    else:
                        return self.conformation #retourne la conformation d'entree ! conditions non reunies pour crankshaft_mouv
                else:
                    return self.conformation #retourne la conformation d'entree ! conditions non reunies pour crankshaft_mouv
    def check_crankshaft_case_ushaped(self, pos):
        """
        check if ushaped_configuration if true for input Position
        """
        g = self.grille
        if (g.check_free(pos[0]),g.check_free(pos[1]),g.check_free(pos[2]),g.check_free(pos[3]),g.check_free(pos[4])) == (0,0,0,0,0):
            return True
        else:
            return False
    def check_turn_dispo(self, pos_a_verif):
        g = self.grille
        if (g.check_free(pos_a_verif[0]), g.check_free(pos_a_verif[1])) == (1,1):
            return True
        else:
            return False
