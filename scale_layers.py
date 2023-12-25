#! /usr/bin/env python

import os, sys
from gimpfu import *

#required to import module item_util
me = os.path.abspath(sys.argv[0])
mydir = os.path.dirname(me)
sys.path.insert(0, mydir)

import item_util

def scale_layers(image, drawable, scale_factor):
    """
    Scale every visible layer by some factor
    Will also center layers
    """

    layers = [] #list of active layers
    try:
        item_util.listAllVisible(image, layers)
        for layer in layers:
            pdb.gimp_layer_scale(layer, layer.width/scale_factor, layer.height/scale_factor, False)

            #center the image
            item_util.center_layer(image, layer)

    except Exception as e:
        pdb.gimp_message(e.args[0])

    return

register(
    "Scale_Layers",
    "Scale layers by inputed factor",
    "Scale all layers",
    "Sophia Lilmohan",
    "Sophia Lilmohan",
    "2023",
    "<Image>/Functionality/Scale_Layers",
    "*",
    [
        (PF_FLOAT, "scale_factor", "scale_factor:", 1)
    ],
    [],
    scale_layers)


main()