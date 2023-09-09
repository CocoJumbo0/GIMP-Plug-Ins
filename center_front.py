#! /usr/bin/env python

from gimpfu import *

def center_elements(image, drawable):
    x_pos = 0
    y_pos = 0
    layers = [] #list of active layers
    try:
        listAllVisible(image, layers)
        for layer in layers:
            x_pos = image.width / 2 - layer.width / 2
            y_pos = image.height / 2 - layer.height / 2
            layer.set_offsets(x_pos, y_pos)
            
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