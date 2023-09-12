#! /usr/bin/env python

from gimpfu import *
import gimpcolor

def remove_white_background(image, drawable):
    """
    (WIP) Removes any white background of images to make them transparent

    """
    layers = []
    listAllVisible(image, layers)
    try:
        for layer in layers:
            #create copy of layer and insert into image
            copy = pdb.gimp_layer_copy(layer, TRUE)
            pdb.gimp_image_insert_layer(image, copy, None, -1)
            
            #desaturate copied layer to create pure white and black silhouette
            pdb.gimp_drawable_desaturate(copy, 1)
            pdb.gimp_drawable_brightness_contrast(copy, -0.50, 0.75)
            
            #turn white into alpha
            tempWhite = gimpcolor.RGB(255, 255, 255) 
            pdb.plug_in_colortoalpha(image, copy, tempWhite)

            #select subject ignoring alpha
            pdb.gimp_image_select_item(image, 0, copy)

            #create and add mask to original image
            mask = pdb.gimp_layer_create_mask(layer, 4)
            pdb.gimp_layer_add_mask(layer, mask)

            #delete copy
            pdb.gimp_image_remove_layer(image, copy)

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
    "remove_background",
    "Roughly removes white background from all visible layer.",
    "Remove white background",
    "Sophia Lilmohan",
    "Sophia Lilmohan",
    "2023",
    "<Image>/Functionality/Remove_White_Background",
    "*",
    [],
    [],
    remove_white_background)

main()