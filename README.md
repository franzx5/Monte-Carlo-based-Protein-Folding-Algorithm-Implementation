
# Subject : REPLIEMENT D’UN MODÈLE SIMPLIFIE DE PROTÉINE PAR UN ALGORITHME DE MONTE CARLO ET ECHANGES DE REPLIQUES

#### Author: AKE Franz-Arnold
#### Université Paris-Diderot
#### Projet Court Python

__Objectif__ 

Réaliser un programme reprenant la méthode décrite dans l'article.
Dans un premier temps l'algorithme de Monte-Carlo simple sera implémenté,
ensuite le R.E. Une séquence arbitraire de protéine pourra être soumis au
programme afin de calculer son repliement par ce modèle.

Based on the article :

Thachuk C, Shmygelska A, Hoos HH. A replica exchange Monte Carlo
algorithm for protein folding in the HP model. BMC Bioinformatics. 2007 Sep
17;8:342. PubMed PMID: 17875212; PubMed Central PMCID: PMC2071922.


Exécution sous l'environnement python 2

1/ Répertoires et Localisation des fichiers
*******************************************

Le répertoire contient les dossiers data, source et docs

le repertoire data/sequencesHP contient des exemples de sequenceHP au format txt
le repertoire src/ contient tous les codes sources pour l'implémentation des différentes classes tel que spécifié dans le rapport du Projet (Annexes)
le repertoire docs/ contient le rapport du projet en format open_office et pdf


2/Programme
***********

Il y a un seul script à exécuter dans le bash nommée REMC

celui-ci prend en paramètre :
1/ un fichier de séquence_HP (répertoire data/sequencesHP)
2/ le nombre de steps pour l'algorithme  (un entier)
3/ le type de mouvement souhaité  - 3 possibilités :   "vhsd" ou "pull" ou "hybrid"
4/ le chemin de destination (Path) pour la sauvegarde du fichier PDB_file retournée par le programme
(Sortie par défaut dans la sortie standard)

Ex: time ./REMC ../data/sequencesHP/sequenceHP1.txt 500 "vhsd" sequence1.pdb


3/Visualisation de la conformation
**********************************

La fichier pdb de sortie est un fichier construit avec les résidus de la séquence équivalents aux positions atomiques,
et pour lequel chaque position atomiques s'est vue attribuer les coordonnées géométriques de résidus dans la conformation
Celui-ci peut être visualisé via l'outil Pymol.

Quelques manipulation rende la visualisation plus aisée (Couleurs et Labels):
Action -> preset -> b factor putty
Action -> preset -> ball and stick
Label -> residue name
Color -> by rep -> label -> black


#4/Modules python importées
***************************
Numpy, Argparse, sys, copy, collections



#Contacts Personnels
#*******************
AKE Franz-Arnold
franz.ake@etu.univ-paris-diderot.fr
aerod7710@gmail.com

