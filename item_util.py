#! /usr/bin/env python

from gimpfu import *

def listAllVisible(parent, outputList):
    """
    Adds every layer/item to outputList
    """
    for layer in parent.layers:
        if pdb.gimp_layer_get_visible(layer):
            outputList.append(layer)
            if pdb.gimp_item_is_group(layer):
                listAllVisible(layer, outputList)


def center_layer(image, layer):
    """
    Centers layer/item onto image
    """
    x_pos = image.width / 2 - layer.width / 2
    y_pos = image.height / 2 - layer.height / 2
    layer.set_offsets(x_pos, y_pos)