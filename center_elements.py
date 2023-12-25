#! /usr/bin/env python

import os, sys
from gimpfu import *

#required to import module item_util
me = os.path.abspath(sys.argv[0])
mydir = os.path.dirname(me)
sys.path.insert(0, mydir)

import item_util

def center_elements(image, drawable):
    """
    Centers every active element to the center of the image/canvas
    """
    layers = [] #list of active layers

    try:
        item_util.listAllVisible(image, layers)
        for layer in layers:
            item_util.center_layer(image, layer)     
    except Exception as e:
        pdb.gimp_message(e.args[0])

    return


register(
    "Center_Elements",
    "Center visible elements in the file.",
    "Center elements.",
    "Sophia Lilmohan",
    "Sophia Lilmohan",
    "2023",
    "<Image>/Functionality/Center_Elements",
    "*",
    [
        #(PF_FLOAT, "y_pos", "y_pos:", 0)
    ],
    [],
    center_elements)


main()