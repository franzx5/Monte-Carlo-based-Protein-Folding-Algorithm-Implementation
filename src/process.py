 #*-*coding:utf-8*-*

#Author: AKE Franz-Arnold
#Universite Paris-Diderot
#Projet Court: ...

#import library
import grille
import conformation
import residue
import vhsd
import collections




#Main
sequenceA = "HPPFPF"
sequenceB = "HPPFPP"
ensA = collections.OrderedDict()
ensB = collections.OrderedDict()

for i, res in enumerate(sequenceA):
    ensA[i] = residue.Residue(res)
for i, res in enumerate(sequenceB):
    ensB[i] = residue.Residue(res)

#conformations
confA = conformation.Conformation(ensA,0)
confB = conformation.Conformation(ensB,0)

confA.start_structure_initialisation()
confB.start_structure_initialisation()

#Grille
g1 = grille.Grille(confA)

#mouvements
mooveA = vhsd.VHSD(g1, confA)
confA = mooveA.end_mouvement(confA.conf[0])
g1.actualiser_grille(confA)
g1.draw_grille()
confA = mooveA.corner_mouvement(confA.conf[1])
g1.actualiser_grille(confA)
g1.draw_grille()
print "\n"
confA.conf[4].coordX += 1
confA.conf[4].coordY -= 1
confA.conf[5].coordX += 1
confA.conf[5].coordY -=1
g1.actualiser_grille(confA)
g1.draw_grille()
confA = mooveA.cranckshaft_mouvement(confA.conf[2])
g1.actualiser_grille(confA)
g1.draw_grille()
