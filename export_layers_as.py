#! /usr/bin/env python

import os
from gimpfu import *

#every layer except background should be off before running script
def export_visible(image, drawable):
    count = 1
    file_extension = '.jpeg'

    #gets whole directory of current opened gimp file.
    #Note: api claims that I need to use g_free()
    currentDirectory = pdb.gimp_image_get_filename(image)
    #gets gimp file name
    filename = pdb.gimp_image_get_name(image)

    #removes filename and adds new folder
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
            if pdb.gimp_item_get_name(layer) == 'Background':
                break

            pdb.gimp_item_set_visible(layer, True)

            newfilename = filename + '-' + str(count) + file_extension
            count += 1
            newDir = currentDirectory + '\\' + newfilename
            
            new_image = pdb.gimp_image_duplicate(image)
            temp_layer = pdb.gimp_image_merge_visible_layers(new_image, CLIP_TO_IMAGE)
            pdb.gimp_file_save(new_image, temp_layer, newDir, newfilename)
            pdb.gimp_image_delete(new_image)

            pdb.gimp_item_set_visible(layer, False)
            pdb.gimp_message(newfilename)
              
        pdb.gimp_message("success! exported " + str(count-1) + " images to " + newDir + "!")
    
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