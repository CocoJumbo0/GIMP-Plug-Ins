#! /usr/bin/env python

import os, sys
from gimpfu import *

#required to import module item_util
me = os.path.abspath(sys.argv[0])
mydir = os.path.dirname(me)
sys.path.insert(0, mydir)

import item_util

def to_new_image(image, drawable):
    """
    copy visible layers and add them to a new image
    if a mask exists on a layer, copy the mask too
    """
    
    layers = [] #list of active layers

    try:
        #get every active layer
        item_util.listAllVisible(image, layers)

        #create new image and insert blank layer
        newImage = gimp.Image(image.width, image.height, RGB)
        newLayer = gimp.Layer(newImage, "temp", newImage.width, newImage.height, RGBA_IMAGE, 100, NORMAL_MODE)
        newImage.add_layer(newLayer, 0)

        for layer in layers:
            #select the layer, copy, and paste it into newImage as new floating layer
            pdb.gimp_image_select_item(image, 0, layer)
            pdb.gimp_edit_copy(layer)
            floatLayer = pdb.gimp_edit_paste(newLayer, True)
            
            #take floating layer and turn to new layer
            pdb.gimp_floating_sel_to_layer(floatLayer)

            floatLayer.name = layer.name

            #if a mask exists
            if layer.mask != None:
                mask = floatLayer.create_mask(ADD_MASK_WHITE)
                floatLayer.add_mask(mask)

                #get channel from original layer
                maskChannel = layer.mask

                pdb.gimp_channel_combine_masks(mask, maskChannel, 2, 0, 0)

        newImage.remove_layer(newLayer)
        gimp.Display(newImage)
        gimp.displays_flush()
        pdb.gimp_selection_none(image)

    except Exception as e:
        pdb.gimp_message(e.args[0])

    return


register(
    "Layers_To_New_Image",
    "Takes visible layers and copies them to a new image",
    "Copy layers to new image",
    "Sophia Lilmohan",
    "Sophia Lilmohan",
    "2023",
    "<Image>/Functionality/Layers_To_New_Image",
    "*",
    [],
    [],
    to_new_image)


main()