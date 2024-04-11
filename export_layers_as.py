#! /usr/bin/env python

import os
from gimpfu import *


def export_visible(image, drawable):
    """
    Exports every layer except Background and anything under it within the GUI

    Background should be left visible if it should be in every exported image
    Gimp file should be saved before running
    """

    exported_count = 1 
    file_extension = '.jpeg' #exported file extension

    currentDirectory = image.filename
    filename = image.name 

    #replace filename with a folder
    #Please don't make your filename the same as your directory or folder lol
    currentDirectory = currentDirectory.replace(filename, '', 1)
    currentDirectory += 'exported'

    if not os.path.exists(currentDirectory):
        os.mkdir(currentDirectory)
    else:
        pdb.gimp_message("path already exists")

    #remove extention of filename
    filename = filename.replace('.xcf', '')

    try:
        for layer in image.layers:
            if layer.name == 'Background':
                break

            layer.visible = True

            #create new file name and create new directory with new file
            newfilename = filename + '-' + str(exported_count) + file_extension
            exported_count += 1
            newDir = currentDirectory + '\\' + newfilename

            #merge image into a single layer and export
            new_image = pdb.gimp_image_duplicate(image)
            temp_layer = new_image.merge_visible_layers(CLIP_TO_IMAGE)
            pdb.gimp_file_save(new_image, temp_layer, newDir, newfilename)
            gimp.delete(temp_layer)
            gimp.delete(new_image)

            layer.visible = False
            pdb.gimp_message(newfilename)
              
        pdb.gimp_message("success! exported " + str(exported_count-1) + " images to " + currentDirectory + "!")
    
    except Exception as e:
        pdb.gimp_message(e.args[0])
    
    return


register(
    "Export_All_Layers",
    "export all layers as JPEG or PNG",
    "export all.",
    "Sophia Lilmohan",
    "Sophia Lilmohan",
    "2023",
    "<Image>/Functionality/Exporter/Export_All_Layers",
    "*",
    [
        #(PF_FLOAT, "y_pos", "y_pos:", 0)
    ],
    [],
    export_visible)

main()