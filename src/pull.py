#-*- coding: utf-8 -*-

#Author: AKE Franz-Arnold
#Universite Paris-Diderot
#Projet Court: ...


#import library
import conformation
import copy


class Pull(object):
    #class to compute pull mouvement
    def __init__(self, input_grille, input_conformation):
        self.grille = copy.deepcopy(input_grille)
        self.conformation = copy.deepcopy(input_conformation)
        self.type = "pull"


    #Methodes
    def pull_mouvement(self, input_residu):
        #function to compute pull_mouvement...
        conf_save = copy.deepcopy(self.conformation) #copie de la conformation
        #obtenir liste des positions libres adjacent au residu i+1
        if input_residu.index_seq != self.conformation.getTaille()-1 and input_residu.index_seq != 0: #pas le dernier résidu
            res_i_droite = self.conformation.conf[input_residu.index_seq+1]
            liste_i_droite = self.grille.get_topological_free_voisins(res_i_droite.get_coords())
            for pos_libre in liste_i_droite:
                if self.grille.check_adjacent_diag(input_residu.get_coords(),pos_libre): #verifier si cette position est adjacente au residu i
                    L = pos_libre #position L
                    L_topologicals_voisins = self.grille.get_topological_voisins_all(L)
                    l_residu_topological_voisins = self.grille.get_topological_voisins_all(input_residu.get_coords())
                    for topo_vois in L_topologicals_voisins:
                        if topo_vois in l_residu_topological_voisins: #si position adjacent à L et input_residu
                            if topo_vois != res_i_droite.get_coords():
                                C = topo_vois #position C
                                res_i_gauche = self.conformation.conf[input_residu.index_seq-1]
                                if res_i_gauche.get_coords() == C: #if C occupied by residue i-1
                                    self.conformation.conf[input_residu.index_seq].set_coords(L) #deplacer résidu i to L
                                    return self.conformation
                                else:
                                    """
                                    NOT WORKING WELL for large sequence in a particular specific case of the pull_mouvement
                                    broken of the conformation !
                                    """
                                    # print "case_2" if C   ----
                                    # self.conformation.conf[input_residu.index_seq].set_coords(L) #deplacer résidu i to L
                                    # res_i_gauche.set_coords(C) #deplacer residu i-1 to C
                                    # self.grille.maj_grille(self.conformation) #mise a jour grille
                                    # index = input_residu.index_seq
                                    # while index-2 >=0: #tq conformation invalide
                                    #         res_j2 = conf_save.conf[index-2]        #serie de pull moves
                                    #         res_j = conf_save.conf[index]
                                    #         print "mouvement réalisé"
                                    #         if self.grille.check_free(res_j.get_coords()):
                                    #             res_j2.set_coords(res_j.get_coords())
                                    #         else:
                                    #             print "COLISION !!!!!!!!!!!"
                                    #         index -= 1
                                    #         self.grille.maj_grille(self.conformation) #mise à jour grille

                                    return self.conformation
            return self.conformation
        else:
            return self.conformation # retourne conformation d'entrée ! conditions non reunies pour pull_mouv
