#! /usr/bin/env python

from gimpfu import *

def placeGuides(image, drawable):
    """
    Place guides on all edges of the canvas
    """

    pdb.gimp_image_add_hguide(image, 0)
    pdb.gimp_image_add_hguide(image, image.height)
    pdb.gimp_image_add_vguide(image, 0)
    pdb.gimp_image_add_vguide(image, image.width)
    
    return

register(
    "PlaceGuides",
    "place guides at all edges of the canvas",
    "place guides",
    "Sophia Lilmohan",
    "Sophia Lilmohan",
    "2023",
    "<Image>/Functionality/PlaceGuides",
    "*",
    [
        #(PF_LAYER, "reg", "reg:", None)
    ],
    [],
    placeGuides)

main()