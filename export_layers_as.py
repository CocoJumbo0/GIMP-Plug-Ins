#! /usr/bin/env python

import os
from gimpfu import *

#every layer except background should be off before running script
#gimp file should also be saved prior running script
def export_visible(image, drawable):
    count = 1 #exported image file count
    file_extension = '.jpeg' #exported image file extension

    currentDirectory = image.filename
    filename = image.name 

    #replaces filename with a new folder
    #Please dont make your filename the same as your directory or folder lol
    currentDirectory = currentDirectory.replace(filename, '', 1)
    currentDirectory += 'exported'

    if not os.path.exists(currentDirectory):
        os.mkdir(currentDirectory)
    else:
        pdb.gimp_message("path already exists")

    #remove extention of filename, add new extention later
    filename = filename.replace('.xcf', '')

    try:        
        for layer in image.layers:
            if layer.name == 'Background':
                break

            layer.visible = True

            newfilename = filename + '-' + str(count) + file_extension
            count += 1
            newDir = currentDirectory + '\\' + newfilename

            new_image = pdb.gimp_image_duplicate(image)
            temp_layer = new_image.merge_visible_layers(CLIP_TO_IMAGE)
            pdb.gimp_file_save(new_image, temp_layer, newDir, newfilename)
            gimp.delete(temp_layer)
            gimp.delete(new_image)

            layer.visible = False
            pdb.gimp_message(newfilename)
              
        pdb.gimp_message("success! exported " + str(count-1) + " images to " + currentDirectory + "!")
    
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
    "<Image>/Functionality/Export_All_Layers",
    "*",
    [
        #(PF_FLOAT, "y_pos", "y_pos:", 0)
    ],
    [],
    export_visible)

main()