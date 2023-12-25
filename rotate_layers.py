#! /usr/bin/env python

import os, sys
from gimpfu import *

#required to import module item_util
me = os.path.abspath(sys.argv[0])
mydir = os.path.dirname(me)
sys.path.insert(0, mydir)

import item_util
 
def rotate_layers(image, drawable):
    """
    Rotates all visible layers by 90 degrees
    """

    layers = [] #list of active layers

    try:
        item_util.listAllVisible(image, layers)

        for layer in layers:
            pdb.gimp_item_transform_rotate_simple(layer, 0, TRUE, 0, 0)

            #centers layers to keep them visible within frame
            item_util.center_layer(image, layer)

    except Exception as e:
        pdb.gimp_message(e.args[0])

    return


register(
    "Rotate_Layers",
    "Rotate visible elements",
    "Rotate elements",
    "Sophia Lilmohan",
    "Sophia Lilmohan",
    "2023",
    "<Image>/Functionality/Rotate_Layers",
    "*",
    [
        #(PF_LAYER, "reg", "reg:", None)
    ],
    [],
    rotate_layers)

main()