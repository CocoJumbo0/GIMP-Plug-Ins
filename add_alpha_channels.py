#! /usr/bin/env python

import os, sys
from gimpfu import *

#required to import module item_util
me = os.path.abspath(sys.argv[0])
mydir = os.path.dirname(me)
sys.path.insert(0, mydir)

import item_util

def add_alpha_channels(image, drawable):
    """
    Adds an alpha channel to every visible layer
    """
    layers = [] #list of active layers

    try:
        item_util.listAllVisible(image, layers)
        for layer in layers:
            pdb.gimp_layer_add_alpha(layer)     
    except Exception as e:
        pdb.gimp_message(e.args[0])

    return


register(
    "Add_Alpha_Channels",
    "Add alphas channel to every visible layer.",
    "Adds alpha channels.",
    "Sophia Lilmohan",
    "Sophia Lilmohan",
    "2023",
    "<Image>/Functionality/Add_Alpha_Channels",
    "*",
    [
        #(PF_FLOAT, "y_pos", "y_pos:", 0)
    ],
    [],
    add_alpha_channels)


main()