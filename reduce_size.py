#! /usr/bin/env python

from gimpfu import *

#will also center layers onto canvas
def reduce_size(image, drawable):
    y_pos = 0
    reduceFactor = 1.30

    #get every visible layer
    layers = []
    listAllVisible(image, layers)
    try:
        for layer in layers:
            pdb.gimp_layer_scale(layer, layer.width/reduceFactor, layer.height/reduceFactor, False)
            
            #center the image
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