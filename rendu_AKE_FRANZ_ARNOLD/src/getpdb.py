



#import library
import collections


def get_pdb(path, input_conformation):
    #function to get a pdb file of the conformation...

    ligne = collections.OrderedDict()
    ligne["field1"] = " " * 6
    ligne["field2"] = " " * 5
    ligne["espace1"] = " "
    ligne["field3"] = " " * 4
    ligne["field4"] = " "
    ligne["field5"] = " " * 3
    ligne["espace2"] = " "
    ligne["field6"] = " "
    ligne["field7"] = " " * 4
    ligne["field8"] = " "
    ligne["espace3"] = " " * 3
    ligne["field9"] = " " * 8
    ligne["field10"] = " " * 8
    ligne["field11"] = " " * 8
    ligne["field12"] = " " * 6
    ligne["field13"] = " " * 6
    ligne["espace4"] = " " * 10
    ligne["field14"] = " " * 2
    ligne["field15"] = " " * 2

    for i, residu in enumerate(input_conformation.conf.items()):
        ligne["field1"] = "HETATM"
        ligne["field2"] = "{:5d}".format(residu[0] + 1)
        ligne["field3"] = "{:^4s}".format(residu[1].typeHP)
        ligne["field5"] = "{:3s}".format(residu[1].typeHP+str(i))
        ligne["field6"] = "{:1s}".format(residu[1].typeHP)
        ligne["field7"] = "{:4d}".format(i)
        ligne["field9"] = "{:8.3f}".format(float(residu[1].coordY))
        ligne["field10"] = "{:8.3f}".format(float(-residu[1].coordX))
        ligne["field11"] = "{:8.3f}".format(float(0))
        ligne["field14"] = "{:>2s}".format("H")
        retour = ""
        for ele in ligne.items():
            retour += ele[1]
        path.write(retour)
        path.write("\n")
    path.close()
