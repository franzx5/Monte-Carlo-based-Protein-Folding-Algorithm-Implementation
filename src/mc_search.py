#*-*coding:utf-8*-*

#Author: AKE Franz-Arnold
#Universite Paris-Diderot
#Projet Court: ...


#import library
import copy
import numpy as np
import vhsd
import pull
import random
import math


class Mc_search(object):
    """
    Class Monte_carlo Search
    =============
    Class to compute an object for monte carlo search algorithm:
    need for initialisation, the following params :
    contains several function to make operations on it
    :input 1:  nb_step      number of steps of running the random residus mooves (int)
    :input 2:  a conformation object
    :input 3: a lattice object
    :input 4: a mouvement object (VHSD or Pull Types)

    certains parameters in the function are fixed like the temperature T ~ 160
    """

    def __init__(self, input_nb_step, input_conformation, input_grille, input_mouvement):
        self.nb_step = input_nb_step
        self.conformation = input_conformation
        self.grille = input_grille
        self.mouvement = input_mouvement

    #Methodes
    def run(self):
        """
        run the Monte carlo search algorithm for the number of step specified
        """
        print "start_conformation_energy is ", self.conformation.compute_energy(self.grille)
        for i in range(self.nb_step):
            conf_bis = copy.deepcopy(self.conformation)
            k = random.randint(0,conf_bis.getTaille()-1) #selection uniforme aleatoire d'un indice de résidu
            res_k = conf_bis.conf[k] #residu aleatoire k

            if self.mouvement.type == "vhsd":
                #plusieurs mouvements vshd possibles
                choix = random.choice(range(3)) #choix aleatoire d'un mouvement
                if choix == 0:
                    conf_bis = self.mouvement.end_mouvement(res_k)
                elif choix == 1:
                    conf_bis = self.mouvement.corner_mouvement(res_k)
                else:
                    continue
                    #conf_bis = self.mouvement.cranckshaft_mouvement(res_k)
            elif self.mouvement.type == "pull":
                conf_bis = self.mouvement.pull_mouvement(res_k) #pull_mouvement
            variation_energy = conf_bis.compute_energy(self.grille) - self.conformation.compute_energy(self.grille)
            if variation_energy <= 0:
                self.conformation = copy.deepcopy(conf_bis)
                self.grille.maj_grille(self.conformation) #mise a jour de la grille
            else:
                q = random.uniform(0,1)
                if q > math.exp(float(-variation_energy)/160):
                    self.conformation = copy.deepcopy(conf_bis)
                    self.grille.maj_grille(self.conformation) #mise a jour de la grille
        print "final_conformation_energy is ", self.conformation.compute_energy(self.grille)
        #retourne conformation finale
        return self.conformation
