#! /usr/bin/env python

from gimpfu import *

#Rotates all visible layers 90 degrees 
def rotate90Degrees(image, drawable):
    layers = []
    listAllVisible(image, layers)

    try:
        for layer in layers:
            pdb.gimp_item_transform_rotate_simple(layer, 0, TRUE, 0, 0)
            pdb.gimp_layer_set_offsets(layer, image.width / 2 - layer.width / 2, -1000)

    except Exception as e:
        pdb.gimp_message(e.args[0])

    return

def listAllVisible(parent, outputList):
    for layer in parent.layers:
        if pdb.gimp_layer_get_visible(layer):
            outputList.append(layer)
            if pdb.gimp_item_is_group(layer):
                listAllVisible(layer, outputList)

register(
    "Rotate90Degrees",
    "Rotate visible elements",
    "Rotate elements",
    "Sophia Lilmohan",
    "Sophia Lilmohan",
    "2023",
    "<Image>/Functionality/Rotate90Degrees",
    "*",
    [
        #(PF_LAYER, "reg", "reg:", None)
    ],
    [],
    rotate90Degrees)

main()