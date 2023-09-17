#! /usr/bin/env python

import os, sys
from gimpfu import *

#required to import module item_util
me = os.path.abspath(sys.argv[0])
mydir = os.path.dirname(me)
sys.path.insert(0, mydir)

import item_util

def reduce_size(image, drawable):
    """
    Reduces every visible layer by some factor (currently by 1.3)
    Additionally will also center layers
    """
    
    #TODO: take in this value as a parameter from GUI
    reduceFactor = 1.30

    layers = [] #list of active layers
    try:
        item_util.listAllVisible(image, layers)
        for layer in layers:
            pdb.gimp_layer_scale(layer, layer.width/reduceFactor, layer.height/reduceFactor, False)

            #center the image
            item_util.center_layer(image, layer)

    except Exception as e:
        pdb.gimp_message(e.args[0])

    return

register(
    "Reduce_Size",
    "Reduce layers size by .25 ",
    "Reduce layers size",
    "Sophia Lilmohan",
    "Sophia Lilmohan",
    "2023",
    "<Image>/Functionality/Reduce_Size",
    "*",
    [
        #(PF_FLOAT, "y_pos", "y_pos:", 0)
    ],
    [],
    reduce_size)


main()